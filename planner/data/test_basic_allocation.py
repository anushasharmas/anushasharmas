# planner/scoring/points_allocator.py
def compute_subject_score(
    exam_urgency: float,
    relative_time_needed: float = 1.0,
    difficulty: float = 1.0,
    credits: float = 1.0,
    coverage_modifier: float = 1.0,
    performance_risk: float = 1.0,
    exam_gap_modifier: float = 1.0
) -> float:
  
    score = (
        exam_urgency
        * relative_time_needed
        * difficulty
        * credits
        * coverage_modifier
        * performance_risk
        * exam_gap_modifier
    )

    return round(score, 3)


URGENCY_MAP = {
    "very_close": 1.5,   # <= 7 days
    "close": 1.2,        # 8–21 days
    "far": 1.0           # > 21 days
}

TIME_MAP = {
    "most": 1.5,
    "medium": 1.0,
    "least": 0.7
}

DIFFICULTY_MAP = {
    "hard": 1.3,
    "medium": 1.0,
    "easy": 0.8
}

COVERAGE_MAP = {
    "just_started": 0.1,
    "partial": 0.4,
    "mostly": 0.7,
    "almost_done": 0.9,
}

CREDITS_MAP = {
    "high":1.2,
    "normal":1,
    "low":0.8
}

PERFORMANCE_MAP = {
    "poor": 1.2,
    "okay":1,
    "well":0.8
}
def get_coverage_modifier(coverage_level: str) -> float:
    """
    Converts coverage level into a priority modifier.
    Lower coverage -> higher modifier.
    """
    coverage_value = COVERAGE_MAP.get(coverage_level, 0.4)
    return 1 - coverage_value

def compute_score_from_inputs(user_inputs: dict) -> float:
   

    # exam_urgency is mandatory
    if "exam_urgency" not in user_inputs:
        raise ValueError("exam_urgency is required to compute score")

    score_params = {
        "exam_urgency": URGENCY_MAP[user_inputs["exam_urgency"]]
    }

    # Optional parameters (only added if user provides input)
    if user_inputs.get("relative_time_needed"):
        score_params["relative_time_needed"] = TIME_MAP[user_inputs["relative_time_needed"]]

    if user_inputs.get("difficulty"):
        score_params["difficulty"] = DIFFICULTY_MAP[user_inputs["difficulty"]]

    if user_inputs.get("credits"):
        score_params["credits"] = CREDITS_MAP[user_inputs["credits"]]

    if user_inputs.get("performance_risk"):
        score_params["performance_risk"] = PERFORMANCE_MAP[user_inputs["performance_risk"]]

    if user_inputs.get("coverage_modifier"):
        score_params["coverage_modifier"] = get_coverage_modifier(user_inputs["coverage_modifier"])

    return compute_subject_score(**score_params)
   
if __name__ == "__main__":
    maths_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["very_close"],
        relative_time_needed=TIME_MAP["most"],
        difficulty=DIFFICULTY_MAP["hard"],
        credits=CREDITS_MAP["high"],
        performance_risk=PERFORMANCE_MAP["poor"],
        coverage_modifier=get_coverage_modifier("just_started")
    )

    english_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["far"],
        relative_time_needed=TIME_MAP["least"],
        difficulty=DIFFICULTY_MAP["easy"],
        credits=CREDITS_MAP["low"],
        performance_risk=PERFORMANCE_MAP["well"],
        coverage_modifier=get_coverage_modifier("almost_done")
    )
  
    physics_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["close"],
        relative_time_needed=TIME_MAP["medium"],
        difficulty=DIFFICULTY_MAP["medium"],
        credits=CREDITS_MAP["normal"],
        performance_risk=PERFORMANCE_MAP["okay"],
        coverage_modifier=get_coverage_modifier("partial")
    )
    print("Maths score:", maths_score)
    print("English score:", english_score)
    print("Physics score:", physics_score)

if __name__ == "__main__":
    # Case 1: Only exam urgency provided
    user_inputs = {
        "exam_urgency": "close"
    }

    score = compute_score_from_inputs(user_inputs)
    print("Score with only exam_urgency:", score)

if __name__ == "__main__":
    # Case 2: exam urgency + difficulty
    user_inputs = {
        "exam_urgency": "close",
        "difficulty": "hard"
    }

    score = compute_score_from_inputs(user_inputs)
    print("Score with urgency + difficulty:", score)

if __name__ == "__main__":
    # Case 3a: No coverage input
    score_no_coverage = compute_score_from_inputs({
        "exam_urgency": "close"
    })

    # Case 3b: Coverage provided
    score_with_coverage = compute_score_from_inputs({
        "exam_urgency": "close",
        "coverage_modifier": "just_started"
    })

    print("Score without coverage:", score_no_coverage)
    print("Score with coverage:", score_with_coverage)

from datetime import date

def calculate_days_left(exam_date: date) -> int:
    today = date.today()
    return max((exam_date - today).days, 0)

def calculate_total_study_units(
    exam_date: date,
    study_days: int,
    hours_per_day: int
) -> int:
    days_left = calculate_days_left(exam_date)
    effective_days = min(study_days, days_left)
    return effective_days * hours_per_day

if __name__ == "__main__":
    exam_date = date(2026, 2, 20)

    study_days = 10
    hours_per_day = 8

    total_units = calculate_total_study_units(
        exam_date,
        study_days,
        hours_per_day
    )

    print(f"Total study units: {total_units}")
    
# Allocates total study units across subjects based on their relative scores.
# Higher score → more units.
# Uses proportional allocation + fair rounding.
# Example: If Maths has highest score, it gets the most units.
def allocate_study_units(subject_scores: dict, unreserved_units: int) -> dict:
    

    if total_units <= 0:
        raise ValueError("total_units must be greater than 0")

    if not subject_scores:
        return {}

    total_score = sum(subject_scores.values())

    if total_score == 0:
        raise ValueError("Total subject score cannot be zero")

    # Initial proportional allocation
    raw_allocation = {
        subject: (score / total_score) * unreserved_units
        for subject, score in subject_scores.items()
    }

    # Floor values to get base allocation
    allocation = {subject: int(units) for subject, units in raw_allocation.items()}

    # Distribute remaining units (due to rounding)
    remaining_units = unreserved_units - sum(allocation.values())

    # Sort subjects by largest fractional remainder
    remainders = sorted(
        raw_allocation.items(),
        key=lambda item: item[1] - int(item[1]),
        reverse=True
    )

    for subject, _ in remainders:
        if remaining_units == 0:
            break
        allocation[subject] += 1
        remaining_units -= 1

    return allocation

if __name__ == "__main__":
    scores = {
        "Maths": maths_score,
        "English": english_score,
        "Physics": physics_score
    }
    reserved_units = len(scores)  # 1 unit per subject
    unreserved_units = total_units - reserved_units
    subject_units = allocate_study_units(scores, unreserved_units=unreserved_units)
    final_units = {subject: round(units + 1) for subject, units in subject_units.items()}
   

print("\nAllocated study units:")
for subject, units in final_units.items():
        print(f"{subject}: {units}")
print(sum(final_units.values()))

def distribute_units_across_days(
    subject_units: dict,
    total_days: int,
    hours_per_day: int,
    diversity: float
) -> dict:
    """
    Distributes subject study units across days.

    Parameters:
    - subject_units: dict[str, int]
        Final units per subject (sum = total_units)
    - total_days: int
        Number of days available
    - hours_per_day: int
        Max study units per day
    - diversity: float (0–1)
        Controls how many subjects appear per day

    Returns:
    - timetable: dict[int, dict[str, int]]
        Day-wise subject-unit allocation
    """
    pass

def distribute_units_across_days(subject_units, total_days, hours_per_day, diversity):
    # Decide max subjects per day
    if diversity <= 0.3:
        max_subjects = 1
    elif diversity <= 0.7:
        max_subjects = 2
    else:
        max_subjects = len(subject_units)

    remaining = subject_units.copy()
    timetable = {}

    for day in range(1, total_days + 1):
        timetable[day] = {}
        capacity = hours_per_day

        # Pick subjects with most remaining units
        available_subjects = sorted(
            [s for s in remaining if remaining[s] > 0],
            key=lambda s: remaining[s],
            reverse=True
        )

        subjects_today = available_subjects[:max_subjects]

        for subject in subjects_today:
            if capacity == 0:
                break
            if remaining[subject] == 0:
                continue

            timetable[day][subject] = 1
            remaining[subject] -= 1
            capacity -= 1

    return timetable
