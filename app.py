import streamlit as st
import time

# --- CONFIGURATION ARCHITECTURE IDENTITYPATH (SEO & GOOGLE INDEXING KEYS) ---
st.set_page_config(
    page_title="IdentityPath | AI Student Profiling System & Career Guidance",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INJECTION DU DESIGN PREMIUM : INTERACTIVE STORY MODE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');
    
    /* Variables de structure */
    :root { --bg-core: #090d16; --card-bg: #111726; --accent-blue: #3b82f6; --accent-green: #10b981; --text-white: #ffffff; }
    
    .main { background-color: #090d16; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #090d16; font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Visibilité absolue sans compromis */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    
    /* Header Industriel IdentityPath - Balisage SEO */
    .seo-banner { text-align: left; padding: 30px; background: linear-gradient(135deg, #111827 0%, #030712 100%); border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 30px; }
    .seo-title { font-size: 38px; font-weight: 800; color: #ffffff !important; letter-spacing: -1px; }
    .seo-keywords { color: #64748b !important; font-size: 12px !important; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
    
    /* Barrettes de niveau & Progression */
    .level-header { background: #1e293b; padding: 10px 20px; border-radius: 8px; border-left: 4px solid #3b82f6; margin-bottom: 20px; font-weight: bold; }
    .progress-wrapper { background: #1e293b; border-radius: 10px; height: 12px; margin-bottom: 35px; overflow: hidden; border: 1px solid #334155; }
    .progress-bar-fill { background: linear-gradient(90deg, #3b82f6, #10b981); height: 100%; transition: width 0.4s ease-in-out; }
    
    /* Composants UI : Choix rapides */
    .dna-container { background: #111726; padding: 25px; border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 25px; }
    .output-card { background: #030712; padding: 22px; border-radius: 12px; border: 1px solid #1e2937; margin-bottom: 15px; }
    .output-card.prime { border-left: 4px solid #10b981; }
    
    /* Badges de l'ADN */
    .dna-badge { background: rgba(59, 130, 246, 0.15); color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.3); padding: 4px 12px; border-radius: 6px; font-size: 13px !important; display: inline-block; margin-right: 8px; margin-top: 6px; font-weight: 600; }
    .salary-tag { background: rgba(16, 185, 129, 0.2); color: #10b981 !important; border: 1px solid #10b981; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 14px !important; display: inline-block; }
    .prob-tag { float: right; background: #1f2937; color: #ffffff !important; border: 1px solid #374151; padding: 3px 10px; border-radius: 20px; font-size: 12px !important; font-weight: bold; }
    
    /* Action Button principal */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 10px !important; padding: 14px 28px !important; border: none !important; width: 100%; font-size: 16px !important; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2); }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(16, 185, 129, 0.3); }
    </style>
""", unsafe_allow_html=True)

# --- BANNIÈRE D'INDEXATION GOOGLE BRANDING ---
st.markdown("""
    <div class="seo-banner">
        <div class="seo-title">🧭 IDENTITYPATH OS</div>
        <div class="seo-keywords">AI Career Guidance • Student Profiling System • Scholarship Matching AI • Education Pathway Generator</div>
    </div>
""", unsafe_allow_html=True)

# --- SYSTÈME D'AUTHENTIFICATION DE LA PLATFORME ---
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

# --- INITIALISATION DU MOTEUR INTERACTIF (STAGES DE PROGRESSION) ---
if "current_level" not in st.session_state: st.session_state.current_level = 1
if "dna_vault" not in st.session_state: st.session_state.dna_vault = {}

# CALCUL DU POURCENTAGE DE LA BARRE DE PROGRESSION COMPORTEMENTALE
progress_percent = (st.session_state.current_level - 1) * 33.3
if st.session_state.current_level == 4: progress_percent = 100.0

st.markdown(f"""
    <div style="margin-bottom: 5px; font-weight: bold; font-size: 14px; color: #94a3b8;">PROFILING TASK COMPLETION : {int(progress_percent)}%</div>
    <div class="progress-wrapper">
        <div class="progress-bar-fill" style="width: {progress_percent}%;"></div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# LEVEL 1: WHO ARE YOU? (BASIC IDENTITY LAYER)
# ==============================================================================
if st.session_state.current_level == 1:
    st.markdown("<div class='level-header'>🎮 LEVEL 1: Who Are You? (Basic Identity Layer)</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Âge de l'étudiant :", ["14 ans", "15 ans", "16 ans", "17 ans", "18 ans", "19 ans+"])
        location = st.text_input("Pays / Ville de résidence actuel :", value="Maroc, Casablanca")
    with col2:
        scolaire = st.selectbox("Niveau scolaire actuel (Crucial) :", [
            "Collège (3ème / Préparation Lycée)",
            "Lycée : Troncs Communs / 10ème année",
            "Lycée : 1ère année Bac / Penultimate Year",
            "Lycée : 2ème année Bac / Terminale",
            "Étudiant Universitaire (En réorientation)"
        ])
        filiere = st.selectbox("Filière académique actuelle ou visée :", [
            "Sciences Mathématiques", "Sciences Physiques / Expérimentales", 
            "Sciences Économiques & Gestion", "Technologies / Informatique", "Lettres & Sciences Humaines"
        ])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Unlock Level 2: Academic Profile ➡️"):
        st.session_state.dna_vault.update({"age": age, "location": location, "scolaire": scolaire, "filiere": filiere})
        st.session_state.current_level = 2
        st.rerun()

# ==============================================================================
# LEVEL 2: YOUR SKILLS (ACADEMIC & LANGUAGE MATRIX)
# ==============================================================================
elif st.session_state.current_level == 2:
    st.markdown("<div class='level-header'>🎮 LEVEL 2: Your Skills (Academic & Language Matrix)</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    st.write("📈 **Auto-évaluation rapide des matières clés :**")
    c1, c2, c3 = st.columns(3)
    with c1:
        feel_math = st.selectbox("Comment tu te sens en Maths ?", ["Facile (Excellent niveau)", "Moyen (Niveau stable)", "Difficile (Points faibles)"])
    with c2:
        feel_physics = st.selectbox("Comment tu te sens en Physique / Sciences ?", ["Facile (Excellent niveau)", "Moyen (Niveau stable)", "Difficile (Points faibles)"])
    with c3:
        note_lycee = st.slider("Moyenne générale approximative (sur 20) :", 10.0, 20.0, 16.5, step=0.1)
        
    st.write("---")
    st.write("🌐 **Profil des langues (Cadre Européen CECRL) :**")
    cl1, cl2, cl3 = st.columns(3)
    with cl1:
        lang_en = st.selectbox("Anglais :", ["C2 (Bilingue)", "C1 (Avancé)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)", "A2 / A1"])
    with cl2:
        lang_fr = st.selectbox("Français :", ["C2 (Bilingue)", "C1 (Avancé)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)", "A2 / A1"])
    with cl3:
        lang_ar = st.selectbox("Arabe :", ["C2 (Bilingue)", "C1 (Avancé)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)", "A2 / A1"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Unlock Level 3: Direction & Goals ➡️"):
        st.session_state.dna_vault.update({
            "math": feel_math, "physics": feel_physics, "note": note_lycee,
            "en": lang_en, "fr": lang_fr, "ar": lang_ar
        })
        st.session_state.current_level = 3
        st.rerun()

# ==============================================================================
# LEVEL 3: FUTURE DIRECTION (INTERESTS, PERSONALITY & CONSTRAINTS)
# ==============================================================================
elif st.session_state.current_level == 3:
    st.markdown("<div class='level-header'>🎮 LEVEL 3: Future Direction (Interests, Personality & Constraints)</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns(2)
    
    with col_i1:
        domaines = st.multiselect("🎯 Sélectionne tes 3 domaines d'intérêt majeurs :", [
            "IA / Tech / Computer Science", "Architecture / Design / Urbanisme", 
            "Médecine / Biotechnologies", "Business / Entrepreneuriat / Finance", 
            "Environnement / Développement Durable", "Droit / Relations Internationales"
        ], default=["IA / Tech / Computer Science", "Architecture / Design / Urbanisme"])
        
        objectifs = st.radio("🏁 Quel est ton objectif ultime à la sortie du lycée ?", [
            "Obtenir une bourse complète (100%) pour l'international",
            "Intégrer une Top Université Mondiale de prestige",
            "Lancer ma Startup / Focus Entrepreneuriat",
            "Pas encore sûr / Je veux que 3allal explore mes options"
        ])
        
    with col_i2:
        perso = st.radio("🧠 Style de travail préféré :", [
            "Je préfère la Pratique & l'Action concrète",
            "Je préfère la Théorie & la Recherche conceptuelle"
        ])
        
        budget = st.selectbox("💰 Contraintes financières familiales (Logistique) :", [
            "Faible (Bourse d'étude complète obligatoire)",
            "Moyen (Prise en charge partielle possible)",
            "Élevé (Financement autonome sans contraintes)"
        ])
        
        mobilité = st.radio("✈️ Mobilité internationale :", ["Je peux partir n'importe où", "Je préfère rester au Maroc"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("⚡ Generate Personalized Future Paths 🚀"):
        st.session_state.dna_vault.update({
            "domaines": domaines, "objectifs",: objectifs, 
            "perso": perso, "budget": budget, "mobilite": mobilité
        })
        st.session_state.current_level = 4
        st.rerun()

# ==============================================================================
# LEVEL 4: INSTANT REWARD (3ALLAL PREDICTIVE INSIGHTS GENERATOR)
# ==============================================================================
elif st.session_state.current_level == 4:
    st.markdown("<div class='level-header'>🏁 LEVEL 4: 3allal Profile Unlock & Instant Pathway Report</div>", unsafe_allow_html=True)
    
    # Lecture des variables de l'ADN compilées
    v = st.session_state.dna_vault
    note_eleve = v["note"]
    filiere_eleve = v["filiere"]
    scolaire_eleve = v["scolaire"]
    
    # Algorithme d'aiguillage sémantique étanche pour déterminer la trajectoire principale
    interets_join = " ".join(v["domaines"]).lower()
    
    if "architecture" in interets_join:
        filiere_label = "Architecture, Design Numérique 3D & Urbanisme Intelligent"
        salaire_label = "45,000$ à 110,000$ / an"
        opt1 = "Bachelor of Architecture (B.Arch) — Focus International (Turquie / Europe / Moyen-Orient)"
        opt2 = "Double Cursus Élite : Ingénierie Civile + Conception d'Espace Durable"
        opt3 = "Écoles Nationales d'Architecture de Prestige (ENA Maroc / Concours direct)"
        mission_1 = "Construire un mini-portfolio de 5 réalisations graphiques ou croquis d'espace."
        road_target = "Architecture & Urban Planning Strategy"
    elif "ia" in interets_join or "tech" in interets_join:
        filiere_label = "Intelligence Artificielle, Cloud Architecture & Computer Science"
        salaire_label = "65,000$ à 155,000$ / an"
        opt1 = "Bachelor in Computer Science — Spécialisation Data & Algorithmes (Canada / Asie)"
        opt2 = "Classes Préparatoires Intégrées ou Grandes Écoles Technologiques d'Élite"
        opt3 = "Filières d'Ingénierie Quantique et Développement de Solutions Logicielles"
        mission_1 = "Valider les bases du langage Python et créer un mini-script d'automatisation."
        road_target = "Computer Science & Tech Innovation"
    elif "médecine" in interets_join or "biotechnologies" in interets_join:
        filiere_label = "Sciences de la Santé, Médecine Clinique & Bio-Informatique"
        salaire_label = "75,000$ à 200,000$ / an"
        opt1 = "Doctorat d'État en Médecine Humaine / Cursus Hospitalier Classique"
        opt2 = "Bachelor en Sciences Biomédicales et Génie Génétique (Écosystèmes Internationaux)"
        opt3 = "Recherche Avancée en Neurosciences et Modélisation Moléculaire"
        mission_1 = "Participer à un stage de sensibilisation ou décrocher une attestation de premiers secours."
        road_target = "Biomedical & Medical Sciences Track"
    else:
        filiere_label = "International Business Management, Finance & Data Analytics"
        salaire_label = "50,000$ à 125,000$ / an"
        opt1 = "Bachelor in Business Administration (BBA) — Double Diplôme International"
        opt2 = "Management des Systèmes d'Information et Analyse Stratégique des Marchés"
        opt3 = "Écoles de Commerce Majeures (FGSES, Portails d'Excellence d'État)"
        mission_1 = "Analyser et cartographier le Business Model d'une startup technologique existante."
        road_target = "Business Strategy & Global Economy"

    # Calcul mathématique des chances réelles d'admission (Score de potentiel)
    chances_calcul = int(note_eleve * 4.65)
    if chances_calcul > 96: chances_calcul = 96

    # 📊 AFFICHAGE VERTICAL : LE RAPPORT DE SYNTHÈSE DIGITAL TWIN
    col_d1, col_d2 = st.columns([1, 2])
    
    with col_d1:
        st.markdown("### 🧬 AI Student DNA Signature")
        st.markdown(f"""
            <div class="dna-container" style="border-top: 4px solid #3b82f6;">
                <p style="font-size: 14px; color:#94a3b8 !important; margin:0;">[FICHE D'IDENTITÉ COMPILÉE EN 2 MIN]</p>
                <h4 style="margin-top:5px; color:#38bdf8 !important;">Statut Détecté</h4>
                <div style="margin-top:10px;">
                    <div class="dna-badge">Niveau: {scolaire_eleve}</div>
                    <div class="dna-badge">Filière Lycée: {filiere_eleve}</div>
                    <div class="dna-badge">Moyenne: {note_eleve}/20</div>
                    <div class="dna-badge">Anglais: {v['en']}</div>
                    <div class="dna-badge">Français: {v['fr']}</div>
                    <div class="dna-badge">Style: {v['perso']}</div>
                    <div class="dna-badge">Budget: {v['budget']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_d2:
        st.markdown("### 🔮 3allal Path Options & Diagnostics")
        
        # Options d'études immédiates
        st.markdown(f"""
            <div class="output-card prime">
                <span class="prob-tag">Score Potentiel : {chances_calcul}%</span>
                <h4 style="margin:0;">🎯 Trajectoire Majeure Identifiée :</h4>
                <p style="font-size: 16px !important; color: #10b981 !important; font-weight: bold; margin-top:3px;">{filiere_label}</p>
                <div style="margin-top:12px;">
                    <b>Option Alpha :</b> {opt1}<br>
                    <b>Option Bêta :</b> {opt2}<br>
                    <b>Option Gamma :</b> {opt3}
                </div>
                <div style="margin-top:15px;">
                    <span style="font-size:13px; color:#94a3b8;">Estimation du Salaire Futur Mondial :</span><br>
                    <div class="salary-tag">💰 {salaire_label}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # 📜 ROADMAP SIMPLE & REALITY CHECK VERTICAL
    st.markdown("### 🧭 GPS Roadmap & Action Plan")
    
    st.markdown(f"""
        <div class="output-card" style="border-left: 4px solid #f59e0b;">
            <h5 style="color:#f59e0b !important;">🚨 AI Reality Check & Gap Analyzer :</h5>
            <p style="font-size:14px; margin-top:5px;">
                "Écoute-moi : ton niveau académique de <b>{note_eleve}/20</b> te donne un excellent élan. Mais attention, ton profil linguistique indique un niveau d'Anglais <b>{v['en']}</b> et de Français <b>{v['fr']}</b>. Pour débloquer la contrainte <b>'{v['budget']}'</b> sans risque de rejet par les commissions internationales, tu dois impérativement transformer tes intérêts en projets concrets avant l'automne pour maximiser tes probabilités."
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="output-card">
            <h5 style="color:#ffffff !important;">🗺️ Missions de Progression (Soft Game Tasks) :</h5>
            <div style="margin-top:10px; padding-left:15px; border-left: 2px dashed #3b82f6;">
                <p style="margin-bottom:12px;"><b>⚡ Mission 1 [Choose your direction] :</b> Fixer de manière étanche ta liste de 3 universités cibles dans ta zone préférentielle (<i>{v['mobilite']}</i>).</p>
                <p style="margin-bottom:12px;"><b>⚡ Mission 2 [Unlock your profile] :</b> {mission_1} Cela servira de preuve d'impact pour ton dossier.</p>
                <p style="margin-bottom:0px;"><b>⚡ Mission 3 [Find your path options] :</b> Planifier un examen blanc de langue officiel pour valider la certification minimale requise pour l'étranger.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    if st.button("🔄 Restart Profiling Mode / Create New Profile"):
        st.session_state.current_level = 1
        st.session_state.dna_vault = {}
        st.rerun()
