# Models

This folder contains the core decision-making logic that transforms inputs (exam metadata, mock scores, constraints) into scheduling and allocation outcomes.

---
## Project Decisions & Rationale

### Scheduling Strategy

* Support two primary modes:

  1. **Long single-subject sessions** — suited for deep work and revision-heavy days.
  2. **Multiple subjects per day** — suited for breadth, momentum, and spaced practice.
* Avoid scheduling **back-to-back high-difficulty subjects** to reduce cognitive fatigue and burnout.

### Design Philosophy

* **Logic clarity over micro-optimizations** to keep behavior predictable and debuggable.
* Decisions are **explicitly documented** to support future refactoring, testing, and extension.
* Prefer deterministic rules with configurable parameters over opaque heuristics.

---

## Scope & Responsibilities

* Translate subject scores and constraints into scheduling decisions.
* Apply fatigue-aware rules and mode selection.
* Remain independent of I/O, UI, and data persistence.

---

## Future Considerations

* Per-subject **difficulty tagging** and adaptive difficulty scaling.
* **Energy-based scheduling** (time-of-day effectiveness).
* Personalization hooks (user preferences, historical performance).
* Pluggable strategy interface for experimenting with alternative models.

---

## Non-Goals

* Data ingestion and cleaning (handled in `data/`).
* Presentation/UI logic.
* Long-term storage or versioning of outputs.
