# Week 2 Baseline Recreation and Comparison

## Scope

This document completes the Week 2 task independently from `docs/02_weekly.md`.
It treats Week 2 as a fresh baseline recreation and comparison exercise.

The selected replication paper is Schneider, Stenger, and Goeke (2014),
*The Electric Vehicle-Routing Problem with Time Windows and Recharging
Stations*, DOI `10.1287/trsc.2013.0490`. This paper defines the E-VRPTW
problem variant used by this repository and provides the core OR/MILP and
hybrid VNS/TS reference direction.

The open-source GA reference is `iRB-Lab/py-ga-VRPTW`, cloned locally under
`reference/py-ga-VRPTW` as a read-only reference. Its algorithmic structure is a
VRPTW genetic algorithm using chromosome encoding, route decoding, selection,
crossover, mutation, and convergence logging. The project implementation in
this repository adapts those ideas to the local Schneider-style `Instance`
model and independent route validator.

## Baseline Classification

| Direction | Baseline type | Week 2 decision |
|---|---|---|
| Schneider et al. (2014) | OR/MILP and hybrid VNS/TS reference for E-VRPTW | Selected as the primary paper to reproduce toward |
| OR-Tools VRPTW | Operations research / constraint-programming baseline | Implemented and reused for 50, 100, and 200-customer runs |
| GA VRPTW | Genetic Algorithm baseline | Implemented in `src/evrptw/baselines/ga_vrptw.py` |
| POMO | Deep reinforcement learning construction baseline | Not reproduced in Week 2 because the original CVRP scope lacks E and TW constraints |
| UAV-Truck | Truck-drone collaborative routing baseline | Not reproduced in Week 2 because it adds synchronization constraints beyond the current EVRP-TW baseline layer |

## Experiment Setup

The Week 2 runner is:

```bash
uv run python -m evrptw.experiments.week02_baseline_comparison --output-dir results/week02
```

Experiment defaults:

| Item | Value |
|---|---|
| Instance scales | 50, 100, 200 customers |
| Seed | 2014 |
| OR-Tools time limit | 30 seconds per instance |
| GA population size | 100 |
| GA generations | 200 |
| GA crossover probability | 0.8 |
| GA mutation probability | 0.2 |
| Independent validator | `validate_routes()` |

The generated Schneider-style instances include one depot, five charging
stations, and the requested number of customers. The Week 2 baselines solve the
VRPTW projection and then validate the resulting routes through the repository's
EVRP-TW validator. Battery capacity is deliberately generous in these generated
instances so Week 2 can focus on baseline recreation before charging-station
insertion is added.

## Results

Raw outputs are written under `results/week02/`. The summary table is
`results/week02/week02_results.csv`, and the GA convergence log is
`results/week02/week02_convergence.csv`.

| Instance | Size | Method | Objective value | Feasible | Runtime (s) | Vehicles | Violations |
|---|---:|---|---:|---|---:|---:|---:|
| `week02_generated_50` | 50 | OR-Tools VRPTW | 653.972 | Yes | 0.016 | 3 | 0 |
| `week02_generated_50` | 50 | GA VRPTW | 1729.089 | Yes | 4.174 | 3 | 0 |
| `week02_generated_100` | 100 | OR-Tools VRPTW | 1197.687 | Yes | 0.087 | 7 | 0 |
| `week02_generated_100` | 100 | GA VRPTW | 4071.713 | Yes | 9.480 | 7 | 0 |
| `week02_generated_200` | 200 | OR-Tools VRPTW | 1816.252 | Yes | 0.412 | 13 | 0 |
| `week02_generated_200` | 200 | GA VRPTW | 9058.009 | Yes | 25.527 | 13 | 0 |

GA convergence summary:

| Instance | Initial best | Final best | Final average | Final feasible rate |
|---|---:|---:|---:|---:|
| `week02_generated_50` | 2416.906 | 1729.089 | 2544.180 | 1.000 |
| `week02_generated_100` | 4841.357 | 4071.713 | 5318.452 | 1.000 |
| `week02_generated_200` | 9848.233 | 9058.009 | 10639.600 | 1.000 |

## Overview and Conclusion

The OR-Tools VRPTW baseline is much stronger on these generated instances. It
produces shorter routes and finishes faster at every tested scale. This is
expected because OR-Tools uses mature routing search machinery, while the GA
baseline is intentionally simple and mainly reproduces the Week 2 method family:
chromosome encoding, route decoding, crossover, mutation, and convergence
tracking.

The GA baseline still provides useful evidence. It improves its best objective
from generation 0 to generation 200 at all three scales, remains feasible under
the independent validator, and exposes the convergence data needed for future
operator tuning. Its current weakness is solution quality, not feasibility.

The main challenge for moving from VRPTW to E-VRPTW is that neither the
reference GA nor POMO natively handles electric-vehicle constraints. The next
implementation step should add EV-specific repair or insertion logic:
detect battery violations, insert charging stations, record charging count and
charging time, then compare `baseline only` against `baseline + charging repair`
on the same instances.

## Verification

The following checks passed after implementation:

```bash
uv run pytest
uv run ruff check .
uv run mypy
uv run python -m evrptw.experiments.week02_baseline_comparison --output-dir results/week02
```
