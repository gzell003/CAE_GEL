import streamlit as st
from data import get_eventos, MOODS, PRESUPUESTOS
from datetime import date

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Modo Plan SD",
    page_icon="🗺️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── SESSION STATE INIT (persiste entre reruns) ────────────────────────────────
st.session_state.setdefault("mood", None)
st.session_state.setdefault("presupuesto_max", 99999)
st.session_state.setdefault("step", "mood")          # mood → resultados
st.session_state.setdefault("plan_guardado", [])

# ── ESTILOS ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #FAF7F2;
    color: #1A1A1A;
}

/* Header */
.header-block {
    background: #1E2761;
    border-left: 6px solid #F96167;
    padding: 24px 28px 20px;
    border-radius: 8px;
    margin-bottom: 28px;
}
.header-title {
    font-family: 'DM Serif Display', serif;
    font-size: 28px;
    color: #fff;
    margin: 0 0 4px;
    letter-spacing: -0.5px;
}
.header-sub {
    font-size: 13px;
    color: rgba(255,255,255,0.6);
    margin: 0;
    letter-spacing: 0.04em;
}

/* Section labels */
.section-label {
    font-size: 10px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #6B6B6B;
    margin-bottom: 12px;
    font-weight: 600;
}

/* Mood buttons */
.stButton > button {
    background: #fff !important;
    border: 1.5px solid #E0DDD8 !important;
    border-radius: 8px !important;
    color: #1A1A1A !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    padding: 10px 14px !important;
    transition: all 0.15s ease !important;
    width: 100% !important;
    text-align: left !important;
}
.stButton > button:hover {
    border-color: #F96167 !important;
    background: #FFF5F5 !important;
}

/* Selected mood pill */
.mood-selected {
    display: inline-block;
    background: #1E2761;
    color: #F9E795;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.08em;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 20px;
    text-transform: uppercase;
}

/* Event card */
.card {
    background: #fff;
    border: 1px solid #E8E4DE;
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 16px;
    border-left: 5px solid #F96167;
    position: relative;
}
.card-new {
    border-left-color: #F9E795;
}
.card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 17px;
    color: #1E2761;
    margin: 0 0 4px;
    line-height: 1.3;
}
.card-tipo {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #6B6B6B;
    margin-bottom: 10px;
}
.card-desc {
    font-size: 13px;
    color: #3a3a3a;
    line-height: 1.55;
    margin-bottom: 12px;
}
.card-meta {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    font-size: 12px;
    color: #6B6B6B;
    margin-bottom: 10px;
}
.card-tag {
    display: inline-block;
    background: #FAF7F2;
    border: 1px solid #E0DDD8;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 11px;
    color: #555;
    margin-right: 4px;
    margin-bottom: 4px;
}
.tag-novedad {
    background: #FFF9E0;
    border-color: #F9E795;
    color: #8a7a00;
    font-weight: 600;
}
.tag-local {
    background: #E8EDFF;
    border-color: #b0bcff;
    color: #1E2761;
}
.precio-badge {
    font-family: 'DM Serif Display', serif;
    font-size: 16px;
    color: #F96167;
    font-weight: bold;
}

/* No results */
.no-results {
    text-align: center;
    padding: 40px 20px;
    color: #6B6B6B;
    font-style: italic;
}

/* Divider */
.divider {
    border: none;
    border-top: 1px solid #E8E4DE;
    margin: 24px 0;
}

/* Footer */
.footer {
    margin-top: 40px;
    padding: 16px 0;
    border-top: 1px solid #E8E4DE;
    text-align: center;
    font-size: 11px;
    color: #aaa;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)


# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-block">
  <p class="header-title">Modo Plan SD 🗺️</p>
  <p class="header-sub">Descubre ocio real en Santo Domingo — filtrado por cómo te sientes hoy</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# STEP 1 — SELECCIÓN DE MOOD
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.step == "mood":

    st.markdown('<p class="section-label">¿Cómo te sientes hoy?</p>', unsafe_allow_html=True)

    cols = st.columns(2)
    for i, mood in enumerate(MOODS):
        with cols[i % 2]:
            label = f"{mood['emoji']} {mood['label']}\n{mood['desc']}"
            if st.button(label, key=f"mood_{mood['key']}"):
                st.session_state.mood = mood
                st.session_state.step = "presupuesto"
                st.rerun()

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">¿Cuánto quieres gastar?</p>', unsafe_allow_html=True)

    pres_cols = st.columns(len(PRESUPUESTOS))
    for i, p in enumerate(PRESUPUESTOS):
        with pres_cols[i]:
            if st.button(p["label"], key=f"pres_{i}"):
                st.session_state.presupuesto_max = p["max"]
                st.rerun()

    # Mostrar selección activa de presupuesto
    pres_actual = next(
        (p["label"] for p in PRESUPUESTOS if p["max"] == st.session_state.presupuesto_max),
        "Sin límite"
    )
    st.caption(f"Presupuesto seleccionado: **{pres_actual}**")


# ══════════════════════════════════════════════════════════════════════════════
# STEP 2 — RESULTADOS FILTRADOS
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == "presupuesto":
    mood = st.session_state.mood
    presupuesto_max = st.session_state.presupuesto_max

    # Mood chip
    st.markdown(
        f'<span class="mood-selected">{mood["emoji"]} {mood["label"]}</span>',
        unsafe_allow_html=True
    )

    # Cambiar mood
    if st.button("← Cambiar mood"):
        st.session_state.step = "mood"
        st.session_state.mood = None
        st.rerun()

    # ── FILTRO ────────────────────────────────────────────────────────────────
    eventos = get_eventos()
    resultados = [
        e for e in eventos
        if mood["key"] in e["mood_fit"]
        and e["precio_aprox"] <= presupuesto_max
    ]

    # Ordenar: novedades primero
    resultados.sort(key=lambda x: (not x["novedad"], x["fecha"]))

    st.markdown(
        f'<p class="section-label">{len(resultados)} planes encontrados para ti</p>',
        unsafe_allow_html=True
    )

    if not resultados:
        st.markdown("""
        <div class="no-results">
            <p>No encontré planes que encajen con tu mood y presupuesto esta semana.</p>
            <p>Intenta con otro mood o ampliando el presupuesto.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for e in resultados[:3]:  # MVP: máximo 3 opciones
            dias_restantes = (e["fecha"] - date.today()).days
            if dias_restantes == 0:
                cuando = "Hoy"
            elif dias_restantes == 1:
                cuando = "Mañana"
            else:
                cuando = f"En {dias_restantes} días"

            precio_str = "Entrada libre" if e["precio_aprox"] == 0 else f"RD${e['precio_aprox']:,}"
            parqueo_str = "✓ Parqueo" if e["parqueo"] else "Sin parqueo"

            novedad_tag = '<span class="card-tag tag-novedad">✦ Novedad</span>' if e["novedad"] else ""
            local_tag = '<span class="card-tag tag-local">Para locales</span>'
            ambiente_tags = "".join([f'<span class="card-tag">{a}</span>' for a in e["ambiente"]])

            card_class = "card card-new" if e["novedad"] else "card"

            st.markdown(f"""
            <div class="{card_class}">
                <p class="card-tipo">{e["tipo"]} · {e["barrio"]}</p>
                <p class="card-title">{e["nombre"]}</p>
                <p class="card-desc">{e["descripcion"]}</p>
                <div class="card-meta">
                    <span>📅 {cuando} · {e["fecha"].strftime("%d %b")}</span>
                    <span>🕐 {e["horario"]}</span>
                    <span>🚗 {parqueo_str}</span>
                    <span class="precio-badge">{precio_str}</span>
                </div>
                <div>{novedad_tag}{local_tag}{ambiente_tags}</div>
            </div>
            """, unsafe_allow_html=True)

            # Botón guardar plan
            col1, col2 = st.columns([3, 1])
            with col2:
                ya_guardado = e["id"] in [p["id"] for p in st.session_state.plan_guardado]
                btn_label = "✓ Guardado" if ya_guardado else "Guardar plan"
                if not ya_guardado:
                    if st.button(btn_label, key=f"save_{e['id']}"):
                        st.session_state.plan_guardado.append(e)
                        st.rerun()
                else:
                    st.caption("✓ En tu lista")

    # ── PLAN GUARDADO ─────────────────────────────────────────────────────────
    if st.session_state.plan_guardado:
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Tu plan guardado</p>', unsafe_allow_html=True)
        for p in st.session_state.plan_guardado:
            precio_str = "Libre" if p["precio_aprox"] == 0 else f"RD${p['precio_aprox']:,}"
            st.markdown(f"""
            <div style="background:#fff;border:1px solid #E8E4DE;border-radius:8px;
                        padding:14px 18px;margin-bottom:10px;display:flex;
                        justify-content:space-between;align-items:center;">
                <div>
                    <strong style="color:#1E2761;font-size:14px;">{p['nombre']}</strong><br>
                    <span style="font-size:12px;color:#6B6B6B;">{p['barrio']} · {p['fecha'].strftime('%d %b')} · {precio_str}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🗑 Limpiar lista"):
            st.session_state.plan_guardado = []
            st.rerun()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">Modo Plan SD · MVP · Data mockeada · Santo Domingo</div>
""", unsafe_allow_html=True)
