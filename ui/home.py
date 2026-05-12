import streamlit as st

from config import (
    BUDGET_OPTIONS,
    MOOD_OPTIONS,
    SEARCHING_MESSAGE,
)
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

    st.markdown(
        """
        <div class="hero-box">
        <h3>Jueves por la noche.</h3>
        <p>
        Antes de terminar en el mismo sitio de siempre,
        encuentra algo que sí valga salir.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_mood = st.selectbox(
        "¿Qué mood tienes hoy?",
        MOOD_OPTIONS,
        help="El mood cambia el tipo de ambiente que vas a recibir.",
    )

    selected_budget = st.selectbox(
        "¿Cuál es tu presupuesto?",
        list(BUDGET_OPTIONS.keys()),
        help="Filtramos opciones que sí encajen con tu bolsillo.",
    )

    results_placeholder = st.empty()

    if st.button("Buscar planes"):
        mood_valid = validate_mood(selected_mood)
        budget_valid = validate_budget(selected_budget)

        if not mood_valid:
            st.error(
                "Ese mood no existe en el sistema."
            )
            return

        if not budget_valid:
            st.error(
                "Ese presupuesto no es válido."
            )
            return

        with st.spinner(SEARCHING_MESSAGE):
            filtered_events = filter_events(
                EVENTS,
                selected_mood,
                selected_budget,
            )

            ranked_events = rank_events(
                filtered_events
            )

        results_placeholder.success(
            f"Encontramos {len(ranked_events)} opciones para tu mood."
        )

        render_results(ranked_events)
