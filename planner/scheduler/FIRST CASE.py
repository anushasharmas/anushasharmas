from typing import Dict, List
hours_per_day=8 #Its already defined in the timetable_generator.py function.
def generate_sequential_schedule(
    subject_units: Dict[str, int],
    subject_order: List[str],
    units_per_day: int = hours_per_day
) -> Dict[int, List[str]]:
    """
    Generates a study schedule where subjects are completed sequentially.

    Args:
        subject_units: total units required per subject
        subject_order: order in which subjects should be studied
        units_per_day: number of study units per day

    Returns:
        Dictionary mapping day number -> list of subjects studied that day
    """
    # Copy to avoid mutating input
    remaining_units = subject_units.copy()

    schedule = {}
    day = 1
    subject_index = 0

    while subject_index < len(subject_order):
        daily_plan = []
        units_left_today = units_per_day

        while units_left_today > 0 and subject_index < len(subject_order):
            subject = subject_order[subject_index]

            if remaining_units[subject] > 0:
                daily_plan.append(subject)
                remaining_units[subject] -= 1
                units_left_today -= 1
            else:
                # Move to next subject once current is exhausted
                subject_index += 1

        schedule[day] = daily_plan
        day += 1

    return schedule
final_units ={"English":2,
              "Maths":65,
              "Physics":13
             }
subject_units = final_units
subject_order = ["English", "Maths", "Physics"]

schedule = generate_sequential_schedule(subject_units, subject_order)

for day, plan in schedule.items():
    print(f"Day {day}: {plan}")
