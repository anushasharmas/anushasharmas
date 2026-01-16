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
    hours_per_day = 4

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
def allocate_study_units(subject_scores: dict, total_units: int) -> dict:
    """
    Allocate study units proportionally based on subject scores.

    Parameters
    ----------
    subject_scores : dict
        {
            "Maths": 7.5,
            "English": 4.2,
            "Physics": 6.1
        }

    total_units : int
        Total available study units (e.g., 12 units over 3 days)

    Returns
    -------
    dict
        {
            "Maths": 4,
            "English": 2,
            "Physics": 3
        }
    """

    if total_units <= 0:
        raise ValueError("total_units must be greater than 0")

    if not subject_scores:
        return {}

    total_score = sum(subject_scores.values())

    if total_score == 0:
        raise ValueError("Total subject score cannot be zero")

    # Initial proportional allocation
    raw_allocation = {
        subject: (score / total_score) * total_units
        for subject, score in subject_scores.items()
    }

    # Floor values to get base allocation
    allocation = {subject: int(units) for subject, units in raw_allocation.items()}

    # Distribute remaining units (due to rounding)
    remaining_units = total_units - sum(allocation.values())

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
        "Maths": 13.3,
        "English": 6.5,
        "Physics": 10.2
    }

    subject_units = allocate_study_units(scores, total_units=total_units)
    print(subject_units)
    
print("\nAllocated study units:")
    for subject, units in subject_units.items():
        print(f"{subject}: {units}")
print(sum(subject_units.values()))
