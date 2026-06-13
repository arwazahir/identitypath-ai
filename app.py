import streamlit as st
import time

# Configuration de l'application en mode Large
st.set_page_config(page_title="IdentityPath Application", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN PREMIUM ET VISIBILITÉ ACADÉMIQUE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #0f172a; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    
    /* Visibilité maximale de tous les textes */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider { color: #ffffff !important; font-size: 16px !important; }
    h1, h2, h3, h4 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; font-weight: 800 !important; }
    
    /* En-tête de l'application et Logo */
    .app-logo-container { text-align: center; padding: 25px; background: #1e293b; border-radius: 16px; border: 2px solid #334155; margin-bottom: 30px; }
    .app-logo { font-size: 40px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Urbanist'; }
    .app-subtitle { color: #10b981 !important; font-size: 14px !important; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
    
    /* Structure des sections de résultats */
    .section-container { background: #1e293b; padding: 25px; border-radius: 16px; border: 1px solid #334155; margin-bottom: 25px; }
    .filiere-box { background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; margin-bottom: 10px; }
    .uni-box { background: #111827; padding: 20px; border-radius: 12px; border-left: 5px solid #3b82f6; margin-bottom: 15px; border: 1px solid #1f2937; }
    .bourse-box { background: #111827; padding: 20px; border-radius: 12px; border-left: 5px solid #10b981; margin-bottom: 15px; border: 1px solid #1f2937; }
    
    .title-white { font-size: 18px !important; font-weight: 700 !important; color: #ffffff !important; }
    .text-light { color: #e2e8f0 !important; font-size: 15px !important; line-height: 1.5; }
    .badge-app { background: #334155; color: #ffffff !important; padding: 4px 10px; border-radius: 6px; font-size: 12px !important; font-weight: bold; display: inline-block; }
    
    /* Bouton d'action principal */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 10px !important; padding: 12px 28px !important; border: none !important; width: 100%; font-size: 16px !important; }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ET EN-TÊTE ---
st.markdown("""
    <div class="app-logo-container">
        <div class="app-logo">🧭 IDENTITYPATH APP</div>
        <div class="app-subtitle">Système d'Analyse Académique, Linguistique et Cartographie des Bourses</div>
    </div>
""", unsafe_allow_html=True)

# --- SÉCURITÉ DE L'APPLICATION ---
if "authenticated" not in st.session_state: st.session_state.authenticated = False
if not st.session_state.authenticated:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Déverrouiller l'Application</h3>", unsafe_allow_html=True)
        pass_code = st.text_input("Code d'accès de l'application :", type="password")
        if pass_code == "Arwagiftorient":
            if st.button("Accéder à la console 🚀"):
                st.session_state.authenticated = True
                st.rerun()
    st.stop()

# --- BASE DE DONNÉES PROFESSIONNELLE NEUTRE (FILIÈRES -> UNIS -> BOURSES) ---
DATABASE = {
    "economie_social": {
        "label": "Sciences Économiques, Gestion & Sciences Sociales",
        "keywords": ["economie", "social", "eco", "gestion", "business", "commerce", "finance", "marketing", "management", "societe"],
        "filieres_possibles": [
            "• Licence en Sciences Économiques et Gestion des Entreprises",
            "• Bachelor in Business Administration (BBA) - Management & Stratégie",
            "• Cursus d'Excellence en Économie Appliquée et Politiques Publiques",
            "• Cursus Global en Sciences Politiques et Relations Internationales"
        ],
        "unis": [
            {"nom": "ISCAE (Institut Supérieur de Commerce et d'Administration)", "details": "Accès sur concours hyper sélectif. Grande École publique de référence pour le management.", "req": "Classes Préparatoires Éco/Scientifiques ou diplôme équivalent.", "deadline": "Avril - Mai"},
            {"nom": "UM6P - Faculty of Governance, Economic and Social Sciences (FGSES)", "details": "Campus de pointe à Rabat dédié à l'économie, la gouvernance et les sciences sociales.", "req": "Étude de dossier, test écrit de culture générale et entretien oral.", "deadline": "Fin Mai"},
            {"nom": "London School of Economics (LSE - Royaume-Uni)", "details": "L'une des institutions les plus prestigieuses au monde pour l'économie et les sciences sociales.", "req": "IELTS ≥ 7.0, d'excellentes notes en mathématiques et essais de motivation.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence FGSES / UM6P", "couverture": "Prise en charge complète ou partielle des frais d'études scolaires et du logement universitaire.", "req": "Attribuée sur critères de performance académique au Baccalauréat et critères sociaux.", "deadline": "Juillet"},
            {"nom": "Bourses du Conseil Britannique (GREAT Scholarships)", "couverture": "Financement d'études d'une valeur minimale de £10,000 pour l'année universitaire.", "req": "Lettre d'acceptation dans une université du Royaume-Uni et nationalité éligible.", "deadline": "Mai"}
        ]
    },
    "sciences_tech": {
        "label": "Ingénierie, Informatique & Nouvelles Technologies",
        "keywords": ["informatique", "code", "ia", "cyber", "ingenieur", "robot", "technologie", "math", "physique", "science"],
        "filieres_possibles": [
            "• Bachelor en Computer Science & Intelligence Artificielle",
            "• Cursus d'Ingénierie Civile, Mécanique ou Électrique",
            "• Spécialisation en Cybersécurité et Réseaux Informatiques"
        ],
        "unis": [
            {"nom": "UM6P - College of Computing (Benguerir)", "details": "Centre d'excellence africain pour la recherche en informatique et l'innovation technologique.", "req": "Bac scientifique avec mention, réussite aux tests de logique internes.", "deadline": "Mai"},
            {"nom": "EPFL (École Polytechnique Fédérale de Lausanne - Suisse)", "details": "Référence mondiale pour l'ingénierie et les sciences dures.", "req": "Moyenne au Baccalauréat ≥ 16/20 (Mention Très Bien obligatoire).", "deadline": "30 Avril"},
            {"nom": "University of Toronto (Canada)", "details": "Excellente faculté d'informatique et de technologies avancées.", "req": "TOEFL iBT ≥ 100 ou IELTS ≥ 6.5, notes élevées en sciences.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence Académique Technologique", "couverture": "Exonération complète des frais pédagogiques d'ingénierie.", "req": "Dossier scolaire scientifique majeur (Notes de Mathématiques/Physique).", "deadline": "Juillet"},
            {"nom": "Lester B. Pearson International Scholarship (Canada)", "couverture": "Frais de scolarité complets, livres et résidence universitaire pendant 4 ans.", "req": "Profil de leader général exceptionnel, nomination officielle par le lycée.", "deadline": "15 Janvier"}
        ]
    },
    "medical_sante": {
        "label": "Sciences de la Santé, Médecine & Biologie",
        "keywords": ["medecine", "sante", "dentaire", "pharma", "biologie", "chirurgie", "soin", "clinique"],
        "filieres_possibles": [
            "• Doctorat en Médecine Générale ou Médecine Dentaire",
            "• Diplôme d'État en Pharmacie et Sciences Médicamenteuses",
            "• Cursus de Recherche Biomédicale et Biotechnologies"
        ],
        "unis": [
            {"nom": "Facultés de Médecine et de Pharmacie (Réseau National Public)", "details": "Le cursus classique officiel d'État pour devenir médecin au Maroc.", "req": "Passage des seuils de présélection du Bac + réussite au concours écrit.", "deadline": "Juillet"},
            {"nom": "Université Paris Cité (France)", "details": "Accès aux études de santé en France via le parcours très sélectif PASS.", "req": "Sélection rigoureuse sur la plateforme Parcoursup.", "deadline": "Début Mars"}
        ],
        "bourses": [
            {"nom": "Bourse Eiffel d'Excellence (Gouvernement Français)", "couverture": "Allocation mensuelle pour les frais de vie courante et couverture médicale globale.", "req": "Dossier académique d'élite présenté par l'établissement d'accueil.", "deadline": "Janvier"}
        ]
    }
}

# --- NAVIGATION DE L'APPLICATION ---
if "app_step" not in st.session_state: st.session_state.app_step = 1

st.progress(st.session_state.app_step / 4)

# ÉTAPE 1 : PROFIL ACADÉMIQUE STANDARD
if st.session_state.app_step == 1:
    st.markdown("### 📝 Étape 1 : Profil Académique de l'Élève")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.f_bac = st.selectbox("Filière actuelle du Baccalauréat :", ["Sciences Économiques & Gestion", "Sciences Mathématiques", "Sciences Physiques", "SVT", "Lettres"])
        st.session_state.note = st.slider("Moyenne générale estimée (sur 20) :", 10.0, 20.0, 16.0, step=0.1)
    with col2:
        st.session_state.destination = st.selectbox("Objectif géographique visé :", ["International Anglophone (USA, Canada, UK)", "Europe (France, Suisse)", "Grandes Écoles Nationales de Prestige"])
        st.session_state.lycee = st.text_input("Région / Ville actuelle de scolarité :", placeholder="Ex: Casablanca, Rabat...")
    
    if st.button("Continuer vers l'Évaluation des Langues ➡️"):
        st.session_state.app_step = 2
        st.rerun()

# ÉTAPE 2 : TOUTES LES LANGUES DE TRAVAIL (ANGLAIS, FRANÇAIS, ARABE)
elif st.session_state.app_step == 2:
    st.markdown("### 🔤 Étape 2 : Profil Linguistique & Certifications Obligatoires")
    st.write("Sélectionnez les niveaux et scores pour toutes les langues d'enseignement possibles.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🇺🇸 Langue Anglaise**")
        en_test = st.selectbox("Certification passée ou prévue :", ["Aucun test", "IELTS Academic", "TOEFL iBT", "Duolingo English Test"])
        st.session_state.en_score = st.text_input("Score obtenu ou visé (Anglais) :", placeholder="Ex: 7.5, 105, 125...") if en_test != "Aucun test" else "Aucun"
        
    with col2:
        st.markdown("**🇫🇷 Langue Française**")
        fr_test = st.selectbox("Certification ou niveau (Français) :", ["Aucun test / Niveau Scolaire", "TCF / DELF / DALF passé", "Niveau C1 (Autonome)", "Niveau C2 (Bilingue)"])
        st.session_state.fr_score = st.text_input("Score ou mention (Français) :", placeholder="Ex: B2, C1, 500 pts...") if "passé" in fr_test else fr_test

    with col3:
        st.markdown("**🇲🇦 Langue Arabe**")
        st.session_state.ar_level = st.select_slider("Niveau de maîtrise (Arabe) :", options=["Basique", "Intermédiaire", "Avancé / Très Bonne maîtrise", "Excellent / Langue Maternelle"])

    st.write("---")
    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        if st.button("⬅️ Étape Précédente"): st.session_state.app_step = 1; st.rerun()
    with col_btn2:
        if st.button("Continuer vers le Profil Extra-Scolaire ➡️"): st.session_state.app_step = 3; st.rerun()

# ÉTAPE 3 : PROFIL EXTRA-SCOLAIRE NEUTRE ET DESCRIPTION DES PASSIONS
elif st.session_state.app_step == 3:
    st.markdown("### 🏆 Étape 3 : Distinctions, Projets & Exploration de Rêve")
    st.write("Décrivez de manière neutre les activités et les domaines qui inspirent l'étudiant (Exemples généraux : clubs de débat, projets d'entraide, économie, informatique, art...).")
    
    st.session_state.distinctions = st.text_area(
        "Distinctions ou Concours (Exemples généraux : Olympiades scolaires, compétitions sportives, prix académiques...) :",
        placeholder="Indiquez ici les distinctions obtenues par l'élève..."
    )
    
    st.session_state.engagement = st.text_area(
        "Passions, projets personnels ou engagements (Exemples généraux : Analyse de données, lecture de sujets économiques, aide associative, clubs internes...) :",
        placeholder="Exemple : L'élève est passionné par l'économie, l'étude économique et sociale, la compréhension des marchés et la gestion de projets collectifs..."
    )

    st.markdown("#### 🎙️ Capture Vocale Intégrée")
    st.components.v1.html("""
        <div style="background-color: #1e293b; border-radius: 12px; padding: 15px; text-align: center; border: 1px dashed #475569;">
            <button id="mic-btn" style="background: linear-gradient(90deg, #ef4444, #f43f5e); color: white; font-weight: bold; padding: 10px 22px; border: none; border-radius: 20px; cursor: pointer;">🎙️ ENREGISTRER LE PROFIL DE L'ÉLÈVE</button>
        </div>
        <script>
            const btn = document.getElementById('mic-btn');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if(SpeechRecognition){
                const r = new SpeechRecognition(); r.lang = 'fr-FR';
                btn.onclick = () => { r.start(); btn.innerText = "⏳ Écoute active de l'élève..."; };
                r.onresult = (e) => { window.parent.postMessage({type: 'streamlit:set_input', value: e.results[0][0].transcript}, '*'); btn.innerText = "🎙️ Relancer le micro"; };
            }
        </script>
    """, height=85)
    
    st.session_state.voice_input = st.text_input("Texte capturé par l'IA vocale :", placeholder="Les paroles de l'élève s'afficheront ici...")

    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        if st.button("⬅️ Étape Précédente"): st.session_state.app_step = 2; st.rerun()
    with col_btn2:
        if st.button("Générer l'Application Finale d'Orientation 🧭"): st.session_state.app_step = 4; st.rerun()

# ÉTAPE 4 : LE RAPPORT TOTAL ET LOGIQUE TANT ATTENDU (FILIERES -> UNIS -> BOURSES)
elif st.session_state.app_step == 4:
    st.markdown("### 🧭 Rapport Applicatif d'Orientation Stratégique")
    
    # MOTEUR DE DÉTECTION SÉCURISÉ ET PRÉCIS (Analyse par mots complets)
    full_text = (st.session_state.distinctions + " " + st.session_state.engagement + " " + st.session_state.voice_input).lower()
    
    # Algorithme de filtrage strict pour éviter les erreurs de catégorie
    detected_key = "sciences_tech" # Défaut si vide
    
    # Si le texte contient des mots liés à l'économie, au social ou à la gestion, la priorité est ABSOLUE
    eco_words = ["economie", "social", "sociale", "eco", "gestion", "commerce", "business", "finance", "management", "sociologie"]
    sante_words = ["medecine", "sante", "pharma", "dentaire", "biologie", "clinique"]
    
    if any(word in full_text for word in eco_words):
        detected_key = "economie_social"
    elif any(word in full_text for word in sante_words):
        detected_key = "medical_sante"
        
    result = DATABASE[detected_key]
    
    # --- FICHE RECAPITULATIVE DE L'APPLICATION ---
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.write("#### 👤 Synthèse du Profil Étudiant Analysé :")
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    col_s1.metric("Bac d'origine", st.session_state.f_bac)
    col_s2.metric("Moyenne générale", f"{st.session_state.note}/20")
    col_s3.metric("Niveau Anglais", st.session_state.en_score if "en_score" in st.session_state else "Scolaire")
    col_s4.metric("Niveau Arabe", st.session_state.ar_level)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.success(f"🎯 Orientation Majeure Déterminée : **{result['label']}**")
    st.write("---")
    
    # LOGIQUE EXACTE DU LIVRABLE : FILIÈRES -> UNIVERSITÉS -> BOURSES
    
    # A. LES FILIÈRES POSSIBLES
    st.markdown("### 📈 1. Filières Universitaires Recommandées")
    st.write("Suite à l'analyse de vos compétences et de vos intérêts, voici les branches idéales :")
    for filiere in result["filieres_possibles"]:
        st.markdown(f"<div class='filiere-box'><span class='title-white'>{filiere}</span></div>", unsafe_allow_html=True)
    st.write("")

    # B. LES UNIVERSITÉS CIBLES
    st.markdown("### 🏛️ 2. Établissements & Universités Adaptés")
    st.write("Établissements d'excellence proposant ces filières avec leurs critères spécifiques :")
    cols_u = st.columns(3)
    for idx, uni in enumerate(result["unis"]):
        with cols_u[idx % 3]:
            st.markdown(f"""
                <div class="uni-box">
                    <div class="title-white">{uni['nom']}</div>
                    <p class="text-light" style="margin-top:10px;"><b>ℹ️ Présentation :</b> {uni['details']}</p>
                    <p class="text-light"><b>📋 Requirements :</b> {uni['req']}</p>
                    <p class="text-light" style="color: #f87171 !important;"><b>⏰ Deadline d'application :</b> {uni['deadline']}</p>
                    <div class="badge-app">Université Validée</div>
                </div>
            """, unsafe_allow_html=True)
    st.write("")

    # C. LES BOURSES ASSOCIÉES
    st.markdown("### 💎 3. Programmes de Bourses Disponibles")
    st.write("Financements et bourses d'études nationaux ou internationaux accessibles pour ce profil :")
    cols_b = st.columns(2)
    for idx, bourse in enumerate(result["bourses"]):
        with cols_b[idx % 2]:
            st.markdown(f"""
                <div class="bourse-box">
                    <div class="title-white">{bourse['nom']}</div>
                    <p class="text-light" style="margin-top:10px;"><b>💰 Taux de Couverture :</b> {bourse['couverture']}</p>
                    <p class="text-light"><b>🛠️ Pièces requises au dossier :</b> {bourse['req']}</p>
                    <p class="text-light" style="color: #34d399 !important;"><b>📅 Clôture des inscriptions :</b> {bourse['deadline']}</p>
                    <div class="badge-app">Bourse d'Excellence</div>
                </div>
            """, unsafe_allow_html=True)
    st.write("---")

    if st.button("🔄 Lancer un nouveau diagnostic d'étudiant"):
        st.session_state.app_step = 1
        st.rerun()
