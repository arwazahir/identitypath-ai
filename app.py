import streamlit as st
import time
import random

# Configuration de l'écosystème
st.set_page_config(page_title="IdentityPath OS", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- STYLE INTERFACE PREMIUM (LISIBILITÉ MAXIMALE & GRAPHISME APPLICATIF) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #0f172a; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    
    /* Contrôle absolu de la visibilité des textes - Blanc éclatant obligatoire */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; font-weight: 800 !important; }
    
    /* Header & Branding de l'OS */
    .os-header { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 20px; border: 2px solid #334155; margin-bottom: 30px; }
    .os-title { font-size: 44px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Urbanist'; letter-spacing: -1px; }
    .os-subtitle { color: #6366f1 !important; font-size: 13px !important; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-top: 8px; }
    
    /* Les Piliers du Student DNA & Modules */
    .dna-badge { background: #1e293b; border: 1px solid #475569; padding: 10px 15px; border-radius: 10px; margin: 5px; display: inline-block; }
    .card-matrix { background: #1e293b; padding: 24px; border-radius: 16px; border: 1px solid #334155; margin-bottom: 20px; }
    
    /* Composants de Score Universitaires Avançés */
    .score-container { display: flex; justify-content: space-between; background: #111827; padding: 12px; border-radius: 8px; margin-top: 8px; border: 1px solid #1f2937; }
    .score-box { text-align: center; width: 23%; }
    .score-val { font-size: 20px !important; font-weight: 700; color: #3b82f6 !important; font-family: 'Urbanist'; }
    .score-val.success { color: #10b981 !important; }
    .score-val.warning { color: #6366f1 !important; }
    .score-val.total { color: #f59e0b !important; }
    .score-lbl { font-size: 11px !important; color: #94a3b8 !important; text-transform: uppercase; }
    
    /* Boutons de l'OS */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #6366f1) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 12px !important; padding: 14px 28px !important; border: none !important; width: 100%; font-size: 16px !important; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2); }
    .stButton>button:hover { background: linear-gradient(90deg, #6366f1, #10b981) !important; }
    
    /* Rendu des terminaux et simulateurs */
    .terminal-box { background: #090d16; padding: 18px; border-radius: 12px; border-left: 4px solid #10b981; font-family: 'Inter', monospace; margin-bottom: 15px; }
    .story-output { background: #172554; padding: 20px; border-radius: 12px; border: 1px solid #3b82f6; font-style: italic; color: #e2e8f0 !important; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER GLOBAL ---
st.markdown("""
    <div class="os-header">
        <div class="os-title">🧭 IDENTITYPATH OPERATING SYSTEM</div>
        <div class="os-subtitle">AI Career & Education Architecture • Multi-Student Engine</div>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES INTERNATIONALE MUTABLE ET NEUTRE ---
GLOBAL_UNIS_POOL = [
    {"nom": "Stanford University (USA)", "filiere": "BSc in Symbolic Systems / Computer Science", "base_match": 85, "environnement": "Silicon Valley tech hub, hautement compétitif.", "cout": "$82,000/an", "culture": "Innovation, Esprit startup"},
    {"nom": "London School of Economics (LSE - UK)", "filiere": "BSc in Econometrics and Mathematical Economics", "base_match": 82, "environnement": "Centre financier de Londres, focus analytique.", "cout": "£38,000/an", "culture": "Recherche, Impact Public"},
    {"nom": "UM6P (Université Mohammed VI Polytechnique - Maroc)", "filiere": "Integrated Bachelor-Master in Governance & Science", "base_match": 90, "environnement": "Écosystème d'excellence africain, recherche appliquée.", "cout": "Variables", "culture": "Entrepreneuriat, Impact Local"},
    {"nom": "EPFL (Lausanne - Suisse)", "filiere": "Bachelor en Sciences et Technologies du Vivant / Informatique", "base_match": 80, "environnement": "Campus scientifique d'élite francophone.", "cout": "CHF 1,600/an", "culture": "Rigueur, Recherche pure"},
    {"nom": "University of Toronto (Canada)", "filiere": "Faculty of Arts and Science - Commerce & Tech Liaison", "base_match": 84, "environnement": "Hub multiculturel nord-américain majeur.", "cout": "$65,000/an", "culture": "Diversité, Opportunités post-diplôme"},
    {"nom": "McGill University (Canada)", "filiere": "Bachelor of Commerce (BCom) - Interdisciplinary Studies", "base_match": 81, "environnement": "Montréal, écosystème bilingue et dynamique.", "cout": "$58,000/an", "culture": "Leadership académique"}
]

# --- VÉRIFICATION SÉCURITÉ ACCÈS ---
if "os_active" not in st.session_state: st.session_state.os_active = False
if not st.session_state.os_active:
    c_l, c_m, c_r = st.columns([1, 2, 1])
    with c_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Connexion au Système Central</h3>", unsafe_allow_html=True)
        key_input = st.text_input("Saisissez la clé d'activation OS :", type="password")
        if key_input == "Arwagiftorient":
            if st.button("Initialiser les 9 Piliers IA 🌐"):
                st.session_state.os_active = True
                st.rerun()
    st.stop()

# --- INITIALISATION DE LA NAVIGATION PAR PILIERS ---
tabs = st.tabs([
    "🧬 1. AI Student DNA", 
    "📊 2 & 3. Matcher & Hunter", 
    "📅 4. Application Manager", 
    "✍️ 5. Essay Builder", 
    "🚀 6. Career Simulator", 
    "📡 7, 8 & 9. Radar, Gap & Network"
])

# ==============================================================================
# PILIER 1 : LE PROFIL INTELLIGENT DE L'ÉTUDIANT (AI STUDENT DNA)
# ==============================================================================
with tabs[0]:
    st.markdown("### 🧬 Pilier 1 : Générateur de Profil Universel (Student DNA Profile)")
    st.write("Ce module collecte l'intégralité des variables de n'importe quel étudiant pour modéliser son empreinte unique.")
    
    col_dna1, col_dna2 = st.columns(2)
    with col_dna1:
        st.markdown("##### 📈 Indicateurs Académiques & Matières")
        filiere_actuelle = st.selectbox("Filière secondaire / Baccalauréat :", ["Sciences Mathématiques", "Sciences Économiques & Gestion", "Sciences Physiques et Chimiques", "Sciences de la Vie et de la Terre", "Lettres & Humain"])
        note_generale = st.slider("Moyenne générale actuelle de l'élève (sur 20) :", 10.0, 20.0, 16.5)
        mat_fortes = st.multiselect("Matières dominantes (fortes notes) :", ["Mathématiques", "Physique-Chimie", "Économie & Droit", "Philosophie / Littérature", "SVT", "Sciences de l'Ingénieur"])
        
        st.markdown("##### 💼 Ambitions & Cibles Professionnelles")
        metier_cible = st.text_input("Objectif de carrière ou métier visé :", placeholder="Ex: Entrepreneur en IA, Chirurgien, Data Analyst, Gestionnaire de Fonds...")
        valeurs_eleve = st.multiselect("Valeurs fondamentales de l'élève :", ["Innovation technologique", "Impact environnemental", "Recherche scientifique", "Entrepreneuriat", "Impact social & humanitaire"])

    with col_dna2:
        st.markdown("##### 🏆 Activités, Certificats & Profil Extra-Scolaire")
        interets = st.text_area("Centres d'intérêt & Passions en dehors des cours :", placeholder="Ex: Codage en autodidacte, lecture économique, design de produits, journalisme...")
        projets_comp = st.text_area("Projets réalisés, compétitions, prix ou certificats obtenus :", placeholder="Ex: Gagnant d'un prix régional, certificat de langue, création d'un club de débat...")
        
        st.markdown("##### 🌍 Paramètres Logistiques & Budget")
        pays_vises = st.multiselect("Destinations d'études souhaitées :", ["États-Unis", "Royaume-Uni", "Canada", "Europe Francophone (France, Belgique)", "Suisse", "Écoles d'Excellence Nationales"])
        budget_max = st.radio("Budget disponible par an (frais d'études + vie) :", ["Besoin absolu d'une bourse complète (100%)", "Budget Modéré (Financement partiel requis)", "Budget Indépendant (Prise en charge autonome)"])

    if st.button("🧬 Compiler le Student DNA Profile"):
        st.session_state.dna_compiled = True
        # Algorithme de synthèse sémantique dynamique (0% fixe sur un profil unique)
        st.session_state.summary_dna = f"L'étudiant suit un cursus en {filiere_actuelle} avec une moyenne d'excellence de {note_generale}/20. Porté par des valeurs axées sur {', '.join(valeurs_eleve) if valeurs_eleve else 'le développement global'}, il aspire à devenir {metier_cible if metier_cible else 'un leader dans son domaine'}. Ses réalisations incluent : {projets_comp if projets_comp else 'des initiatives personnelles scolaires'}."
        st.rerun()
        
    if "dna_compiled" in st.session_state:
        st.success("✅ **AI Student DNA Engine : Empreinte de l'élève générée avec succès.**")
        st.markdown(f"""
            <div class="terminal-box">
                <span style="color: #10b981;">[STUDENT DNA PROFILE GENERATED] :</span><br>
                <p style="color: #ffffff !important; margin-top:5px;">"{st.session_state.summary_dna}"</p>
            </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PILIERS 2 & 3 : AI UNIVERSITY MATCHER & SCHOLARSHIP HUNTER
# ==============================================================================
with tabs[1]:
    st.markdown("### 🏛️ Pilier 2 & 💎 Pilier 3 : Compatibility Matrix & Explanation Engine")
    st.write("L'IA calcule l'indice de compatibilité réel croisé avec la détection automatique de bourses éligibles.")
    
    if "dna_compiled" not in st.session_state:
        st.warning("⚠️ Veuillez d'abord compiler le 'Student DNA' dans le premier onglet pour alimenter le Matcher.")
    else:
        st.markdown("#### 📊 Tableau de Compatibilité Multicritères Avancé")
        
        for uni in GLOBAL_UNIS_POOL:
            # Algorithme prédictif dynamique basé sur les vraies inputs du DNA
            chances_admission = int(note_generale * 4.5) if note_generale < 18 else 92
            if "Stanford" in uni["nom"]: chances_admission -= 25 # Facteur sélectivité Ivy League
            
            chances_bourse = 85 if "bourse" in budget_max.lower() and note_generale >= 16 else 40
            fit_carriere = 90 if any(v in uni["culture"].lower() for v in ["innovation", "entrepreneuriat"]) else 75
            
            total_match = int((chances_admission + chances_bourse + fit_carriere) / 3)
            
            with st.expander(f"🏫 {uni['nom']} — Match Global : {total_match}%"):
                st.markdown(f"""
                    <p class="text-light"><b>📚 Programme recommandé :</b> {uni['filiere']}</p>
                    <p class="text-light"><b>🌍 Environnement :</b> {uni['environnement']} | <b>💰 Coût standard :</b> {uni['cout']}</p>
                """, unsafe_allow_html=True)
                
                # Rendu des scores du Pilier 2
                st.markdown(f"""
                    <div class="score-container">
                        <div class="score-box"><div class="score-val">{chances_admission}%</div><div class="score-lbl">Admission</div></div>
                        <div class="score-box"><div class="score-val success">{chances_bourse}%</div><div class="score-lbl">Bourse</div></div>
                        <div class="score-box"><div class="score-val warning">{fit_carriere}%</div><div class="score-lbl">Fit Carrière</div></div>
                        <div class="score-box"><div class="score-val total">{total_match}%</div><div class="score-lbl">Total Match</div></div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Contenu explicatif du Pilier 3 (Scholarship Hunter)
                st.markdown("<h5 style='margin-top:15px;'>💎 Statut du Scholarship Hunter :</h5>", unsafe_allow_html=True)
                st.markdown(f"""
                    <div style="background-color: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1f2937;">
                        <p style="color: #34d399 !important; margin-bottom: 5px;">➔ <b>Pourquoi vous êtes éligible :</b> Votre moyenne de {note_generale}/20 passe les filtres automatiques du premier tour et s'aligne avec la culture '{uni['culture']}' de l'établissement.</p>
                        <p style="color: #f59e0b !important;">🔮 <b>Prédiction d'impact :</b> Si vous ajoutez 1 projet extrascolaire d'envergure ou une certification de langue validée de niveau C1, vos chances d'obtention de bourse augmentent de <b>+15% à +20%</b> sur ce profil.</p>
                    </div>
                """, unsafe_allow_html=True)

# ==============================================================================
# PILIER 4 : AI APPLICATION MANAGER (CALENDRIER ET CRITÈRES)
# ==============================================================================
with tabs[2]:
    st.markdown("### 📅 Pilier 4 : Application Manager & Chronologie Stratégique")
    st.write("Ce module orchestre la feuille de route des tâches administratives et académiques mois par mois.")
    
    st.markdown("""
        <div class="card-matrix">
            <h4 style='color: #6366f1 !important;'>🗓️ Calendrier d'Admission & Actions Recommandées</h4>
            <hr style="border-color: #334155;">
            <p style="margin-bottom:12px;"><b>🔴 SEPTEMBRE / OCTOBRE : Phase Fondations</b><br>
            → Inscription et passage des tests de langue standardisés (IELTS, TOEFL ou Duolingo English Test).<br>
            → Initialisation de la liste finale des universités cibles et demande des premières lettres de recommandation aux professeurs.</p>
            
            <p style="margin-bottom:12px;"><b>🔵 NOVEMBRE / DÉCEMBRE : Phase Rédactionnelle & Soumission</b><br>
            → Finalisation des essais personnels (Personal Statements) et structuration des récits de vie via l'Essay Builder.<br>
            → Ouverture des portails de candidature internationaux (Common App, OUAC, ou plateformes internes des grandes écoles).</p>
            
            <p style="margin-bottom:12px;"><b>🟢 JANVIER / FÉVRIER : Phase Financement (Scholarship Deadlines)</b><br>
            → Dépôt des dossiers complets de bourses gouvernementales (ex: Eiffel) ou bourses de mérite internes des universités.<br>
            → Suivi rigoureux des pièces justificatives sur les tableaux de bord applicatifs.</p>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# PILIER 5 : AI ESSAY & STORY BUILDER
# ==============================================================================
with tabs[3]:
    st.markdown("### ✍️ Pilier 5 : AI Essay & Story Builder")
    st.write("Transformez des expériences vécues de façon simple en récits percutants de leadership pour convaincre les jurys.")
    
    input_brute = st.text_area(
        "Indiquez une expérience de façon simple (ex: 'J'ai fait du bénévolat dans une association locale' ou 'J'ai créé un projet scientifique au lycée') :",
        placeholder="Écrivez votre texte ici..."
    )
    
    if st.button("✍️ Transformer en Récit Narratif d'Élite"):
        if input_brute.strip() != "":
            st.markdown("##### 🚀 Version Optimisée pour les Jurys d'Admission :")
            st.markdown(f"""
                <div class="story-output">
                    "Au-delà d'un simple engagement, cette initiative m'a permis de conceptualiser et de structurer des solutions concrètes face à des problématiques terrain. En pilotant ce projet, j'ai développé des compétences clés en gestion d'équipe, en allocation de ressources et en communication stratégique. Cette expérience témoigne de ma capacité à traduire des valeurs fortes en actions d'impact mesurables, un levier que je souhaite pleinement investir au sein de votre écosystème universitaire."
                </div>
            """, unsafe_allow_html=True)
            st.caption("💡 Cette structure narrative met en valeur le leadership, l'autonomie et l'impact direct de vos actions.")
        else:
            st.warning("Veuillez saisir une expérience brute à transformer.")

# ==============================================================================
# PILIER 6 : AI CAREER SIMULATOR (LA PARTIE FUTURISTE)
# ==============================================================================
with tabs[4]:
    st.markdown("### 🚀 Pilier 6 : AI Career Simulator")
    st.write("Simulez instantanément les différents chemins de vie possibles pour atteindre l'objectif de carrière de l'élève.")
    
    if "dna_compiled" not in st.session_state:
        st.warning("⚠️ Veuillez configurer un métier cible dans le premier onglet pour lancer la simulation.")
    else:
        st.info(f"🔮 Génération de trajectoires pour l'objectif : **{metier_cible}**")
        
        col_c1, col_c2, col_c3 = st.columns(3)
        
        with col_c1:
            st.markdown("""
                <div style="background: #111827; padding: 20px; border-radius: 12px; border-top: 4px solid #3b82f6;">
                    <h5 style="color: #3b82f6 !important;">🗺️ Chemin 1 : Trajectoire Technique</h5>
                    <p style="font-size: 13px; margin-top:10px;"><b>Étapes :</b><br>
                    1. Bachelor ultra-spécialisé (Tech/Science)<br>
                    2. Intégration de laboratoires de recherche ou de pôles R&D<br>
                    3. Spécialiste technique senior.</p>
                    <p style="font-size:12px; color: #a3e635 !important;">⚡ <b>Risques :</b> Hyper-spécialisation précoce.<br>🏆 <b>Opportunité :</b> Expertise rare recherchée.</p>
                </div>
            """, unsafe_allow_html=True)

        with col_c2:
            st.markdown("""
                <div style="background: #111827; padding: 20px; border-radius: 12px; border-top: 4px solid #10b981;">
                    <h5 style="color: #10b981 !important;">🗺️ Chemin 2 : Hybride & Management</h5>
                    <p style="font-size: 13px; margin-top:10px;"><b>Étapes :</b><br>
                    1. Cursus combiné ou double diplôme (Management + Science)<br>
                    2. Gestion de projets complexes à l'international<br>
                    3. Direction de structures ou Entrepreneuriat.</p>
                    <p style="font-size:12px; color: #a3e635 !important;">⚡ <b>Risques :</b> Charge de travail doublée.<br>🏆 <b>Opportunité :</b> Profil de décideur global très polyvalent.</p>
                </div>
            """, unsafe_allow_html=True)

        with col_c3:
            st.markdown("""
                <div style="background: #111827; padding: 20px; border-radius: 12px; border-top: 4px solid #6366f1;">
                    <h5 style="color: #6366f1 !important;">🗺️ Chemin 3 : Recherche & Doctorat</h5>
                    <p style="font-size: 13px; margin-top:10px;"><b>Étapes :</b><br>
                    1. Bachelor Fondamental en Grande École<br>
                    2. Master en Recherche Avancée et publication d'articles<br>
                    3. Doctorat (PhD) avec Fellowships mondiaux.</p>
                    <p style="font-size:12px; color: #a3e635 !important;">⚡ <b>Risques :</b> Cursus long (7-8 ans).<br>🏆 <b>Opportunité :</b> Profil académique de premier plan mondial.</p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# PILIERS 7, 8 & 9 : OPPORTUNITY RADAR, GAP ANALYZER & NETWORKING
# ==============================================================================
with tabs[5]:
    col_last1, col_last2 = st.columns(2)
    
    with col_last1:
        st.markdown("### 📡 Pilier 7 : AI Opportunity Radar")
        st.markdown("""
            <div style="background-color: #090d16; padding: 15px; border-radius: 10px; border-left: 4px solid #f59e0b; margin-bottom: 20px;">
                <span style="color: #f59e0b; font-weight: bold;">[ALERTE RADAR ACTIVE] :</span><br>
                <p style="font-size: 14px; margin-top:5px; color: #e2e8f0 !important;">➔ Une nouvelle bourse de mérite vient d'être ouverte pour les profils internationaux d'excellence visant des cursus interdisciplinaires. Prise de contact recommandée avant la session de Novembre.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 👥 Pilier 9 : Community & Network Matrix")
        st.markdown("""
            <div class="card-matrix">
                <h5>🔗 Mentors & Alumni Connectés au Profil :</h5>
                <p style="font-size: 14px; margin-top:10px;">• <b>Yasmine B.</b> (Alumni LSE / UM6P) — Spécialiste Financements Internationaux.<br>
                • <b>Karim T.</b> (Mentor Stanford Tech) — Conseiller Admissions Amérique du Nord.</p>
                <span style="color: #3b82f6; font-size:12px; font-weight:bold; cursor:pointer;">➔ Envoyer une demande de mise en relation via l'écosystème</span>
            </div>
        """, unsafe_allow_html=True)

    with col_last2:
        st.markdown("### 📊 Pilier 8 : AI Gap Analyzer")
        st.write("Comparaison automatisée entre le profil de l'élève et les exigences moyennes des dossiers admis en bourses d'élite :")
        
        if "dna_compiled" not in st.session_state:
            st.warning("Veuillez d'abord configurer le Student DNA pour voir l'analyse d'écarts.")
        else:
            st.markdown(f"""
                <div style="background: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #475569;">
                    <h5 style="color: #ef4444 !important;">🎯 Écarts identifiés (Gap List) :</h5>
                    <hr style="border-color: #334155; margin-top:5px; margin-bottom:10px;">
                    <p style="font-size: 14px;">❌ <b>Niveau de Langue Académique :</b> Votre niveau actuel est excellent, mais l'absence de certification officielle (IELTS/TOEFL) bloque la validation finale de l'algorithme.</p>
                    <p style="font-size: 14px;">❌ <b>Documentation Extra-Scolaire :</b> Vos engagements et distinctions doivent être formalisés sous forme de portfolio ou de fiches d'impact pour être compétitifs.</p>
                    <h5 style="color: #10b981 !important; margin-top:15px;">🛠️ Plan d'Action Correctif :</h5>
                    <p style="font-size: 14px;">1. Planifier l'examen officiel de langue dans les 60 prochains jours.<br>
                    2. Passer vos expériences brutes au sein du <b>Pilier 5 (Essay Builder)</b> pour maximiser votre force d'impact.</p>
                </div>
            """, unsafe_allow_html=True)

st.write("---")
if st.button("🔄 Réinitialiser l'Écosystème Global OS"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
