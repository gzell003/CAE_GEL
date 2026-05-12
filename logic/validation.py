from config import BUDGET_OPTIONS, MOOD_OPTIONS


def validate_mood(selected_mood: str) -> bool:
    return selected_mood in MOOD_OPTIONS


def validate_budget(selected_budget: str) -> bool:
    return selected_budget in BUDGET_OPTIONS
