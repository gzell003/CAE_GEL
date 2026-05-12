import streamlit as st

from config import BUDGET_OPTIONS, MOOD_OPTIONS
from data.events import EVENTS
from data.models import initialize_database
from logic.filters import filter_events
from logic.ranking import rank_events
from logic.validation import (
    validate_budget,
    validate_mood,
)
from ui.results import render_results


def render_home() -> None:
    try:
        initialize_database()

    except RuntimeError as error:
        st.error(str(error))
        return

    selected_mood = st.selectbox(
        "¿Qué mood tienes hoy?",
        MOOD_OPTIONS,
    )

    selected_budget = st.selectbox(
        "¿Cuál es tu presupuesto?",
        list(BUDGET_OPTIONS.keys()),
    )

    if st.button("Buscar planes"):
        mood_valid = validate_mood(selected_mood)
        budget_valid = validate_budget(selected_budget)

        if not mood_valid:
            st.error("Mood inválido.")
            return

        if not budget_valid:
            st.error("Presupuesto inválido.")
            return

        filtered_events = filter_events(
            EVENTS,
            selected_mood,
            selected_budget,
        )

        ranked_events = rank_events(filtered_events)

        render_results(ranked_events)
