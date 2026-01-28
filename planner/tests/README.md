# Tests

This folder contains automated tests that verify the correctness,
stability, and expected behavior of the planner system.

Tests are designed to:
- Validate individual units of logic (unit tests)
- Catch regressions when code changes
- Ensure constraints, scoring, and scheduling behave as expected

## What Belongs Here

- Unit tests for pure functions
- Edge-case validations
- Deterministic tests with fixed inputs and expected outputs
- Regression tests for previously fixed bugs

Examples:
- Scoring function returns expected score for given inputs
- Study unit distributor respects daily limits
- Constraint violations are correctly detected

## What Does NOT Belong Here

- Manual experiments or exploratory runs
- Scripts that print output for inspection
- One-off sanity checks
- Performance benchmarks without assertions

## Notes

- Tests should be deterministic and repeatable
- No randomness unless explicitly controlled
- Prefer small, focused tests over large end-to-end runs
