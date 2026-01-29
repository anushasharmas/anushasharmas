# Constraints

This module defines the rules and limits that guide how study units are
distributed across days and within a day.

Constraints do not determine *how important* a subject is (that is handled
by the scoring system). Instead, they control *how and when* allocated study
units may be scheduled.

The goal of this module is to ensure that generated timetables remain
realistic, flexible, and cognitively sustainable.

---
## Scope of Constraints

### Cognitive Constraints
- Prevent scheduling high-difficulty or high-focus subjects back-to-back.
- Prefer placing demanding subjects earlier in the day when possible.
- Allow lighter subjects to be used as buffers to reduce mental fatigue.

### Time Constraints
- Enforce a maximum daily study limit defined by the user.
- Avoid forcing long, continuous study sessions unless explicitly preferred.
- Support sustainable pacing over aggressive front-loading.

### User Constraints
- Respect explicit user preferences such as:
  - Subject ordering
  - Preferred study times
  - Rest days or lighter days
- Allow user preferences to override default scheduling behavior.
- Prioritize flexibility and easy rescheduling.

---

## Design Principles

- Constraints are treated as **soft rules**, not hard blockers.
- When conflicts arise, lower-priority constraints may be relaxed.
- Explainability is preferred over complex optimization.
- The system favors predictable, human-like schedules.

---

## Non-Goals

- This module does not attempt to compute globally optimal schedules.
- It does not enforce rigid or irreversible scheduling decisions.
- Complex heuristics and optimization algorithms are intentionally avoided.

---

## Current Status

- Constraint logic is currently defined conceptually.
- Concrete enforcement will be applied during the day-by-day distribution phase.
- Additional constraints may be layered incrementally as the scheduler evolves.
