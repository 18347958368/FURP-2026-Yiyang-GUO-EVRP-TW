from __future__ import annotations

from evrptw.metrics import evaluate_route_metrics
from evrptw.models import Instance, Node, NodeType, Vehicle


def test_week03_metrics_classify_energy_and_charging_fields() -> None:
    instance = Instance(
        "metrics_toy",
        (
            Node("D0", NodeType.DEPOT, 0.0, 0.0, 0.0, 0.0, 1_000.0, 0.0),
            Node("S1", NodeType.STATION, 30.0, 0.0, 0.0, 0.0, 1_000.0, 0.0),
            Node("C1", NodeType.CUSTOMER, 60.0, 0.0, 1.0, 0.0, 1_000.0, 0.0),
        ),
        Vehicle(
            battery_capacity=50.0,
            load_capacity=10.0,
            consumption_rate=1.0,
            inverse_refueling_rate=0.1,
            average_velocity=1.0,
        ),
    )

    metrics = evaluate_route_metrics(
        instance,
        [["D0", "S1", "C1", "D0"]],
        method="TEST",
        seed=1,
        runtime_seconds=0.5,
    )

    assert metrics.feasible is False
    assert metrics.energy_violations == 1
    assert metrics.charging_count == 1
    assert metrics.charging_time == 3.0
    assert metrics.first_infeasible_step == "route 1 leg 3 C1->D0: battery depleted"
