import streamlit as st


def inject_branding() -> None:
    st.markdown(
        """
        <style>
        .stButton button {
            width: 100%;
            border-radius: 14px;
            height: 3rem;
            font-weight: 600;
        }

        .event-card {
            padding: 1.2rem;
            border: 1px solid #2A2D35;
            border-radius: 18px;
            margin-bottom: 1rem;
            background-color: #151922;
        }

        .event-title {
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .event-meta {
            opacity: 0.85;
            margin-bottom: 0.25rem;
        }

        .hero-box {
            padding: 1rem;
            border-radius: 18px;
            background-color: #151922;
            margin-bottom: 1.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
