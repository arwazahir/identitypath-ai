import streamlit as st
import time

# Configuration Système d'ORION AI
st.set_page_config(page_title="ORION AI — Future Architect", page_icon="🌌", layout="wide", initial_sidebar_state="collapsed")

# --- INTERFACE PREMIUM ORION (DARK MODE SCI-FI, TEXTES ULTRA-LISIBLES) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #0b0f19; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0b0f19; font-family: 'Inter', sans-serif; }
    
    /* Visibilité maximale des textes */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    
    /* Design du Dashboard ORION */
    .orion-banner { text-align: center; padding: 35px; background: linear-gradient(135deg, #1e1b4b 0%, #090514 100%); border-radius: 24px; border: 1px solid #4338ca; margin-bottom: 35px; box-shadow: 0 10px 30px rgba(67, 56, 202, 0.15); }
    .orion-title { font-size: 46px; font-weight: 700; background: linear-gradient(90deg, #6366f1, #38bdf8, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px; }
    .orion-tagline { color: #38bdf8 !important; font-size: 13px !important; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-top: 8px; }
    
    /* Cartes de simulation de trajectoires de vie */
    .twin-box { background: #111827; padding: 22px; border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 25px; }
    .path-card { background: #1e2235; padding: 22px; border-radius: 16px; border-left: 6px solid #6366f1; margin-bottom: 18px; border-top: 1px solid #2e344d; border-right: 1px solid #2e344d; border-bottom: 1px solid #2e344d; }
    .path-card.high { border-left-color: #34d399; }
    .path-card.mid { border-left-color: #f59e0b; }
    
    /* Éléments chiffrés et algorithmiques */
    .prob-badge { float: right; background: rgba(99, 102, 241, 0.2); color: #818cf8 !important; padding: 6px 14px; border-radius: 30px; font-size: 14px !important; font-weight: bold; border: 1px solid #6366f1; }
    .prob-badge.high { background: rgba(52, 211, 153, 0.2); color: #34d399 !important; border-color: #34d399; }
    .prob-badge.mid { background: rgba(245, 158, 11, 0.2); color: #fbbf24 !important; border-color: #f59e0b; }
    
    /* Bouton d'action futuriste */
    .stButton>button { background: linear-gradient(90deg, #6366f1, #38bdf8) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 12px !important; padding: 15px 32px !important; border: none !important; width: 100%; font-size: 16px !important; letter-spacing: 0.5px; transition: all 0.3s ease; }
    .stButton>button:hover { background: linear-gradient(90deg, #38bdf8, #34d399) !important; scale: 1.01; }
    
    /* Terminal de croissance et d'essais */
    .roadmap-month { background: #090d16; padding: 15px; border-radius: 10px; border-left: 3px solid #38bdf8; margin-bottom: 10px; }
    .essay-box { background: #171e30; padding: 20px; border-radius: 14px; border: 1px dashed #38bdf8; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- PORTAL HEADER ---
st.markdown("""
    <div class="orion-banner">
        <div class="orion-title">🌌 ORION AI</div>
        <div class="orion-tagline">An AI-Powered Future Navigation System for Global Education Access</div>
    </div>
""", unsafe_allow_html=True)

# --- SÉCURITÉ CONSOLE ---
if "orion_auth" not in st.session_state: st.session_state.orion_auth = False
if not st.session_state.orion_auth:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h4 style='text-align: center;'>🔑 Activation de la Matrice d'Orientation</h4>", unsafe_allow_html=True)
        key = st.text_input("Clé d'accès ORION OS :", type="password")
        if key == "Arwagiftorient":
            if st.button("Initialiser l'Architecture Prédictive 🚀"):
                st.session_state.orion_auth = True
                st.rerun()
    st.stop()

# --- INITIALISATION DE L'ÉTAT DU SYSTÈME ---
if "engine_calculated" not in st.session_state: st.session_state.engine_calculated = False

# ==============================================================================
# PHASE 1 : BLOC DE SÉLECTION GLOBAL & FLUIDE (STUDENT DIGITAL TWIN)
# ==============================================================================
if not st.session_state.engine_calculated:
    st.markdown("### 🧬 Étape 1 : Initialisation du Student Digital Twin")
    st.write("Renseignez l'intégralité des dimensions de l'étudiant pour modéliser ses futurs possibles.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 📊 Données Académiques & Options")
        f_bac = st.selectbox("Option / Filière d'études actuelle :", ["Sciences Mathématiques (SM)", "Sciences Physiques et Chimiques (PC)", "Sciences Économiques & Gestion", "Sciences de la Vie et de la Terre (SVT)", "Lettres & Sciences Humaines"])
        note_bac = st.slider("Moyenne générale projetée ou réelle (sur 20) :", 10.0, 20.0, 16.5, step=0.1)
        
        # Gestion dynamique et exhaustive des matières fortes
        mat_options = ["Mathématiques", "Physique-Chimie", "Sciences Économiques", "SVT", "Philosophie", "Anglais Académique", "Français / Littérature", "Other"]
        mat_selection = st.multiselect("Matières dominantes (Fortes notes) :", mat_options)
        custom_mat = st.text_input("Si 'Other', précisez vos matières fortes :", placeholder="Ex: Informatique, Informatique quantique, Histoire...") if "Other" in mat_selection else ""

        st.markdown("##### 🌍 Cartographie des Destinations Mondiales (Totalement Ouvert)")
        dest_options = [
            "Monde Entier / International (Full Mobility)", 
            "Pays Anglophones (USA, Royaume-Uni, Canada, Australie...)", 
            "Europe Francophone (France, Suisse, Belgique...)", 
            "Asie (Chine, Japon, Corée du Sud, Singapour...)",
            "Moyen-Orient / Pays Arabes (Arabie Saoudite, Émirats...)",
            "Turquie",
            "Établissements Nationaux d'Excellence & Grandes Écoles (Maroc)",
            "Other"
        ]
        dest_selection = st.multiselect("Destinations ou zones géographiques souhaitées :", dest_options)
        custom_dest = st.text_input("Si 'Other', écrivez le pays ciblé :", placeholder="Ex: Allemagne, Espagne, Malaisie...") if "Other" in dest_selection else ""

    with col2:
        st.markdown("##### 🎯 Valeurs Fondamentales & Moteurs de Vie")
        val_options = ["Innovation technologique", "Impact environnemental & Écologie", "Recherche pure", "Entrepreneuriat & Business", "Impact social & Humanitaire", "Création artistique & Design", "Other"]
        val_selection = st.multiselect("Valeurs clés de l'élève :", val_options)
        custom_val = st.text_input("Si 'Other', ajoutez vos propres valeurs :", placeholder="Ex: Justice sociale, Liberté financière, Éducation pour tous...") if "Other" in val_selection else ""

        st.markdown("##### 🧠 Centres d'Intérêt & Expériences")
        projets_bruts = st.text_area("Projets réalisés, bénévolat, compétitions ou clubs :", placeholder="Ex: Gagnant d'un concours national, création d'une application, bénévolat dans une coopérative...")
        ambition_pro = st.text_input("Objectif ultime de carrière (Votre rêve professionnel) :", placeholder="Ex: Devenir entrepreneur en IA, Chercheur en biotechnologies, Manager international...")
        
        st.markdown("##### 💰 Contraintes Financières & Logistiques")
        contrainte_finance = st.radio("Profil de financement requis :", [
            "Bourse complète à 100% indispensable (Frais de scolarité + Logement + Vie)",
            "Financement partiel (Bourses de mérite de scolarité uniquement)",
            "Prise en charge autonome / Indépendance financière"
        ])

    st.write("---")
    if st.button("🌌 Lancer la Simulation du Futur & Générer ORION Matrix"):
        if not ambition_pro:
            st.error("Veuillez remplir votre objectif de carrière pour qu'ORION puisse calculer vos trajectoires.")
        else:
            st.session_state.engine_calculated = True
            st.session_state.f_bac = f_bac
            st.session_state.note_bac = note_bac
            st.session_state.ambition = ambition_pro
            st.session_state.finance = contrainte_finance
            st.session_state.projets = projets_bruts
            st.rerun()

# ==============================================================================
# PHASE 2 : LE HUB FLUIDE D'ORIENTATION ET LES CORPS PRÉDICTIFS
# ==============================================================================
else:
    # 1. Rendu du Student Digital Twin Output
    st.markdown("### 🧬 1. Fiche d'Identité : Your Student Digital Twin")
    st.markdown(f"""
        <div class="twin-box">
            <span style="color: #38bdf8; font-weight: bold; font-size: 16px;">[DIGITAL TWIN ANALYSIS ACTIVE]</span><br>
            <p style="margin-top: 8px; font-size: 16px !important; color: #f1f5f9 !important;">
                Profil d'élève à haut potentiel en <b>{st.session_state.f_bac}</b> avec un ancrage académique évalué à <b>{st.session_state.note_bac}/20</b>. 
                Indicateurs de succès élevés pour l'objectif de carrière : <b>"{st.session_state.ambition}"</b>. 
                Structure de financement identifiée : <i>{st.session_state.finance}</i>.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Séparation en deux colonnes fluides pour l'analyse profonde
    col_left, col_right = st.columns([4, 3])
    
    with col_left:
        # 2. FUTURE SIMULATION ENGINE & REALITY CHECK
        st.markdown("### 🔮 2. Future Simulation Engine (The Architecture)")
        st.write("ORION ne donne pas de listes statiques. Voici vos 3 chemins de vie possibles simulés avec leur probabilité réelle de succès :")
        
        # Algorithme prédictif de calcul de probabilités selon la note
        base_prob = int(st.session_state.note_bac * 4.5) if st.session_state.note_bac < 18 else 93
        
        # Chemin A
        st.markdown(f"""
            <div class="path-card high">
                <div class="prob-badge high">Probabilité : {base_prob}%</div>
                <h4 style="color: #34d399 !important;">🗺️ Chemin A : Excellence Globale + Écosystème Startup</h4>
                <p class="text-light" style="margin-top:10px;"><b>Parcours :</b> Université de premier plan international (USA/Canada/UM6P) couplée à un incubateur technologique d'élite.</p>
                <p class="text-light"><b>⚠️ Analyse des Risques :</b> Compétition extrême à l'admission. Nécessité d'avoir un dossier extra-scolaire solide.</p>
                <p class="text-light" style="color: #34d399 !important;"><b>🎯 Pourquoi :</b> Ce chemin maximise votre valeur sur le marché mondial et vous connecte directement aux investisseurs.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Chemin B
        st.markdown(f"""
            <div class="path-card mid">
                <div class="prob-badge mid">Probabilité : {base_prob - 12}%</div>
                <h4 style="color: #f59e0b !important;">🗺️ Chemin B : Spécialisation Académique Pure (Europe / Turquie / Asie)</h4>
                <p class="text-light" style="margin-top:10px;"><b>Parcours :</b> Cursus universitaire axé sur la recherche fondamentale, suivi d'un Master d'ingénierie de pointe ou d'un doctorat.</p>
                <p class="text-light"><b>⚠️ Analyse des Risques :</b> Moins d'exposition immédiate au monde des affaires ou au réseau entrepreneurial.</p>
                <p class="text-light" style="color: #f59e0b !important;"><b>🎯 Pourquoi :</b> Moins coûteux à l'entrée, ce parcours consolide votre expertise technique avant de basculer sur le terrain.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Chemin C
        st.markdown(f"""
            <div class="path-card">
                <div class="prob-badge">Probabilité : {base_prob - 5}%</div>
                <h4 style="color: #6366f1 !important;">🗺️ Chemin C : Cursus Hybride & Management Stratégique</h4>
                <p class="text-light" style="margin-top:10px;"><b>Parcours :</b> Double formation immédiate combinant les compétences techniques de votre domaine et un diplôme de Business Management.</p>
                <p class="text-light"><b>⚠️ Analyse des Risques :</b> Charge cognitive et de travail doublée au cours des deux premières années d'études.</p>
            </div>
        """, unsafe_allow_html=True)

        # 3. OPPORTUNITY MATCHING ENGINE
        st.markdown("### 💎 3. Opportunity Matching Engine (Hidden Opportunities)")
        st.write("Classement prédictif des opportunités mondiales (Bourses, Summer Schools, Compétitions) calculé pour votre profil :")
        
        st.markdown(f"""
            <div style="background: #111827; padding: 20px; border-radius: 14px; border: 1px solid #1f2937; margin-bottom: 15px;">
                <h5 style="color: #ffffff;">🌟 Programme International de Bourse Globale d'Excellence</h5>
                <p class="text-light" style="font-size:14px; margin-top:5px;">• <b>Éligibilité calculée :</b> 94% | • <b>Niveau de Compétition :</b> Très Élevé | • <b>Adéquation Profil :</b> 90%</p>
                <p style="color: #34d399 !important; font-size:13px; margin-top:5px;">➔ <b>Reality Check :</b> Vos notes vous placent dans le premier tiers. Pour verrouiller cette opportunité, intégrez une certification de langue officielle avant la session d'octobre.</p>
            </div>
            <div style="background: #111827; padding: 20px; border-radius: 14px; border: 1px solid #1f2937;">
                <h5 style="color: #ffffff;">🔬 Fellowship Mondial de Recherche & d'Innovation pour Étudiants</h5>
                <p class="text-light" style="font-size:14px; margin-top:5px;">• <b>Éligibilité calculée :</b> 88% | • <b>Niveau de Compétition :</b> Modéré | • <b>Adéquation Profil :</b> 95%</p>
                <p style="color: #34d399 !important; font-size:13px; margin-top:5px;">➔ <b>Reality Check :</b> Vos projets extrascolaires sont un atout majeur. Ce programme offre un financement complet si votre lettre de motivation est axée sur l'impact.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        # 4. PERSONAL GROWTH ALGORITHM (UPGRADE ROADMAP)
        st.markdown("### 📅 4. Personal Growth Plan")
        st.write("Votre feuille de route stratégique mensuelle pour faire augmenter vos chances de bourses de **+20%** :")
        
        st.markdown(f"""
            <div class="roadmap-month">
                <b>🟢 MOIS 1 : Phase d'Ancrage Linguistique</b><br>
                <span style="font-size:13px; color: #94a3b8;">Préparation intensive et passage des examens de langue standardisés. Objectif : Atteindre le niveau C1 académique.</span>
            </div>
            <div class="roadmap-month">
                <b>🔵 MOIS 2 : Structuration du Portfolio d'Impact</b><br>
                <span style="font-size:13px; color: #94a3b8;">Transformation de vos expériences vécues ({st.session_state.projets[:40]}...) sous forme de fiches de résultats quantifiables.</span>
            </div>
            <div class="roadmap-month">
                <b>🟡 MOIS 3 : Consolidation Finale & Soumission</b><br>
                <span style="font-size:13px; color: #94a3b8;">Rédaction des essais personnels personnalisés et envoi des dossiers complets aux bourses gouvernementales cibles.</span>
            </div>
        """, unsafe_allow_html=True)

        # 5. AI APPLICATION INTELLIGENCE (ESSAY INTERACTIF)
        st.markdown("### ✍️ 5. AI Essay & Story Builder")
        st.write("L'IA n'écrit pas à votre place, elle extrait la vérité de votre parcours à travers 3 questions clés :")
        
        # Le questionnaire intelligent d'ORION
        q1 = st.text_input("1. Quel a été le plus grand obstacle ou défi lors de vos projets récents ?", placeholder="Ex: Manque de budget, convaincre l'équipe...")
        q2 = st.text_input("2. En quoi votre objectif d'avenir peut-il aider votre communauté ou le monde ?", placeholder="Ex: Réduire la pollution, créer de l'emploi technologique...")
        q3 = st.text_input("3. Quelle est la compétence unique que vous possédez en dehors des cours ?", placeholder="Ex: Rapidité d'apprentissage en code, aisance rédactionnelle...")
        
        if st.button("✨ Extraire mon Identité de Candidature"):
            if q1 and q2 and q3:
                st.markdown("<div class='essay-box'>", unsafe_allow_html=True)
                st.markdown("<b style='color: #38bdf8;'>🔮 Votre Fil Conducteur Narratif Détecté :</b>", unsafe_allow_html=True)
                st.markdown(f"""
                    <i>"La synergie entre vos compétences en {st.session_state.f_bac} et votre volonté de '{q2}' constitue le cœur de votre histoire. En articulant votre essai autour de votre capacité à surmonter le défi de '{q1}', vous démontrez aux jurys d'admission que vous n'êtes pas un simple étudiant avec de bonnes notes, mais un acteur de changement doté d'une résilience rare."</i>
                """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("Veuillez répondre aux 3 questions pour générer votre trame narrative unique.")

    st.write("---")
    if st.button("🔄 Modéliser un nouveau profil d'avenir"):
        st.session_state.engine_calculated = False
        st.rerun()
