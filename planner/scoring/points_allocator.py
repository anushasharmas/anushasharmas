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
    """
    Computes a priority score for a subject based on multiple factors.

    All inputs are expected to be relative weights.
    Defaults represent a neutral value.
    """

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
    """
    Converts user-friendly inputs into numeric values and computes
    the final subject score using default-safe kwargs orchestration.

    user_inputs example:
    {
        "exam_urgency": "close",
        "relative_time_needed": "most",
        "difficulty": "hard",
        "credits": "high",
        "performance_risk": "poor",
        "coverage_modifier": "just_started",
        
    }
    """

    # exam_urgency is mandatory
    if "exam_urgency" not in user_inputs:
        raise ValueError("exam_urgency is required to compute score")

    kwargs = {
        "exam_urgency": URGENCY_MAP[user_inputs["exam_urgency"]]
    }

    # Optional parameters (only added if user provides input)
    if user_inputs.get("relative_time_needed"):
        kwargs["relative_time_needed"] = TIME_MAP[user_inputs["relative_time_needed"]]

    if user_inputs.get("difficulty"):
        kwargs["difficulty"] = DIFFICULTY_MAP[user_inputs["difficulty"]]

    if user_inputs.get("credits"):
        kwargs["credits"] = CREDITS_MAP[user_inputs["credits"]]

    if user_inputs.get("performance_risk"):
        kwargs["performance_risk"] = PERFORMANCE_MAP[user_inputs["performance_risk"]]

    if user_inputs.get("coverage_modifier"):
        kwargs["coverage_modifier"] = get_coverage_modifier(user_inputs["coverage_modifier"])

    return compute_subject_score(**kwargs)

if __name__ == "__main__":
    maths_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["close"],
        relative_time_needed=TIME_MAP["most"],
        difficulty=DIFFICULTY_MAP["hard"],
        credits=CREDITS_MAP["high"],
        performance_risk=PERFORMANCE_MAP["poor"],
        coverage_modifier=get_coverage_modifier("just_started")
    )

    english_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["close"],
        relative_time_needed=TIME_MAP["least"],
        difficulty=DIFFICULTY_MAP["easy"],
        credits=CREDITS_MAP["normal"],
        performance_risk=PERFORMANCE_MAP["okay"],
        coverage_modifier=get_coverage_modifier("mostly")
    )

    print("Maths score:", maths_score)
    print("English score:", english_score)

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

if __name__ == "__main__":
    main()
