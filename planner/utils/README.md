# Utilities

This module contains shared helper functions used across multiple parts
of the planner system.

Utilities support the core logic but do not make scheduling, scoring,
or allocation decisions themselves.

The purpose of the `utils` module is to:
- Avoid code duplication
- Keep core logic modules clean and focused
- Centralize reusable calculations and validations
- Provide stable, low-level building blocks

---

## What Belongs Here

Utility functions should be generic and reusable across the project.
Typical responsibilities include:

- Date and time calculations  
  (e.g., days until exam, date normalization)
- Common mathematical helpers  
  (e.g., normalization, safe division, rounding helpers)
- Input validation and sanity checks  
  (e.g., non-negative units, valid ranges)
- Lightweight formatting or conversion helpers  
  (e.g., hours ↔ study units)

---

## What Does NOT Belong Here

- Business or domain-specific logic  
  (e.g., subject scoring, scheduling decisions)
- Constraint enforcement
- User preference handling
- State management or orchestration logic

If a function requires knowledge of *why* something is scheduled,
it does not belong in `utils`.

---

## Design Philosophy

Utility functions should:
- Be small and single-purpose
- Avoid side effects and hidden state
- Be easy to test and reuse
- Remain independent of planner-specific workflows

Utilities are treated as **pure helpers**, not decision-makers.

---

## Guiding Principle

If removing a utility function would require rewriting logic in multiple
places, it belongs here.  
If removing it changes planner behavior, it probably does not.
