from __future__ import annotations

from evrptw.metrics import evaluate_route_metrics
from evrptw.models import Instance, Node, NodeType, Vehicle
from evrptw.repairs import insert_charging_stations


def test_charging_repair_inserts_reachable_station_without_reordering_customers() -> None:
    instance = Instance(
        "repair_toy",
        (
            Node("D0", NodeType.DEPOT, 0.0, 0.0, 0.0, 0.0, 1_000.0, 0.0),
            Node("S1", NodeType.STATION, 50.0, 0.0, 0.0, 0.0, 1_000.0, 0.0),
            Node("C1", NodeType.CUSTOMER, 60.0, 0.0, 1.0, 0.0, 1_000.0, 0.0),
        ),
        Vehicle(
            battery_capacity=80.0,
            load_capacity=10.0,
            consumption_rate=1.0,
            inverse_refueling_rate=0.1,
            average_velocity=1.0,
        ),
    )
    baseline_routes = [["D0", "C1", "D0"]]
    baseline_metrics = evaluate_route_metrics(
        instance,
        baseline_routes,
        method="BASELINE",
        seed=1,
        runtime_seconds=0.0,
    )

    repair = insert_charging_stations(instance, baseline_routes)
    repaired_routes = [list(route) for route in repair.routes]
    repaired_metrics = evaluate_route_metrics(
        instance,
        repaired_routes,
        method="REPAIRED",
        seed=1,
        runtime_seconds=repair.runtime_seconds,
    )

    assert baseline_metrics.energy_violations == 1
    assert repaired_routes == [["D0", "C1", "S1", "D0"]]
    assert repaired_metrics.feasible is True
    assert repaired_metrics.energy_violations == 0
    assert repair.inserted_station_count == 1
    assert repair.unrepaired_legs == ()
