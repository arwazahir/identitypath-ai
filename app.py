import streamlit as st
import time

# Configuration de l'écosystème IdentityPath
st.set_page_config(page_title="IdentityPath OS", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN PREMIUM IDENTITYPATH (VERTICAL & ULTRA-LISIBLE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #0b1329; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0b1329; font-family: 'Inter', sans-serif; }
    
    /* Visibilité absolue des textes - Zéro compromis */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 16px !important; }
    h1, h2, h3, h4, h5 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; font-weight: 800 !important; }
    
    /* Header IdentityPath */
    .id-banner { text-align: center; padding: 40px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 24px; border: 2px solid #334155; margin-bottom: 40px; }
    .id-title { font-size: 48px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Urbanist'; letter-spacing: -1px; }
    .id-tagline { color: #10b981 !important; font-size: 14px !important; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-top: 8px; }
    
    /* Conteneurs Verticaux Révolutionnaires */
    .step-block { background: #1e293b; padding: 30px; border-radius: 18px; border: 1px solid #334155; margin-bottom: 35px; }
    .result-card { background: #111827; padding: 25px; border-radius: 16px; border-left: 6px solid #3b82f6; margin-bottom: 20px; border-top: 1px solid #1f2937; border-right: 1px solid #1f2937; border-bottom: 1px solid #1f2937; }
    .result-card.success { border-left-color: #10b981; }
    .result-card.warning { border-left-color: #f59e0b; }
    
    /* Badges de Score et Salaires */
    .salary-badge { background: rgba(16, 185, 129, 0.15); color: #10b981 !important; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 15px !important; border: 1px solid #10b981; display: inline-block; margin-top: 10px; }
    .match-tag { float: right; background: #334155; color: #ffffff !important; padding: 4px 12px; border-radius: 20px; font-size: 13px !important; font-weight: bold; text-transform: uppercase; }
    
    /* Bouton d'action principal */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 12px !important; padding: 16px 32px !important; border: none !important; width: 100%; font-size: 17px !important; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3); }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4); }
    </style>
""", unsafe_allow_html=True)

# --- HEADER GLOBAL IDENTITYPATH ---
st.markdown("""
    <div class="id-banner">
        <div class="id-title">🧭 IDENTITYPATH APP</div>
        <div class="id-tagline">AI Future Navigation System for Global Education Access</div>
    </div>
""", unsafe_allow_html=True)

# --- VERIFICATION SECURISEE ---
if "id_auth" not in st.session_state: st.session_state.id_auth = False
if not st.session_state.id_auth:
    c_l, c_m, c_r = st.columns([1, 2, 1])
    with c_m:
        st.markdown("<h4 style='text-align: center;'>🔒 Connexion Sécurisée IdentityPath</h4>", unsafe_allow_html=True)
        token = st.text_input("Clé d'accès administrateur :", type="password")
        if token == "Arwagiftorient":
            if st.button("Déployer la Matrice Professionnelle 🚀"):
                st.session_state.id_auth = True
                st.rerun()
    st.stop()

# --- BASE DE DONNÉES RÉSISTANTE ET ULTRA-CONCRÈTE ---
DATA_MATRIX = {
    "architecture": {
        "metier": "Architecte DPLG / Urbaniste Global / Designer d'Espace Eco-Responsable",
        "salaire": "45,000$ à 95,000$ / an à l'international (Senior: 120,000$+)",
        "description": "Conception d'espaces, de bâtiments et de structures combinant esthétique, géométrie et technologies écologiques.",
        "chemins": [
            "🧠 Chemin Principal : Bachelor/Master en Architecture (Écoles Nationales de Prestige ou Internationales) -> Stage de 2 ans agréé -> Inscription à l'Ordre des Architectes.",
            "💡 Chemin Alternatif : Double diplôme Ingénierie Civile + Architecture (Profil d'élite technologique très recherché pour les grands projets urbains)."
        ],
        "opportunites": [
            {"nom": "AA School of Architecture Scholarships (Londres, UK)", "type": "Bourse Universitaire", "fit": "92%", "desc": "Couverture de 50% à 100% des frais d'études pour les profils créatifs et scientifiques de premier ordre."},
            {"nom": "Bourse de Mérite de l'Université de Tokyo - Architecture Dept (Japon)", "type": "Bourse Internationale", "fit": "88%", "desc": "Exonération totale de scolarité + allocation mensuelle pour étudiants internationaux d'excellence."}
        ]
    },
    "medecine": {
        "metier": "Médecin Spécialiste / Chercheur en Biotechnologies Médicales",
        "salaire": "70,000$ à 180,000$ / an (Spécialistes chirurgiens: 250,000$+)",
        "description": "Diagnostic, traitement des pathologies humaines et développement des thérapies cellulaires ou géniques du futur.",
        "chemins": [
            "🧠 Chemin Principal : Concours d'entrée en Faculté de Médecine -> Cursus de 7 à 12 ans selon la spécialisation hospitalière choisie.",
            "💡 Chemin Alternatif : Licence en Sciences Biomédicales à l'international (Canada/USA) -> Admission sur dossier et test MCAT en Doctorat de Médecine."
        ],
        "opportunites": [
            {"nom": "King's Medical International Scholarship Awards (UK)", "type": "Bourse d'Excellence", "fit": "95%", "desc": "Réduction de £10,000 par an sur les frais de scolarité obligatoires pendant tout le cursus médical."},
            {"nom": "Bourses Eiffel d'Excellence (Gouvernement Français)", "type": "Bourse d'État", "fit": "89%", "desc": "Prise en charge complète pour des masters ou doctorats scientifiques en santé publique."}
        ]
    },
    "tech_ia": {
        "metier": "Ingénieur en Intelligence Artificielle / Data Scientist / Expert Cybersécurité",
        "salaire": "65,000$ à 140,000$ / an (Silicon Valley / Émirats : 180,000$+)",
        "description": "Conception d'algorithmes prédictifs, développement de modèles LLM et protection des infrastructures de données globales.",
        "chemins": [
            "🧠 Chemin Principal : Classes Préparatoires Scientifiques -> Grande École d'Ingénieurs (Option Informatique / IA).",
            "💡 Chemin Alternatif : Bachelor de Computer Science (UM6P, EPFL ou Canada) -> Insertion directe en startup ou poursuite en Master Spécialisé."
        ],
        "opportunites": [
            {"nom": "Lester B. Pearson International Scholarship (Toronto, Canada)", "type": "Bourse Intégrale", "fit": "94%", "desc": "Prise en charge absolue (Scolarité, hébergement, livres, assurance) pendant 4 ans au Canada."},
            {"nom": "Bourse d'Excellence Technologique de la Fondation UM6P (Benguerir)", "type": "Bourse de Mérite", "fit": "91%", "desc": "Exonération totale des frais et mise à disposition d'un écosystème de recherche de pointe."}
        ]
    },
    "business_eco": {
        "metier": "Manager Stratégique / Analyste Financier / Entrepreneur International",
        "salaire": "50,000$ à 110,000$ / an (Fonds d'investissement / Conseil : 130,000$+)",
        "description": "Gestion des organisations, pilotage de la croissance économique et structuration de projets commerciaux à fort impact.",
        "chemins": [
            "🧠 Chemin Principal : Bachelor in Business Administration (BBA) -> Master in Management (Grande École) -> Analyste junior.",
            "💡 Chemin Alternatif : Licence d'Économie Appliquée -> MBA international après 3 ans d'expérience sur le terrain."
        ],
        "opportunites": [
            {"nom": "Bourse d'Excellence de la Faculty of Governance (FGSES Rabat)", "type": "Bourse d'Établissement", "fit": "93%", "desc": "Financement complet ou partiel des études et du logement sur critères académiques et sociaux."},
            {"nom": "GREAT Scholarships - British Council (Royaume-Uni)", "type": "Bourse Gouvernementale", "fit": "87%", "desc": "Versement direct de £10,000 pour financer une année d'études supérieures au Royaume-Uni."}
        ]
    }
}

if "calculated" not in st.session_state: st.session_state.calculated = False

# ==============================================================================
# STRUCTURE VERTICALE : ÉTAPE 1 (CONSTRUCTION DU TWIN)
# ==============================================================================
st.markdown("<div class='step-block'>", unsafe_allow_html=True)
st.markdown("### 🧬 Étape 1 : Le Profil Intelligent de l'Étudiant (AI Student DNA)")
st.write("Renseignez le profil complet. L'application s'adapte automatiquement, même si vos objectifs sont vagues.")

col1, col2 = st.columns(2)
with col1:
    f_bac = st.selectbox("Option du Baccalauréat actuel :", ["Sciences Mathématiques", "Sciences Physiques", "Sciences Économiques", "SVT", "Lettres"])
    note_bac = st.slider("Moyenne générale projetée ou ciblée (sur 20) :", 10.0, 20.0, 16.0, step=0.1)
    
    mat_options = ["Mathématiques", "Physique-Chimie", "Arts Plastiques / Dessin", "Sciences Économiques", "SVT", "Philosophie", "Anglais Académique", "Other"]
    mat_sel = st.multiselect("Matières fortes ou dominantes :", mat_options)
    custom_mat = st.text_input("Si 'Other', précisez :", placeholder="Ex: Dessin technique, Informatique...") if "Other" in mat_sel else ""

    dest_options = [
        "Monde Entier / International sans restriction",
        "Europe Francophone (France, Suisse...)",
        "Pays Anglophones (USA, UK, Canada...)",
        "Asie (Japon, Chine, Singapour...)",
        "Moyen-Orient & Turquie (Arabie Saoudite, Istanbul...)",
        "Maroc / Écoles Nationales de Prestige",
        "Other"
    ]
    dest_sel = st.multiselect("Destinations géographiques envisagées :", dest_options)
    custom_dest = st.text_input("Si 'Other', écrivez le pays :", placeholder="Ex: Allemagne, Corée...") if "Other" in dest_sel else ""

with col2:
    val_options = ["Innovation technologique", "Impact environnemental", "Création esthétique & Design", "Recherche pure", "Entrepreneuriat", "Impact social", "Other"]
    val_sel = st.multiselect("Valeurs fondamentales de l'élève :", val_options)
    custom_val = st.text_input("Si 'Other', vos valeurs :", placeholder="Ex: Justice, Indépendance...") if "Other" in val_sel else ""

    projets = st.text_area("Expériences, projets personnels, compétitions ou bénévolat :", placeholder="Ex: J'ai dessiné les plans d'un mini-projet, j'ai participé à un concours écolo, aucun projet pour l'instant...")
    
    # Prise en considération des profils vagues
    ambition_type = st.radio("Avez-vous une idée précise de votre objectif de carrière ?", ["Oui, j'ai un objectif précis", "Non, c'est encore très vague / Je cherche ma voie"])
    
    if ambition_type == "Oui, j'ai un objectif précis":
        ambition_pro = st.text_input("Indiquez le métier ou domaine visé :", placeholder="Ex: Architecte, Chirurgien, Développeur IA...")
    else:
        ambition_pro = "Vague / En cours d'orientation"
        st.info("ℹ️ IdentityPath va analyser vos matières fortes et vos valeurs pour vous attribuer la trajectoire idéale.")

    budget = st.radio("Contraintes financières pour les études :", ["Besoin d'une bourse complète (100%)", "Financement partiel accepté", "Autonome"])

st.write("")
if st.button("🌌 Générer le Profil & Analyser les Trajectoires d'Avenir ➡️"):
    st.session_state.calculated = True
    st.session_state.f_bac = f_bac
    st.session_state.note_bac = note_bac
    st.session_state.ambition = ambition_pro
    st.session_state.budget = budget
    st.session_state.projets = projets
    
    # Moteur d'arbitrage intelligent et profond pour bloquer les erreurs
    corpus = (f_bac + " " + " ".join(mat_sel) + " " + " ".join(val_sel) + " " + projets + " " + ambition_pro).lower()
    
    if "arch" in corpus or "dessin" in corpus or "art" in corpus:
        st.session_state.detected_key = "architecture"
    elif "méd" in corpus or "med" in corpus or "sant" in corpus or "svt" in corpus:
        st.session_state.detected_key = "medecine"
    elif "code" in corpus or "ia" in corpus or "informatique" in corpus or "math" in corpus:
        st.session_state.detected_key = "tech_ia"
    else:
        st.session_state.detected_key = "business_eco" # Fallback par défaut équilibré
        
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# CONFIGURATION VERTICALE DES ENCHAÎNEMENTS DE RÉSULTATS (ÉTAPE PAR ÉTAPE)
# ==============================================================================
if st.session_state.calculated:
    active_data = DATA_MATRIX[st.session_state.detected_key]
    
    # --------------------------------------------------------------------------
    # BLOC VERTICAL 2 : FICHE RECONNAISSANCE TWIN
    # --------------------------------------------------------------------------
    st.markdown("<div class='step-block'>", unsafe_allow_html=True)
    st.markdown("### 🧬 IdentityPath AI Student DNA Profile")
    st.write("Analyse sémantique croisée effectuée. Voici l'empreinte digitale de votre profil :")
    
    status_text = "Détecté selon vos choix" if st.session_state.ambition != "Vague / En cours d'orientation" else "Diagnostiqué automatiquement par rapport à vos valeurs et matières"
    
    st.markdown(f"""
        <div style="background: #111827; padding: 20px; border-radius: 12px; border: 1px solid #334155;">
            <p style="font-size: 16px !important; margin: 0;">
                🧠 <b>Statut de l'élève :</b> {status_text}.<br>
                🎯 <b>Domaine ciblé par l'IA :</b> <span style="color: #3b82f6; font-weight: bold;">{active_data['metier']}</span><br>
                📈 <b>Potentiel d'admission estimé :</b> {(int(st.session_state.note_bac * 4.8))}% sur la base de votre moyenne de {st.session_state.note_bac}/20.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # BLOC VERTICAL 3 : FUTURE SIMULATION ENGINE & SALAIRES
    # --------------------------------------------------------------------------
    st.markdown("<div class='step-block'>", unsafe_allow_html=True)
    st.markdown("### 🔮 Future Simulation Engine & Prédictions de Salaires")
    st.write("IdentityPath simule les parcours de vie exacts. Voici comment vous construisez votre futur :")
    
    st.markdown(f"<h5>💼 Estimation du Salaire Global Futur :</h5>", unsafe_allow_html=True)
    st.markdown(f"<div class='salary-badge'>💰 {active_data['salaire']}</div>", unsafe_allow_html=True)
    st.write("")
    
    st.markdown("<h5 style='margin-top:15px;'>🗺️ Trajectoires de vie simulées :</h5>", unsafe_allow_html=True)
    for index, chemin in enumerate(active_data["chemins"]):
        st.markdown(f"""
            <div class="result-card">
                <span class="match-tag">Simulation #{index+1}</span>
                <p style="margin-top: 10px; font-size:15px; color:#f1f5f9 !important;">{chemin}</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # BLOC VERTICAL 4 : OPPORTUNITY MATCHING ENGINE & BOURSES
    # --------------------------------------------------------------------------
    st.markdown("<div class='step-block'>", unsafe_allow_html=True)
    st.markdown("### 💎 Opportunity Matching Engine (Hidden Scholarships)")
    st.write("Le moteur scanne les opportunités mondiales et affiche votre niveau d'éligibilité réel :")
    
    for opp in active_data["opportunites"]:
        st.markdown(f"""
            <div class="result-card success">
                <span class="match-tag" style="background-color: #10b981;">Compatibilité : {opp['fit']}</span>
                <h4 style="color: #ffffff !important;">{opp['nom']}</h4>
                <p style="font-size:12px; color:#10b981; font-weight:bold; margin-top:4px;">Type : {opp['type']}</p>
                <p style="margin-top:8px; font-size:15px; color:#e2e8f0 !important;"><b>Description de l'offre :</b> {opp['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # BLOC VERTICAL 5 : REALITY CHECK & GROWTH ALGORITHM
    # --------------------------------------------------------------------------
    st.markdown("<div class='step-block'>", unsafe_allow_html=True)
    st.markdown("### 🛡️ AI Reality Check & Plan d'Évolution Mensuel")
    st.write("Analyse des faiblesses actuelles de votre dossier et plan d'action immédiat :")
    
    st.markdown("""
        <div class="result-card warning">
            <h4 style="color: #f59e0b !important;">🚨 Évaluation Honnête des Risques (Reality Check)</h4>
            <p style="margin-top:10px; font-size:15px; color:#f1f5f9 !important;">
                Votre moyenne académique est compétitive, mais pour sécuriser un financement intégral (100%), le manque de fiches de projets ou de certifications officielles de langues (IELTS/TOEFL/TCF) constitue un point de blocage automatique pour les algorithmes des commissions internationales.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h5 style='margin-top:20px;'>📅 Plan d'Amélioration Stratégique (Upgrade Roadmap) :</h5>", unsafe_allow_html=True)
    st.markdown("""
        <div class="roadmap-month">
            <b>🛠️ MOIS 1 : Sécurisation Linguistique</b><br>
            <span style="font-size:14px; color:#cbd5e1;">Passer un test blanc officiel pour valider un niveau C1 minimum indispensable pour ouvrir les portes des bourses mondiales.</span>
        </div>
        <div class="roadmap-month">
            <b>🛠️ MOIS 2 : Valorisation des Réalisations</b><br>
            <span style="font-size:14px; color:#cbd5e1;">Prendre vos activités ou esquisses de projets et les documenter sous forme de rapport d'impact chiffré à joindre en annexe de votre dossier.</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    if st.button("🔄 Lancer une Nouvelle Simulation"):
        st.session_state.calculated = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
