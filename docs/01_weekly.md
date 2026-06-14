# Week 1 Progress Log

### Week 1 — 2026-06-14

**Attended this week's meeting:** Not applicable — no meeting was scheduled this
week because the supervisor was unable to reserve a classroom. This was not an
absence and no leave request was required.

**Progress this week**
- Surveyed the literature on the Electric Vehicle Routing Problem with Time
  Windows (E-VRPTW), prioritising highly cited papers associated with strong
  universities and research institutions. Compared candidate papers by topic
  relevance, citation impact, publication venue, institutional background,
  implementation difficulty, and availability of public benchmark data.
- Selected Schneider, Stenger, and Goeke (2014), *The Electric Vehicle-Routing
  Problem with Time Windows and Recharging Stations*, as the primary replication
  paper. Recorded its complete citation, DOI, selection rationale, BibTeX entry,
  and public benchmark-data link. Also identified supporting journal articles
  on partial charging, nonlinear charging, heterogeneous electric fleets, and
  the wider electric-goods-distribution research context, recording their
  titles and DOIs for later reading.
- Verified and organised the formal 2014 journal version of the primary paper in
  a local literature directory outside the Git repository. Other candidate
  PDFs are to be obtained by the student and added only after their formal
  journal versions have been verified. Created an ignored local shortcut from
  the repository so copyrighted papers and large local files remain outside
  Git while the literature directory stays convenient to access.
- Established an isolated Apple Silicon research environment using Python
  3.13.13 and `uv`. Added `.python-version`, `pyproject.toml`, and `uv.lock` so
  the Python version and dependency set can be reproduced consistently. Python
  3.13.14 was initially requested, but no ARM64 build was available, so the
  latest available Python 3.13 patch release was used instead of system Python
  3.14.
- Installed the main numerical and research packages: NumPy, SciPy, Pandas,
  NetworkX, Numba, Matplotlib, Seaborn, and JupyterLab. Added OR-Tools and HiGHS
  as open-source optimisation tools.
- Prepared the native development toolchain with Apple Clang, CMake, Ninja,
  C++20, pybind11, and scikit-build-core. This environment can later support
  performance-sensitive VNS/TS components without changing the Python-based
  experiment workflow.
- Installed the IBM CPLEX 22.2, DOcplex, and Gurobi 13.0.2 Python packages so
  the project is ready for mathematical modelling once the required academic
  licences and the replication implementation are available.
- Added separate configuration profiles for future paper-comparable experiments
  and local performance experiments. The reproduction profile reserves the
  paper's single-thread setting, fixed random seed, ten repetitions, and
  7,200-second exact-solver time limit.
- Expanded `.gitignore` to exclude virtual environments, caches, build output,
  datasets, generated results, solver files, licence files, credentials, local
  literature, logs, and scratch directories.

**Challenges & blockers**
- The unrestricted IBM CPLEX licence requested through the
  [IBM Academic Initiative](https://www.ibm.com/products/ilog-cplex-optimization-studio/pricing)
  requires identity verification and approval time. Full-scale CPLEX work must
  wait until the academic entitlement is approved and activated.

**Next steps**
- Continue reviewing additional E-VRPTW literature to improve understanding of
  the problem formulation, benchmark conventions, solution methods, and
  potential innovation directions.
- Read the selected primary paper closely and begin mapping its mathematical
  notation, assumptions, and constraints before starting implementation.
- Wait for the IBM Academic Initiative review to finish, then activate the
  unrestricted CPLEX licence.

**Hours spent (optional):** Approximately 40 hours (8 hours per day, Monday to
Friday).

**Links (optional):**
- [Primary paper selection and candidate comparison](reference_selection.md)
- [Project bibliography](references.bib)
- [Environment installation guide](environment.md)
- [Python project dependencies](../pyproject.toml)
- [Locked dependency versions](../uv.lock)
- [Paper-comparable experiment profile](../configs/reproduction.toml)
- [Public E-VRPTW benchmark dataset](https://doi.org/10.17632/h3mrm5dhxw.1)
