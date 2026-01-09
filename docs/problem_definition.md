# Adaptive Exam Study Planner – Problem Definition

## 1. Problem Statement
Students preparing for exams often struggle to create effective study plans that
account for multiple subjects, varying priorities, deadlines, and personal constraints.
Most existing planners are static and do not adapt when conditions change.

This project aims to build an adaptive study planner that dynamically generates
personalized study timetables based on priorities, constraints, and preferences.

## 2. Target Users
- Students preparing for competitive or academic exams
- Learners managing multiple subjects simultaneously
- Users with limited daily study time

## 3. Inputs
- Subjects and topics
- Exam dates or deadlines
- Priority or weight/credits for each subject
- Available study hours per day
- User preferences (fatigue, difficulty level)
- Subject affinity or comfort level
- Percentage of syllabus already completed
  
## 4. Constraints
- Fixed exam deadlines
- Maximum study hours per day
- Uneven subject difficulty
- Need for revision and rest days

## 5. Expected Output
- Daily and weekly study schedules
- Balanced time allocation across subjects
- Automatic adjustment when inputs change
- Ability to dynamically redistribute study time if a planned session is missed

## Adaptation Logic (High-Level)
If a scheduled study session is missed, the system should re-optimize the remaining
schedule to maintain overall efficiency while respecting constraints and priorities.
