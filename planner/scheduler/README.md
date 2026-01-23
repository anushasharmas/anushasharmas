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

## How the Scheduler Works

1. The user provides subjects along with relative parameters such as:
   - Difficulty level
   - Time required compared to other subjects

2. These parameters are converted into weighted points.

3. Subjects with higher total points are allocated more study units.

4. While generating the timetable:
   - Very difficult subjects are not placed back-to-back
   - Sessions can be either:
     - A long session of a single subject, or
     - Multiple subjects split within a day

This approach keeps the base logic simple while allowing future extensions
like fatigue handling, revision buffers, and adaptive rescheduling.
