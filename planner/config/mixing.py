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
