from __future__ import annotations

import time
from dataclasses import asdict, dataclass

from evrptw.models import Instance, NodeType


@dataclass(frozen=True, slots=True)
class ChargingRepairResult:
    routes: tuple[tuple[str, ...], ...]
    inserted_station_count: int
    unrepaired_legs: tuple[str, ...]
    runtime_seconds: float

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def insert_charging_stations(
    instance: Instance,
    routes: list[list[str]],
) -> ChargingRepairResult:
    started_at = time.perf_counter()
    by_name = instance.by_name
    repaired_routes: list[tuple[str, ...]] = []
    inserted_station_count = 0
    unrepaired_legs: list[str] = []

    for route_index, route in enumerate(routes, start=1):
        if len(route) < 2 or any(node_name not in by_name for node_name in route):
            repaired_routes.append(tuple(route))
            continue

        battery = instance.vehicle.battery_capacity
        repaired = [route[0]]

        for origin_name, destination_name in zip(route, route[1:], strict=False):
            origin = by_name[origin_name]
            destination = by_name[destination_name]
            required_energy = (
                origin.distance_to(destination) * instance.vehicle.consumption_rate
            )

            if battery + 1e-9 < required_energy:
                station_name = _best_station_for_leg(
                    instance,
                    origin_name=origin_name,
                    destination_name=destination_name,
                    available_battery=battery,
                )
                if station_name is None:
                    unrepaired_legs.append(
                        f"route {route_index} {origin_name}->{destination_name}"
                    )
                else:
                    station = by_name[station_name]
                    battery -= origin.distance_to(station) * instance.vehicle.consumption_rate
                    repaired.append(station_name)
                    inserted_station_count += 1
                    battery = instance.vehicle.battery_capacity
                    origin = station
                    required_energy = (
                        origin.distance_to(destination) * instance.vehicle.consumption_rate
                    )

            battery -= required_energy
            repaired.append(destination_name)
            if destination_name in by_name and by_name[destination_name].kind is NodeType.STATION:
                battery = instance.vehicle.battery_capacity

        repaired_routes.append(tuple(repaired))

    return ChargingRepairResult(
        routes=tuple(repaired_routes),
        inserted_station_count=inserted_station_count,
        unrepaired_legs=tuple(unrepaired_legs),
        runtime_seconds=time.perf_counter() - started_at,
    )


def _best_station_for_leg(
    instance: Instance,
    *,
    origin_name: str,
    destination_name: str,
    available_battery: float,
) -> str | None:
    by_name = instance.by_name
    origin = by_name[origin_name]
    destination = by_name[destination_name]
    direct_distance = origin.distance_to(destination)
    candidates: list[tuple[float, str]] = []

    for station in instance.stations:
        energy_to_station = origin.distance_to(station) * instance.vehicle.consumption_rate
        energy_station_to_destination = (
            station.distance_to(destination) * instance.vehicle.consumption_rate
        )
        if energy_to_station > available_battery + 1e-9:
            continue
        if energy_station_to_destination > instance.vehicle.battery_capacity + 1e-9:
            continue
        extra_distance = (
            origin.distance_to(station)
            + station.distance_to(destination)
            - direct_distance
        )
        candidates.append((extra_distance, station.name))

    if not candidates:
        return None
    return min(candidates)[1]
