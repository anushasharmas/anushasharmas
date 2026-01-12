# Scoring

This module analyses the provided inputs and assigns a numerical score to
each subject or task based on factors such as difficulty, importance,
credits, and exam proximity.

The computed scores are used to simplify decision-making and enable efficient
and proportional allocation of available study time during scheduling.

## Scoring Module – Design Overview

The scoring system assigns an importance score to each subject based on
multiple interpretable factors.

### Data Maps
The module uses static maps to convert user-friendly inputs into
numeric representations:

- Urgency map (exam proximity)
- Relative time needed map
- Difficulty map
- Credits / weightage map
- Performance risk map
- Coverage map (syllabus completion)

### Coverage Handling
Coverage represents progress, not priority. Lower coverage increases
priority through an inverse coverage modifier function.

### Functions
- `compute_subject_score()` combines all factors into a final score
- `get_coverage_modifier()` converts syllabus completion into a
  priority boost

This separation keeps data representation and decision logic clean
and extensible.

points_allocator.py
├── URGENCY_MAP, TIME_MAP, DIFFICULTY_MAP, etc.    (static maps)
├── get_coverage_modifier()                        (domain logic)
├── compute_subject_score()                        (core scoring)
├── compute_score_from_inputs(user_inputs)         (this kwargs orchestration)
└── if __name__ == "__main__":                     (example/test run)
