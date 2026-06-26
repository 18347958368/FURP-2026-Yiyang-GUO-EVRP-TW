# Week 3 Experiment Design, Evaluation, and Report

## Experimental Setup

The Week 3 research question is:

> On the same EVRP-TW instances, does charging insertion improve feasibility
> compared with the VRPTW baselines, and what objective-value and runtime cost
> does it introduce?

The experiment uses generated Schneider-style EVRP-TW instances derived from
the Week 2 generator. Each instance has one depot, five charging stations, and
50, 100, or 200 customers. To expose the electric-vehicle constraint, vehicle
battery capacity is reduced to `80.0`; all methods are evaluated by the same
independent EVRP-TW validator.

The compared methods are:

| Method | Description |
|---|---|
| `OR_TOOLS_VRPTW` | OR-Tools VRPTW baseline; ignores charging during construction |
| `OR_TOOLS_VRPTW_CHARGING_REPAIR` | OR-Tools route plus charging-station insertion |
| `GA_VRPTW` | Genetic Algorithm VRPTW baseline; stochastic |
| `GA_VRPTW_CHARGING_REPAIR` | GA route plus charging-station insertion |

Fair-comparison controls:

- same instance set for all methods;
- same distance and coordinate data;
- same objective definition: validated total route distance;
- same EVRP-TW validator for feasibility and violations;
- three seeds: `2014`, `2015`, and `2016`;
- OR-Tools time limit: 30 seconds per instance;
- GA settings: population size 100, 200 generations, crossover probability
  0.8, mutation probability 0.2.

The runnable command is:

```bash
uv run python -m evrptw.experiments.week03_evaluation --output-dir results/week03
```

Raw JSON outputs are under `results/week03/raw/`. Cleaned summary copies are
also available in `experiments/summaries/`.

## Results

The full per-run table is `results/week03/week03_per_run_results.csv`. The
aggregated table is `results/week03/week03_summary_results.csv`.

| Size | Method | Runs | Feasible rate | Avg. runtime (s) | Avg. energy violations | Avg. charging count |
|---:|---|---:|---:|---:|---:|---:|
| 50 | `GA_VRPTW` | 3 | 0.000 | 3.634 | 26.667 | 0.000 |
| 50 | `GA_VRPTW_CHARGING_REPAIR` | 3 | 0.000 | 3.634 | 2.667 | 24.000 |
| 50 | `OR_TOOLS_VRPTW` | 3 | 0.000 | 0.020 | 32.000 | 0.000 |
| 50 | `OR_TOOLS_VRPTW_CHARGING_REPAIR` | 3 | 0.000 | 0.020 | 28.000 | 0.667 |
| 100 | `GA_VRPTW` | 3 | 0.000 | 8.622 | 48.667 | 0.000 |
| 100 | `GA_VRPTW_CHARGING_REPAIR` | 3 | 0.000 | 8.622 | 6.667 | 42.000 |
| 100 | `OR_TOOLS_VRPTW` | 3 | 0.000 | 0.080 | 57.000 | 0.000 |
| 100 | `OR_TOOLS_VRPTW_CHARGING_REPAIR` | 3 | 0.000 | 0.080 | 57.000 | 0.000 |
| 200 | `GA_VRPTW` | 3 | 0.000 | 23.554 | 106.000 | 0.000 |
| 200 | `GA_VRPTW_CHARGING_REPAIR` | 3 | 0.000 | 23.555 | 12.333 | 93.667 |
| 200 | `OR_TOOLS_VRPTW` | 3 | 0.000 | 0.406 | 83.667 | 0.000 |
| 200 | `OR_TOOLS_VRPTW_CHARGING_REPAIR` | 3 | 0.000 | 0.406 | 81.667 | 0.333 |

No method produced a fully feasible EVRP-TW solution under the reduced
80-unit battery setting. This is a negative result, but it is useful: it shows
that a late, local charging insertion rule is not sufficient to transform a
VRPTW route into a feasible EVRP-TW route.

## Discussion

The charging repair is much more effective on the GA baseline than on the
OR-Tools baseline in terms of reducing energy violations. For GA, the average
energy violations drop from 26.667 to 2.667 on size 50, from 48.667 to 6.667 on
size 100, and from 106.000 to 12.333 on size 200. The cost is more charging
stops and higher route distance.

The OR-Tools baseline remains much faster and shorter, but the repaired version
barely improves energy feasibility. This occurs because OR-Tools constructs
compact multi-customer VRPTW routes without considering battery state. By the
time a route first violates battery capacity, the nearest charging station may
already be unreachable. The current repair rule only inserts a station when the
next leg is already infeasible; it does not anticipate future battery needs.

The main trade-off is therefore not objective value versus runtime. Runtime
overhead from charging insertion is negligible in these experiments. The real
trade-off is route compactness versus EV feasibility. Short VRPTW routes can be
poor EVRP-TW routes if they pass too few charging opportunities.

## Failure Cases

Failure cases are recorded in `results/week03/week03_failure_cases.md`. Typical
examples are:

| Instance | Method | First infeasible step | Diagnosis |
|---|---|---|---|
| `week03_generated_50_seed_2014` | `OR_TOOLS_VRPTW` | `C38->C20` battery depleted | compact VRPTW route ignores charging reachability |
| `week03_generated_50_seed_2014` | `GA_VRPTW` | `C23->D0` battery depleted | single route segment exceeds return energy |
| `week03_generated_100_seed_2015` | `GA_VRPTW_CHARGING_REPAIR` | `C45->D0` battery depleted | repair reduces but does not eliminate energy failures |

These failures suggest that EVRP-TW feasibility cannot be treated as a final
post-processing detail. Battery state must influence route construction,
customer splitting, or earlier charging insertion decisions.

## Conclusion

Week 3 establishes a controlled experimental workflow rather than just a
runnable solver. The current charging insertion repair does not improve
feasible rate under the 80-unit battery setting, but it substantially reduces
GA energy violations with negligible runtime overhead. The OR-Tools baseline
remains fast and short, but its VRPTW routes are not EV-feasible after simple
post-processing. The next step should add anticipatory charging logic or route
splitting before infeasibility occurs, then rerun the same Week 3 evaluation
tables.
