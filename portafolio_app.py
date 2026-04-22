import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ─── CONFIG ────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jenifer González | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── ESTILOS GLOBALES ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* Fondo oscuro elegante */
.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #0f1117 50%, #0a0e1a 100%);
    color: #e0e0e0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #161b22 100%);
    border-right: 1px solid #21262d;
}

/* Ocultar header de Streamlit */
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

/* Tipografía */
h1, h2, h3 { font-family: 'Space Mono', monospace !important; }
p, li, span { font-family: 'Inter', sans-serif !important; }

/* Cards personalizadas */
.card {
    background: linear-gradient(135deg, #161b22 0%, #1c2128 100%);
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 10px 0;
    transition: all 0.3s ease;
}
.card:hover {
    border-color: #58a6ff;
    box-shadow: 0 0 20px rgba(88, 166, 255, 0.1);
    transform: translateY(-2px);
}

.card-qa {
    border-left: 4px solid #f97316;
}
.card-ds {
    border-left: 4px solid #3b82f6;
}

/* Badges de tecnologías */
.tech-badge {
    display: inline-block;
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 3px 10px;
    margin: 3px;
    font-size: 12px;
    font-family: 'Space Mono', monospace;
    color: #8b949e;
}

/* Métricas */
.metric-box {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 16px;
    text-align: center;
}
.metric-num {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: #58a6ff;
}
.metric-label {
    font-size: 0.75rem;
    color: #8b949e;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Botones */
.stButton > button {
    font-family: 'Space Mono', monospace !important;
    border-radius: 8px !important;
    border: 1px solid #30363d !important;
    background: #21262d !important;
    color: #e0e0e0 !important;
    padding: 8px 20px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    border-color: #58a6ff !important;
    color: #58a6ff !important;
    background: rgba(88, 166, 255, 0.1) !important;
}

/* Tag de mundo */
.world-tag-qa {
    background: rgba(249, 115, 22, 0.15);
    border: 1px solid #f97316;
    color: #f97316;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 12px;
    font-family: 'Space Mono', monospace;
}
.world-tag-ds {
    background: rgba(59, 130, 246, 0.15);
    border: 1px solid #3b82f6;
    color: #3b82f6;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 12px;
    font-family: 'Space Mono', monospace;
}

/* Timeline */
.timeline-item {
    border-left: 2px solid #30363d;
    padding-left: 16px;
    margin-left: 8px;
    margin-bottom: 16px;
}
.timeline-dot {
    width: 10px; height: 10px;
    background: #58a6ff;
    border-radius: 50%;
    margin-left: -20px;
    float: left;
    margin-top: 5px;
}

/* Sidebar nav */
.nav-item {
    padding: 8px 12px;
    border-radius: 8px;
    margin: 4px 0;
    cursor: pointer;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ─── ESTADO GLOBAL ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"

# ─── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 20px 0 10px;">
        <div style="font-family:'Space Mono',monospace; font-size:18px; font-weight:700; color:#e0e0e0;">
            Jenifer González
        </div>
        <div style="font-size:11px; color:#8b949e; margin-top:4px;">
            QA Automation → Data Science
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<p style='font-size:10px; color:#8b949e; text-transform:uppercase; letter-spacing:2px; padding: 4px 0;'>Navegación</p>", unsafe_allow_html=True)

    pages = {
        "home": "🏠  Inicio",
        "qa_world": "🧪  Mundo QA",
        "ds_world": "📊  Mundo Data Science",
        "about": "👩‍💻  Sobre mí",
    }

    for key, label in pages.items():
        is_active = st.session_state.page == key
        if st.button(
            label,
            key=f"nav_{key}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.page = key
            st.rerun()

    st.divider()
    st.markdown("""
    <div style="font-size:11px; color:#8b949e; padding: 8px 0;">
        <div style="margin-bottom:8px;">🔗 <a href="https://www.linkedin.com/in/jenifer-paola-gonzalez-peñuela/" style="color:#58a6ff; text-decoration:none;">LinkedIn</a></div>
        <div style="margin-bottom:8px;">🐙 <a href="https://github.com/Jenifer-Gonzalez-DS-QA" style="color:#58a6ff; text-decoration:none;">GitHub</a></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:auto; padding-top:20px;">
        <a href="#" style="text-decoration:none;">
            <div style="background:#21262d; border:1px solid #30363d; border-radius:8px; padding:10px; text-align:center; font-family:'Space Mono',monospace; font-size:12px; color:#e0e0e0;">
                📄 Descargar CV
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)


# ─── PÁGINA: HOME ───────────────────────────────────────────────────────────────
def page_home():
    st.markdown("""
    <div style="text-align:center; padding: 40px 0 20px;">
        <div style="font-family:'Space Mono',monospace; font-size:13px; color:#8b949e; letter-spacing:3px; margin-bottom:16px;">
            BIENVENIDO A MI PORTAFOLIO
        </div>
        <h1 style="font-size:3rem; margin:0; background:linear-gradient(90deg, #f97316, #3b82f6); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
            Jenifer González
        </h1>
        <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#8b949e; margin: 12px 0 24px;">
            QA Automation Engineer &nbsp;→&nbsp; Data Scientist
        </div>
        <p style="max-width:600px; margin:0 auto; color:#8b949e; font-size:15px; line-height:1.7;">
            Ingeniera de Sistemas con experiencia en aseguramiento de calidad y metodologías ágiles,
            en transición activa hacia la Ciencia de Datos. Combino la mentalidad QA —rigor, trazabilidad,
            confiabilidad— con análisis y modelos predictivos de impacto real.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Dos mundos
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card card-qa" style="text-align:center; padding:32px 24px; cursor:pointer;">
            <div style="font-size:3rem; margin-bottom:12px;">🧪</div>
            <div style="font-family:'Space Mono',monospace; font-size:1.2rem; color:#f97316; margin-bottom:8px;">
                Mundo QA
            </div>
            <p style="color:#8b949e; font-size:14px; line-height:1.6;">
                Frameworks de automatización, CI/CD con GitHub Actions, dashboards de métricas
                de calidad en tiempo real. 3 proyectos que forman un ecosistema completo.
            </p>
            <div style="margin-top:16px;">
                <span class="tech-badge">Pytest</span>
                <span class="tech-badge">GitHub Actions</span>
                <span class="tech-badge">Plotly</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧪 Explorar mundo QA", use_container_width=True, key="go_qa"):
            st.session_state.page = "qa_world"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="card card-ds" style="text-align:center; padding:32px 24px; cursor:pointer;">
            <div style="font-size:3rem; margin-bottom:12px;">📊</div>
            <div style="font-family:'Space Mono',monospace; font-size:1.2rem; color:#3b82f6; margin-bottom:8px;">
                Mundo Data Science
            </div>
            <p style="color:#8b949e; font-size:14px; line-height:1.6;">
                Machine Learning, Deep Learning y análisis predictivo aplicado a industria,
                salud y telecomunicaciones. Modelos reales con impacto de negocio medible.
            </p>
            <div style="margin-top:16px;">
                <span class="tech-badge">Scikit-learn</span>
                <span class="tech-badge">XGBoost</span>
                <span class="tech-badge">TensorFlow</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Explorar mundo DS", use_container_width=True, key="go_ds"):
            st.session_state.page = "ds_world"
            st.rerun()

    # Stats rápidos
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Space Mono,monospace; font-size:10px; color:#8b949e; text-transform:uppercase; letter-spacing:2px; text-align:center; margin-bottom:16px;'>EN NÚMEROS</div>", unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)
    metrics = [
        ("6", "Proyectos"),
        ("3", "QA Repos"),
        ("3", "DS Modelos"),
        ("51", "Pruebas auto."),
        ("3", "Stacks tech"),
    ]
    for col, (num, label) in zip([c1, c2, c3, c4, c5], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-num">{num}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)


# ─── PÁGINA: MUNDO QA ───────────────────────────────────────────────────────────
def page_qa_world():
    st.markdown("""
    <div style="margin-bottom:24px;">
        <span class="world-tag-qa">🧪 QA AUTOMATION</span>
        <h2 style="margin:12px 0 4px;">Ecosistema de Automatización</h2>
        <p style="color:#8b949e; font-size:14px;">
            Tres proyectos diseñados para trabajar juntos: framework base → análisis de datos → CI/CD automático.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Selector de proyecto
    proyecto_qa = st.selectbox(
        "Selecciona un proyecto",
        ["📊 QA Dashboard — Métricas en tiempo real",
         "🔌 API Testing Framework — CRUD completo",
         "🔄 QA CI/CD Pipeline — Automatización total"],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── PROYECTO 1: QA DASHBOARD
    if "QA Dashboard" in proyecto_qa:
        col1, col2 = st.columns([1.2, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="card card-qa">
                <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#f97316; margin-bottom:8px;">
                    📊 QA Dashboard
                </div>
                <p style="color:#8b949e; font-size:14px; line-height:1.7;">
                    Dashboard interactivo que combina automatización de pruebas de API con análisis
                    de datos. Ejecuta 22 tests contra una API REST, guarda resultados en CSV acumulativo
                    y genera visualizaciones Plotly en tiempo real. Un solo comando hace todo.
                </p>
                <div style="margin:16px 0;">
                    <span class="tech-badge">Python 3.11</span>
                    <span class="tech-badge">Pandas</span>
                    <span class="tech-badge">Plotly</span>
                    <span class="tech-badge">Requests</span>
                </div>
                <div style="font-size:13px; color:#8b949e;">
                    <div style="margin-bottom:6px;">✅ 22 pruebas CRUD automatizadas</div>
                    <div style="margin-bottom:6px;">✅ CSV acumulativo con timestamps</div>
                    <div style="margin-bottom:6px;">✅ Dashboard HTML sin servidor</div>
                    <div>✅ KPIs + tendencia entre ejecuciones</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("🔗 Ver repositorio en GitHub",
                           "https://github.com/Jenifer-Gonzalez-DS-QA/qa-dashboard",
                           use_container_width=True)

        with col2:
            # Demo interactiva del dashboard
            st.markdown("**Demo: Simulación de métricas de calidad**")

            # Generar datos sintéticos representativos
            np.random.seed(42)
            methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
            success_rates = [100, 95, 90, 88, 92]
            response_times = [45, 120, 98, 105, 78]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=methods,
                y=success_rates,
                marker_color=["#22c55e" if r == 100 else "#f97316" if r < 92 else "#3b82f6" for r in success_rates],
                name="Tasa de éxito %",
                text=[f"{r}%" for r in success_rates],
                textposition="outside"
            ))
            fig.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#8b949e",
                height=280,
                margin=dict(t=20, b=20, l=10, r=10),
                showlegend=False,
                yaxis=dict(range=[80, 105], gridcolor="#21262d"),
                xaxis=dict(gridcolor="#21262d")
            )
            st.plotly_chart(fig, use_container_width=True)

            # Métricas clave
            m1, m2, m3 = st.columns(3)
            m1.metric("✅ Pasaron", "21", "de 22")
            m2.metric("⏱ Promedio", "89ms")
            m3.metric("🏆 Éxito", "95.5%")

    # ── PROYECTO 2: API TESTING FRAMEWORK
    elif "API Testing" in proyecto_qa:
        col1, col2 = st.columns([1.2, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="card card-qa">
                <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#f97316; margin-bottom:8px;">
                    🔌 API Testing Framework
                </div>
                <p style="color:#8b949e; font-size:14px; line-height:1.7;">
                    Framework profesional de automatización de pruebas para APIs REST. Cubre operaciones
                    CRUD completas sobre usuarios, posts, comentarios y todos con reportes HTML automáticos.
                    Diseñado para ser extensible y reutilizable.
                </p>
                <div style="margin:16px 0;">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">Pytest</span>
                    <span class="tech-badge">Requests</span>
                    <span class="tech-badge">pytest-html</span>
                </div>
                <div style="font-size:13px; color:#8b949e;">
                    <div style="margin-bottom:6px;">✅ CRUD sobre 4 endpoints</div>
                    <div style="margin-bottom:6px;">✅ Reportes HTML auto-generados</div>
                    <div style="margin-bottom:6px;">✅ Fixtures y conftest reutilizables</div>
                    <div>✅ Sin dependencia de credenciales externas</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("🔗 Ver repositorio en GitHub",
                           "https://github.com/Jenifer-Gonzalez-DS-QA/api-testing-framework",
                           use_container_width=True)

        with col2:
            st.markdown("**Demo: Cobertura por endpoint y método**")

            endpoints = ["GET /posts", "POST /posts", "PUT /posts/{id}", "PATCH /posts/{id}", "DELETE /posts/{id}",
                         "GET /users", "GET /comments", "GET /todos"]
            passed = [5, 3, 2, 2, 2, 4, 3, 3]
            failed = [0, 1, 0, 0, 0, 0, 0, 0]

            fig = go.Figure()
            fig.add_trace(go.Bar(name="✅ Passed", x=endpoints, y=passed, marker_color="#22c55e"))
            fig.add_trace(go.Bar(name="❌ Failed", x=endpoints, y=failed, marker_color="#ef4444"))

            fig.update_layout(
                barmode="stack",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#8b949e",
                height=280,
                margin=dict(t=20, b=20, l=10, r=10),
                legend=dict(bgcolor="rgba(0,0,0,0)"),
                xaxis=dict(tickangle=-30, gridcolor="#21262d"),
                yaxis=dict(gridcolor="#21262d")
            )
            st.plotly_chart(fig, use_container_width=True)

    # ── PROYECTO 3: CI/CD PIPELINE
    elif "CI/CD" in proyecto_qa:
        col1, col2 = st.columns([1.2, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="card card-qa">
                <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#f97316; margin-bottom:8px;">
                    🔄 QA CI/CD Pipeline
                </div>
                <p style="color:#8b949e; font-size:14px; line-height:1.7;">
                    Suite de pruebas con 3 niveles integrada con GitHub Actions. Las pruebas corren
                    automáticamente en cada push, PR y de lunes a viernes a las 8am. Mentalidad DevOps
                    aplicada al QA: las pruebas no se ejecutan manualmente, corren solas.
                </p>
                <div style="margin:16px 0;">
                    <span class="tech-badge">Pytest</span>
                    <span class="tech-badge">GitHub Actions</span>
                    <span class="tech-badge">pytest-html</span>
                    <span class="tech-badge">YAML</span>
                </div>
                <div style="font-size:13px; color:#8b949e;">
                    <div style="margin-bottom:6px;">🔥 17 pruebas Smoke (críticas)</div>
                    <div style="margin-bottom:6px;">🔄 28 pruebas de Regresión</div>
                    <div style="margin-bottom:6px;">⚡ 6 pruebas de Performance (&lt;3s)</div>
                    <div>📊 Artifacts HTML por 30 días</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("🔗 Ver repositorio en GitHub",
                           "https://github.com/Jenifer-Gonzalez-DS-QA/qa-cicd-pipeline",
                           use_container_width=True)

        with col2:
            st.markdown("**Pipeline: Distribución de pruebas por nivel**")

            labels = ["🔥 Smoke", "🔄 Regression", "⚡ Performance"]
            values = [17, 28, 6]
            colors = ["#f97316", "#3b82f6", "#a855f7"]

            fig = go.Figure(go.Pie(
                labels=labels,
                values=values,
                hole=0.6,
                marker_colors=colors,
                textinfo="label+percent",
                textfont_size=12,
            ))
            fig.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#8b949e",
                height=280,
                margin=dict(t=20, b=20, l=10, r=10),
                showlegend=False,
                annotations=[dict(text="51 tests", x=0.5, y=0.5,
                                  font_size=16, font_color="#e0e0e0", showarrow=False)]
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
            <div style="font-size:12px; color:#8b949e; text-align:center;">
                ⚡ Se activa en cada <code>push</code> y <code>pull request</code> automáticamente
            </div>
            """, unsafe_allow_html=True)

    # Relación entre proyectos
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="background:rgba(249,115,22,0.05); border-color:#f97316;">
        <div style="font-family:'Space Mono',monospace; font-size:13px; color:#f97316; margin-bottom:8px;">
            💡 Los 3 proyectos forman un ecosistema completo
        </div>
        <div style="display:flex; align-items:center; gap:12px; font-size:13px; color:#8b949e; flex-wrap:wrap;">
            <span>🔌 API Testing Framework</span>
            <span style="color:#f97316;">→</span>
            <span>📊 QA Dashboard</span>
            <span style="color:#f97316;">→</span>
            <span>🔄 CI/CD Pipeline</span>
        </div>
        <div style="font-size:12px; color:#8b949e; margin-top:8px;">
            Base: estructura y cliente HTTP &nbsp;→&nbsp; Análisis: métricas y visualización &nbsp;→&nbsp; Automatización: corre solo en cada push
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── PÁGINA: MUNDO DATA SCIENCE ─────────────────────────────────────────────────
def page_ds_world():
    st.markdown("""
    <div style="margin-bottom:24px;">
        <span class="world-tag-ds">📊 DATA SCIENCE</span>
        <h2 style="margin:12px 0 4px;">Proyectos de Machine Learning</h2>
        <p style="color:#8b949e; font-size:14px;">
            Modelos predictivos aplicados a industria pesada, visión por computadora y telecomunicaciones.
        </p>
    </div>
    """, unsafe_allow_html=True)

    proyecto_ds = st.selectbox(
        "Selecciona un proyecto",
        ["🥇 Predicción de Recuperación de Oro",
         "👁 Verificación de Edad con Deep Learning",
         "📱 Churn en Telecomunicaciones"],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── DS PROYECTO 1: ORO
    if "Oro" in proyecto_ds:
        col1, col2 = st.columns([1.2, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="card card-ds">
                <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#3b82f6; margin-bottom:8px;">
                    🥇 Predicción de Recuperación de Oro
                </div>
                <div style="font-size:12px; color:#8b949e; margin-bottom:10px;">
                    Industria pesada · Regresión · Optimización de procesos
                </div>
                <p style="color:#8b949e; font-size:14px; line-height:1.7;">
                    Modelo de ML para predecir la cantidad de oro extraído del mineral en etapas de
                    flotación y purificación. El modelo ayuda a optimizar la producción e identificar
                    parámetros no rentables en el proceso industrial.
                </p>
                <div style="margin:16px 0;">
                    <span class="tech-badge">XGBoost</span>
                    <span class="tech-badge">Scikit-learn</span>
                    <span class="tech-badge">Pandas</span>
                    <span class="tech-badge">sMAPE</span>
                </div>
                <div style="font-size:13px; color:#8b949e;">
                    <div style="margin-bottom:6px;">✅ EDA de proceso industrial minero</div>
                    <div style="margin-bottom:6px;">✅ Ingeniería de características sobre etapas</div>
                    <div style="margin-bottom:6px;">✅ Métrica personalizada sMAPE ponderado</div>
                    <div>✅ Comparación RandomForest vs XGBoost vs baseline</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("🔗 Ver repositorio en GitHub",
                           "https://github.com/Jenifer-Gonzalez-DS-QA/Prediccion-de-recuperacion-de-oro",
                           use_container_width=True)

        with col2:
            st.markdown("**Demo interactiva: Simula predicción de recuperación**")

            with st.form("gold_form"):
                reagent_floatation = st.slider("Reactivo flotación (xanthate)", 1.0, 15.0, 7.5, 0.1)
                pulp_density = st.slider("Densidad del pulp (%)", 20.0, 60.0, 40.0, 0.5)
                air_feed = st.slider("Alimentación de aire", 500.0, 1500.0, 900.0, 10.0)
                submitted = st.form_submit_button("🔮 Predecir recuperación", use_container_width=True)

            if submitted:
                # Simulación representativa
                pred = 65 + (reagent_floatation - 7.5) * 2.1 + (pulp_density - 40) * 0.3 + (air_feed - 900) * 0.01
                pred = max(40, min(95, pred))
                st.metric("Recuperación estimada (rougher)", f"{pred:.1f}%",
                          f"{'↑ Buena' if pred > 70 else '↓ Optimizar parámetros'}")

                # Gauge visual
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=pred,
                    number={"suffix": "%", "font": {"color": "#e0e0e0"}},
                    gauge={
                        "axis": {"range": [0, 100], "tickcolor": "#8b949e"},
                        "bar": {"color": "#3b82f6"},
                        "steps": [
                            {"range": [0, 50], "color": "#1c2128"},
                            {"range": [50, 75], "color": "#1c2128"},
                            {"range": [75, 100], "color": "#1c2128"}
                        ],
                        "threshold": {"line": {"color": "#22c55e", "width": 3}, "value": 75},
                        "bgcolor": "#161b22"
                    }
                ))
                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    font_color="#8b949e",
                    height=220,
                    margin=dict(t=20, b=10, l=10, r=10)
                )
                st.plotly_chart(fig, use_container_width=True)

    # ── DS PROYECTO 2: EDAD
    elif "Edad" in proyecto_ds:
        col1, col2 = st.columns([1.2, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="card card-ds">
                <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#3b82f6; margin-bottom:8px;">
                    👁 Verificación de Edad con Deep Learning
                </div>
                <div style="font-size:12px; color:#8b949e; margin-bottom:10px;">
                    Computer Vision · Deep Learning · Clasificación
                </div>
                <p style="color:#8b949e; font-size:14px; line-height:1.7;">
                    Modelo de aprendizaje profundo para estimar la edad de personas a partir de
                    fotografías faciales. Aplicación directa en retail para verificación de edad
                    en la compra de productos regulados.
                </p>
                <div style="margin:16px 0;">
                    <span class="tech-badge">TensorFlow</span>
                    <span class="tech-badge">ResNet50</span>
                    <span class="tech-badge">Keras</span>
                    <span class="tech-badge">MAE</span>
                </div>
                <div style="font-size:13px; color:#8b949e;">
                    <div style="margin-bottom:6px;">✅ Transfer learning con ResNet50</div>
                    <div style="margin-bottom:6px;">✅ Data augmentation aplicado</div>
                    <div style="margin-bottom:6px;">✅ Evaluación con MAE</div>
                    <div>✅ Aplicación en control de ventas reguladas</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("🔗 Ver repositorio en GitHub",
                           "https://github.com/Jenifer-Gonzalez-DS-QA/Verificacion_de_Edad",
                           use_container_width=True)

        with col2:
            st.markdown("**Distribución simulada de edades en dataset**")

            np.random.seed(0)
            ages = np.concatenate([
                np.random.normal(25, 5, 300),
                np.random.normal(40, 8, 400),
                np.random.normal(60, 7, 200)
            ])
            ages = np.clip(ages, 1, 80).astype(int)

            fig = px.histogram(
                x=ages, nbins=40,
                color_discrete_sequence=["#3b82f6"],
                labels={"x": "Edad", "y": "Frecuencia"}
            )
            fig.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#8b949e",
                height=280,
                margin=dict(t=20, b=20, l=10, r=10),
                xaxis=dict(gridcolor="#21262d"),
                yaxis=dict(gridcolor="#21262d"),
                bargap=0.05
            )
            st.plotly_chart(fig, use_container_width=True)

            st.metric("MAE del modelo", "~7.2 años", "Error medio absoluto")

    # ── DS PROYECTO 3: CHURN TELCO
    elif "Churn" in proyecto_ds or "Teleco" in proyecto_ds:
        col1, col2 = st.columns([1.2, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="card card-ds">
                <div style="font-family:'Space Mono',monospace; font-size:1.1rem; color:#3b82f6; margin-bottom:8px;">
                    📱 Churn en Telecomunicaciones
                </div>
                <div style="font-size:12px; color:#8b949e; margin-bottom:10px;">
                    Clasificación · Retención de clientes · Negocio
                </div>
                <p style="color:#8b949e; font-size:14px; line-height:1.7;">
                    Modelo predictivo para identificar clientes en riesgo de cancelación (churn)
                    en una empresa de telecomunicaciones. Permite acciones preventivas de retención
                    antes de que el cliente se vaya.
                </p>
                <div style="margin:16px 0;">
                    <span class="tech-badge">LightGBM</span>
                    <span class="tech-badge">Scikit-learn</span>
                    <span class="tech-badge">Pandas</span>
                    <span class="tech-badge">ROC-AUC</span>
                </div>
                <div style="font-size:13px; color:#8b949e;">
                    <div style="margin-bottom:6px;">✅ Análisis de features de comportamiento</div>
                    <div style="margin-bottom:6px;">✅ Manejo de desbalance de clases</div>
                    <div style="margin-bottom:6px;">✅ Optimización de umbral de decisión</div>
                    <div>✅ Feature importance interpretable</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("🔗 Ver repositorio en GitHub",
                           "https://github.com/Jenifer-Gonzalez-DS-QA/Proyecto_Telecomunicaciones",
                           use_container_width=True)

        with col2:
            st.markdown("**Demo: Predicción de riesgo de churn**")

            with st.form("churn_form"):
                antiguedad = st.slider("Meses como cliente", 1, 72, 12)
                llamadas_soporte = st.slider("Llamadas a soporte (último mes)", 0, 10, 2)
                cargo_mensual = st.slider("Cargo mensual (USD)", 20.0, 120.0, 65.0, 0.5)
                tiene_contrato = st.radio("Tipo de contrato", ["Mensual", "1 año", "2 años"], horizontal=True)
                pred_churn = st.form_submit_button("⚠️ Analizar riesgo", use_container_width=True)

            if pred_churn:
                # Score simulado representativo
                score = 0.4
                score -= antiguedad * 0.005
                score += llamadas_soporte * 0.07
                score += (cargo_mensual - 65) * 0.002
                if tiene_contrato == "Mensual":
                    score += 0.2
                elif tiene_contrato == "2 años":
                    score -= 0.25
                score = max(0.02, min(0.98, score))

                risk_color = "#ef4444" if score > 0.6 else "#f97316" if score > 0.35 else "#22c55e"
                risk_label = "⚠️ ALTO RIESGO" if score > 0.6 else "⚡ RIESGO MEDIO" if score > 0.35 else "✅ BAJO RIESGO"

                st.markdown(f"""
                <div style="background:#161b22; border:2px solid {risk_color}; border-radius:10px; padding:16px; text-align:center; margin-top:8px;">
                    <div style="font-size:1.8rem; font-weight:700; color:{risk_color}; font-family:'Space Mono',monospace;">
                        {score*100:.0f}%
                    </div>
                    <div style="font-size:13px; color:{risk_color};">{risk_label}</div>
                    <div style="font-size:11px; color:#8b949e; margin-top:6px;">
                        Probabilidad de cancelación en los próximos 30 días
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ─── PÁGINA: SOBRE MÍ ───────────────────────────────────────────────────────────
def page_about():
    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown("""
        <div class="card" style="text-align:center; padding:32px;">
            <div style="width:100px; height:100px; background:linear-gradient(135deg,#f97316,#3b82f6);
                        border-radius:50%; margin:0 auto 16px; display:flex; align-items:center;
                        justify-content:center; font-size:2.5rem;">
                👩‍💻
            </div>
            <div style="font-family:'Space Mono',monospace; font-size:1.2rem; color:#e0e0e0; margin-bottom:6px;">
                Jenifer González
            </div>
            <div style="font-size:12px; color:#8b949e; margin-bottom:16px;">
                Bogotá, Colombia
            </div>
            <div style="font-size:13px; color:#8b949e; line-height:1.8;">
                Ingeniera de Sistemas<br>
                QA Automation Engineer<br>
                Scrum Master<br>
                Data Scientist en formación
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Habilidades blandas**")
        habilidades = ["Pensamiento analítico", "Orientada a calidad", "Trabajo en equipo ágil",
                       "Comunicación técnica", "Mentalidad de mejora continua", "Resolución de problemas"]
        for h in habilidades:
            st.markdown(f"<div style='font-size:13px; color:#8b949e; padding:4px 0;'>→ {h}</div>",
                        unsafe_allow_html=True)

    with col2:
        st.markdown("#### Mi trayectoria")

        timeline_items = [
            ("#22c55e", "2024 – Hoy", "Bootcamp Data Science · TripleTen",
             "ML, Deep Learning, NLP, Streamlit. Construcción de portafolio con proyectos reales."),
            ("#3b82f6", "2023 – 2024", "QA Automation Engineer",
             "Automatización de pruebas con Python y Pytest. Integración CI/CD con GitHub Actions. Diseño de frameworks reutilizables."),
            ("#f97316", "2019 – 2023", "QA Manual + Scrum Master",
             "Gestión de calidad en equipos ágiles. Liderazgo de ceremonias Scrum/Kanban. Documentación de casos de prueba."),
            ("#8b949e", "2019", "Ingeniería de Sistemas",
             "Formación base en desarrollo de software, bases de datos, redes y programación."),
        ]

        for color, year, title, desc in timeline_items:
            st.markdown(f"""
            <div style="border-left:3px solid {color}; padding:8px 16px; margin-bottom:16px;">
                <div style="font-size:11px; color:{color}; font-family:'Space Mono',monospace; letter-spacing:1px;">
                    {year}
                </div>
                <div style="font-size:14px; color:#e0e0e0; font-weight:600; margin:4px 0;">
                    {title}
                </div>
                <div style="font-size:13px; color:#8b949e; line-height:1.6;">
                    {desc}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Lo que busco")
        st.markdown("""
        <div class="card card-ds" style="font-size:14px; color:#8b949e; line-height:1.7;">
            Un rol donde pueda conectar mi experiencia en QA y metodologías ágiles con la
            Ciencia de Datos. Me interesa especialmente cualquier posición donde los datos
            confiables y los procesos de calidad sean parte del mismo flujo de trabajo.
            <br><br>
            <span style="color:#3b82f6;">Data Analyst · Data Engineer · QA Data · Analytics Engineer</span>
        </div>
        """, unsafe_allow_html=True)


# ─── ROUTER ─────────────────────────────────────────────────────────────────────
page = st.session_state.page
if page == "home":
    page_home()
elif page == "qa_world":
    page_qa_world()
elif page == "ds_world":
    page_ds_world()
elif page == "about":
    page_about()
