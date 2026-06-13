import streamlit as st
import time

# Configuration stricte de l'application
st.set_page_config(page_title="IdentityPath Application", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN APPLICATION PRO & VISIBILITÉ MAXIMALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
    
    /* Couleurs de l'application */
    .main { background-color: #0f172a; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    
    /* Force TOUS les textes Streamlit standards à être blancs et parfaitement lisibles */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider { color: #ffffff !important; font-size: 16px !important; }
    h1, h2, h3, h4 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; font-weight: 800 !important; }
    
    /* Le Logo de l'Application */
    .app-logo-container { text-align: center; padding: 20px; background: #1e293b; border-radius: 16px; border: 2px solid #334155; margin-bottom: 25px; }
    .app-logo { font-size: 38px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Urbanist'; }
    .app-subtitle { color: #10b981 !important; font-size: 15px !important; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
    
    /* Cartes Universités & Bourses hyper contrastées */
    .card-uni { background: #1e293b; padding: 22px; border-radius: 12px; border-left: 6px solid #3b82f6; margin-bottom: 15px; border-top: 1px solid #475569; border-right: 1px solid #475569; border-bottom: 1px solid #475569; }
    .card-bourse { background: #1e293b; padding: 22px; border-radius: 12px; border-left: 6px solid #10b981; margin-bottom: 15px; border-top: 1px solid #475569; border-right: 1px solid #475569; border-bottom: 1px solid #475569; }
    
    .title-item { font-size: 20px !important; font-weight: 700 !important; color: #ffffff !important; margin-bottom: 8px; }
    .text-item { color: #f1f5f9 !important; font-size: 15px !important; line-height: 1.5; }
    .badge-tag { background: #334155; color: #ffffff !important; padding: 5px 12px; border-radius: 6px; font-size: 13px !important; font-weight: bold; display: inline-block; margin-top: 8px; border: 1px solid #475569; }
    
    /* Boutons de l'application */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 10px !important; padding: 12px 28px !important; border: none !important; width: 100%; font-size: 16px !important; }
    </style>
""", unsafe_allow_html=True)

# --- EN-TÊTE ET LOGO OFFICIEL DE L'APPLICATION ---
st.markdown("""
    <div class="app-logo-container">
        <div class="app-logo">🧭 IDENTITYPATH APP</div>
        <div class="app-subtitle">Moteur d'Analyse Universel & Algorithme de Bourses d'Excellence</div>
    </div>
""", unsafe_allow_html=True)

# --- SÉCURISATION DU PRODUIT ---
if "app_auth" not in st.session_state: st.session_state.app_auth = False
if not st.session_state.app_auth:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Activation de l'Application</h3>", unsafe_allow_html=True)
        code = st.text_input("Veuillez entrer le code d'accès étudiant :", type="password")
        if code == "Arwagiftorient":
            if st.button("Lancer l'Application 🚀"):
                st.session_state.app_auth = True
                st.rerun()
    st.stop()

# --- BASE DE DONNÉES GLOBALE ET NEUTRE ---
APP_DATABASE = {
    "sciences_tech": {
        "label": "Ingénierie, Intelligence Artificielle & Technologies",
        "keywords": ["informatique", "code", "ia", "cyber", "ingenieur", "robot", "technologie", "math", "physique"],
        "unis": [
            {"nom": "UM6P (Université Mohammed VI Polytechnique)", "filiere": "School of Computer Science", "req": "Moyenne élevée au Bac scientifique, examen de sélection écrit et oral.", "deadline": "Mai - Juin"},
            {"nom": "EPFL (Suisse)", "filiere": "Bachelor en Sciences Informatiques", "req": "Moyenne au Baccalauréat ≥ 16/20 (Mention Très Bien obligatoire).", "deadline": "30 Avril"},
            {"nom": "University of Toronto (Canada)", "filiere": "Faculty of Engineering", "req": "Score IELTS ≥ 6.5 ou TOEFL ≥ 100, solides bases en mathématiques.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence Académique UM6P", "couverture": "Prise en charge de 100% des frais pédagogiques et du logement.", "req": "Dossier académique majeur et critères sociaux.", "deadline": "Juillet"},
            {"nom": "Lester B. Pearson Scholarship (Canada)", "couverture": "Frais de scolarité complets, hébergement et livres pendant 4 ans.", "req": "Excellence académique globale, lettre de nomination officielle de l'école.", "deadline": "15 Janvier"}
        ]
    },
    "business_finance": {
        "label": "Management, Sciences Économiques & Entrepreneuriat",
        "keywords": ["business", "management", "commerce", "finance", "marketing", "economie", "gestion"],
        "unis": [
            {"nom": "ISCAE (Institut Supérieur de Commerce)", "filiere": "Management & Commerce International", "req": "Sélection sur concours national après les classes préparatoires.", "deadline": "Avril / Mai"},
            {"nom": "HEC Paris (France)", "filiere": "BSc in Data, Society and Organisations", "req": "Dossier scolaire de premier rang, lettre de motivation et entretien.", "deadline": "Sessions de Octobre à Mars"},
            {"nom": "Wharton School (University of Pennsylvania - USA)", "filiere": "Bachelor of Science in Economics", "req": "Dossier global d'excellence (SAT/ACT, essais, recommandations).", "deadline": "5 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence de la Fondation HEC", "couverture": "Exonération partielle à totale des frais annuels de scolarité.", "req": "Attribuée automatiquement lors de l'admission aux profils majeurs.", "deadline": "Lors de l'admission"},
            {"nom": "Penn World Scholars Program (USA)", "couverture": "Aide financière sur mesure indexée sur les besoins du profil.", "req": "Potentiel de leadership international avéré et engagement citoyen.", "deadline": "Lors du dépôt de candidature"}
        ]
    },
    "medical_sante": {
        "label": "Sciences Médicales, Biologie & Santé",
        "keywords": ["medecine", "sante", "dentaire", "pharma", "biologie", "chirurgie", "clinique", "soin"],
        "unis": [
            {"nom": "Facultés de Médecine et de Pharmacie (Public)", "filiere": "Médecine Générale / Odontologie", "req": "Présélection nationale basée sur la note du Bac + Concours écrit.", "deadline": "Juillet"},
            {"nom": "Université Paris Cité (France)", "filiere": "Parcours Accès Santé (PASS)", "req": "Sélection rigoureuse sur dossier Parcoursup (Spécialités scientifiques).", "deadline": "Début Mars"},
            {"nom": "King's College London (UK)", "filiere": "Medicine MBBS", "req": "IELTS ≥ 7.0, réussite à l'examen clinique britannique UCAT.", "deadline": "15 Octobre"}
        ],
        "bourses": [
            {"nom": "Bourse Eiffel d'Excellence (France)", "couverture": "Allocation mensuelle fixe et prise en charge des frais de transport.", "req": "Profil international d'élite présenté par une université française.", "deadline": "Janvier"},
            {"nom": "King's International Scholarship Awards", "couverture": "Réduction significative sur les frais de scolarité internationaux.", "req": "Dossier d'admission validé et rédaction d'un essai de recherche.", "deadline": "Fin Avril"}
        ]
    }
}

# --- NAVIGATION DE L'APPLICATION ---
if "step" not in st.session_state: st.session_state.step = 1

# Barre d'avancement
st.progress(st.session_state.step / 4)

# ÉTAPE 1 : PROFIL ACADÉMIQUE
if st.session_state.step == 1:
    st.markdown("### 📝 Étape 1 : Situation Académique globale")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.filiere_bac = st.selectbox("Série ou filière du diplôme préparé :", ["Sciences Mathématiques", "Sciences Physiques et Chimiques", "Sciences Économiques & Gestion", "Sciences de la Vie et de la Terre", "Lettres & Sciences Humaines"])
        st.session_state.note = st.slider("Note globale moyenne estimée (sur 20) :", 10.0, 20.0, 15.5, step=0.1)
    with col2:
        st.session_state.zone = st.selectbox("Objectif géographique prioritaire :", ["Monde Anglophone (USA, Canada, UK)", "Europe (France, Suisse, Belgique)", "Établissements Nationaux de Prestige"])
        st.session_state.etablissement = st.text_input("Ville ou région actuelle de scolarisation :", placeholder="Ex: Casablanca, Rabat, Tanger...")
        
    if st.button("Étape Suivante : Évaluation Linguistique ➡️"):
        st.session_state.step = 2
        st.rerun()

# ÉTAPE 2 : CERTIFICATIONS DE LANGUE
elif st.session_state.step == 2:
    st.markdown("### 🔤 Étape 2 : Niveau de Langue & Certifications")
    
    col1, col2 = st.columns(2)
    with col1:
        test_type = st.radio("Disposez-vous d'une certification de langue anglaise ?", ["Aucun test pour le moment", "IELTS Academic", "TOEFL iBT", "Duolingo English Test"])
    with col2:
        if test_type != "Aucun test pour le moment":
            score_lang = st.text_input("Indiquez le score obtenu ou visé :", placeholder="Ex: IELTS 7.0, TOEFL 95...")
            st.session_state.score_lang = score_lang
        else:
            st.session_state.score_lang = "Aucun test disponible"
            
    st.session_state.niveau_fr = st.select_slider("Niveau de maîtrise de la langue française :", options=["Intermédiaire (B1)", "Avancé (B2)", "Excellent / Autonome (C1)", "Bilingue / Maternelle (C2)"])

    c_b1, c_b2 = st.columns([1, 5])
    with c_b1:
        if st.button("⬅️ Étape Précédente"): st.session_state.step = 1; st.rerun()
    with c_b2:
        if st.button("Étape Suivante : Profil Extracourriculaire ➡️"): st.session_state.step = 3; st.rerun()

# ÉTAPE 3 : EXTRACURRICULAIRE NEUTRE & SANS EXEMPLES PERSONNELS
elif st.session_state.step == 3:
    st.markdown("### 🏆 Étape 3 : Distinctions, Projets & Compétitions")
    st.write("Les critères de bourses internationales reposent sur les activités en dehors des cours. Indiquez vos éléments de manière générale.")
    
    st.session_state.distinctions = st.text_area(
        "Distinctions ou prix (Exemples généraux : Concours régionaux, Olympiades de mathématiques, compétitions scolaires...) :",
        placeholder="Décrivez vos prix de façon factuelle si vous en possédez..."
    )
    
    st.session_state.engagement = st.text_area(
        "Engagements ou projets (Exemples généraux : Clubs de lycée, actions d'aide sociale, projets technologiques, activités de création numérique...) :",
        placeholder="Décrivez vos projets et implications en dehors des salles de classe..."
    )

    st.markdown("#### 🎙️ Module d'Expression Libre")
    st.write("Présentez votre projet à l'oral pour l'analyse textuelle de l'application :")
    
    st.components.v1.html("""
        <div style="background-color: #1e293b; border-radius: 12px; padding: 15px; text-align: center; border: 1px dashed #475569;">
            <button id="start-record" style="background: linear-gradient(90deg, #ef4444, #f43f5e); color: white; font-weight: bold; padding: 10px 22px; border: none; border-radius: 20px; cursor: pointer;">🎙️ ACTIVER LE MICROPHONE</button>
        </div>
        <script>
            const btn = document.getElementById('start-record');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if(SpeechRecognition){
                const rec = new SpeechRecognition(); rec.lang = 'fr-FR';
                btn.onclick = () => { rec.start(); btn.innerText = "⏳ Analyse vocale active..."; };
                rec.onresult = (e) => { window.parent.postMessage({type: 'streamlit:set_input', value: e.results[0][0].transcript}, '*'); btn.innerText = "🎙️ Relancer le micro"; };
            }
        </script>
    """, height=85)
    
    st.session_state.vocal_text = st.text_input("Transcription automatique de la voix :", placeholder="Votre projet de vive voix s'affichera ici...")

    c_b1, c_b2 = st.columns([1, 5])
    with c_b1:
        if st.button("⬅️ Étape Précédente"): st.session_state.step = 2; st.rerun()
    with c_b2:
        if st.button("Générer l'Analyse d'Orientation Globale 🧭"): st.session_state.step = 4; st.rerun()

# ÉTAPE 4 : DIAGNOSTIC APPLICATION COMPLET
elif st.session_state.step == 4:
    st.markdown("### 🧭 Rapport Applicatif de Synthèse")
    
    # Analyse brute par l'algorithme
    glob_text = (st.session_state.distinctions + " " + st.session_state.engagement + " " + st.session_state.vocal_text).lower()
    
    detected_sector = "business_finance" # Valeur par défaut logique
    if any(k in glob_text for k in ["code", "tech", "informatique", "ia", "cyber", "ingenieur", "robot"]):
        detected_sector = "sciences_tech"
    elif any(k in glob_text for k in ["medecine", "sante", "pharma", "dentaire", "biologie"]):
        detected_sector = "medical_sante"
        
    data_res = APP_DATABASE[detected_sector]
    
    # 1. VISUALISATION DU PROFIL DU CANDIDAT
    st.markdown("#### 📊 Fiche Récapitulative de l'Étudiant")
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    col_f1.metric("Diplôme Visé", st.session_state.filiere_bac)
    col_f2.metric("Note Estimée", f"{st.session_state.note}/20")
    col_f3.metric("Niveau Anglais", st.session_state.score_lang)
    col_f4.metric("Niveau Français", st.session_state.niveau_fr)
    
    st.markdown(f"**Filière Majeure Détectée par l'IA :** {data_res['label']}")
    st.write("---")
    
    # 2. AFFICHAGE DES UNIVERSITES CIBLES
    st.markdown("### 🏛️ 1. Établissements & Universités Recommandés")
    cols_u = st.columns(3)
    for index, uni in enumerate(data_res["unis"]):
        with cols_u[index % 3]:
            st.markdown(f"""
                <div class="card-uni">
                    <div class="title-item">{uni['nom']}</div>
                    <p class="text-item"><b>📚 Cursus conseillé :</b> {uni['filiere']}</p>
                    <p class="text-item"><b>📋 Conditions / Requirements :</b> {uni['req']}</p>
                    <p class="text-item" style="color: #f87171 !important;"><b>📅 Date Limite / Deadline :</b> {uni['deadline']}</p>
                    <div class="badge-tag">Université Cible</div>
                </div>
            """, unsafe_allow_html=True)
            
    # 3. AFFICHAGE DES BOURSES DISPONIBLES
    st.markdown("### 💎 2. Programmes de Bourses d'Études Associés")
    cols_b = st.columns(2)
    for index, bourse in enumerate(data_res["bourses"]):
        with cols_b[index % 2]:
            st.markdown(f"""
                <div class="card-bourse">
                    <div class="title-item">{bourse['nom']}</div>
                    <p class="text-item"><b>💰 Volume de couverture :</b> {bourse['couverture']}</p>
                    <p class="text-item"><b>🛠️ Éléments à joindre au dossier :</b> {bourse['req']}</p>
                    <p class="text-item" style="color: #34d399 !important;"><b>📅 Date Clôture :</b> {bourse['deadline']}</p>
                    <div class="badge-tag">Financement Disponible</div>
                </div>
            """, unsafe_allow_html=True)
            
    # 4. FEUILLE DE ROUTE STRATÉGIQUE (LISIBLE ET CLAIRE)
    st.markdown("### 📈 3. Directives Stratégiques du Moteur d'Orientation")
    st.markdown("""
        <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #475569;">
            <p style="color: #ffffff !important; margin-bottom: 10px;">• <b>Optimisation de la Moyenne :</b> Votre objectif de note doit rester stable pour franchir les seuils automatiques de présélection des dossiers internationaux.</p>
            <p style="color: #ffffff !important; margin-bottom: 10px;">• <b>Planification des Certifications :</b> Si vous visez des destinations anglophones ou d'excellence, prévoyez de passer vos examens officiels (IELTS, TOEFL, Duolingo) au moins 3 mois avant les deadlines indiquées.</p>
            <p style="color: #ffffff !important;">• <b>Valorisation du Dossier :</b> Veillez à documenter correctement chaque projet et chaque engagement afin de pouvoir rédiger des lettres de motivation percutantes pour les jurys de bourses.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("")

    if st.button("🔄 Relancer un Diagnostic Applicatif"):
        st.session_state.step = 1
        st.rerun()
