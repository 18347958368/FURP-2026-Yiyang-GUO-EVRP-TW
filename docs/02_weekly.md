# Week 2 Progress Log

### Week 2 — 2026-06-21

**Attended this week's meeting:** Yes.

**Progress this week**
- Installed Ubuntu 26.04 Desktop ARM64 on the Apple Silicon MacBook Pro using
  UTM and QEMU virtualisation. Configured the virtual machine with 8 virtual
  CPUs, 8 GiB of memory, a 64 GB virtual disk, and UTM shared networking.
- Prepared the Ubuntu environment for research and development. Configured
  Chinese language support and CJK fonts, local SmartDNS resolution, Codex CLI,
  SPICE clipboard integration, and a VirtFS shared-directory mount between
  macOS and Ubuntu. DNS and HTTP connectivity were verified for both domestic
  and international sites.
- Systematically read Schneider, Stenger, and Goeke (2014), *The Electric
  Vehicle-Routing Problem with Time Windows and Recharging Stations*. Reviewed
  the E-VRPTW definition and assumptions, mathematical formulation, benchmark
  instances, hybrid Variable Neighborhood Search/Tabu Search (VNS/TS)
  algorithm, parameter settings, and computational experiments.
- Documented the remaining virtual-machine usability checks rather than
  treating the setup as fully complete. End-to-end clipboard behaviour,
  VirtFS write access for the normal Ubuntu user, and display-window fitting
  still require final verification.

**Challenges & blockers**
- Academic licence verification remains unresolved for both IBM CPLEX and
  Gurobi. Their Python interfaces are installed, but unrestricted academic
  licences are not yet available, so paper-scale experiments that depend on
  these commercial solvers cannot currently be run.

**Next steps**
- Obtain and parse the public E-VRPTW benchmark instances used by the selected
  paper.
- Implement the paper's core data structures, mathematical formulation, and
  route-feasibility checks.
- Reproduce small-instance results first. If the commercial solver licences
  remain unavailable, use the open-source HiGHS solver to validate the model
  and implementation where possible.
- Begin implementing the paper's hybrid VNS/TS baseline after the parser and
  small-instance validation workflow are working.

**Links (optional):**
- [Primary paper selection and replication boundary](reference_selection.md)
- [Local research environment and solver setup](environment.md)
- [Paper-comparable experiment profile](../configs/reproduction.toml)
- [Public E-VRPTW benchmark dataset](https://doi.org/10.17632/h3mrm5dhxw.1)
