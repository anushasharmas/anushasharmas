# Scheduler

This module contains the core scheduling logic responsible for generating
adaptive study timetables based on user inputs and defined constraints.

It uses the output from the scoring module to prioritize subjects or tasks
according to their computed weightage, and allocates the remaining available
study time in an efficient and balanced manner.

## Current Responsibilities

- Convert total available study time into discrete study units
- Allocate study units proportionally based on subject scores
- Ensure:
  - No fractional study units
  - Total allocated units exactly match available units
  - Fair distribution when rounding is required

---
