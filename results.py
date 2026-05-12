import streamlit as st

from config import MAX_RESULTS
from data.models import save_plan


def render_results(events: list) -> None:
    if not events:
        st.warning("No encontramos planes para ese mood y presupuesto.")
        return

    limited_events = events[:MAX_RESULTS]

    for event in limited_events:
        st.markdown(
            f"""
            <div class="event-card">
                <h3>{event["title"]}</h3>
                <p>Zona: {event["zone"]}</p>
                <p>Precio: RD${event["price"]}</p>
                <p>Parqueo: {event["parking"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            f'Guardar {event["title"]}',
            key=event["id"],
        ):
            try:
                save_plan(event["title"])
                st.success("Plan guardado.")

            except RuntimeError as error:
                st.error(str(error))
