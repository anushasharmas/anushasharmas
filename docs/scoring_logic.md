# Scoring Logic – V1 Design

This document defines the scoring strategy used by the adaptive exam
study planner to prioritize subjects and allocate study time in a
balanced and explainable manner.

The system is designed to work with minimal user input while still
handling differences in syllabus size, difficulty, and exam structure.

---

## Design Principles

- Prefer relative judgments over absolute percentages
- Minimize cognitive load on the user
- Separate priority estimation from scheduling execution
- Use deterministic and explainable logic

---

## Core Scoring Factors

These factors primarily determine how much total study time a subject
should receive.

### 1. Exam Urgency
Represents how close the exam date is. Subjects with nearer exams are
assigned higher urgency scores to ensure adequate preparation time.

Urgency influences *total time allocation*, while revision proximity
is handled later by the scheduler.

---

### 2. Relative Effort
A subjective estimate of how much total time a subject is expected to
require compared to others.

Users may classify subjects as:
- Most time
- Medium (default)
- Least time

This factor implicitly captures syllabus size, practice requirements,
and perceived workload.

---

### 3. Relative Difficulty
Represents perceived difficulty of the subject. This may be expressed
as:
- Bucketed values (Easy / Medium / Hard), or
- A relative ranking or scale (e.g., 1–10)

Difficulty captures conceptually hard or application-heavy subjects
without explicitly labeling subject types.

---

### 4. Credits / Subject Weightage
Accounts for the academic importance of the subject based on credits,
marks contribution, or institutional weightage.

Subjects with higher academic impact receive proportionally higher
priority.

---

## Modifier Factors

These factors adjust the base score without dominating the allocation.

### 5. Exam Gap / Spacing
Accounts for the spacing between exams:
- Consecutive or closely spaced exams may slightly increase priority
- Longer gaps may slightly reduce urgency

This helps manage cognitive load during dense exam schedules.

---

### 6. Coverage Modifier
Used only as a dampening factor rather than an absolute progress measure.
Higher coverage slightly reduces priority but never removes a subject
from consideration.

---

### 7. Performance Risk
Accounts for historical performance or confidence levels:
- Subjects previously failed
- Subjects with consistently low scores
- Subjects requiring extra reinforcement

This factor ensures weak areas are not neglected.

---

## Score Calculation (Conceptual)

The final score for each subject is computed as a weighted combination
of core factors, followed by modifier adjustments.

Scores are normalized and passed
