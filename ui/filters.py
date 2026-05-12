from config import BUDGET_OPTIONS


def filter_events(events: list, mood: str, budget: str) -> list:
    budget_limit = BUDGET_OPTIONS[budget]

    filtered = []

    for event in events:
        matches_mood = mood in event["moods"]
        matches_budget = event["price"] <= budget_limit

        if matches_mood and matches_budget:
            filtered.append(event)

    return filtered
