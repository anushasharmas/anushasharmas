# Data

This folder contains sample input data and datasets used to evaluate
and validate the planner logic.
The data here supports development, testing, and experimentation,
and is intentionally kept separate from core logic.

## Directory Structure

- `raw/`  
  Original, unmodified data sources.  
  These files should be treated as read-only.

- `processed/`  
  Cleaned, transformed, or derived datasets used by the system
  during modeling, analysis, or mock runs.

- `external/`  
  Third-party or externally sourced data files.

## Guidelines

- Do not modify files inside `raw/`
- All data processing or transformation logic lives in `/scripts`
- Large or sensitive datasets are excluded from version control
- Data files should remain static and free of executable code

## Notes

- This folder should not contain business logic or experiments
- Executable sanity checks or mock runs b
