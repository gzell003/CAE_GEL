from config import (
    BUDGET_OPTIONS,
    MOOD_OPTIONS,
)


def validate_mood(
    selected_mood: str,
) -> bool:
    """
    Valida mood seleccionado.

    Inputs:
        selected_mood: mood del usuario.

    Outputs:
        bool.
    """

    if not selected_mood:
        return False

    return selected_mood in MOOD_OPTIONS


def validate_budget(
    selected_budget: str,
) -> bool:
    """
    Valida presupuesto seleccionado.

    Inputs:
        selected_budget: presupuesto.

    Outputs:
        bool.
    """

    if not selected_budget:
        return False

    return selected_budget in BUDGET_OPTIONS
