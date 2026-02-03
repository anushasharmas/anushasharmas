# Models

This folder contains **data models and structures** used to represent
subjects, computed scores, and final unit allocations.

Models are **pure representations** — they do not contain scheduling logic.

---

## Design Philosophy

- Models describe *what the data is*, not *what to do with it*
- All heavy computation happens outside models
- Models act as a contract between:
  - scoring
  - scheduling
  - validation
  - output layers

---

## Core Concepts

### Subject Model (Conceptual)

Each subject is described using qualitative attributes provided by the user.
These attributes are later converted into numerical weights by the scoring
system.

Typical attributes include:
- urgency
- available time
- difficulty
- syllabus coverage
- credits
- past performance

Models **do not interpret these attributes** — they only store them.

---

### Score Model

Scores represent the **relative importance or priority** of a subject.

They are computed using configurable maps such as:
- urgency map
- time availability map
- difficulty map
- coverage map
- credits map
- performance map

Scores are:
- comparable across subjects
- intermediate values
- not directly used for scheduling

---

### Final Unit Allocation Model

The final unit allocation represents the **absolute study load**
for each subject.

Example:

```python
final_units = {
    "Maths": 45,
    "Physics": 32,
    "English": 3
}
