MIXING_PRESETS = {
    "none": 1.0,      # no mixing
    "low": 0.7,
    "medium": 0.5,
    "high": 0.3
}

def resolve_max_consecutive_units(
    units_per_day: int,
    mixing_level: str
) -> int:
    percent = MIXING_PRESETS[mixing_level]
    return max(1, int(percent * units_per_day))
if subject == last_subject and consecutive_count[subject] >= max_consecutive:
    continue
from typing import Dict, List
from collections import defaultdict

DIFFICULTY_MAP = {
    "hard": 1.3,
    "medium": 1.0,
    "easy": 0.8
}


def generate_schedule(
    final_units: Dict[str, int],
    subject_difficulty: Dict[str, str],
    units_per_day: int,
    max_consecutive: int,
    max_subjects_per_day: int = 3
) -> Dict[int, List[str]]:
    """
    Unified scheduler using max consecutive units as mixing control.
    """

    remaining = final_units.copy()
    schedule = {}
    day = 1

    while any(u > 0 for u in remaining.values()):
        daily_plan = []
        consecutive = defaultdict(int)
        last_subject = None

        # Pick subjects still pending
        active_subjects = [s for s, u in remaining.items() if u > 0]

        # Sort by difficulty, then remaining units
        active_subjects.sort(
            key=lambda s: (
                DIFFICULTY_MAP[subject_difficulty[s]],
                remaining[s]
            ),
            reverse=True
        )

        active_subjects = active_subjects[:max_subjects_per_day]

        for _ in range(units_per_day):
            for subject in active_subjects:
                if remaining[subject] == 0:
                    continue

                if subject == last_subject and consecutive[subject] >= max_consecutive:
                    continue

                # assign
                daily_plan.append(subject)
                remaining[subject] -= 1

                if subject == last_subject:
                    consecutive[subject] += 1
                else:
                    consecutive[subject] = 1
                    last_subject = subject

                break

        schedule[day] = daily_plan
        day += 1

    return schedule
