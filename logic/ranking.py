from config import EVENT_TAG_PRIORITY


def rank_events(events: list) -> list:

    def calculate_score(event: dict) -> int:
        score = 0

        for tag in event["tags"]:
            score += EVENT_TAG_PRIORITY.get(tag, 0)

        return score

    return sorted(
        events,
        key=calculate_score,
        reverse=True,
    )
