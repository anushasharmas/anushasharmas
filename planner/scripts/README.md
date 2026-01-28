# Scripts

This folder contains executable helper scripts used for:
- Manual testing
- Sanity checks
- Experiments
- Prototyping and debugging

Scripts help validate system behavior during development
before logic is formalized into automated tests.

## What Belongs Here

- Mock runs combining multiple modules
- Exploratory executions to inspect outputs
- Temporary experiments with example values
- CLI-style runners for local testing

Examples:
- Running scoring and scheduling together with sample inputs
- Inspecting study unit distribution behavior
- Debugging interactions between modules

## What Does NOT Belong Here

- Core business logic
- Reusable library code
- Automated unit tests
- Static datasets

## Notes

- Scripts may be deleted or refactored over time
- Stable logic discovered here should eventually be moved into tests
- Scripts are allowed to print, log, or visually inspect results
