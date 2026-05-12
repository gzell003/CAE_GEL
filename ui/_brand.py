import streamlit as st


def inject_branding() -> None:
    st.markdown(
        """
        <style>
        .stButton button {
            width: 100%;
            border-radius: 12px;
        }

        .event-card {
            padding: 1rem;
            border: 1px solid #333333;
            border-radius: 12px;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
