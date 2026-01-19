# Utilities

Helper functions for validation, time calculations, and common operations
used across the planner system.

This folder contains shared helper functions that are used across
multiple parts of the project.

The goal of the `utils` module is to:
- Avoid code duplication
- Keep core logic files clean and focused
- Centralize commonly used calculations and validations

## What Belongs Here

Typical responsibilities of utility functions include:
- Date and time calculations
- Common mathematical or logical helpers
- Input validation helpers
- Reusable formatting or conversion functions

## Design Philosophy

Utility functions should:
- Be small and single-purpose
- Avoid side effects
- Be easy to test and reuse
- Remain independent of business-specific logic

Keeping utilities well-defined makes the project easier to maintain
and extend in the future.
