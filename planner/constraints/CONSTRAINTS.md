# =======================================================
# Scheduling Constraints & Design Principles
# =======================================================

# ----------------------------
# 1. Cognitive Constraints
# ----------------------------
# - Avoid cognitive overload:
#   High-difficulty or high-focus subjects should not be scheduled
#   in consecutive study blocks.
#
# - Energy-aware placement:
#   Subjects requiring sustained concentration should be placed
#   earlier in the day where possible.
#
# - Variety for retention:
#   Lighter or low-focus subjects may be interleaved between
#   heavy subjects to reduce fatigue.


# ----------------------------
# 2. Time Constraints
# ----------------------------
# - Daily capacity limit:
#   Total study units scheduled per day must not exceed the
#   user-defined daily limit.
#
# - Session flexibility:
#   Longer study sessions are optional and should only be
#   scheduled when explicitly preferred by the user.
#
# - Sustainable pacing:
#   Avoid aggressive front-loading that may cause burnout,
#   unless exam urgency strongly requires it.


# ----------------------------
# 3. User Constraints
# ----------------------------
# - User preference precedence:
#   Explicit user preferences (subject order, preferred time slots,
#   rest days) override default scheduling logic.
#
# - Adaptive flexibility:
#   The schedule should support easy reshuffling without breaking
#   overall subject balance.
#
# - Graceful degradation:
#   When constraints conflict, relax lower-priority rules instead
#   of failing or over-optimizing.


# ----------------------------
# 4. System Design Boundaries (Non-Goals)
# ----------------------------
# - No global optimization guarantee:
#   The planner does not attempt to find a globally optimal schedule.
#
# - Explainability over complexity:
#   Scheduling decisions should remain transparent and easy to
#   understand for the user.
#
# - Incremental refinement:
#   The system favors s
