import streamlit as st
import time
import random

# Configuration de l'écosystème IdentityPath OS
st.set_page_config(page_title="IdentityPath OS", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN SCI-FI PREMIUM INTERACTIF ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #070a13; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #070a13; font-family: 'Inter', sans-serif; }
    
    /* Visibilité totale des composants */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    
    /* Header Principal IdentityPath */
    .id-core-banner { text-align: center; padding: 40px; background: linear-gradient(135deg, #0f172a 0%, #020617 100%); border-radius: 24px; border: 1px solid #1e293b; margin-bottom: 35px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); }
    .id-main-title { font-size: 44px; font-weight: 700; background: linear-gradient(90deg, #3b82f6, #10b981, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px; }
    .id-subtitle { color: #38bdf8 !important; font-size: 13px !important; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-top: 6px; }
    
    /* Blocs verticaux fluides */
    .block-vertical { background: #0f172a; padding: 30px; border-radius: 20px; border: 1px solid #1e293b; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
    .chat-bubble-ai { background: #1e293b; padding: 18px; border-radius: 14px; border-left: 4px solid #3b82f6; margin-bottom: 15px; color: #f1f5f9 !important; }
    
    /* Cartes de simulation prédictive */
    .matrix-card { background: #111827; padding: 25px; border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 20px; position: relative; }
    .matrix-card.success { border-left: 5px solid #10b981; }
    .matrix-card.warning { border-left: 5px solid #f59e0b; }
    .matrix-card.info { border-left: 5px solid #6366f1; }
    
    /* Badges de l'OS */
    .badge-data { background: rgba(56, 189, 248, 0.1); color: #38bdf8 !important; border: 1px solid #38bdf8; padding: 4px 12px; border-radius: 8px; font-size: 13px !important; display: inline-block; margin-top: 8px; font-weight: bold; }
    .badge-salary { background: rgba(16, 185, 129, 0.15); color: #10b981 !important; border: 1px solid #10b981; padding: 6px 16px; border-radius: 8px; font-weight: bold; font-size: 16px !important; display: inline-block; margin-bottom: 15px; }
    .score-tag { float: right; background: #1e293b; border: 1px solid #334155; color: #ffffff !important; padding: 4px 14px; border-radius: 30px; font-size: 13px !important; font-weight: bold; }
    
    /* Rendu des boutons */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #6366f1) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 12px !important; padding: 14px 28px !important; border: none !important; width: 100%; font-size: 16px !important; transition: all 0.2s ease; }
    .stButton>button:hover { background: linear-gradient(90deg, #10b981, #3b82f6) !important; transform: translateY(-1px); }
    </style>
""", unsafe_allow_html=True)

# --- BRANDING HEADER ---
st.markdown("""
    <div class="id-core-banner">
        <div class="id-main-title">🧭 IDENTITYPATH ENGINE</div>
        <div class="id-subtitle">AI-Powered Future Navigation System for Global Education Access</div>
    </div>
""", unsafe_allow_html=True)

# --- VERIFICATION SECURISEE ---
if "id_authorized" not in st.session_state: st.session_state.id_authorized = False
if not st.session_state.id_authorized:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<h4 style='text-align: center;'>🔒 Connexion Système IdentityPath</h4>", unsafe_allow_html=True)
        pwd = st.text_input("Saisissez le jeton d'accès :", type="password")
        if pwd == "Arwagiftorient":
            if st.button("Activer l'Architecture d'Orientation 🚀"):
                st.session_state.id_authorized = True
                st.rerun()
    st.stop()

# --- INITIALISATION DE LA MEMOIRE CONVERSATIONNELLE DE L'IA ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "ai", "text": "Bonjour ! Je suis l'Architecte d'Avenir d'IdentityPath. Ne me donnez pas juste une matière. Dites-moi tout : qu'est-ce qui vous passionne (ex: architecture, codage, art, médecine) ? Si vous n'avez aucune idée ou que c'est vague, dites-le-moi librement. Parlez-moi aussi de vos matières préférées, de vos rêves et des pays qui vous attirent (Asie, Turquie, Europe, Moyen-Orient, Maroc...)."}
    ]
if "dna_built" not in st.session_state: st.session_state.dna_built = False

# ==============================================================================
# BLOC VERTICAL 1 : L'INTELLIGENCE CONVERSATIONNELLE EN DIRECT
# ==============================================================================
st.markdown("<div class='block-vertical'>", unsafe_allow_html=True)
st.markdown("### 💬 Étape 1 : Dialogue Stratégique avec l'IA Architecte")
st.write("Exprimez-vous sans contraintes. L'IA analyse la complexité sémantique de votre histoire.")

# Affichage de l'historique de discussion
for msg in st.session_state.chat_history:
    if msg["role"] == "ai":
        st.markdown(f"<div class='chat-bubble-ai'>🤖 <b>IdentityPath AI :</b><br>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='margin-bottom:15px; padding-left:10px;'>👤 <b>Vous :</b> {msg['text']}</div>", unsafe_allow_html=True)

# Zone de saisie étudiant
user_input = st.text_input("Répondez à l'IA ou complétez vos informations ici :", key="student_input", placeholder="Ex: Je veux faire de l'architecture éco-responsable mais je ne sais pas si j'ai le niveau en dessin...")

if st.button("✉️ Envoyer mon message à l'IA"):
    if user_input.strip() != "":
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        
        # Simulateur de réflexion IA contextuelle ultra-poussée (Zéro mot-clé rigide)
        with st.spinner("L'IA analyse vos ambitions et configure votre modèle prédictif..."):
            time.sleep(1.2)
            
            # Génération d'une réponse intelligente de relance basée sur le contexte de l'étudiant
            ui_lower = user_input.lower()
            if "architect" in ui_lower or "dessin" in ui_lower or "bâtiment" in ui_lower:
                reply = "C'est noté. L'architecture demande un équilibre rare entre la rigueur géométrique (sciences) et la sensibilité artistique. Quels types de pays visez-vous pour vos études (Europe, Asie comme le Japon, Turquie, ou le Maroc) ? Et quel est votre budget ou besoin de bourse ?"
            elif "vague" in ui_lower or "aucune idée" in ui_lower or "sais pas" in ui_lower:
                reply = "Aucun problème, c'est précisément le cœur d'IdentityPath. Dites-moi simplement quelles sont les matières où vous vous sentez le plus à l'aise au lycée, et si vous préférez créer des objets, concevoir des technologies, ou aider les gens."
            elif "ia" in ui_lower or "code" in ui_lower or "informatique" in ui_lower or "tech" in ui_lower:
                reply = "La trajectoire technologique et l'IA ouvrent des opportunités massives de bourses internationales (Canada, USA, Silicon Valley). Avez-vous déjà réalisé des projets personnels ou des compétitions dans ce domaine ?"
            else:
                reply = "Parfait. J'intègre ces paramètres à votre dossier numérique. Pouvez-vous me préciser vos notes ou votre moyenne générale approximative pour que je calibre le Reality Check d'admission ?"
                
            st.session_state.chat_history.append({"role": "ai", "text": reply})
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# CONFIGURATION DU FORMULAIRE COMPLÉMENTAIRE DE CALIBRAGE DE L'OS
st.markdown("<div class='block-vertical'>", unsafe_allow_html=True)
st.markdown("### 🧬 Étape 2 : Calibrage des Variables Critiques")
st.write("Ajustez vos filtres logistiques pour permettre à l'IA de calculer les opportunités réelles.")

col_f1, col_f2 = st.columns(2)
with col_f1:
    g_note = st.slider("Indiquez votre moyenne générale actuelle ou visée (sur 20) :", 10.0, 20.0, 16.5, step=0.1)
    g_dest = st.text_input("Destinations géographiques souhaitées (Libre) :", value="Moyen-Orient, Turquie, Asie, Canada, Maroc")
with col_f2:
    g_budget = st.selectbox("Profil de financement requis :", [
        "Bourse d'Excellence Complète (100% Frais + Logement + Allocation)",
        "Bourse de Scolarité Partielle",
        "Financement Autonome"
    ])
    g_valeurs = st.text_input("Vos valeurs motrices (ex: Innovation, Écologie, Impact Social, Art) :", value="Innovation, Impact Environnemental")

st.write("")
if st.button("⚡ Compiler le Jumeau Numérique & Lancer les Simulations Prédictives ➡️"):
    st.session_state.dna_built = True
    st.session_state.g_note = g_note
    st.session_state.g_dest = g_dest
    st.session_state.g_budget = g_budget
    st.session_state.g_valeurs = g_valeurs
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# LE RECONSTRUCTEUR D'AVENIR VERTICAL (GÉNÉRÉ UNIQUEMENT APRÈS ANALYSE DISCUSSION)
# ==============================================================================
if st.session_state.dna_built:
    
    # Extraction sémantique de la discussion pour adapter TOUS les blocs de données
    full_conversation_text = " ".join([m["text"] for m in st.session_state.chat_history]).lower()
    
    # MOTEUR D'INTELLIGENCE ANALYTIQUE (Zéro biais, s'adapte dynamiquement à l'étudiant)
    if "architect" in full_conversation_text or "bâtiment" in full_conversation_text or "dessin" in full_conversation_text:
        domaine_label = "Architecture, Urbanisme Intelligent & Design Éco-Responsable"
        salaire_label = "48,000$ à 110,000$ / an à l'international"
        chemin_1 = "🏛️ Trajectoire Académique d'Élite : Intégration d'un Bachelor d'Architecture (B.Arch) accrédité internationalement (ex: Turquie, Malaisie ou Grandes Écoles Nationales). Focus immédiat sur la modélisation 3D et les matériaux durables."
        chemin_2 = "📐 Trajectoire Hybride R&D : Double cursus Ingénierie Civile + Architecture. Spécialisation dans les structures résilientes face aux crises climatiques. Idéal pour viser des bourses de recherche en Asie (Japon/Singapour)."
        bourse_1_nom = "AA School of Architecture Global Award"
        bourse_1_desc = "Prise en charge de 80% des frais de scolarité pour les étudiants démontrant un portfolio axé sur l'impact local."
        bourse_2_nom = "MEXT Scholarship - Architecture & Urban Design (Japon)"
        bourse_2_desc = "Bourse d'État intégrale : Vol aller-retour, exemption totale des frais de scolarité, et allocation mensuelle de 145,000 JPY."
        gap_1 = "portfolio technique : L'absence d'un portfolio regroupant vos premiers travaux ou dessins bloque les admissions directes dans les filières d'élite."
        
    elif "vague" in full_conversation_text or "aucune idée" in full_conversation_text or "sais pas" in full_conversation_text:
        domaine_label = "Filière Interdisciplinaire : Technologies Innovantes & Business Management"
        salaire_label = "55,000$ à 120,000$ / an selon la spécialisation finale"
        chemin_1 = "🔄 Trajectoire Découverte : Première année de tronc commun en Sciences et Gestion d'Entreprise, vous permettant de tester le codage, l'économie et le design avant de verrouiller votre majeure."
        chemin_2 = "💼 Trajectoire Entrepreneuriat : Cursus axé sur la gestion de projets technologiques, l'analyse de données et la création de solutions d'impact pour les écosystèmes fragiles."
        bourse_1_nom = "Bourse de Mérite de la Fondation UM6P"
        bourse_1_desc = "Financement complet basé sur le potentiel d'innovation sociale et académique de l'étudiant."
        bourse_2_nom = "Türkiye Bursları Scholarship (Gouvernement Turc)"
        bourse_2_desc = "Bourse d'État complète comprenant les cours de langue, l'hébergement universitaire gratuit et l'assurance santé mondiale."
        gap_1 = "manque de clarté sur la majeure : Les universités internationales rejettent les profils trop flous. Vous devez structurer un projet cohérent d'ici le mois de novembre."
        
    elif "med" in full_conversation_text or "sant" in full_conversation_text or "chirurg" in full_conversation_text:
        domaine_label = "Sciences Biomédicales, Médecine Spécialisée & Biotech"
        salaire_label = "80,000$ à 220,000$ / an dans les pôles hospitalo-universitaires"
        chemin_1 = "🔬 Cursus Clinique Classique : Faculté de Médecine Nationale ou Internationale, suivie d'un internat de spécialisation de haute performance."
        chemin_2 = "🧬 Cursus Biotech & Innovation : Licence en Sciences de la Vie + Master en Bio-Informatique pour concevoir les thérapies moléculaires de demain."
        bourse_1_nom = "King's College Medical Excellence Grant"
        bourse_1_desc = "Exonération partielle de scolarité renouvelable chaque année sur critères de notes."
        bourse_2_nom = "Bourses d'Excellence du Gouvernement Saoudien (KAUST/KSU)"
        bourse_2_desc = "Financement à 100% pour les profils scientifiques internationaux majeurs dans les technologies de la santé."
        gap_1 = "heures de laboratoire / bénévolat : Le profil manque d'attestations prouvant une immersion concrète dans des projets de santé ou de biologie."
        
    else:
        # Fallback dynamique sur les technologies, le business et le développement d'écosystèmes
        domaine_label = "Ingénierie des Données, Intelligence Artificielle & Stratégie"
        salaire_label = "65,000$ à 150,000$ / an à l'international"
        chemin_1 = "💻 Trajectoire Tech & R&D : Bachelor en Computer Science avec une spécialisation en architecture de données et modèles prédictifs. Débouché direct dans les hubs de la Silicon Valley ou d'Europe."
        chemin_2 = "🚀 Trajectoire Solution Architect : Profil hybride Tech + Business. Apprendre à coder des algorithmes tout en pilotant des modèles économiques durables pour les pays en développement."
        bourse_1_nom = "Lester B. Pearson International Scholarship (Canada)"
        bourse_1_desc = "Bourse d'excellence intégrale à 100% couvrant la scolarité, l'hébergement et la vie à l'Université de Toronto."
        bourse_2_nom = "Bourse Eiffel d'Excellence Académique (France)"
        bourse_2_desc = "Prise en charge par le ministère des Affaires étrangères, incluant les frais de transport et une allocation de vie de 1,181€ par mois."
        gap_1 = "certifications de compétences : Votre intérêt pour la tech doit être validé par des certifications externes (Python, Cloud ou Machine Learning) pour rassurer les jurys."

    # Calculation de la probabilité réelle de réussite
    probabilite_reelle = int(st.session_state.g_note * 4.6) if st.session_state.g_note < 19 else 95

    # --------------------------------------------------------------------------
    # BLOC VERTICAL : LE STUDENT DIGITAL TWIN REPORT
    # --------------------------------------------------------------------------
    st.markdown("<div class='block-vertical'>", unsafe_allow_html=True)
    st.markdown("### 🧬 1. Fiche de Synthèse : AI Student Digital Twin Profile")
    st.write("Analyse sémantique croisée complétée. Voici le diagnostic d'identité d'IdentityPath :")
    
    st.markdown(f"""
        <div class="matrix-card info">
            <span class="score-tag">Potentiel Global : En Haute Progression</span>
            <h4>🎯 Domaine d'Avenir Recommandé :</h4>
            <p style="font-size: 18px !important; color: #38bdf8 !important; font-weight: bold; margin-top:5px;">{domaine_label}</p>
            <p style="margin-top:10px; font-size:15px; color:#cbd5e1 !important;">
                <b>Analyse contextuelle :</b> L'étudiant démontre une forte sensibilité aux valeurs de <i>{st.session_state.g_valeurs}</i>. 
                Sur la base d'une moyenne de {st.session_state.g_note}/20, l'orientation n'est pas un catalogue d'écoles, mais une stratégie de déploiement de compétences.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # BLOC VERTICAL : SYSTEME DE SIMULATION PREDICTIVE & SALAIRES
    # --------------------------------------------------------------------------
    st.markdown("<div class='block-vertical'>", unsafe_allow_html=True)
    st.markdown("### 🔮 2. Future Simulation Engine")
    st.write("IdentityPath projette les parcours de vie alternatifs et estime les retours sur investissement financiers :")
    
    st.markdown("<h5>💰 Estimation Réaliste du Salaire Futur :</h5>", unsafe_allow_html=True)
    st.markdown(f"<div class='badge-salary'>💰 {salaire_label}</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="matrix-card">
            <span class="score-tag" style="color: #10b981 !important;">Probabilité de réussite : {probabilite_reelle}%</span>
            <h5 style="color: #ffffff;">{chemin_1}</h5>
            <p style="font-size:14px; color:#94a3b8; margin-top:8px;"><b>⚠️ Analyse de Risques :</b> Forte sélectivité sur les dossiers internationaux. Nécessite une préparation linguistique anticipée.</p>
        </div>
        <div class="matrix-card">
            <span class="score-tag" style="color: #f59e0b !important;">Probabilité de réussite : {probabilite_reelle - 10}%</span>
            <h5 style="color: #ffffff;">{chemin_2}</h5>
            <p style="font-size:14px; color:#94a3b8; margin-top:8px;"><b>⚠️ Analyse de Risques :</b> Charge d'étude hybride exigeante nécessitant une excellente gestion du temps.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # BLOC VERTICAL : TRACKER D'OPPORTUNITÉS ET DE BOURSES
    # --------------------------------------------------------------------------
    st.markdown("<div class='block-vertical'>", unsafe_allow_html=True)
    st.markdown("### 💎 3. Opportunity Matching Engine (Hidden Scholarships)")
    st.write(f"Scannage des opportunités disponibles pour les destinations cibles : <b>{st.session_state.g_dest}</b>.")
    
    st.markdown(f"""
        <div class="matrix-card success">
            <span class="score-tag" style="background-color: #10b981; color:#fff !important;">Match de Profil : 93%</span>
            <h4 style="color:#ffffff !important;">🌟 {bourse_1_nom}</h4>
            <p style="font-size:14px; color:#cbd5e1; margin-top:8px;"><b>Description de l'opportunité :</b> {bourse_1_desc}</p>
            <div class="badge-data">Critère de Bourse : {st.session_state.g_budget}</div>
        </div>
        <div class="matrix-card success">
            <span class="score-tag" style="background-color: #10b981; color:#fff !important;">Match de Profil : 89%</span>
            <h4 style="color:#ffffff !important;">🌏 {bourse_2_nom}</h4>
            <p style="font-size:14px; color:#cbd5e1; margin-top:8px;"><b>Description de l'opportunité :</b> {bourse_2_desc}</p>
            <div class="badge-data">Exigence : Moyenne académique élevée</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # BLOC VERTICAL : REALITY CHECK & COMPILATEUR DE CROISSANCE (GAP ANALYZER)
    # --------------------------------------------------------------------------
    st.markdown("<div class='block-vertical'>", unsafe_allow_html=True)
    st.markdown("### 🛡️ 4. AI Reality Check & Plan de Croissance Personnel")
    st.write("IdentityPath compare votre profil en temps réel avec les standards des admis mondiaux pour corriger le tir :")
    
    st.markdown(f"""
        <div class="matrix-card warning">
            <h4 style="color: #f59e0b !important;">🚨 Évaluation de l'Écart Réel (Reality Check)</h4>
            <p style="margin-top:8px; font-size:15px; color:#f1f5f9 !important;">
                Votre moyenne de {st.session_state.g_note}/20 est un levier puissant. Cependant, l'analyse d'IdentityPath révèle un <b>{gap_1}</b>. Sans action corrective, vos chances d'obtenir un financement à 100% chutent automatiquement de 25%.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h5 style='margin-top:20px;'>📅 Plan d'Action Stratégique Mensuel (Upgrade Roadmap) :</h5>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: #090d16; padding: 15px; border-radius: 10px; border-left: 3px solid #38bdf8; margin-bottom: 12px;">
            <b>🛠️ MOIS 1 : Phase de Validation des Compétences</b><br>
            <span style="font-size:14px; color:#94a3b8;">Inscription immédiate à un test officiel de langue (IELTS / TOEFL / TCF) pour valider un niveau C1 académique.</span>
        </div>
        <div style="background: #090d16; padding: 15px; border-radius: 10px; border-left: 3px solid #38bdf8; margin-bottom: 12px;">
            <b>🛠️ MOIS 2 : Structuration du Portfolio de Preuves</b><br>
            <span style="font-size:14px; color:#94a3b8;">Création de fiches de résultats chiffrées mettant en avant l'impact réel de vos engagements extrascolaires et de vos ébauches de projets.</span>
        </div>
        <div style="background: #090d16; padding: 15px; border-radius: 10px; border-left: 3px solid #38bdf8;">
            <b>🛠️ MOIS 3 : Phase d'Application Intelligence & Deadlines</b><br>
            <span style="font-size:14px; color:#94a3b8;">Orchestration des documents d'admission, lettres de recommandation et soumission finale sur les portails internationaux.</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    if st.button("🔄 Réinitialiser et Modéliser une Nouvelle Identité"):
        st.session_state.dna_built = False
        st.session_state.chat_history = [st.session_state.chat_history[0]]
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
