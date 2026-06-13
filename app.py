import streamlit as st

# --- CONFIGURATION ARCHITECTURE IDENTITYPATH ---
st.set_page_config(
    page_title="IdentityPath | AI Student Profiling System",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INJECTION DU DESIGN PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;500;600;700;800&family=Space+Grotesk:wght=500;700&display=swap');
    :root { --bg-core: #090d16; --card-bg: #111726; --accent-blue: #3b82f6; --accent-green: #10b981; }
    .main { background-color: #090d16; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #090d16; font-family: 'Plus Jakarta Sans', sans-serif; }
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    .seo-banner { text-align: left; padding: 30px; background: linear-gradient(135deg, #111827 0%, #030712 100%); border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 30px; }
    .seo-title { font-size: 38px; font-weight: 800; color: #ffffff !important; letter-spacing: -1px; }
    .seo-keywords { color: #64748b !important; font-size: 12px !important; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
    .level-header { background: #1e293b; padding: 10px 20px; border-radius: 8px; border-left: 4px solid #3b82f6; margin-bottom: 20px; font-weight: bold; }
    .progress-wrapper { background: #1e293b; border-radius: 10px; height: 12px; margin-bottom: 35px; overflow: hidden; border: 1px solid #334155; }
    .progress-bar-fill { background: linear-gradient(90deg, #3b82f6, #10b981); height: 100%; }
    .dna-container { background: #111726; padding: 25px; border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 25px; }
    .output-card { background: #030712; padding: 22px; border-radius: 12px; border: 1px solid #1e2937; margin-bottom: 15px; }
    .output-card.prime { border-left: 4px solid #10b981; }
    .dna-badge { background: rgba(59, 130, 246, 0.15); color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.3); padding: 4px 12px; border-radius: 6px; font-size: 13px !important; display: inline-block; margin-right: 8px; margin-top: 6px; font-weight: 600; }
    .salary-tag { background: rgba(16, 185, 129, 0.2); color: #10b981 !important; border: 1px solid #10b981; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 14px !important; display: inline-block; }
    .prob-tag { float: right; background: #1f2937; color: #ffffff !important; border: 1px solid #374151; padding: 3px 10px; border-radius: 20px; font-size: 12px !important; font-weight: bold; }
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 10px !important; padding: 14px 28px !important; border: none !important; width: 100%; font-size: 16px !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="seo-banner">
        <div class="seo-title">🧭 IDENTITYPATH OS</div>
        <div class="seo-keywords">AI Career Guidance • Student Profiling System</div>
    </div>
""", unsafe_allow_html=True)

if "auth_verified" not in st.session_state: st.session_state.auth_verified = False
if not st.session_state.auth_verified:
    c_l, c_m, c_r = st.columns([1, 1.8, 1])
    with c_m:
        st.markdown("<h4 style='text-align: center;'>🔐 Accessing IdentityPath Core</h4>", unsafe_allow_html=True)
        pwd = st.text_input("Enter Jumper Security Token :", type="password")
        if pwd == "Arwagiftorient":
            if st.button("Boot Profiling Engine ⚡"):
                st.session_state.auth_verified = True
                st.rerun()
    st.stop()

if "current_level" not in st.session_state: st.session_state.current_level = 1
if "dna_vault" not in st.session_state: st.session_state.dna_vault = {}

progress_percent = (st.session_state.current_level - 1) * 33.3
if st.session_state.current_level == 4: progress_percent = 100.0

st.markdown(f"""
    <div style="margin-bottom: 5px; font-weight: bold; font-size: 14px; color: #94a3b8;">PROFILING TASK COMPLETION : {int(progress_percent)}%</div>
    <div class="progress-wrapper"><div class="progress-bar-fill" style="width: {progress_percent}%;"></div></div>
""", unsafe_allow_html=True)

if st.session_state.current_level == 1:
    st.markdown("<div class='level-header'>🎮 LEVEL 1: Who Are You?</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Âge de l'étudiant :", ["14 ans", "15 ans", "16 ans", "17 ans", "18 ans", "19 ans+"])
        location = st.text_input("Pays / Ville :", value="Maroc, Casablanca")
    with col2:
        scolaire = st.selectbox("Niveau scolaire :", ["Collège", "Lycée : Troncs Communs", "Lycée : 1ère année Bac", "Lycée : 2ème année Bac", "Université"])
        filiere = st.selectbox("Filière visée :", ["Sciences Mathématiques", "Sciences Physiques", "Sciences Économiques", "Technologies / Informatique"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Unlock Level 2 ➡️"):
        st.session_state.dna_vault.update({"age": age, "location": location, "scolaire": scolaire, "filiere": filiere})
        st.session_state.current_level = 2
        st.rerun()

elif st.session_state.current_level == 2:
    st.markdown("<div class='level-header'>🎮 LEVEL 2: Your Skills</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: feel_math = st.selectbox("Maths :", ["Excellent", "Moyen", "Difficile"])
    with c2: feel_physics = st.selectbox("Physique :", ["Excellent", "Moyen", "Difficile"])
    with c3: note_lycee = st.slider("Moyenne :", 10.0, 20.0, 16.5, step=0.1)
    cl1, cl2, cl3 = st.columns(3)
    with cl1: lang_en = st.selectbox("Anglais :", ["C2", "C1", "B2", "B1"])
    with cl2: lang_fr = st.selectbox("Français :", ["C2", "C1", "B2", "B1"])
    with cl3: lang_ar = st.selectbox("Arabe :", ["C2", "C1", "B2", "B1"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Unlock Level 3 ➡️"):
        st.session_state.dna_vault.update({"math": feel_math, "physics": feel_physics, "note": note_lycee, "en": lang_en, "fr": lang_fr, "ar": lang_ar})
        st.session_state.current_level = 3
        st.rerun()

elif st.session_state.current_level == 3:
    st.markdown("<div class='level-header'>🎮 LEVEL 3: Future Direction</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        domaines = st.multiselect("🎯 Domaines :", ["IA / Tech", "Architecture / Design", "Médecine", "Business / Finance", "Environnement"], default=["IA / Tech"])
        objectifs = st.radio("🏁 Objectif :", ["Bourse complète international", "Top Université", "Startup", "Pas encore sûr"])
    with col_i2:
        perso = st.radio("🧠 Style :", ["Pratique & Action", "Théorie & Recherche"])
        budget = st.selectbox("💰 Budget :", ["Bourse obligatoire", "Prise en charge partielle", "Autonome"])
        mobilite = st.radio("✈️ Mobilité :", ["International", "Maroc"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("⚡ Generate Paths 🚀"):
        st.session_state.dna_vault.update({"domaines": domaines, "objectifs": objectifs, "perso": perso, "budget": budget, "mobilite": mobilite})
        st.session_state.current_level = 4
        st.rerun()

elif st.session_state.current_level == 4:
    st.markdown("<div class='level-header'>🏁 LEVEL 4: Report</div>", unsafe_allow_html=True)
    v = st.session_state.dna_vault
    interets_join = " ".join(v["domaines"]).lower()
    
    if "architecture" in interets_join:
        filiere_label, salaire_label = "Architecture & Design", "45,000$ à 110,000$"
        opt1, opt2, opt3 = "Bachelor of Architecture", "Ingénierie Civile", "ENA Maroc"
    elif "ia" in interets_join or "tech" in interets_join:
        filiere_label, salaire_label = "Intelligence Artificielle & Computer Science", "65,000$ à 155,000$"
        opt1, opt2, opt3 = "Bachelor in Computer Science", "Grandes Écoles Tech", "Génie Logiciel"
    else:
        filiere_label, salaire_label = "Business Management & Finance", "50,000$ à 125,000$"
        opt1, opt2, opt3 = "BBA International", "Management des SI", "Écoles de Commerce"

    chances_calcul = min(int(v["note"] * 4.65), 96)
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        st.markdown(f"""
            <div class="dna-container">
                <h4>🧬 DNA Signature</h4>
                <div class="dna-badge">Moyenne: {v['note']}/20</div>
                <div class="dna-badge">Anglais: {v['en']}</div>
                <div class="dna-badge">Budget: {v['budget']}</div>
            </div>
        """, unsafe_allow_html=True)
    with col_d2:
        st.markdown(f"""
            <div class="output-card prime">
                <span class="prob-tag">Score: {chances_calcul}%</span>
                <h4>🎯 Trajectoire : {filiere_label}</h4>
                <p><b>Alpha :</b> {opt1}<br><b>Bêta :</b> {opt2}<br><b>Gamma :</b> {opt3}</p>
                <div class="salary-tag">💰 {salaire_label} / an</div>
            </div>
        """, unsafe_allow_html=True)
    if st.button("🔄 Restart"):
        st.session_state.current_level = 1
        st.session_state.dna_vault = {}
        st.rerun()
