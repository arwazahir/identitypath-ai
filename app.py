import streamlit as st
import time

st.set_page_config(page_title="IdentityPath AI App", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN PREMIUM REVISITÉ ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
    .main { background-color: #0f172a; color: #f8fafc; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    h1, h2, h3, h4 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; }
    .brand-header { text-align: center; padding: 30px 20px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 20px; border: 1px solid #334155; margin-bottom: 25px; }
    .brand-logo { font-size: 42px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .card-dashboard { background: #1e293b; padding: 25px; border-radius: 16px; border: 1px solid #334155; margin-bottom: 20px; }
    .uni-card { background: #111827; padding: 20px; border-radius: 12px; border-left: 5px solid #3b82f6; margin-bottom: 15px; border-top: 1px solid #1f2937; border-right: 1px solid #1f2937; border-bottom: 1px solid #1f2937; }
    .bourse-card { background: #111827; padding: 20px; border-radius: 12px; border-left: 5px solid #10b981; margin-bottom: 15px; border-top: 1px solid #1f2937; border-right: 1px solid #1f2937; border-bottom: 1px solid #1f2937; }
    .badge-blue { background: #1e3a8a; color: #93c5fd; padding: 4px 10px; border-radius: 8px; font-size: 12px; font-weight: 600; display: inline-block; }
    .badge-green { background: #064e3b; color: #a7f3d0; padding: 4px 10px; border-radius: 8px; font-size: 12px; font-weight: 600; display: inline-block; }
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: white !important; font-weight: bold !important; border-radius: 12px !important; padding: 10px 25px !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-header"><div class="brand-logo">🧭 IDENTITYPATH APP</div><div style="color: #94a3b8; font-size: 16px;">Moteur d\'Analyse Globale & Cartographie des Bourses Internationales</div></div>', unsafe_allow_html=True)

# --- ACCÈS SÉCURISÉ ---
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Activation de l'Application</h3>", unsafe_allow_html=True)
        code = st.text_input("Entrez votre code d'accès IdentityPath :", type="password")
        if code == "Arwagiftorient":
            if st.button("Ouvrir la Console d'Orientation 🚀"):
                st.session_state.auth = True
                st.rerun()
    st.stop()

# --- BASE DE DONNÉES EXPERTE (UNIVERSITÉS + BOURSES + DETAILS) ---
DATA_ENGINE = {
    "tech": {
        "unis": [
            {"nom": "UM6P - Benguerir (Maroc)", "filiere": "School of Computer Science / 1337", "req": "Moyenne > 16/20, Bac SM ou PC, tests de logique internes.", "deadline": "Fin Mai / Début Juin"},
            {"nom": "EPFL (Suisse)", "filiere": "Bachelor in Computer Science", "req": "Moyenne générale au Bac ≥ 16/20 (Mention TB) en filière scientifique.", "deadline": "30 Avril"},
            {"nom": "University of Toronto (Canada)", "filiere": "Faculty of Applied Science & Engineering", "req": "IELTS ≥ 6.5 ou TOEFL ≥ 100, Moyenne forte en Maths/Physique.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence UM6P", "couverture": "Exonération 100% des frais de scolarité + logement", "req": "Critères sociaux + Mention Très Bien au Bac.", "deadline": "Juillet"},
            {"nom": "Lester B. Pearson International Scholarship (Canada)", "couverture": "Frais de scolarité complets, livres, résidence pendant 4 ans", "req": "IELTS/TOEFL excellent, Profil de leader exceptionnel, nomination par le lycée, Awards extra-scolaires.", "deadline": "15 Janvier"}
        ]
    },
    "business": {
        "unis": [
            {"nom": "ISCAE Casablanca (Maroc)", "filiere": "Grande École de Commerce", "req": "Concours écrit + oral après Classes Préparatoires ou Licence.", "deadline": "Avril (Prépa)"},
            {"nom": "HEC Paris (France)", "filiere": "BSc in Data, Society and Organisations / Cursus Grande École", "req": "Dossier académique d'élite, Score SAT/ACT recommandé, Entretien de motivation.", "deadline": "Plusieurs sessions (Octobre à Mars)"},
            {"nom": "Wharton School - University of Pennsylvania (USA)", "filiere": "Bachelor of Science in Economics", "req": "SAT (1500+ conseillé), TOEFL/IELTS, 2 à 3 lettres de recommandation, Essais.", "deadline": "1 Novembre (Early) / 5 Janvier (Regular)"}
        ],
        "bourses": [
            {"nom": "Bourses de la Fondation HEC Paris", "couverture": "Réduction importante ou totale des frais de scolarité", "req": "Admis au programme + critères d'excellence et de diversité internationale.", "deadline": "Lors de l'admission"},
            {"nom": "Penn World Scholars (USA)", "couverture": "Aide financière sur mesure pouvant couvrir la totalité du cursus", "req": "Potentiel de leadership mondial, profil académique d'exception, engagements associatifs.", "deadline": "Automne lors du dépôt du dossier"}
        ]
    },
    "sante": {
        "unis": [
            {"nom": "Facultés de Médecine et de Pharmacie (FMP Maroc)", "filiere": "Médecine Générale / Dentaire", "req": "Seuil de présélection (Note Bac) + Concours national écrit.", "deadline": "Juillet"},
            {"nom": "Université Paris Cité (France)", "filiere": "Parcours Accès Santé (PASS)", "req": "Excellent dossier sur Parcoursup, fortes notes en SVT/Physique.", "deadline": "Début Mars"},
            {"nom": "King's College London (UK)", "filiere": "Medicine MBBS", "req": "IELTS ≥ 7.0, examen UCAT obligatoire, 3 matières scientifiques fortes au Bac.", "deadline": "15 Octobre"}
        ],
        "bourses": [
            {"nom": "Bourse du Gouvernement Français (Eiffel / Universités)", "couverture": "Allocation mensuelle + prise en charge des frais de couverture médicale", "req": "Dossier académique d'élite, réservé aux étudiants internationaux brillants.", "deadline": "Janvier"},
            {"nom": "King's International Scholarships", "couverture": "Réduction de £10,000 par an sur les frais de scolarité", "req": "Avoir une offre d'admission, essais spécifiques sur le projet professionnel.", "deadline": "Fin Avril"}
        ]
    },
    "art": {
        "unis": [
            {"nom": "ENA (École Nationale d'Architecture Maroc)", "filiere": "Architecture et Urbanisme", "req": "Sélection stricte sur moyenne nationale du Bac + Concours écrit d'art/géométrie.", "deadline": "Fin Juin"},
            {"nom": "Parsons School of Design (New York, USA)", "filiere": "BFA in Communication Design / Architecture", "req": "Portfolio artistique complet (15-20 images), TOEFL ≥ 92 / Duolingo ≥ 115, Essais.", "deadline": "15 Janvier"},
            {"nom": "Central Saint Martins (Londres, UK)", "filiere": "BA Graphic Communication Design", "req": "Portfolio innovant, IELTS ≥ 6.0, entretien vidéo.", "deadline": "25 Janvier"}
        ],
        "bourses": [
            {"nom": "Parsons Merit-Based Scholarship", "couverture": "Couverture partielle à totale des frais de scolarité complexes", "req": "Attribuée automatiquement aux meilleurs portfolios et dossiers académiques.", "deadline": "Lors de l'application"},
            {"nom": "Bourses du British Council (Great Scholarships)", "couverture": "Financement d'une année d'études d'un montant de £10,000", "req": "Étudiant marocain accepté dans une université britannique partenaire.", "deadline": "Mai"}
        ]
    }
}

# --- SYSTÈME D'APPLICATION EN ÉTAPES ---
if "app_step" not in st.session_state: st.session_state.app_step = 1

# Barre de progression
st.progress(st.session_state.app_step / 4)

# ÉTAPE 1 : PROFIL ACADÉMIQUE STANDARD
if st.session_state.app_step == 1:
    st.markdown("### 📊 Étape 1 : Identité Académique & Géographique")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.f_bac = st.selectbox("Filière de votre Baccalauréat :", ["Sciences Mathématiques (SM)", "Sciences Physiques (PC)", "Sciences Économiques", "SVT", "Lettres"])
        st.session_state.moyenne = st.slider("Moyenne générale estimée ou obtenue :", 10.0, 20.0, 16.0, step=0.1)
    with col2:
        st.session_state.destination = st.selectbox("Où souhaitez-vous étudier ?", ["International Anglophone (USA, Canada, UK)", "Europe Francophone (France, Suisse, Belgique)", "Maroc (Grandes Écoles de prestige)", "Partout où il y a des bourses intégrales"])
        st.session_state.lycee = st.text_input("Nom de votre lycée et ville :", placeholder="Ex: Lycée Lyautey, Casablanca")
    
    if st.button("Continuer vers l'analyse des langues ➡️"):
        st.session_state.app_step = 2
        st.rerun()

# ÉTAPE 2 : TESTS DE LANGUES ET COMPÉTENCES
elif st.session_state.app_step == 2:
    st.markdown("### 🔤 Étape 2 : Certifications de Langue & Tests")
    st.write("Les universités internationales exigent des preuves de niveau. Indiquez vos tests passés ou prévus.")
    
    col1, col2 = st.columns(2)
    with col1:
        has_test = st.radio("Avez-vous déjà passé ou planifié un test d'anglais ?", ["Non, aucun pour l'instant", "Oui, l'IELTS", "Oui, le TOEFL", "Oui, le Duolingo English Test"])
    with col2:
        if has_test != "Non, aucun pour l'instant":
            score = st.text_input("Quel est votre score (ou score visé) ?", placeholder="Ex: IELTS 7.5, Duolingo 125...")
            st.session_state.lang_score = score
        else:
            st.session_state.lang_score = "Aucun test planifié"
            
    st.session_state.french_level = st.select_slider("Quel est votre niveau en Français ?", options=["Intermédiaire (B1)", "Avancé (B2)", "Autonome / Excellent (C1)", "Bilingue / Langue Maternelle (C2)"])

    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        if st.button("⬅️ Retour"): st.session_state.app_step = 1; st.rerun()
    with col_btn2:
        if st.button("Continuer vers le Dossier d'Excellence ➡️"): st.session_state.app_step = 3; st.rerun()

# ÉTAPE 3 : AWARDS & EXTRA-SCOLAIRE (LA DIFFÉRENCE IDENTITYPATH)
elif st.session_state.app_step == 3:
    st.markdown("### 🏆 Étape 3 : Awards, Compétitions & Engagement Extra-Scolaire")
    st.write("C'est ici que se gagnent les bourses internationales. Racontez vos accomplissements (Prix, concours, bénévolat, projets).")
    
    has_awards = st.checkbox("J'ai déjà remporté un prix, une compétition nationale/internationale ou un projet d'innovation.")
    if has_awards:
        awards_details = st.text_area("Détaillez vos Awards et Distinctions :", placeholder="Ex: 1er place compétition nationale d'innovation environnementale, projet de filtration écologique...")
        st.session_state.awards = awards_details
    else:
        st.session_state.awards = "Aucun award mentionné"
        
    volunteer = st.text_area("Projets personnels ou bénévolat (Cooperatives, Design, Entrepreneuriat) :", placeholder="Ex: Création de contenu graphique bénévole pour des coopératives de femmes, gestion de projet digital...")
    st.session_state.volunteer = volunteer

    st.markdown("#### 🎙️ Expression Libre (Optionnel)")
    st.write("Utilisez le micro si vous préférez exprimer votre projet d'avenir à l'oral :")
    st.components.v1.html("""
        <div style="background-color: #1e293b; border-radius: 12px; padding: 15px; text-align: center;">
            <button id="mic" style="background: #ef4444; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer;">🎙️ Démarrer l'Écoute Vocale</button>
        </div>
        <script>
            const btn = document.getElementById('mic');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if(SpeechRecognition){
                const r = new SpeechRecognition(); r.lang = 'fr-FR';
                btn.onclick = () => { r.start(); btn.innerText = "⚡ Analyse en cours..."; };
                r.onresult = (e) => { window.parent.postMessage({type: 'streamlit:set_input', value: e.results[0][0].transcript}, '*'); btn.innerText = "🎙️ Recommencer"; };
            }
        </script>
    """, height=90)
    
    captured_speech = st.text_input("Texte extrait de la voix (ou à taper) :", placeholder="Complétez votre profil de vive voix...")

    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        if st.button("⬅️ Retour"): st.session_state.app_step = 2; st.rerun()
    with col_btn2:
        if st.button("Générer mon Itinéraire d'Excellence 🧭"):
            st.session_state.speech = captured_speech
            st.session_state.app_step = 4
            st.rerun()

# ÉTAPE 4 : CARTOGRAPHIE RAPPORT GLOBAL (UNIVERSITÉS + BOURSES + CRITÈRES)
elif st.session_state.app_step == 4:
    st.markdown("### 🧭 Rapport d'Analyse Identitaire Global")
    st.write("Voici le diagnostic complet formulé par l'algorithme IdentityPath APP.")
    
    # Analyse croisée des mots-clés du profil
    profil_text = (st.session_state.awards + " " + st.session_state.volunteer + " " + st.session_state.speech).lower()
    
    detected_key = "business" # Par défaut
    if any(w in profil_text for w in ["code", "tech", "informatique", "ia", "cyber", "ordinateur", "software"]):
        detected_key = "tech"
    elif any(w in profil_text for w in ["medecine", "sante", "docteur", "biologie", "soin", "clinique"]):
        detected_key = "sante"
    elif any(w in profil_text for w in ["art", "design", "architecture", "dessin", "graphisme", "creatif"]):
        detected_key = "art"
        
    engine_data = DATA_ENGINE[detected_key]
    
    # 1. TABLEAU DE BORD DE L'ÉLÈVE
    st.markdown("<div class='card-dashboard'>", unsafe_allow_html=True)
    st.write("#### 👤 Profil de l'Étudiant Analysé :")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bac visé", st.session_state.f_bac)
    c2.metric("Moyenne estimée", f"{st.session_state.moyenne}/20")
    c3.metric("Test Anglais", st.session_state.lang_score)
    c4.metric("Niveau Français", st.session_state.french_level)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 2. SECTEUR D'ORIENTATION RECOMMANDÉ
    st.success(f"💡 Secteur Majeur Détecté : {detected_key.upper()}")
    
    # 3. AFFICHAGE DES UNIVERSITÉS PRÉCISES
    st.write("### 🏛️ 1. Universités cibles & Requirements")
    cols_u = st.columns(3)
    for i, uni in enumerate(engine_data["unis"]):
        with cols_u[i % 3]:
            st.markdown(f"""
                <div class="uni-card">
                    <div class="badge-blue">Filière : {uni['filiere']}</div>
                    <div class="uni-title" style="margin-top:10px;">{uni['nom']}</div>
                    <p style="font-size:14px; color:#cbd5e1;"><b>📋 Requirements :</b> {uni['req']}</p>
                    <p style="font-size:14px; color:#f87171;"><b>⏰ Deadline :</b> {uni['deadline']}</p>
                </div>
            """, unsafe_allow_html=True)
            
    # 4. AFFICHAGE DES BOURSES PRÉCISES
    st.write("### 💎 2. Bourses d'Excellence Disponibles")
    cols_b = st.columns(2)
    for i, bourse in enumerate(engine_data["bourses"]):
        with cols_b[i % 2]:
            st.markdown(f"""
                <div class="bourse-card">
                    <div class="badge-green">Type : {bourse['couverture']}</div>
                    <div class="uni-title" style="margin-top:10px;">{bourse['nom']}</div>
                    <p style="font-size:14px; color:#cbd5e1;"><b>🛠️ Qu'ajouter au dossier ?</b> {bourse['req']}</p>
                    <p style="font-size:14px; color:#10b981;"><b>📅 Fin des candidatures :</b> {bourse['deadline']}</p>
                </div>
            """, unsafe_allow_html=True)
            
    # 5. RECOMMANDATION STRATÉGIQUE ADAPTEE AU JURY
    st.write("### 📈 3. Conseils de notre Expert pour ton Dossier")
    if st.session_state.awards != "Aucun award mentionné":
        st.info("💡 **Stratégie d'Excellence Gagnante :** Votre profil contient déjà un Award ou un projet d'innovation. C'est votre plus grande force pour l'international (bourses Pearson ou USA). Vous devez rédiger vos essais de motivation en centrant toute votre histoire sur cet accomplissement et le lier à votre future filière.")
    else:
        st.warning("💡 **Conseil Dossier :** Pour maximiser vos chances d'obtenir les bourses internationales présentées ci-dessus, vous devez impérativement ajouter une activité extra-scolaire forte ou un projet d'innovation personnel avant la date limite d'inscription.")

    if st.button("🔄 Lancer une nouvelle simulation d'application"):
        st.session_state.app_step = 1
        st.rerun()
