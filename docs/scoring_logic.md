# Scoring Logic – V1 Design

This document outlines the initial scoring strategy used by the adaptive
exam study planner to prioritize subjects and allocate study time.

## Design Principles
- Minimize user input while maintaining meaningful prioritization
- Use relative measures instead of absolute percentages
- Prefer explainable and deterministic logic over opaque heuristics

## Scoring Factors

### 1. Exam Urgency
Represents how close the exam date is. Subjects with nearer exams are
assigned higher urgency scores.

### 2. Relative Effort
A subjective estimate of how much total time a subject is expected to
require. Users may classify subjects as:
- Most time
- Medium (default)
- Least time

### 3. Difficulty
Represents perceived subject difficulty and captures application-heavy
or conceptually hard subjects implicitly.

### 4. Coverage Modifier
Used only as a dampening factor rather than an absolute progress measure.
Higher coverage slightly reduces priority but never eliminates it.

## Score Calculation

The final score for each subject is computed multiplicatively:

score = urgency × effort × difficulty × coverage_modifier

These scores are later normalized and used by the scheduler to distribute
available study time proportionally across subjects.
