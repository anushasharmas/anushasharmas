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

    units = allocate_study_units(scores, total_units=12)
    print(units)
