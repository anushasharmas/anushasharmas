from datetime import date

def compute_total_study_units(
    exam_date: date,
    today: date,
    study_days_per_week: int,
    hours_per_day: int
) -> int:
    """
    Returns total available study units (1 unit = 1 hour)
    """

    days_left = (exam_date - today).days
    if days_left <= 0:
        return 0

    # Average study days available
    effective_study_days = (days_left / 7) * study_days_per_week

    total_units = int(effective_study_days * hours_per_day)

    return max(total_units, 0)

total_units = compute_total_study_units(
    exam_date=exam_date,
    today=date.today(),
    study_days_per_week=5,
    hours_per_day=4
)

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
        "Maths": 7.5,
        "English": 4.2,
        "Physics": 6.1
    }

    units = allocate_study_units(scores, total_units=total_units)
    print(units)
    
subject_units = allocate_study_units(
    subject_scores,
    total_units
)
print(subject_units)
print("\nAllocated study units:")
    for subject, units in allocation.items():
        print(f"{subject}: {units}")
