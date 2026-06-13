import streamlit as st

# --- CONFIGURATION ARCHITECTURE IDENTITYPATH (SEO & GOOGLE INDEXING) ---
st.set_page_config(
    page_title="IdentityPath | AI Student Profiling System & Scholarship Engine",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SYSTEM DESIGN PREMIUM (DEEP DARK UI & INTERACTIVE STORY MODE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;500;600;700;800&family=Space+Grotesk:wght=500;700&display=swap');
    
    :root { 
        --bg-core: #090d16; 
        --card-bg: #111726; 
        --accent-blue: #3b82f6; 
        --accent-green: #10b981; 
        --accent-amber: #f59e0b;
    }
    
    .main { background-color: #090d16; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #090d16; font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Harmonisation globale de la visibilité des textes */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    
    /* Header Industriel IdentityPath */
    .seo-banner { text-align: left; padding: 30px; background: linear-gradient(135deg, #111827 0%, #030712 100%); border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 30px; }
    .seo-title { font-size: 38px; font-weight: 800; color: #ffffff !important; letter-spacing: -1px; }
    .seo-keywords { color: #64748b !important; font-size: 12px !important; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
    
    /* Navigation & Barrettes de Progression */
    .level-header { background: #1e293b; padding: 12px 20px; border-radius: 8px; border-left: 4px solid #3b82f6; margin-bottom: 25px; font-weight: bold; font-size: 16px !important; }
    .progress-wrapper { background: #1e293b; border-radius: 10px; height: 12px; margin-bottom: 35px; overflow: hidden; border: 1px solid #334155; }
    .progress-bar-fill { background: linear-gradient(90deg, #3b82f6, #10b981); height: 100%; transition: width 0.4s ease-in-out; }
    
    /* Conteneurs de Données & Cartes d'Analyse */
    .dna-container { background: #111726; padding: 25px; border-radius: 16px; border: 1px solid #1f2937; margin-bottom: 25px; }
    .output-card { background: #030712; padding: 25px; border-radius: 14px; border: 1px solid #1e2937; margin-bottom: 20px; line-height: 1.6; }
    .output-card.prime { border-left: 5px solid #10b981; background: linear-gradient(180deg, #111726 0%, #0d1321 100%); }
    .output-card.scholarship { border-left: 5px solid #3b82f6; }
    .output-card.warning { border-left: 5px solid #f59e0b; }
    
    /* Badges UI */
    .dna-badge { background: rgba(59, 130, 246, 0.12); color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.25); padding: 5px 14px; border-radius: 8px; font-size: 13px !important; display: inline-block; margin-right: 8px; margin-top: 8px; font-weight: 600; }
    .salary-tag { background: rgba(16, 185, 129, 0.15); color: #10b981 !important; border: 1px solid rgba(16, 185, 129, 0.4); padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 15px !important; display: inline-block; margin-top: 5px; }
    .prob-tag { float: right; background: #1f2937; color: #ffffff !important; border: 1px solid #374151; padding: 4px 12px; border-radius: 20px; font-size: 13px !important; font-weight: bold; }
    
    /* Bouton d'Action Principal Universel */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 12px !important; padding: 16px 32px !important; border: none !important; width: 100%; font-size: 16px !important; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.25); transition: all 0.2s ease; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.35); }
    </style>
""", unsafe_allow_html=True)

# --- BANNIÈRE DE MARQUE IDENTITYPATH ---
st.markdown("""
    <div class="seo-banner">
        <div class="seo-title">🧭 IDENTITYPATH OS</div>
        <div class="seo-keywords">AI Career Guidance • Student Profiling System • Scholarship Matching AI • University Pathway Blueprint</div>
    </div>
""", unsafe_allow_html=True)

# --- DOUBLE SÉCURITÉ DE LA PLATFORME ---
if "auth_verified" not in st.session_state: st.session_state.auth_verified = False
if not st.session_state.auth_verified:
    c_l, c_m, c_r = st.columns([1, 1.8, 1])
    with c_m:
        st.markdown("<h4 style='text-align: center; margin-bottom: 20px;'>🔐 Accessing IdentityPath Core Matrix</h4>", unsafe_allow_html=True)
        pwd = st.text_input("Enter Jumper Security Token :", type="password")
        if pwd == "Arwagiftorient":
            if st.button("Boot Profiling Engine ⚡"):
                st.session_state.auth_verified = True
                st.rerun()
    st.stop()

# --- INITIALISATION DES VARIABLES ET ÉTAPES ---
if "current_level" not in st.session_state: st.session_state.current_level = 1
if "dna_vault" not in st.session_state: st.session_state.dna_vault = {}

# CALCUL ET AFFICHAGE DE LA BARRE DE PROGRESSION EN TEMPS RÉEL
progress_percent = (st.session_state.current_level - 1) * 33.33
if st.session_state.current_level == 4: progress_percent = 100.0

st.markdown(f"""
    <div style="margin-bottom: 6px; font-weight: bold; font-size: 13px; color: #94a3b8; letter-spacing: 0.5px;">PROFILING TASK COMPLETION : {int(progress_percent)}%</div>
    <div class="progress-wrapper">
        <div class="progress-bar-fill" style="width: {progress_percent}%;"></div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# LEVEL 1: IDENTITY LAYER
# ==============================================================================
if st.session_state.current_level == 1:
    st.markdown("<div class='level-header'>🎮 LEVEL 1: Who Are You? (Basic Identity Layer)</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Âge actuel de l'étudiant :", ["15 ans", "16 ans", "17 ans", "18 ans", "19 ans+"])
        location = st.text_input("Pays / Ville de résidence actuel :", value="Maroc, Casablanca")
    with col2:
        scolaire = st.selectbox("Niveau scolaire actuel (Crucial) :", [
            "Collège (3ème / Préparation Lycée)",
            "Lycée : Troncs Communs / 10ème année",
            "Lycée : 1ère année Bac / Penultimate Year",
            "Lycée : 2ème année Bac / Terminale",
            "Étudiant Universitaire (En quête de réorientation)"
        ])
        filiere = st.selectbox("Filière académique actuelle ou visée :", [
            "Sciences Mathématiques (A / B)", 
            "Sciences Physiques / Expérimentales", 
            "Sciences Économiques & Gestion", 
            "Technologies / Informatique / STE"
        ])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Unlock Level 2: Academic Profile ➡️"):
        st.session_state.dna_vault.update({"age": age, "location": location, "scolaire": scolaire, "filiere": filiere})
        st.session_state.current_level = 2
        st.rerun()

# ==============================================================================
# LEVEL 2: ACADEMIC & LANGUAGE MATRIX
# ==============================================================================
elif st.session_state.current_level == 2:
    st.markdown("<div class='level-header'>🎮 LEVEL 2: Your Skills (Academic & Language Matrix)</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    
    st.write("📊 **Auto-évaluation des blocs de compétences majeurs :**")
    c1, c2, c3 = st.columns(3)
    with c1:
        feel_math = st.selectbox("Aisance en Mathématiques :", ["Excellent (Facile / Esprit Logique)", "Moyen (Travailleur / Stable)", "Difficile (Lacunes / Points faibles)"])
    with c2:
        feel_physics = st.selectbox("Aisance en Sciences / Physique / SVT :", ["Excellent (Facile / Passionné)", "Moyen (Stable / Maîtrisé)", "Difficile (Complexe / Laborieux)"])
    with c3:
        note_lycee = st.slider("Moyenne générale estimée ou visée au Bac (sur 20) :", 10.0, 20.0, 16.5, step=0.1)
        
    st.write("---")
    st.write("🌐 **Matrice des Langues (Standard International CECRL) :**")
    cl1, cl2, cl3 = st.columns(3)
    with cl1:
        lang_en = st.selectbox("Niveau d'Anglais (IELTS/TOEFL visé) :", ["C2 (Bilingue / Fluide)", "C1 (Avancé / Professionnel)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)"])
    with cl2:
        lang_fr = st.selectbox("Niveau de Français (TCF/DELF acquis) :", ["C2 (Bilingue / Maternel)", "C1 (Avancé / Fluide)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)"])
    with cl3:
        lang_ar = st.selectbox("Niveau d'Arabe (Langue d'étude/Maternelle) :", ["C2 (Bilingue)", "C1 (Avancé)", "B2 (Maîtrisé)", "B1 (Basique)"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Unlock Level 3: Direction & Goals ➡️"):
        st.session_state.dna_vault.update({
            "math": feel_math, "physics": feel_physics, "note": note_lycee,
            "en": lang_en, "fr": lang_fr, "ar": lang_ar
        })
        st.session_state.current_level = 3
        st.rerun()

# ==============================================================================
# LEVEL 3: FUTURE DIRECTION & CONSTRAINTS
# ==============================================================================
elif st.session_state.current_level == 3:
    st.markdown("<div class='level-header'>🎮 LEVEL 3: Future Direction (Interests, Personality & Constraints)</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns(2)
    
    with col_i1:
        domaines = st.multiselect("🎯 Sélectionne tes domaines d'intérêt majeurs (Combine pour affiner) :", [
            "IA / Tech / Computer Science", 
            "Architecture / Design / Urbanisme", 
            "Médecine / Biotechnologies / Santé", 
            "Environnement / Développement Durable / Écosystèmes", 
            "Business / Entrepreneuriat / Stratégie"
        ], default=["Médecine / Biotechnologies / Santé", "Environnement / Développement Durable / Écosystèmes"])
        
        objectifs = st.radio("🏁 Quel est ton objectif de parcours ultime ?", [
            "Obtenir une bourse d'étude complète (100%) à l'international",
            "Intégrer une Université Mondiale de prestige (Élite)",
            "Bâtir des projets concrets, innover et focus Entrepreneuriat / Startup",
            "Maximiser les opportunités d'accès d'Excellence au Maroc (UM6P, ENA, FMP...)"
        ])
        
    with col_i2:
        perso = st.radio("🧠 Philosophie et style de travail préféré :", [
            "Je suis un 'Builder' : J'aime l'action concrète, tester, échouer et reconstruire",
            "Je suis un 'Chercheur' : J'aime la théorie pure, l'analyse approfondie et les concepts"
        ])
        
        budget = st.selectbox("💰 Profil de prise en charge financière :", [
            "Contrainte forte (Bourse d'étude complète obligatoire)",
            "Prise en charge partielle (Frais logistiques ou scolarité partielle gérable)",
            "Autonomie financière complète (Pas de contraintes de budget)"
        ])
        
        mobilite = st.radio("✈️ Périmètre de mobilité géographique :", [
            "Ouverture totale (Europe, Amérique, Moyen-Orient, Asie)",
            "Focus territorial strict (Rester et exceller au Maroc)"
        ])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("⚡ Run Deep AI Mapping & Diagnostics 🚀"):
        st.session_state.dna_vault.update({
            "domaines": domaines, "objectifs": objectifs, 
            "perso": perso, "budget": budget, "mobilite": mobilite
        })
        st.session_state.current_level = 4
        st.rerun()

# ==============================================================================
# LEVEL 4: INTERACTIVE INTELLIGENT EXPERT REPORT (3ALLAL ENGINE V3)
# ==============================================================================
elif st.session_state.current_level == 4:
    st.markdown("<div class='level-header'>🏁 LEVEL 4: 3allal Profile Unlock & High-Fidelity Blueprint Report</div>", unsafe_allow_html=True)
    
    v = st.session_state.dna_vault
    note_eleve = v["note"]
    filiere_eleve = v["filiere"]
    scolaire_eleve = v["scolaire"]
    interets_join = " // ".join(v["domaines"])
    
    # INITIALISATION DE LA BASE DE CONNAISSANCES DE L'ALGORITHME DE DÉCISION
    filiere_label = "Filière Multidisciplinaire sur-mesure"
    filiere_desc = "Analyse croisée en cours."
    universites = []
    bourses = []
    salaire_label = "Sur-mesure"
    action_specifique = ""

    # --- SCÉNARIO HYBRIDE MAJEUR : MÉDECINE / SANTÉ + ENVIRONNEMENT ---
    if "Médecine" in interets_join and "Environnement" in interets_join:
        filiere_label = "Santé Environnementale, Éco-Biotechnologies & Gestion des Écosystèmes Fragiles"
        filiere_desc = "Cette trajectoire d'élite combine les sciences médicales avancées avec la préservation écologique. Elle cible le développement de solutions de filtration biologique, la lutte contre l'éco-toxicologie moléculaire et la réhabilitation des zones humides ou écosystèmes côtiers menacés."
        universites = [
            "Wageningen University & Research (Pays-Bas) — Numéro 1 mondial en Sciences de l'Environnement et Agriculture.",
            "KAUST (King Abdullah University of Science and Technology) — Laboratoires de pointe sur les écosystèmes côtiers de la Mer Rouge et biosciences.",
            "Université de Montpellier (France) — Pôle d'excellence européen en Éco-toxicologie et Biotechnologies Marines.",
            "UM6P (Université Mohammed VI Polytechnique - Maroc) — Green Tech Institute (GTI) & School of Agriculture, Fertilization & Environmental Sciences."
        ]
        bourses = [
            "Bourse d'Excellence Complète KAUST : Financement à 100% (Scolarité, hébergement de haut standing, couverture médicale complète et allocation mensuelle).",
            "Bourse d'Excellence UM6P : Exonération totale ou partielle des frais de scolarité calculée sur le mérite académique et les critères socio-économiques.",
            "Bourses d'Excellence Orange / Fondation Sanady : Programmes de soutien aux innovateurs marocains de filières scientifiques.",
            "Bourses d'Étude du Gouvernement Hollandais (Orange Knowledge Programme) : Pour les filières de durabilité de l'eau et de biosciences."
        ]
        salaire_label = "55,000$ à 135,000$ / an"
        action_specifique = "Concocter un dossier axé sur l'impact en créant ou documentant un prototype d'intégration écologique (ex: traitement de sédiments ou bio-filtration par charbon actif). C'est la clé absolue pour prouver ta valeur de 'Builder'."

    # --- SCÉNARIO MAJEUR : IA / TECH / COMPUTER SCIENCE ---
    elif "IA / Tech" in interets_join:
        filiere_label = "Intelligence Artificielle, Cloud Architecture & Computer Science"
        filiere_desc = "Spécialisation de haut niveau axée sur la création d'algorithmes prédictifs, le traitement de grands volumes de données (Data Science) et le déploiement d'applications intelligentes appliquées à des problématiques industrielles ou sociétales."
        universites = [
            "NUS (National University of Singapore) — Leader asiatique incontesté de l'innovation logicielle.",
            "EPFL (École Polytechnique Fédérale de Lausanne - Suisse) — Hub mondial d'ingénierie et de systèmes intelligents.",
            "University of Waterloo (Canada) — Réputée pour ses programmes de Co-op en ingénierie logicielle avec la Silicon Valley.",
            "Écosystème 1337 / UM6P (Maroc) — Codage en peer-to-peer sans professeur, axé sur l'autonomie pure."
        ]
        bourses = [
            "Bourse SINGA (Singapore International Graduate Award) : Prise en charge intégrale des frais et de la vie sur place.",
            "Bourse d'Excellence de l'EPFL : Destinée aux profils académiques internationaux hors du commun.",
            "Prise en charge intégrale de l'écosystème 1337 (Gratuité totale de la formation et accès aux infrastructures de pointe)."
        ]
        salaire_label = "70,000$ à 165,000$ / an"
        action_specifique = "Développer, tester et déployer ton propre script d'automatisation ou un MVP (Minimum Viable Product) en Python sur le web. Rien ne vaut une URL fonctionnelle pour clouer le bec aux recruteurs."

    # --- SCÉNARIO MAJEUR : ARCHITECTURE / DESIGN / URBANISME ---
    elif "Architecture" in interets_join:
        filiere_label = "Architecture Durable, Conception Bioclimatique & Urbanisme Intelligent"
        filiere_desc = "Discipline à l'intersection de la création artistique graphique et de l'ingénierie civile. Elle vise à repenser les espaces de vie, optimiser l'efficacité énergétique des bâtiments et planifier les Smart Cities de demain."
        universites = [
            "Politecnico di Milano (Italie) — Une des plus anciennes et prestigieuses universités d'Europe en architecture et design.",
            "METU (Middle East Technical University - Turquie) — Excellence académique anglophone de premier plan.",
            "Écoles Nationales d'Architecture (ENA Maroc) — Le réseau d'État de référence pour le diplôme d'architecte national."
        ]
        bourses = [
            "Bourse Türkiye Bursları : Financement complet par l'État turc (Logement, scolarité, cours de langue et billet d'avion).",
            "Bourses du Gouvernement Italien (MAECI) : Allocations d'études pour les étudiants étrangers d'excellence.",
            "Bourses de mérite interne des Réseaux Nationaux d'Ingénierie."
        ]
        salaire_label = "45,000$ à 110,000$ / an"
        action_specifique = "Rassembler tes créations, croquis d'espace et designs numériques dans un portfolio visuel hautement réaliste et authentique. C'est l'atout numéro 1 exigé par les jurys internationaux."

    # --- SCÉNARIO PAR DÉFAUT / BUSINESS & STRATÉGIE ---
    else:
        filiere_label = "International Business Management, Finance & Data Strategy"
        filiere_desc = "Parcours orienté vers la direction d'entreprise, la modélisation financière, l'analyse stratégique des marchés internationaux et l'entrepreneuriat technologique."
        universites = [
            "FGSES (Faculty of Governance, Economic and Social Sciences - UM6P Maroc) — Pôle d'excellence en politiques publiques et économie.",
            "HEC Lausanne (Suisse) — Faculté des Hautes Études Commerciales de réputation internationale.",
            "ESCP Business School (Campus de Paris / Berlin / Londres) — Top Business School mondiale."
        ]
        bourses = [
            "Bourse de la Fondation Al Ghurair : Financement destiné aux étudiants arabes performants dans les universités partenaires.",
            "Bourse d'Excellence FGSES / UM6P : Couverture adaptée selon le profil d'entrée de l'élève.",
            "Bourses de Mobilité Erasmus+ de l'Union Européenne."
        ]
        salaire_label = "50,000$ à 125,000$ / an"
        action_specifique = "Modéliser le Business Model complet d'une structure ou d'une coopérative réelle pour prouver ton aptitude à optimiser la connectivité commerciale et l'impact opérationnel."

    # CALCUL DU SCORE DE CONFIANCE ADMISSIBILITÉ (CORRÉLATION DE LA MOYENNE)
    chances_calcul = min(int(note_eleve * 4.8), 98)

    # AFFICHAGE DU PANNEAU DE RÉSULTATS INTERACTIFS
    col_d1, col_d2 = st.columns([1.3, 2])
    
    with col_d1:
        st.markdown("### 🧬 AI Student DNA Signature")
        st.markdown(f"""
            <div class="dna-container" style="border-top: 4px solid #3b82f6;">
                <p style="font-size: 12px; color:#94a3b8 !important; margin:0; font-family:'Space Grotesk'; text-transform:uppercase; letter-spacing:1px;">Verified Platform Output</p>
                <div style="margin-top:15px;">
                    <div class="dna-badge">Niveau : {scolaire_eleve}</div>
                    <div class="dna-badge">Secteur d'étude : {filiere_eleve}</div>
                    <div class="dna-badge">Performance : {note_eleve}/20</div>
                    <div class="dna-badge">English Track : {v['en']}</div>
                    <div class="dna-badge">French Track : {v['fr']}</div>
                    <div class="dna-badge">Arabic Track : {v['ar']}</div>
                    <div class="dna-badge">Philosophie : Action & Building</div>
                    <div class="dna-badge">Financement : {v['budget']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_d2:
        st.markdown("### 🔮 Cartographie & Trajectoire de Carrière")
        st.markdown(f"""
            <div class="output-card prime">
                <span class="prob-tag">Indice Admissibilité : {chances_calcul}%</span>
                <h4 style="margin:0; color:#10b981 !important;">🎯 Orienté : {filiere_label}</h4>
                <p style="font-size:14px; margin-top:10px; color:#e2e8f0 !important;">{filiere_desc}</p>
                
                <div style="margin-top:18px; background:rgba(255,255,255,0.02); padding:15px; border-radius:10px; border: 1px solid rgba(255,255,255,0.06);">
                    <span style="font-size:12px; color:#38bdf8; text-transform:uppercase; font-weight:bold; letter-spacing:0.5px;">🏫 Liste des Universités Cibles Recommandées :</span>
                    <ul style="margin-top:8px; padding-left:20px; font-size:14px; color:#ffffff !important;">
                        {"".join([f"<li style='margin-bottom:6px;'>{uni}</li>" for uni in universites])}
                    </ul>
                </div>
                
                <div style="margin-top:15px;">
                    <span style="font-size:13px; color:#94a3b8;">Estimation Potentiel Salaire International :</span><br>
                    <div class="salary-tag">💰 {salaire_label}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🎓 Moteur d'Appariement d'Aides Financières & Bourses (Scholarship Matching)")
    st.markdown(f"""
        <div class="output-card scholarship">
            <h5 style="color:#3b82f6 !important; margin:0; font-size:16px;">✨ Programmes de Bourses d'Études Détectés (Compatibilité {chances_calcul}%) :</h5>
            <p style="font-size:14px; color:#94a3b8; margin-top:4px;">Filtre appliqué basé sur la contrainte financière : <i>"{v['budget']}"</i></p>
            <ul style="margin-top:12px; font-size:14px; padding-left:20px; line-height:1.7;">
                {"".join([f"<li style='margin-bottom:10px;'><b>{bourse.split(' : ')[0]}</b> : {bourse.split(' : ')[1] if len(bourse.split(' : ')) > 1 else ''}</li>" for bourse in bourses])}
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧭 GPS Diagnostic & Feuille de Route Stratégique")
    st.markdown(f"""
        <div class="output-card warning">
            <h5 style="color:#f59e0b !important; margin:0; font-size:16px;">🚨 AI Reality Check par 3allal :</h5>
            <p style="font-size:15px; margin-top:10px; color:#e2e8f0 !important;">
                "Écoute bien : afficher une moyenne de <b>{note_eleve}/20</b> au lycée est un excellent passeport académique. Mais pour te démarquer des milliers de dossiers mondiaux et briser la barrière de ton profil financier (<i>{v['budget']}</i>), la théorie ne suffira jamais. Les comités d'admission des bourses d'élite cherchent des étudiants qui construisent, qui testent et qui créent un impact mesurable.<br><br>
                <b>Ta priorité absolue dès maintenant :</b><br>
                👉 {action_specifique}<br><br>
                <b>Planification Temporelle :</b> Ne te laisse pas surprendre. Fixe et passe tes examens de compétences linguistiques officiels (IELTS pour l'Anglais / TCF pour le Français) dès l'automne afin de blinder ton dossier pour le cycle d'application international 2026-2027."
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    if st.button("🔄 Lancer une nouvelle simulation de profil d'étudiant"):
        st.session_state.current_level = 1
        st.session_state.dna_vault = {}
        st.rerun()
        
