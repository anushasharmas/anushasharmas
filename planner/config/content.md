# Configuration

This folder contains user-controlled and system-level configuration
that influences scheduling behavior without modifying core logic.

All values defined here are **inputs** to the scheduler, not scheduling
algorithms themselves.

---

## Design Principles

- Configuration defines **constraints and preferences**, not logic.
- Scheduler behavior must change by adjusting config values only.
- Config must remain stable even if scheduling strategies evolve.

---

## Mixing Configuration

Mixing controls how many consecutive study units of a single subject
are allowed within a day.

Instead of fixed scheduling modes (e.g., light / heavy mixing),
the system uses a **maximum consecutive unit constraint**.

### Mixing Presets

Defined in `mixing.py`:

```python
MIXING_PRESETS = {
    "none": 1.0,     # no mixing
    "low": 0.7,
    "medium": 0.5,
    "high": 0.3
}
