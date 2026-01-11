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
    "low": 1.0,
    "medium": 0.8,
    "high": 0.6
}

if __name__ == "__main__":
    maths_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["close"],
        relative_time_needed=TIME_MAP["most"],
        difficulty=DIFFICULTY_MAP["hard"],
        credits=1.2,
        coverage_modifier=COVERAGE_MAP["medium"]
    )

    english_score = compute_subject_score(
        exam_urgency=URGENCY_MAP["close"],
        relative_time_needed=TIME_MAP["least"],
        difficulty=DIFFICULTY_MAP["easy"],
        credits=1.0,
        coverage_modifier=COVERAGE_MAP["low"]
    )

    print("Maths score:", maths_score)
    print("English score:", english_score)

if __name__ == "__main__":
    main()
