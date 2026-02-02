# Config

This folder contains **configuration and tunable parameters** used across the project.
Configurations define *what can be adjusted* without changing core logic. No decision-making or computation should live here.

---

## Purpose

* Centralize all **magic numbers** and defaults
* Allow easy experimentation and tuning
* Keep logic in `models/`, `scoring/`, and `schedule/` clean and readable
* Enable future user-level customization

---
## What Belongs Here

Examples of valid config items:

* Default / neutral values for scoring factors
* Weight coefficients for priority calculation
* Thresholds for switching scheduling modes
* Global limits (e.g., max difficulty per day)
* Feature flags (enable/disable experimental behavior)

Typical files:

```
config/
├── defaults.py        # neutral values, fallbacks
├── weights.py         # scoring and priority weights
├── thresholds.py      # decision cutoffs
└── README.md
```

---
## What Does NOT Belong Here

❌ Any logic or conditionals
❌ Functions with side effects
❌ Data loading or parsing
❌ User-specific or sensitive data

If a value requires computation or context, it belongs elsewhere.

---

## Design Principles

* **Declarative, not procedural**
* Values should be named clearly and self-explanatory
* Prefer constants over derived values
* Changes here should not require refactoring logic

---

## Future Extensions

* External config formats (YAML / JSON)
* Profile-based configs (beginner / intensive / revision)
* UI-driven configuration overrides

---

## Notes

Treat this folder as the system's **control panel** — turning knobs, not changing behavior.
