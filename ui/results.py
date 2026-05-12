import streamlit as st

from config import (
    EMPTY_RESULTS_MESSAGE,
    MAX_RESULTS,
    SUCCESS_SAVE_MESSAGE,
)
from data.models import save_plan


def render_results(events: list) -> None:
    """
    Renderiza recomendaciones visuales.

    Inputs:
        events: lista de eventos.

    Outputs:
        None.
    """

    if not events:
        st.warning(EMPTY_RESULTS_MESSAGE)
        return

    st.subheader("Planes recomendados para hoy")

    limited_events = events[:MAX_RESULTS]

    for event in limited_events:

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(
                    f"### {event['title']}"
                )

                st.caption(
                    f"📍 {event['zone']}"
                )

            with col2:
                st.metric(
                    "Precio",
                    f"RD${event['price']}"
                )

            st.write(
                f"🚗 Parqueo: {event['parking']}"
            )

            moods = " · ".join(
                event["moods"]
            )

            st.write(
                f"🎭 Mood ideal: {moods}"
            )

            tags = " · ".join(
                event["tags"]
            )

            st.write(
                f"✨ Tags: {tags}"
            )

            save_button = st.button(
                f'Guardar "{event["title"]}"',
                key=f'save_{event["id"]}',
                use_container_width=True,
            )

            if save_button:
                try:
                    with st.spinner(
                        "Guardando plan..."
                    ):
                        save_plan(
                            event["title"]
                        )

                    st.success(
                        SUCCESS_SAVE_MESSAGE
                    )

                    st.toast(
                        f'{event["title"]} guardado'
                    )

                except RuntimeError as error:
                    st.error(str(error))

            st.divider()
