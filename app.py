import streamlit as st
import time

# Configuration d'IdentityPath OS
st.set_page_config(page_title="IdentityPath — 3allal", page_icon="🎮", layout="wide", initial_sidebar_state="collapsed")

# --- STYLE GRAPHIQUE JEU VIDÉO / RPG ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Inter:wght@400;600;700&display=swap');
    
    .main { background-color: #05070f; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #05070f; font-family: 'Inter', sans-serif; }
    
    /* Titres et visibilité */
    h1, h2, h3, h4, h5 { font-family: 'Orbitron', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    .stMarkdown, p, span, label { color: #e2e8f0 !important; font-size: 15px !important; }
    
    /* Header Gaming */
    .game-banner { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e1b4b 0%, #030712 100%); border-radius: 20px; border: 2px solid #4338ca; margin-bottom: 30px; box-shadow: 0 0 25px rgba(99, 102, 241, 0.3); }
    .game-title { font-size: 42px; font-weight: 900; background: linear-gradient(90deg, #3b82f6, #ff007f, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 1px; }
    .game-subtitle { color: #38bdf8 !important; font-size: 12px !important; font-weight: bold; letter-spacing: 3px; text-transform: uppercase; margin-top: 5px; }
    
    /* Blocs de quêtes et cartes */
    .quest-section { background: #0b0f19; padding: 25px; border-radius: 16px; border: 1px solid #1e2937; margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.4); }
    .avatar-card { background: linear-gradient(145deg, #111827, #1f2937); padding: 20px; border-radius: 12px; border: 2px solid #3b82f6; margin-bottom: 20px; }
    .mission-card { background: #161c2e; padding: 18px; border-radius: 10px; border-left: 5px solid #ff007f; margin-bottom: 15px; }
    .mission-card.completed { border-left-color: #10b981; }
    
    /* Badges de Récompenses et Statistiques */
    .stat-badge { background: rgba(59, 130, 246, 0.2); color: #3b82f6 !important; border: 1px solid #3b82f6; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 13px !important; display: inline-block; margin-right: 10px; }
    .reward-badge { background: rgba(16, 185, 129, 0.2); color: #10b981 !important; border: 1px solid #10b981; padding: 6px 14px; border-radius: 6px; font-weight: bold; font-size: 15px !important; display: inline-block; margin-top: 10px; }
    
    /* Override Radio Buttons & Widgets pour look Cyberpunk */
    div[data-testid="stRadio"] > label { font-weight: bold !important; color: #38bdf8 !important; }
    
    /* Boutons de niveau supérieur */
    .stButton>button { background: linear-gradient(90deg, #ff007f, #7c3aed) !important; color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-weight: bold !important; border-radius: 10px !important; padding: 14px 25px !important; border: none !important; width: 100%; font-size: 16px !important; box-shadow: 0 0 15px rgba(255, 0, 127, 0.4); }
    .stButton>button:hover { background: linear-gradient(90deg, #10b981, #3b82f6) !important; box-shadow: 0 0 20px rgba(16, 185, 129, 0.5); }
    </style>
""", unsafe_allow_html=True)

# --- PORTAL HEADER ---
st.markdown("""
    <div class="game-banner">
        <div class="game-title">🧭 IDENTITYPATH</div>
        <div class="game-subtitle">Propulsé par l'IA 3allal — Future Build Engine</div>
    </div>
""", unsafe_allow_html=True)

# --- CODE D'ACCÈS ---
if "game_auth" not in st.session_state: st.session_state.game_auth = False
if not st.session_state.game_auth:
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown("<h4 style='text-align: center; color: #ff007f !important;'>🎮 Insérer un jeton pour jouer</h4>", unsafe_allow_html=True)
        token = st.text_input("Clé d'activation :", type="password")
        if token == "Arwagiftorient":
            if st.button("Lancer la Partie 🚀"):
                st.session_state.game_auth = True
                st.rerun()
    st.stop()

if "avatar_generated" not in st.session_state: st.session_state.avatar_generated = False

# ==============================================================================
# CONFIGURATION : LE DESIGN PAR CLICS (PAS DE TEXTE À TAPER)
# ==============================================================================
if not st.session_state.avatar_generated:
    st.markdown("### 🛠️ Configuration de ton Avatar d'Avenir")
    st.write("Sélectionne tes briques de vie en un clic. 3allal s'occupe de compiler ton jumeau numérique.")
    
    st.markdown("<div class='quest-section'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        guilde = st.radio("🎯 Choisis ta Guilde Principale (Ton intérêt majeur) :", [
            "📐 Archi-Tech & Design (Architecture, Urbanisme, Modélisation)",
            "🤖 Cyber-Minds (Intelligence Artificielle, Informatique, Cyber)",
            "🧬 Bio-Hackers (Médecine, Santé, Biotechnologies)",
            "📊 Global Traders (Business, Entrepreneuriat, Stratégie)",
            "🔍 Je suis perdu (Aide-moi à choisir, 3allal !)"
        ])
        
        matiere = st.selectbox("⚡ Choisis ton Super-Pouvoir Académique actuel :", [
            "Sciences Physiques & Géométrie",
            "Algorithmes & Mathématiques",
            "Sciences Naturelles & SVT",
            "Créativité Visuelle & Dessin",
            "Analyse Économique & Logique"
        ])
        
    with col2:
        destination = st.selectbox("🌍 Zone de déploiement de tes rêves :", [
            "🌏 Hub Asiatique (Japon, Chine, Singapour)",
            "🕌 Moyen-Orient & Turquie (Arabie Saoudite, Istanbul, Émirats)",
            "🍁 Amériques & Pays Anglophones (Canada, USA, UK)",
            "🇪🇺 Écosystème Européen (France, Suisse, Allemagne)",
            "🇲🇦 Écoles Nationales de Prestige (Maroc)"
        ])
        
        gold_profile = st.radio("💰 Ta contrainte de pièces d'or (Budget) :", [
            "Bourse intégrale requise (100% de financement obligatoire)",
            "Bourse partielle acceptée",
            "Autosuffisance financière"
        ])
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='quest-section'>", unsafe_allow_html=True)
    note_curseur = st.slider("📈 Ton niveau d'énergie actuel (Moyenne scolaire estimée sur 20) :", 10.0, 20.0, 16.5, step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🌌 Forger mon Profil de Futur & Activer 3allal"):
        st.session_state.avatar_generated = True
        st.session_state.guilde = guilde
        st.session_state.matiere = matiere
        st.session_state.destination = destination
        st.session_state.gold = gold_profile
        st.session_state.note = note_curseur
        st.rerun()

# ==============================================================================
# LE DASHBOARD DE JEU : CHEMINS, MISSIONS ET PROGRESSION VERTICALE
# ==============================================================================
else:
    # Analyse automatique par 3allal si l'étudiant est indécis
    guilde_active = st.session_state.guilde
    if "Je suis perdu" in guilde_active:
        if "Dessin" in st.session_state.matiere or "Physiques" in st.session_state.matiere:
            guilde_active = "📐 Archi-Tech & Design (Attribué par 3allal 🔮)"
            domaine_key = "archi"
        elif "Algorithmes" in st.session_state.matiere:
            guilde_active = "🤖 Cyber-Minds (Attribué par 3allal 🔮)"
            domaine_key = "tech"
        elif "SVT" in st.session_state.matiere:
            guilde_active = "🧬 Bio-Hackers (Attribué par 3allal 🔮)"
            domaine_key = "bio"
        else:
            guilde_active = "📊 Global Traders (Attribué par 3allal 🔮)"
            domaine_key = "biz"
    else:
        domaine_key = "archi" if "Archi" in guilde_active else ("tech" if "Cyber" in guilde_active else ("bio" if "Bio" in guilde_active else "biz"))

    # Assignation des bases de données de jeu en fonction du choix
    if domaine_key == "archi":
        metier_title = "Eco-Architecte Digital & Urbaniste du Futur"
        salaire_est = "50,000$ - 105,000$ / an"
        chemin_desc = "Intégrer un cursus d'architecture couplé au design numérique 3D pour réinventer les écosystèmes urbains."
        q1, q2 = "Passer un test de dessin technique ou créer un mini-portfolio de 3 croquis", "Valider une certification de modélisation 3D basique"
        bourse_nom = "Bourse d'Excellence en Design Créatif & Technique"
    elif domaine_key == "tech":
        metier_title = "Architecte de Solutions d'IA & Machine Learning"
        salaire_est = "70,000$ - 160,000$ / an"
        chemin_desc = "Se positionner sur le développement de modèles prédictifs et d'outils d'optimisation automatisés."
        q1, q2 = "Développer un script d'automatisation ou participer à un mini-hackathon", "Compléter le premier module d'un certificat d'algorithmes"
        bourse_nom = "Global Tech Innovation Fellowship"
    elif domaine_key == "bio":
        metier_title = "Ingénieur en Biotech & Technologies Médicales"
        salaire_est = "75,000$ - 180,000$ / an"
        chemin_desc = "Faire le pont entre la biologie cellulaire et les outils logiciels d'analyse médicale."
        q1, q2 = "Rédiger un résumé de recherche sur une innovation médicale récente", "Suivre un stage d'observation en laboratoire ou clinique"
        bourse_nom = "International Life Sciences Merit Award"
    else:
        metier_title = "Manager de Projets Technologiques & Stratégie"
        salaire_est = "55,000$ - 130,000$ / an"
        chemin_desc = "Piloter les investissements et structurer des modèles de business innovants à forte scalabilité."
        q1, q2 = "Analyser le business model d'une startup connue", "Suivre une initiation à la finance de marché ou à l'analyse de données"
        bourse_nom = "GREAT Entrepreneurial Scholarship"

    # Calcul de la jauge de niveau d'avatar
    win_chance = int(st.session_state.note * 4.6) if st.session_state.note < 19 else 94

    # 📊 BLOC 1 : STATUT DE L'AVATAR
    st.markdown("<div class='quest-section'>", unsafe_allow_html=True)
    st.markdown("### 🧬 1. Ton Avatar Jumeau Numérique")
    
    st.markdown(f"""
        <div class="avatar-card">
            <span style="color: #ff007f; font-weight: bold; font-size: 13px; letter-spacing: 1px;">[AVATAR SYNCHRONISÉ]</span>
            <h4 style="margin-top: 5px; color: #38bdf8 !important;">{metier_title}</h4>
            <div style="margin-top: 10px;">
                <div class="stat-badge">Classe : {guilde_active}</div>
                <div class="stat-badge">Matière Initiale : {st.session_state.matiere}</div>
                <div class="stat-badge">Niveau : {st.session_state.note}/20</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 🔮 BLOC 2 : CHEMIN ET SIMULATION DE SALAIRE
    st.markdown("<div class='quest-section'>", unsafe_allow_html=True)
    st.markdown("### 🔮 2. Chemin Personnalisé & Trajectoire de Vie")
    st.write("Voici la ligne de temps générée instantanément pour ton objectif :")
    
    st.markdown(f"""
        <div class="mission-card completed">
            <span class="score-tag" style="color: #10b981 !important;">Probabilité de Succès : {win_chance}%</span>
            <h5 style="color: #10b981 !important;">🎯 Ton Chemin de Vie Idéal :</h5>
            <p style="margin-top: 5px; font-size: 15px;"><b>Parcours :</b> {chemin_desc}</p>
            <p style="font-size: 13px; color: #94a3b8 !important;"><b>Zone ciblée :</b> {st.session_state.destination}</p>
            <div class="reward-badge">💰 Récompense de Butin (Salaire Estimé) : {salaire_est}</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 💎 BLOC 3 : LE TABLEAU DES QUÊTES D'AMÉLIORATION (GAP ANALYZER)
    st.markdown("<div class='quest-section'>", unsafe_allow_html=True)
    st.markdown("### 📜 3. Ton Tableau de Quêtes Étape par Étape")
    st.write("Remplis ces missions simples pour accumuler de l'XP et sécuriser ton admission :")
    
    st.markdown(f"""
        <div class="mission-card">
            <span class="score-tag" style="color: #ff007f !important;">+150 XP</span>
            <h5>⚔️ Quête Immediate : Débloquer le Verrou Linguistique</h5>
            <p style="margin-top:5px; font-size:14px; color: #cbd5e1 !important;">Prendre 15 minutes pour évaluer ton niveau sur un test blanc officiel de langue (IELTS/TOEFL/TCF). Objectif : Valider le niveau requis pour la zone <i>{st.session_state.destination}</i>.</p>
        </div>
        <div class="mission-card">
            <span class="score-tag" style="color: #ff007f !important;">+250 XP</span>
            <h5>🛡️ Quête de Profil : Forger tes Preuves d'Impact</h5>
            <p style="margin-top:5px; font-size:14px; color: #cbd5e1 !important;">Mission : <b>{q1}</b>. Cela permettra à 3allal de blinder ton dossier face aux universités internationales.</p>
        </div>
        <div class="mission-card">
            <span class="score-tag" style="color: #ff007f !important;">+400 XP</span>
            <h5>🏆 Quête Avancée : Dompter la Spécialisation</h5>
            <p style="margin-top:5px; font-size:14px; color: #cbd5e1 !important;">Mission : <b>{q2}</b> afin de te démarquer des autres candidats mondiaux.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 🛡️ BLOC 4 : OPPORTUNITÉS & REALITY CHECK DE 3ALLAL
    st.markdown("<div class='quest-section'>", unsafe_allow_html=True)
    st.markdown("### 💎 4. Le Radar d'Opportunités de 3allal")
    
    st.markdown(f"""
        <div class="avatar-card" style="border-color: #f59e0b;">
            <h5 style="color: #f59e0b !important;">🚨 Le Reality Check de 3allal :</h5>
            <p style="margin-top: 5px; font-size: 14px;">
                "Écoute-moi bien : avec ton niveau actuel de <b>{st.session_state.note}/20</b>, tu as un excellent moteur. Mais si tu demandes l'option <b>'{st.session_state.gold}'</b> sans valider tes quêtes d'XP d'ici l'automne, les algorithmes de bourses vont te mettre de côté. Remplis la quête linguistique le mois prochain pour passer ta probabilité à <b>{min(win_chance + 12, 98)}%</b> !"
            </p>
        </div>
        
        <div class="mission-card completed" style="background: #091a18; border-left-color: #10b981;">
            <span class="score-tag" style="background: #10b981; color: #fff !important;">Match : 91%</span>
            <h5 style="color: #ffffff !important;">🌟 Opportunité Détectée : {bourse_nom}</h5>
            <p style="margin-top:5px; font-size:14px; color: #a7f3d0 !important;"><b>Avantage :</b> Ajustée à ton critère ({st.session_state.gold}). Offre une couverture de scolarité prioritaire pour la zone {st.session_state.destination}.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    if st.button("🔄 Recommencer une Partie / Créer un Nouvel Avatar"):
        st.session_state.avatar_generated = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
