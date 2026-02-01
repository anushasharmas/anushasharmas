from typing import Dict, List
from collections import defaultdict
hours_per_day=8 #Its already defined in the timetable_generator.py function.

DIFFICULTY_MAP = {
    "hard": 1.3,
    "medium": 1.0,
    "easy": 0.8
}


def generate_light_mixed_schedule(
    subject_units: Dict[str, int],
    subject_difficulty: Dict[str, str],
    units_per_day: int = hours_per_day,
    max_subjects_per_day: int = 3
) -> Dict[int, List[str]]:
    """
    Case 2: Light Mixing Scheduler

    Rules:
    - 2–3 subjects per day (max_subjects_per_day)
    - No subject takes more than half the daily units consecutively
    - Difficulty guides daily priority (hard > medium > easy)
    """

    remaining_units = final_units.copy()
    schedule = {}
    day = 1

    while any(units > 0 for units in remaining_units.values()):
        daily_plan = []
        consecutive_count = defaultdict(int)
        last_subject = None

        # Select eligible subjects for the day
        active_subjects = [
            s for s, u in remaining_units.items() if u > 0
        ]

        # Sort by difficulty weight and remaining units
        active_subjects.sort(
            key=lambda s: (
                DIFFICULTY_MAP[subject_difficulty[s]],
                remaining_units[s]
            ),
            reverse=True
        )

        # Limit subjects for the day
        active_subjects = active_subjects[:max_subjects_per_day]

        for _ in range(units_per_day):
            # Pick next valid subject
            for subject in active_subjects:
                if remaining_units[subject] == 0:
                    continue

                if subject == last_subject and consecutive_count[subject] >= units_per_day // 2:
                    continue

                # Assign unit
                daily_plan.append(subject)
                remaining_units[subject] -= 1

                if subject == last_subject:
                    consecutive_count[subject] += 1
                else:
                    consecutive_count[subject] = 1

                last_subject = subject
                break

        schedule[day] = daily_plan
        day += 1

    return schedule
final_units ={"English":2,
              "Maths":65,
              "Physics":13
             }
schedule = generate_light_mixed_schedule(
    subject_units=final_units,
    subject_difficulty={
        "Maths": "hard",
        "Physics": "hard",
        "English": "easy"
    },
    units_per_day=hours_per_day
)
for day, plan in schedule.items():
    print(f"Day {day}: {plan}")
