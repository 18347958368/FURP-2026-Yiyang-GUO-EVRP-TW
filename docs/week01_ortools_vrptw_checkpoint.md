# Week 1 OR-Tools VRPTW Checkpoint

## Scope

This checkpoint implements the Week 1 OR-Tools VRPTW path from the reference
repository. It is independent of `docs/01_weekly.md` and does not use that file
as evidence.

Reflection and Week 2 planning are intentionally omitted.

## Environment

| Item | Record |
|---|---|
| Operating system | macOS Apple Silicon environment |
| Python version | 3.13.13 |
| Package manager | uv |
| Solver package | OR-Tools 9.15.6755 |
| Project command for environment metadata | `uv run evrptw-env --output results/week01/environment.json` |
| Hardware record | Captured in `results/week01/environment.json` when the command is run |

## Baseline Choice

| Field | Value |
|---|---|
| Starter path | OR-Tools VRPTW path |
| Baseline solver | Google OR-Tools `RoutingModel` |
| Problem variant | VRPTW |
| Instance | `src/evrptw/instances/week01_vrptw_toy.txt` |
| Instance size | 1 depot, 8 customers, 2 vehicles |
| Evidence type | Textual route output and machine-readable JSON |

## Smoke-Test Commands

```bash
uv run evrptw-env --output results/week01/environment.json
uv run python -m evrptw.baselines.ortools_vrptw \
  --instance src/evrptw/instances/week01_vrptw_toy.txt \
  --output results/week01/ortools_vrptw_smoke_test.json
```

## Expected Recorded Outputs

The baseline command prints and writes:

- instance name and size;
- solver status;
- objective value;
- validated total distance;
- feasibility status;
- runtime in seconds;
- route text for each used vehicle;
- arrival time and load after service for each stop;
- validation violations, if any.

The JSON output contains these required fields:

```text
instance_name
customer_count
vehicle_count
solver_status
solver_objective
validation_total_distance
feasible
runtime_seconds
routes
route_reports
violations
```

## Smoke-Test Result

The Week 1 smoke test was run with:

```bash
uv run python -m evrptw.baselines.ortools_vrptw \
  --instance src/evrptw/instances/week01_vrptw_toy.txt \
  --output results/week01/ortools_vrptw_smoke_test.json
```

| Field | Value |
|---|---|
| Instance | `week01_vrptw_toy` |
| Size | 8 customers, 2 vehicles |
| Solver status | `ROUTING_SUCCESS` |
| Objective value | 80 |
| Validated total distance | 80.0 |
| Feasibility status | feasible |
| Runtime | 0.005355 seconds |
| Violations | none |

Textual route evidence:

```text
Vehicle 0: D0(t=0, load=0) -> C1(t=5, load=2) -> C2(t=15, load=4) -> C3(t=25, load=6) -> C4(t=35, load=8) -> D0(t=60, load=8)
Vehicle 1: D0(t=0, load=0) -> C5(t=5, load=2) -> C6(t=15, load=4) -> C7(t=25, load=6) -> C8(t=35, load=8) -> D0(t=60, load=8)
```

## Validation

The OR-Tools route output is independently checked with the repository's
`validate_routes()` function. The Week 1 smoke test is complete only when:

- OR-Tools returns a solution;
- all 8 customers are visited exactly once;
- the independent validation report is feasible;
- objective value, feasibility status, runtime, and route text are present.

Run:

```bash
uv run pytest
uv run ruff check .
uv run mypy
```
