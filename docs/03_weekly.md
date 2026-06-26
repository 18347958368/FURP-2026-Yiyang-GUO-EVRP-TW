# Week 3 Progress Log

### Week 3 — 2026-06-27

**Attended this week's meeting:** Not recorded in this repository.

**Progress this week**
- Recovered the delayed Week 1 and Week 2 technical progress and brought the
  repository up to the Week 3 standard required by the reference project. The
  delay came mainly from the need to first understand the EVRP-TW problem,
  Python project structure, solver output, and baseline experiment workflow.
- Completed the Week 1 OR-Tools VRPTW baseline smoke test. The repository now
  has a deterministic toy VRPTW instance, an OR-Tools baseline runner, route
  validation, environment recording, and a Week 1 checkpoint document.
- Completed the Week 2 baseline recreation and comparison work. I implemented a
  GA VRPTW baseline inspired by the read-only `py-ga-VRPTW` reference project,
  compared it with the OR-Tools VRPTW baseline on 50-, 100-, and 200-customer
  generated Schneider-style instances, and recorded objective value,
  feasibility, runtime, vehicle count, violations, and GA convergence.
- Completed the Week 3 controlled EVRP-TW evaluation. I added a Week 3
  experiment runner comparing `baseline only` against `baseline + charging
  insertion repair` on the same instance sets and random seeds.
- Added unified metrics for objective value, feasibility, runtime, capacity
  violations, time-window violations, energy violations, charging count,
  charging time, and first infeasible step.
- Produced raw outputs, cleaned per-run results, cleaned summary results, and a
  failure-case table. Small curated summary tables are stored under
  `experiments/summaries/`, while full generated outputs remain under the
  Git-ignored `results/` directory.
- Wrote the Week 3 experimental report in
  `docs/week03_experiment_design_and_evaluation.md`.
- Verified the codebase with `uv run pytest`, `uv run ruff check .`, and
  `uv run mypy`.

**Challenges & blockers**
- I am not a computer science student, so the first two weeks required more
  background learning than originally expected. I had to understand Python
  package structure, OR-Tools, GA-style baseline design, command-line experiment
  runners, and how to record reproducible research outputs before the
  implementation work could become stable.
- EVRP-TW is not only a shortest-route problem. A valid experiment must track
  feasibility, time-window constraints, battery constraints, charging behavior,
  random seeds, runtime, and failure cases. This made the early learning curve
  steeper, but it was necessary for producing a defensible Week 3 experiment.
- The Week 3 charging insertion repair reduced GA energy violations
  substantially, but it did not produce fully feasible EVRP-TW solutions under
  the 80-unit battery setting. This is a useful negative result: late local
  charging insertion is not enough when the route has already moved beyond a
  reachable charging opportunity.
- CPLEX and Gurobi academic licence access remains outside the current Week 3
  workflow. The Week 3 experiment therefore uses OR-Tools and the local GA
  baseline, which is sufficient for the reference repository's evaluation and
  reporting requirement.

**Next steps**
- Improve charging insertion from a late repair rule to anticipatory charging
  logic that inserts a charging station before the battery becomes critically
  low.
- Add route splitting or customer reassignment when no charging station is
  reachable from the current route segment.
- Rerun the same Week 3 evaluation tables after improving the repair logic, so
  the comparison remains fair and reproducible.
- Begin mapping the formal Schneider benchmark instances into the local parser
  and validator.
- Avoid moving to POMO or Truck-Drone Routing until the EVRP-TW baseline and
  charging-feasibility workflow are more stable.

**Hours spent (optional):** Not recorded.

**Links (optional):**
- [Week 1 OR-Tools checkpoint](week01_ortools_vrptw_checkpoint.md)
- [Week 2 baseline recreation](week02_baseline_recreation.md)
- [Week 3 experimental report](week03_experiment_design_and_evaluation.md)
- [Week 3 summary results](../experiments/summaries/week03_summary_results.csv)
- [Week 3 per-run results](../experiments/summaries/week03_per_run_results.csv)
