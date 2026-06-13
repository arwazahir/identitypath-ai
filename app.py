import streamlit as st

# --- CONFIGURATION ARCHITECTURE IDENTITYPATH AI (SEO ENGINES) ---
st.set_page_config(
    page_title="IdentityPath AI | Global Student Profiling & Scholarship Matrix",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SYSTEM DESIGN ULTRA-PREMIUM (FLUID DEEP DARK UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;500;600;700;800&family=Space+Grotesk:wght=500;700&display=swap');
    
    :root { 
        --bg-core: #060a12; 
        --card-bg: #0b111e; 
        --accent-blue: #2563eb; 
        --accent-green: #059669; 
        --accent-amber: #d97706;
    }
    
    .main { background-color: #060a12; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #060a12; font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Global Text Visibility */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    
    /* Branding Banner & Google SEO Meta-Hooks */
    .seo-banner { text-align: left; padding: 30px; background: linear-gradient(135deg, #0f172a 0%, #020617 100%); border-radius: 16px; border: 1px solid #1e293b; margin-bottom: 30px; }
    .seo-title { font-size: 40px; font-weight: 800; color: #ffffff !important; letter-spacing: -1px; font-family: 'Space Grotesk'; }
    .seo-keywords { color: #475569 !important; font-size: 11px !important; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 5px; font-weight: 600; }
    
    /* Dynamic Layout Components */
    .level-header { background: #1e293b; padding: 14px 22px; border-radius: 10px; border-left: 4px solid #2563eb; margin-bottom: 25px; font-weight: 700; font-size: 17px !important; }
    .progress-wrapper { background: #1e293b; border-radius: 10px; height: 8px; margin-bottom: 35px; overflow: hidden; }
    .progress-bar-fill { background: linear-gradient(90deg, #2563eb, #059669); height: 100%; transition: width 0.5s ease; }
    
    .dna-container { background: #0b111e; padding: 25px; border-radius: 16px; border: 1px solid #1e293b; margin-bottom: 25px; }
    .output-card { background: #020617; padding: 25px; border-radius: 14px; border: 1px solid #1e293b; margin-bottom: 20px; line-height: 1.6; }
    .output-card.prime { border-left: 5px solid #059669; background: linear-gradient(180deg, #0b111e 0%, #070c16 100%); }
    .output-card.scholarship { border-left: 5px solid #2563eb; }
    .output-card.warning { border-left: 5px solid #d97706; }
    
    .dna-badge { background: rgba(37, 99, 235, 0.12); color: #60a5fa !important; border: 1px solid rgba(96, 165, 250, 0.25); padding: 6px 14px; border-radius: 8px; font-size: 13px !important; display: inline-block; margin-right: 8px; margin-top: 8px; font-weight: 600; }
    .salary-tag { background: rgba(5, 150, 105, 0.15); color: #34d399 !important; border: 1px solid rgba(52, 211, 153, 0.4); padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 15px !important; display: inline-block; margin-top: 5px; }
    .prob-tag { float: right; background: #1e293b; color: #ffffff !important; border: 1px solid #334155; padding: 4px 12px; border-radius: 20px; font-size: 13px !important; font-weight: bold; }
    
    /* Interactive Fluid Buttons */
    .stButton>button { background: linear-gradient(90deg, #2563eb, #059669) !important; color: #ffffff !important; font-weight: 700 !important; border-radius: 12px !important; padding: 16px 32px !important; border: none !important; width: 100%; font-size: 16px !important; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2); transition: all 0.2s ease; }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(5, 150, 105, 0.3); }
    </style>
""", unsafe_allow_html=True)

# --- GOOGLE SEARCH INDEXING OPTIMIZATION OVERLAYS ---
# Ce bloc injecte des métadonnées invisibles lues par les robots Google pour indexer "IdentityPath" et "IdentityPath AI" au top des résultats.
st.markdown("""
    <div style="display:none;">
        <h1>IdentityPath AI</h1>
        <h2>IdentityPath Student Profiling Matrix and Scholarship Search Engine</h2>
        <p>The official IdentityPath AI platform for global university matching, career guidance, and premium orientation mapping.</p>
    </div>
""", unsafe_allow_html=True)

# --- BANNIÈRE PRINCIPALE ---
st.markdown("""
    <div class="seo-banner">
        <div class="seo-title">🧭 IDENTITYPATH AI</div>
        <div class="seo-keywords">Official Guidance Engine • Advanced Student DNA Profiling • Global Scholarship Data-Matrix</div>
    </div>
""", unsafe_allow_html=True)

# --- ZONE D'ACCÈS DU CODE PROMO (JUMPER TOKEN 0$) ---
if "auth_verified" not in st.session_state: st.session_state.auth_verified = False
if not st.session_state.auth_verified:
    c_l, c_m, c_r = st.columns([1, 1.8, 1])
    with c_m:
        st.markdown("""
            <div class='dna-container' style='text-align: center;'>
                <h4 style='margin-bottom: 10px;'>🔐 Activate IdentityPath Premium Access</h4>
                <p style='color: #94a3b8 !important; font-size: 14px !important;'>Enter your exclusive 100% OFF promotional voucher code ($0) below to unlock the full AI matrix.</p>
            </div>
        """, unsafe_allow_html=True)
        pwd = st.text_input("Voucher Promo Code / Jumper Security Token :", type="password", placeholder="Enter your $0 access token...")
        if pwd == "Arwagiftorient":
            if st.button("Apply Promo Code & Boot Matrix ⚡"):
                st.session_state.auth_verified = True
                st.rerun()
        elif pwd != "":
            st.error("Invalid voucher token code. Please check your credentials.")
    st.stop()

# --- INITIALISATION DES DESIGNS DE SESSIONS ---
if "current_level" not in st.session_state: st.session_state.current_level = 1
if "dna_vault" not in st.session_state: st.session_state.dna_vault = {}

progress_percent = (st.session_state.current_level - 1) * 33.33
if st.session_state.current_level == 4: progress_percent = 100.0

st.markdown(f"""
    <div style="margin-bottom: 6px; font-weight: bold; font-size: 13px; color: #64748b; letter-spacing: 0.5px;">PROFILING INTELLIGENCE PROGRESSION : {int(progress_percent)}%</div>
    <div class="progress-wrapper"><div class="progress-bar-fill" style="width: {progress_percent}%;"></div></div>
""", unsafe_allow_html=True)

# ==============================================================================
# LEVEL 1: PROFILE STRUCTURING LAYER
# ==============================================================================
if st.session_state.current_level == 1:
    st.markdown("<div class='level-header'>🎮 LEVEL 1: Academic Identity & Geographic Boundaries</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Âge de l'étudiant :", ["15 ans", "16 ans", "17 ans", "18 ans", "19 ans+"])
        location = st.text_input("Pays et Ville de résidence actuelle :", value="Maroc, Casablanca")
    with col2:
        scolaire = st.selectbox("Niveau scolaire actuel de l'apprenant :", ["Collège", "Lycée : Troncs Communs", "Lycée : 1ère année Bac (Penultimate Year)", "Lycée : 2ème année Bac (Terminale)", "Étudiant d'Enseignement Supérieur"])
        filiere = st.selectbox("Filière d'études ou spécialisation actuelle :", ["Sciences Mathématiques", "Sciences Physiques / Expérimentales", "Sciences Économiques & Gestion", "Sciences Technologiques / Informatique"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Analyze & Unlock Level 2 ➡️"):
        st.session_state.dna_vault.update({"age": age, "location": location, "scolaire": scolaire, "filiere": filiere})
        st.session_state.current_level = 2
        st.rerun()

# ==============================================================================
# LEVEL 2: METRIC & PERFORMANCE MATRIX
# ==============================================================================
elif st.session_state.current_level == 2:
    st.markdown("<div class='level-header'>🎮 LEVEL 2: Grade Capital & Multi-Language Matrix</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: feel_math = st.selectbox("Niveau d'aisance - Bloc Mathématiques :", ["Excellent (Esprit analytique/logique)", "Moyen (Travailleur/Stable)", "Difficile (Besoins de bases)"])
    with c2: feel_physics = st.selectbox("Niveau d'aisance - Bloc Sciences & Expérimentation :", ["Excellent (Passionné)", "Moyen (Maîtrisé)", "Difficile (Complexe)"])
    with c3: note_lycee = st.slider("Moyenne générale (Actuelle ou Visée au Baccalauréat) :", 10.0, 20.0, 17.5, step=0.1)
    st.write("---")
    st.markdown("🌐 **Évaluation Linguistique Standardisée (CECRL) :**")
    cl1, cl2, cl3 = st.columns(3)
    with cl1: lang_en = st.selectbox("Anglais (IELTS / TOEFL visé) :", ["C2 (Bilingue / Fluide)", "C1 (Avancé)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)"])
    with cl2: lang_fr = st.selectbox("Français (TCF / DELF acquis) :", ["C2 (Bilingue / Maternel)", "C1 (Avancé)", "B2 (Intermédiaire)", "B1 (Basique)"])
    with cl3: lang_ar = st.selectbox("Arabe (Langue maternelle / d'étude) :", ["C2 (Bilingue)", "C1 (Avancé)", "B2 (Maîtrisé)"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Process Metrics & Unlock Level 3 ➡️"):
        st.session_state.dna_vault.update({"math": feel_math, "physics": feel_physics, "note": note_lycee, "en": lang_en, "fr": lang_fr, "ar": lang_ar})
        st.session_state.current_level = 3
        st.rerun()

# ==============================================================================
# LEVEL 3: DYNAMIC INTENT & KEYWORD ENGINE
# ==============================================================================
elif st.session_state.current_level == 3:
    st.markdown("<div class='level-header'>🎮 LEVEL 3: Deep Ambitions, Skills Preferences & Mindset Text Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    
    st.markdown("##### 🎯 Déclaration d'Intérêts Multi-Champs")
    domaines = st.multiselect("Sélectionne tes grands secteurs d'affinité (Combine plusieurs choix libres pour croiser les données) :", [
        "Création, Design, Arts & Architecture",
        "Informatique, Tech, IA & Software Engineering",
        "Business, Stratégie, Entrepreneuriat & Finance",
        "Gouvernance, Économie, Sciences Politiques & Sociales",
        "Ingénierie, Sciences Physiques, Énergie & Mécanique",
        "Médecine, Biosciences, Santé & Éco-Systèmes"
    ], default=["Création, Design, Arts & Architecture"])
    
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        objectifs = st.radio("Quel est le vecteur de réussite recherché ?", [
            "Décrocher une Bourse d'Étude Internationale Complète (100% de prise en charge)",
            "Viser l'Excellence Académique Pure au sein des Universités Mondiales d'Élite",
            "Créer l'impact direct : Focus Bâtir des Projets Concrets & Entrepreneuriat / Startup",
            "Parcours de Haute Performance Territorial au Maroc (UM6P, Réseaux d'État Élite, FMP, ENA)"
        ])
        budget = st.selectbox("Profil de Prise en Charge Économique :", ["Bourse complète obligatoire", "Co-financement / Prise en charge partielle", "Autonomie financière totale"])
    with col_i2:
        perso = st.radio("Philosophie opérationnelle préférée :", ["Je suis un 'Builder' (Créer du concret, tester, échouer, rebâtir)", "Je suis un 'Chercheur' (Analyse conceptuelle, recherche théorique)"])
        mobilite = st.radio("Périmètre Géographique Souhaité :", ["Ouverture Internationale Globale (Europe, Amérique, Moyen-Orient, Asie)", "Focus Territorial Précis (Maroc uniquement)"])
    
    st.write("---")
    st.markdown("##### 🧠 Moteur sémantique textuel : Que veux-tu accomplir ? (Saisie libre)")
    user_keywords = st.text_area(
        "Décris ici avec tes propres mots ce que tu aimes faire, créer ou étudier (ex: 'j'aime dessiner des plans, coder des scripts, organiser des projets, aider les coopératives, le design graphique...'). Notre IA va scanner chaque mot pour mapper ton profil :",
        placeholder="Tape ton texte ici..."
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("⚡ Run IdentityPath Multi-Field Semantic Analysis 🚀"):
        st.session_state.dna_vault.update({"domaines": domaines, "objectifs": objectifs, "perso": perso, "budget": budget, "mobilite": mobilite, "keywords": user_keywords.lower()})
        st.session_state.current_level = 4
        st.rerun()

# ==============================================================================
# LEVEL 4: THE BIG DATA DYNAMIC MAPPING MATRIX (NO EXAMPLES - ALL FIELDS)
# ==============================================================================
elif st.session_state.current_level == 4:
    st.markdown("<div class='level-header'>🏁 LEVEL 4: Comprehensive AI Keyword Scan & Multi-Pathway Match Report</div>", unsafe_allow_html=True)
    v = st.session_state.dna_vault
    
    # SYSTEME D'ANALYSE PAR MOTS-CLÉS (KEYWORD SEMANTIC ENGINE)
    # L'algorithme scanne chaque lettre et mot entrés pour déceler les ambitions cachées de l'élève.
    kw = v["keywords"]
    detected_tracks = list(v["domaines"])
    
    # Injection automatique si détection sémantique par mot-clé
    if "code" in kw or "script" in kw or "informatique" in kw or "python" in kw or "ia" in kw or "tech" in kw:
        if "Informatique, Tech, IA & Software Engineering" not in detected_tracks:
            detected_tracks.append("Informatique, Tech, IA & Software Engineering")
    if "dessin" in kw or "plan" in kw or "architecture" in kw or "design" in kw or "art" in kw or "graphique" in kw:
        if "Création, Design, Arts & Architecture" not in detected_tracks:
            detected_tracks.append("Création, Design, Arts & Architecture")
    if "business" in kw or "entreprise" in kw or "finance" in kw or "startup" in kw or "coopérative" in kw:
        if "Business, Stratégie, Entrepreneuriat & Finance" not in detected_tracks:
            detected_tracks.append("Business, Stratégie, Entrepreneuriat & Finance")

    # BASE DE DONNÉES GLOBALE (THE CORE BIG DATASET FOR MATCHING DOZENS OF UNIVERSITIES)
    database = {
        "Création, Design, Arts & Architecture": {
            "title": "Architecture, Arts Graphiques, Design Computationnel & Urbanisme Durable",
            "branches": ["• Architecture d'Intérieur & Scénographie", "• Urbanisme Durable et Smart Cities", "• Design Graphique Numérique et UI/UX Design", "• Beaux-Arts, Stylisme et Arts Visuels", "• Computational Structural Design"],
            "global_unis": [
                "• Politecnico di Milano (Italie) — Référence mondiale en design et architecture.",
                "• TU Delft (Pays-Bas) — Top mondial en ingénierie d'espace et urbanisme bas-carbone.",
                "• Middle East Technical University (METU - Turquie) — Excellence anglophone reconnue.",
                "• University of the Arts London (UAL - UK) — Leader d'Europe pour les arts créatifs et le graphisme.",
                "• Pratt Institute / Parsons School of Design (New York, USA) — Hub d'innovation visuelle.",
                "• Kyoto Institute of Technology (Japon) — Design traditionnel croisé avec l'innovation.",
                "• ETH Zürich (Suisse) — Département d'Architecture de très haut standing scientifique.",
                "• National University of Singapore (NUS) — Architecture tropicale et planification urbaine.",
                "• McGill University (Canada) — School of Architecture (Programmes d'excellence)."
            ],
            "maroc_unis": [
                "• Écoles Nationales d'Architecture (Réseau ENA : Rabat, Fès, Tétouan, Marrakech, Agadir, Oujda).",
                "• School of Architecture, Planning and Design (SAP+D - UM6P Benguerir).",
                "• École Supérieure des Arts Visuels de Marrakech (ESAV) — Arts numériques et graphisme.",
                "• Académie des Arts Traditionnels (Casablanca) — Ingénierie du patrimoine."
            ],
            "scholarships": [
                "• Bourse Complète Türkiye Bursları : Scolarité intégrale, hébergement, cours de langue et transport aérien.",
                "• Bourse d'Excellence Italienne (MAECI) : Allocations d'études pour les cursus premium de design.",
                "• Bourse de Mérite Académique SAP+D / UM6P : Exonération totale ou partielle selon revenus et dossier.",
                "• Bourses d'Excellence du British Council (Great Scholarships) : Pour les filières créatives au Royaume-Uni."
            ],
            "salary": "45,000$ à 120,000$ / an",
            "roadmap": "Bâtir d'urgence un portfolio numérique hautement réaliste et authentique regroupant tes projets, maquettes ou créations visuelles. C'est la pièce maîtresse exigée par les comités."
        },
        "Informatique, Tech, IA & Software Engineering": {
            "title": "Computer Science, Intelligence Artificielle, Data Science & Cloud Engineering",
            "branches": ["• Génie Logiciel & Applications Distribuées", "• Machine Learning & Algorithmique Prédictive", "• Cybersécurité Avancée et Cryptographie", "• Cloud Architecture & DevOps Engineering", "• Informatique Quantique"],
            "global_unis": [
                "• MIT (Massachusetts Institute of Technology - USA) — L'élite mondiale absolue du code.",
                "• National University of Singapore (NUS) — Hub technologique majeur d'Asie.",
                "• EPFL (Lausanne, Suisse) — Centre européen majeur en systèmes intelligents.",
                "• University of Waterloo (Canada) — Réputée pour ses stages Co-op intégrés dans la Silicon Valley.",
                "• Tsinghua University (Chine) — Leader d'Asie en recherche d'algorithmes et IA.",
                "• KAUST (Arabie Saoudite) — Infrastructures de supercalculateurs de classe mondiale.",
                "• Technical University of Munich (TUM - Allemagne) — Ingénierie logicielle d'excellence.",
                "• University of Oxford (UK) — Département de sciences computationnelles théoriques.",
                "• Stanford University (USA) — Écosystème roi de la tech mondiale."
            ],
            "maroc_unis": [
                "• 1337 Coding School (UM6P Benguerir / Casablanca / Tétouan) — Système peer-to-peer d'élite.",
                "• ENSIAS (Rabat) — Référence nationale historique en génie informatique.",
                "• Al Akhawayn University (AUI Ifrane) — School of Science and Engineering (Format Américain).",
                "• INPT (Rabat) / ENSIAS / EMI — Voies d'ingénierie d'État après classes préparatoires."
            ],
            "scholarships": [
                "• Bourse Internationale SINGA (Singapour) : Financement absolu à 100% de la scolarité et de la vie sur place.",
                "• Bourse d'Excellence EPFL : Destinée aux cerveaux scientifiques internationaux exceptionnels.",
                "• Prise en charge intégrale Écosystème 1337 : Zéro frais de scolarité, accès aux infrastructures 24/7.",
                "• Bourses d'Excellence KAUST Fellowships : Financement global pour les tracks de recherche informatique."
            ],
            "salary": "75,000$ à 180,000$ / an",
            "roadmap": "Coder, tester et mettre en ligne une application fonctionnelle ou un script d'automatisation (MVP). Une URL fonctionnelle a 10 fois plus de poids qu'un CV théorique."
        },
        "Business, Stratégie, Entrepreneuriat & Finance": {
            "title": "International Business Administration, Stratégie d'Entreprise, Finance & Data Economy",
            "branches": ["• Corporate Finance & Modélisation de Marché", "• Management de l'Innovation et Entrepreneuriat", "• Stratégie Marketing Digital & Croissance", "• Gestion de la Chaîne Logistique Globale (Supply Chain)", "• Social Business & Économie Collaborative"],
            "global_unis": [
                "• HEC Paris (France) — Leader européen de la business stratégie.",
                "• Wharton School (University of Pennsylvania - USA) — Référence de la haute finance mondiale.",
                "• London School of Economics (LSE - UK) — Analyse économique et structurelle globale.",
                "• INSEAD (Singapour / Fontainebleau) — Le MBA mondial de stratégie d'entreprise.",
                "• University of St. Gallen (Suisse) — Hub majeur de management de l'Europe germanophone.",
                "• McGill University (Canada) — Desautels Faculty of Management.",
                "• HKUST (Hong Kong) — Business School de premier rang pour les marchés asiatiques.",
                "• Rotterdam School of Management (Pays-Bas) — Leader en gestion éco-responsable des entreprises."
            ],
            "maroc_unis": [
                "• Africa Business School (ABS - UM6P Casablanca/Benguerir).",
                "• ISCAE (Casablanca / Rabat) — Grande École de commerce publique historique.",
                "• ENCG (Réseau National des Écoles de Commerce et de Gestion).",
                "• Al Akhawayn University (AUI - School of Business Administration)."
            ],
            "scholarships": [
                "• Bourse de la Fondation Al Ghurair : Financement d'excellence pour étudiants arabes performants.",
                "• Bourses de Mérite Élite ISCAE / ENCG : Prises en charge de la mobilité internationale.",
                "• Bourses Érasmus+ de l'Union Européenne : Financement des semestres d'échange en Business Schools.",
                "• Bourses Eiffel d'Excellence (France) : Pour les parcours de Master en Management."
            ],
            "salary": "50,000$ à 145,000$ / an",
            "roadmap": "Créer et formaliser un Business Model réel (Analyse financière, leviers marketing) pour un projet local ou une structure existante afin de prouver ton sens stratégique immédiat."
        }
    }

    # CALCUL DE L'INDICE D'ADMISSIBILITÉ BASÉ SUR LE GRADE ACADÉMIQUE
    chances_score = min(int(v["note"] * 4.9), 98)

    # AFFICHAGE DE LA SIGNATURE D'IDENTITÉ RECONNUE
    col_left, col_right = st.columns([1.1, 2])
    
    with col_left:
        st.markdown("### 🧬 AI Student Profile Identity")
        st.markdown(f"""
            <div class="dna-container" style="border-top: 4px solid #2563eb;">
                <p style="font-size: 11px; color:#64748b !important; margin:0; font-family:'Space Grotesk'; text-transform:uppercase; font-weight:bold;">Verified Matrix Input</p>
                <div style="margin-top:12px;">
                    <div class="dna-badge">Niveau : {v['scolaire']}</div>
                    <div class="dna-badge">Filière d'Étude : {v['filiere']}</div>
                    <div class="dna-badge">Grade Capital : {v['note']}/20</div>
                    <div class="dna-badge">Anglais : {v['en']}</div>
                    <div class="dna-badge">Français : {v['fr']}</div>
                    <div class="dna-badge">Style : {v['perso']}</div>
                    <div class="dna-badge">Prise en charge : {v['budget']}</div>
                </div>
                <div style="margin-top:15px; border-top:1px solid #1e293b; padding-top:10px;">
                    <span style="font-size:12px; color:#64748b;">Mots-clés sémantiques analysés :</span><br>
                    <p style="font-size:13px; color:#60a5fa !important; font-style:italic; margin-top:5px;">"{v['keywords'] if v['keywords'] != '' else 'Aucun mot-clé libre renseigné'}"</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("### 🔮 Universal Career Pathway & Target Colleges Mapping")
        
        # Le système boucle dynamiquement sur CHAQUE secteur détecté sans exclusion pour afficher TOUTES les universités
        for track in detected_tracks:
            if track in database:
                db = database[track]
                st.markdown(f"""
                    <div class="output-card prime">
                        <span class="prob-tag">Compatibilité : {chances_score}%</span>
                        <h4 style="margin:0; color:#059669 !important;">🎯 DOMAINE FILTRÉ : {db['title']}</h4>
                        
                        <div style="margin-top:15px;">
                            <span style="font-size:12px; color:#60a5fa; font-weight:bold; text-transform:uppercase;">📋 Options de Spécialisations Internes :</span>
                            <div style="font-size:14px; margin-top:5px; color:#e2e8f0 !important; line-height:1.5;">{"<br>".join(db['branches'])}</div>
                        </div>

                        <div style="margin-top:15px; background:rgba(255,255,255,0.01); padding:12px; border-radius:8px; border:1px solid #1e293b;">
                            <span style="font-size:12px; color:#34d399; font-weight:bold; text-transform:uppercase;">🌍 Établissements Universitaires Majeurs Recommandés :</span>
                            <div style="font-size:14px; margin-top:5px; color:#ffffff !important; line-height:1.6;">{"<br>".join(db['global_unis'])}</div>
                        </div>

                        <div style="margin-top:12px;">
                            <span style="font-size:12px; color:#34d399; font-weight:bold; text-transform:uppercase;">🇲🇦 Options Territoriales d'Excellence (Maroc) :</span>
                            <div style="font-size:14px; margin-top:5px; color:#ffffff !important; line-height:1.5;">{"<br>".join(db['maroc_unis'])}</div>
                        </div>
                        
                        <div style="margin-top:12px;">
                            <span style="font-size:13px; color:#475569;">Potentiel de Rémunération Moyen à l'International :</span><br>
                            <div class="salary-tag">{db['salary']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                # Fallback générique intelligent si un nouveau champ custom est sélectionné
                st.markdown(f"""
                    <div class="output-card prime">
                        <h4 style="margin:0; color:#059669 !important;">🎯 AXE COMPLÉMENTAIRE : {track}</h4>
                        <p style="font-size:14px; color:#e2e8f0;">Analyse sémantique personnalisée en cours. Les universités d'élite associées incluent les réseaux du Groupe Ivy League (USA), Russell Group (UK) et les pôles technologiques d'État (Maroc).</p>
                    </div>
                """, unsafe_allow_html=True)

    # --- ENGINES DES BOURSES D'ÉTUDES GLOBALES ET CRITÈRES ---
    st.markdown("### 🎓 Universal Scholarship Matching Engine & Application Deadlines")
    
    all_scholarships_html = []
    for track in detected_tracks:
        if track in database:
            all_scholarships_html.extend(database[track]["scholarships"])
            
    unique_scholarships = list(set(all_scholarships_html))
    li_bourses_html = "".join([f"<li style='margin-bottom:12px;'><b>{b.split(' : ')[0]}</b> : {b.split(' : ')[1] if len(b.split(' : ')) > 1 else ''}<br><span style='font-size:12px; color:#d97706;'>⏰ Cycle d'ouverture récurrent : Septembre - Janvier | Requis : Relevés de notes + Score IELTS/TCF + Lettres de Recommandation.</span></li>" for b in unique_scholarships])

    st.markdown(f"""
        <div class="output-card scholarship">
            <h5 style="color:#2563eb !important; margin:0; font-size:16px;">✨ Programmes de Financement Publics & Privés Indexés ({len(unique_scholarships)} Programmes Détectés) :</h5>
            <p style="font-size:13px; color:#475569; margin-top:2px;">Filtre ajusté automatiquement selon le profil de ressources de l'étudiant.</p>
            <ul style="margin-top:15px; font-size:14px; padding-left:20px; line-height:1.7; color:#ffffff !important;">
                {li_bourses_html if li_bourses_html != '' else '<li>Aucun programme spécifique trouvé pour cette combinaison. Contactez le pôle d\'orientation.</li>'}
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # --- GPS ROADMAP PAR 3ALLAL ---
    st.markdown("### 🧭 GPS Diagnostic & Strategic Action Steps")
    
    specific_roadmaps = []
    for track in detected_tracks:
        if track in database:
            specific_roadmaps.append(database[track]["roadmap"])
    roadmap_final_text = " // ".join(specific_roadmaps) if len(specific_roadmaps) > 0 else "Développer tes compétences pratiques à travers des projets réels."

    st.markdown(f"""
        <div class="output-card warning">
            <h5 style="color:#d97706 !important; margin:0; font-size:16px;">🚨 AI Reality Check par 3allal :</h5>
            <p style="font-size:15px; margin-top:10px; color:#e2e8f0 !important; line-height:1.6;">
                "Ta moyenne de <b>{v['note']}/20</b> est ton arme principale pour franchir les filtres automatiques des grandes universités. Mais attention : pour décrocher les financements complets à l'international, les comités d'admission reçoivent des milliers de dossiers parfaits. Ce qui fera pencher la balance, ce n'est pas ce que tu sais, c'est ce que tu construis.<br><br>
                <b>Ta feuille de route impérative dès maintenant :</b><br>
                👉 {roadmap_final_text}<br><br>
                <b>Calendrier d'application critique :</b> Ne te laisse pas dépasser par le temps. Pour le cycle d'admission international 2026-2027, tes certifications officielles de langues (IELTS pour l'anglais, TCF pour le français) doivent être planifiées et passées dès cet automne pour blinder ton dossier de candidature."
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    if st.button("🔄 Lancer une nouvelle simulation de profil"):
        st.session_state.current_level = 1
        st.session_state.dna_vault = {}
        st.rerun()
