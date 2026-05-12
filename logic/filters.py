from config import BUDGET_OPTIONS


def filter_events(
    events: list,
    mood: str,
    budget: str,
) -> list:
    """
    Filtra eventos por mood y presupuesto.

    Inputs:
        events: lista de eventos.
        mood: mood seleccionado.
        budget: presupuesto seleccionado.

    Outputs:
        Lista filtrada.

    Errors:
        ValueError si budget no existe.
    """

    if budget not in BUDGET_OPTIONS:
        raise ValueError(
            "Presupuesto fuera de catálogo."
        )

    budget_limit = BUDGET_OPTIONS[budget]

    filtered_events = []

    for event in events:
        matches_mood = mood in event["moods"]

        matches_budget = (
            event["price"] <= budget_limit
        )

        if matches_mood and matches_budget:
            filtered_events.append(event)

    return filtered_events
