import streamlit as st

from config import (
    EMPTY_RESULTS_MESSAGE,
    MAX_RESULTS,
    SUCCESS_SAVE_MESSAGE,
)
from data.models import save_plan


def render_results(events: list) -> None:
    if not events:
        st.warning(EMPTY_RESULTS_MESSAGE)
        return

    limited_events = events[:MAX_RESULTS]

    st.subheader("Planes recomendados para hoy")

    for event in limited_events:
        tags = ", ".join(event["tags"])

        st.markdown(
            f"""
            <div class="event-card">
                <div class="event-title">
                    {event["title"]}
                </div>

                <div class="event-meta">
                    📍 {event["zone"]}
                </div>

                <div class="event-meta">
                    💸 RD${event["price"]}
                </div>

                <div class="event-meta">
                    🚗 Parqueo: {event["parking"]}
                </div>

                <div class="event-meta">
                    🎭 Ambiente: {tags}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            f'Guardar "{event["title"]}"',
            key=f'save_{event["id"]}',
        ):
            try:
                with st.spinner(
                    "Guardando tu plan..."
                ):
                    save_plan(event["title"])

                st.success(
                    SUCCESS_SAVE_MESSAGE
                )

                st.toast(
                    f'{event["title"]} guardado.'
                )

            except RuntimeError as error:
                st.error(str(error))
