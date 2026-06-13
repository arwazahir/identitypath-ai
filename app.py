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
    
    .stMarkdown, p, span, label, .stSelectbox, .stSlider, .stMultiSelect { color: #ffffff !important; font-size: 15px !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Space Grotesk', sans-serif; color: #ffffff !important; font-weight: 700 !important; }
    
    .seo-banner { text-align: left; padding: 30px; background: linear-gradient(135deg, #0f172a 0%, #020617 100%); border-radius: 16px; border: 1px solid #1e293b; margin-bottom: 30px; }
    .seo-title { font-size: 40px; font-weight: 800; color: #ffffff !important; letter-spacing: -1px; font-family: 'Space Grotesk'; }
    .seo-keywords { color: #475569 !important; font-size: 11px !important; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 5px; font-weight: 600; }
    
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
    .req-tag { background: rgba(217, 119, 6, 0.15); color: #fbbf24 !important; border: 1px solid rgba(217, 119, 6, 0.3); padding: 4px 10px; border-radius: 6px; font-size: 13px !important; font-weight: 600; display: inline-block; margin-top: 4px; }
    .prob-tag { float: right; background: #1e293b; color: #ffffff !important; border: 1px solid #334155; padding: 4px 12px; border-radius: 20px; font-size: 13px !important; font-weight: bold; }
    
    .stButton>button { background: linear-gradient(90deg, #2563eb, #059669) !important; color: #ffffff !important; font-weight: 700 !important; border-radius: 12px !important; padding: 16px 32px !important; border: none !important; width: 100%; font-size: 16px !important; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2); transition: all 0.2s ease; }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(5, 150, 105, 0.3); }
    </style>
""", unsafe_allow_html=True)

# Google Metadata Injection SEO
st.markdown('<div style="display:none;"><h1>IdentityPath AI</h1><p>Official Orientation Website</p></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="seo-banner">
        <div class="seo-title">🧭 IDENTITYPATH AI</div>
        <div class="seo-keywords">Official Guidance Engine • Advanced Student DNA Profiling • Global Scholarship Data-Matrix</div>
    </div>
""", unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS CODE PROMO COMPTE DE CONFIANCE ---
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
    st.stop()

if "current_level" not in st.session_state: st.session_state.current_level = 1
if "dna_vault" not in st.session_state: st.session_state.dna_vault = {}

progress_percent = (st.session_state.current_level - 1) * 33.33
if st.session_state.current_level == 4: progress_percent = 100.0

st.markdown(f"""
    <div style="margin-bottom: 6px; font-weight: bold; font-size: 13px; color: #64748b;">PROFILING INTELLIGENCE PROGRESSION : {int(progress_percent)}%</div>
    <div class="progress-wrapper"><div class="progress-bar-fill" style="width: {progress_percent}%;"></div></div>
""", unsafe_allow_html=True)

# --- LEVEL 1 ---
if st.session_state.current_level == 1:
    st.markdown("<div class='level-header'>🎮 LEVEL 1: Academic Identity & Geographic Boundaries</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("Âge de l'étudiant :", ["15 ans", "16 ans", "17 ans", "18 ans", "19 ans+"])
        location = st.text_input("Pays et Ville de résidence actuelle :", value="Maroc, Casablanca")
    with col2:
        scolaire = st.selectbox("Niveau scolaire actuel :", ["Collège", "Lycée : Troncs Communs", "Lycée : 1ère année Bac (Penultimate Year)", "Lycée : 2ème année Bac (Terminale)", "Étudiant d'Enseignement Supérieur"])
        filiere = st.selectbox("Filière d'études actuelle :", ["Sciences Mathématiques", "Sciences Physiques / Expérimentales", "Sciences Économiques & Gestion", "Sciences Technologiques / Informatique"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Analyze & Unlock Level 2 ➡️"):
        st.session_state.dna_vault.update({"age": age, "location": location, "scolaire": scolaire, "filiere": filiere})
        st.session_state.current_level = 2
        st.rerun()

# --- LEVEL 2 ---
elif st.session_state.current_level == 2:
    st.markdown("<div class='level-header'>🎮 LEVEL 2: Grade Capital & Multi-Language Matrix</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: feel_math = st.selectbox("Aisance - Bloc Mathématiques :", ["Excellent", "Moyen", "Difficile"])
    with c2: feel_physics = st.selectbox("Aisance - Bloc Sciences / Physique :", ["Excellent", "Moyen", "Difficile"])
    with c3: note_lycee = st.slider("Moyenne générale (Actuelle ou Visée) :", 10.0, 20.0, 17.5, step=0.1)
    st.write("---")
    cl1, cl2, cl3 = st.columns(3)
    with cl1: lang_en = st.selectbox("Anglais (IELTS / TOEFL visé) :", ["C2 (Bilingue / Fluide)", "C1 (Avancé)", "B2 (Intermédiaire Supérieur)", "B1 (Intermédiaire)"])
    with cl2: lang_fr = st.selectbox("Français (TCF / DELF acquis) :", ["C2 (Bilingue / Maternel)", "C1 (Avancé)", "B2 (Intermédiaire)", "B1 (Basique)"])
    with cl3: lang_ar = st.selectbox("Arabe :", ["C2 (Bilingue)", "C1 (Avancé)", "B2 (Maîtrisé)"])
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Process Metrics & Unlock Level 3 ➡️"):
        st.session_state.dna_vault.update({"math": feel_math, "physics": feel_physics, "note": note_lycee, "en": lang_en, "fr": lang_fr, "ar": lang_ar})
        st.session_state.current_level = 3
        st.rerun()

# --- LEVEL 3 ---
elif st.session_state.current_level == 3:
    st.markdown("<div class='level-header'>🎮 LEVEL 3: Deep Ambitions, Skills Preferences & Mindset Text Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='dna-container'>", unsafe_allow_html=True)
    domaines = st.multiselect("Sélectionne tes grands secteurs d'affinité :", [
        "Création, Design, Arts & Architecture",
        "Informatique, Tech, IA & Software Engineering",
        "Business, Stratégie, Entrepreneuriat & Finance",
        "Sciences Fondamentales, Ingénierie & Énergie",
        "Bio-Sciences, Santé & Écosystèmes Environnementaux"
    ], default=["Création, Design, Arts & Architecture"])
    
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        objectifs = st.radio("Quel est le vecteur de réussite recherché ?", [
            "Décrocher une Bourse d'Étude Internationale Complète (100% de prise en charge)",
            "Viser l'Excellence Académique Pure au sein des Universités Mondiales d'Élite",
            "Créer l'impact direct : Focus Bâtir des Projets Concrets & Entrepreneuriat",
            "Parcours de Haute Performance Territorial au Maroc (UM6P, Réseaux d'État)"
        ])
        budget = st.selectbox("Profil de Prise en Charge Économique :", ["Bourse complète obligatoire", "Co-financement / Prise en charge partielle", "Autonomie financière totale"])
    with col_i2:
        perso = st.radio("Philosophie opérationnelle préférée :", ["Je suis un 'Builder' (Création pratique, MVP)", "Je suis un 'Chercheur' (Analyse, Théorie)"])
        mobilite = st.radio("Périmètre Géographique Souhaité :", ["Ouverture Internationale Globale", "Focus Territorial Précis (Maroc)"])
    
    st.write("---")
    user_keywords = st.text_area(
        "Moteur sémantique textuel : Décris ici en saisie libre tes passions, tes idées de projets et ce que tu souhaites créer :",
        placeholder="Ex: J'aime l'art graphique, l'écologie, lancer des projets, coder..."
    )
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("⚡ Run IdentityPath Multi-Field Semantic Analysis 🚀"):
        st.session_state.dna_vault.update({"domaines": domaines, "objectifs": objectifs, "perso": perso, "budget": budget, "mobilite": mobilite, "keywords": user_keywords.lower()})
        st.session_state.current_level = 4
        st.rerun()

# --- LEVEL 4 ---
elif st.session_state.current_level == 4:
    st.markdown("<div class='level-header'>🏁 LEVEL 4: Personalized Deep-Data Diagnostic Profile & University Matching Requirements</div>", unsafe_allow_html=True)
    v = st.session_state.dna_vault
    kw = v["keywords"]
    detected_tracks = list(v["domaines"])
    
    # Scan sémantique d'appoint
    if any(w in kw for w in ["code", "script", "informatique", "python", "ia", "tech"]):
        if "Informatique, Tech, IA & Software Engineering" not in detected_tracks: detected_tracks.append("Informatique, Tech, IA & Software Engineering")
    if any(w in kw for w in ["dessin", "plan", "architecture", "design", "art", "graphique"]):
        if "Création, Design, Arts & Architecture" not in detected_tracks: detected_tracks.append("Création, Design, Arts & Architecture")
    if any(w in kw for w in ["business", "entreprise", "finance", "startup", "coopérative", "commerce"]):
        if "Business, Stratégie, Entrepreneuriat & Finance" not in detected_tracks: detected_tracks.append("Business, Stratégie, Entrepreneuriat & Finance")

    # STRUCTURE COMPLÈTE BIG DATA - EXIGENCES ADMISSIBILITÉ (REQUIREMENTS ELÈVE PAR ÉLÈVE)
    database = {
        "Création, Design, Arts & Architecture": {
            "title": "Architecture, Arts Graphiques, Design Computationnel & Urbanisme Durable",
            "branches": [
                "• Architecture d'Intérieur & Design d'Espace Scénique",
                "• Urbanisme Tactique, Villes Intelligentes & Éco-Quartiers",
                "• Design Graphique Avancé, Branding Visuel & UI/UX Design",
                "• Arts Plastiques, Modélisation Algorithmique 3D & Design Industriel"
            ],
            "unis": [
                {"name": "Politecnico di Milano (Italie)", "type": "Monde", "gpa": "Bac avec mention (>15.5/20)", "lang": "Anglais B2 minimum (IELTS 6.0) ou Italien B2", "deadline": "Février - Avril", "docs": "Portfolio créatif + Test d'entrée d'architecture (TEST AR)"},
                {"name": "TU Delft (Pays-Bas)", "type": "Monde", "gpa": "Excellence académique (>16.5/20)", "lang": "IELTS 6.5 minimum / TOEFL iBT 90", "deadline": "15 Janvier (Numerus Fixus)", "docs": "Portfolio de projets + Lettre de motivation stratégique + CV"},
                {"name": "University of the Arts London (UAL - UK)", "type": "Monde", "gpa": "Dossier artistique haut niveau (>14/20)", "lang": "IELTS 6.5 (avec 6.0 minimum dans chaque bloc)", "deadline": "Janvier - Mars", "docs": "Portfolio numérique de 20 pages + Entretien individuel"},
                {"name": "Middle East Technical University (METU - Turquie)", "type": "Monde", "gpa": "Moyenne au Bac >15/20", "lang": "TOEFL iBT 84 ou examen interne", "deadline": "Juillet", "docs": "Dossier scolaire + SAT facultatif mais recommandé"},
                {"name": "Parsons School of Design (New York, USA)", "type": "Monde", "gpa": "GPA élevé requis (Équivalent >16/20)", "lang": "TOEFL 92 ou IELTS 7.0", "deadline": "15 Janvier", "docs": "Parsons Challenge (3 œuvres d'art) + Portfolio + 2 Lettres de recommandation"},
                {"name": "École Nationale d'Architecture (Réseau ENA Maroc)", "type": "Maroc", "gpa": "Sélection stricte sur note du Bac (Seuil historique ~16.0/20)", "lang": "Français fluide requis", "deadline": "Juillet (Post-Bac)", "docs": "Formulaire d'inscription national + Réussite au concours écrit d'architecture"},
                {"name": "UM6P - SAP+D (School of Architecture - Benguerir)", "type": "Maroc", "gpa": "Étude de dossier rigoureuse (>15/20)", "lang": "Français et Anglais (Niveau d'étude hybride)", "deadline": "Mai - Juillet", "docs": "Test écrit de culture spatiale et géométrie + Entretien de motivation devant jury"}
            ],
            "scholarships": [
                "• Bourse Complète Türkiye Bursları (Turquie) : 100% scolarité, logement universitaire gratuit, allocation mensuelle, assurance maladie et billet d'avion.",
                "• Bourse DSU (Italie) : Exonération des taxes, repas offerts au restaurant universitaire et aide financière annuelle selon critères sociaux.",
                "• Bourse d'Excellence du Mérite UM6P : Couverture totale ou partielle du coût des études et du logement basée sur la performance académique globale."
            ]
        },
        "Informatique, Tech, IA & Software Engineering": {
            "title": "Computer Science, Intelligence Artificielle, Data Science & Cloud Engineering",
            "branches": [
                "• Génie Logiciel, Algorithmique & Systèmes Distribués",
                "• Data Science, Deep Learning & Modélisation Prédictive",
                "• Cybersécurité des Réseaux Informatiques et Cryptographie",
                "• Cloud Architecture, Systèmes Autonomes & DevOps"
            ],
            "unis": [
                {"name": "National University of Singapore (NUS)", "type": "Monde", "gpa": "Profil scientifique d'élite (>17.5/20)", "lang": "IELTS 6.5 / TOEFL 93", "deadline": "Décembre - Février", "docs": "Scores de mathématiques avancées + Activités parascolaires d'impact"},
                {"name": "EPFL (Lausanne, Suisse)", "type": "Monde", "gpa": "Moyenne générale au Baccalauréat Scientifique >= 16.0/20 (Condition d'accès stricte)", "lang": "Français C1 minimum requis pour le Bachelor", "deadline": "30 Avril", "docs": "Relevés de notes officiels du Bac + Validation des matières scientifiques"},
                {"name": "University of Waterloo (Canada)", "type": "Monde", "gpa": "Excellence en Mathématiques/Sciences (>17/20)", "lang": "IELTS 7.0 / TOEFL 90", "deadline": "Février", "docs": "Formulaire AIF (Admission Information Form) détaillant tes projets de code personnels"},
                {"name": "KAUST (Arabie Saoudite)", "type": "Monde", "gpa": "Dossier d'élite en STEM (Filières scientifiques)", "lang": "IELTS 6.5 minimum / TOEFL 79", "deadline": "Janvier (Early) / Mars", "docs": "3 Lettres de recommandation de professeurs de sciences + CV de projets technologiques"},
                {"name": "1337 Coding School (UM6P Benguerir / Casa / Tétouan)", "type": "Maroc", "gpa": "Aucun diplôme ni note requis (Sélection par la logique pure)", "lang": "Aucun prérequis de niveau linguistique au départ", "deadline": "Ouvert toute l'année (Inscription en ligne)", "docs": "Passage des tests de logique en ligne + Épreuve immersive de la 'Piscine' de 4 semaines"},
                {"name": "ENSIAS (Rabat)", "type": "Maroc", "gpa": "Classement d'excellence au Concours National Commun (CNC)", "lang": "Français et Anglais technique", "deadline": "Juillet (Post-Prepa)", "docs": "Attestation d'affectation des Classes Préparatoires aux Grandes Écoles (CPGE)"}
            ],
            "scholarships": [
                "• Bourse Complète SINGA (Singapour) : Financement complet des frais universitaires, allocation mensuelle de subsistance et frais d'installation.",
                "• Bourse d'Excellence KAUST Fellowships : Financement à 100% de la scolarité, logement gratuit, couverture médicale complète et allocation annuelle substantielle.",
                "• Écosystème Gratuit 1337 : Formation entièrement financée par l'écosystème UM6P, scolarité à 0 DH pour tous les étudiants retenus."
            ]
        },
        "Business, Stratégie, Entrepreneuriat & Finance": {
            "title": "International Business Administration, Stratégie d'Entreprise, Finance & Data Economy",
            "branches": [
                "• Corporate Finance, Analyse de Marché & Gestion des Risques",
                "• Management de l'Innovation, Entrepreneuriat & Gestion de Startup",
                "• Stratégie Marketing Digital, E-Commerce & Growth Hacking",
                "• Management de Projets et Digitalisation des Coopératives Sociales"
            ],
            "unis": [
                {"name": "HEC Paris (France)", "type": "Monde", "gpa": "Dossier académique d'exception (>16.5/20) ou Classe prépa", "lang": "Anglais ou Français selon le track choisi (IELTS 7.0 conseillé)", "deadline": "Plusieurs sessions (Octobre à Avril)", "docs": "Score de test de logique (GMAT/TAGE MAGE) + 2 Lettres de recommandation académiques"},
                {"name": "London School of Economics (LSE - UK)", "type": "Monde", "gpa": "Moyenne au Bac d'élite (>17/20 requis)", "lang": "IELTS 7.0 (avec 7.0 minimum dans chaque compétence)", "deadline": "15 Janvier (Via UCAS)", "docs": "Personal Statement ultra-poussé axé sur l'économie et la logique d'entreprise"},
                {"name": "Rotterdam School of Management (Pays-Bas)", "type": "Monde", "gpa": "Moyenne générale solide (>15/20)", "lang": "IELTS 6.5 / TOEFL iBT 91", "deadline": "Janvier - Avril", "docs": "CV + Test de Mathématiques interne ou score SAT math décent"},
                {"name": "Africa Business School (ABS - UM6P Casablanca)", "type": "Maroc", "gpa": "Sélection sur dossier de performance (>14.5/20)", "lang": "Anglais professionnel (Cursus anglophone)", "deadline": "Mai - Août", "docs": "Dossier de candidature + Test d'admission de logique interne + Entretien oral"},
                {"name": "ISCAE (Casablanca)", "type": "Maroc", "gpa": "Présélection sur note du Bac ou réussite des classes prépas", "lang": "Français et Anglais d'affaires", "deadline": "Mai (Concours d'accès direct)", "docs": "Dossier scolaire + Épreuves écrites du concours de l'ISCAE (Maths, Anglais, Culture G)"}
            ],
            "scholarships": [
                "• Bourse Eiffel d'Excellence (France) : Allocation mensuelle de subsistance de haut niveau, prise en charge des transports et couverture sociale.",
                "• Bourse de la Fondation Al Ghurair : Financement complet ou partiel pour les profils arabes à fort potentiel de leadership en gestion et entrepreneuriat.",
                "• Bourse Érasmus+ de Mobilité : Aide financière mensuelle accordée pour les semestres d'échange internationaux au sein des Business Schools européennes."
            ]
        }
    }

    # CALCUL DE L'INDICE D'ADMISSIBILITÉ DE L'ÉLÈVE
    student_gpa = v["note"]
    student_eng = v["en"]
    student_fr = v["fr"]
    chances_score = min(int(student_gpa * 4.9), 98)

    col_left, col_right = st.columns([1, 2.2])
    
    with col_left:
        st.markdown("### 🧬 AI Student Profile Identity")
        st.markdown(f"""
            <div class="dna-container" style="border-top: 4px solid #2563eb;">
                <p style="font-size: 11px; color:#64748b !important; margin:0; font-family:'Space Grotesk'; text-transform:uppercase; font-weight:bold;">Verified Matrix Input</p>
                <div style="margin-top:12px;">
                    <div class="dna-badge">Niveau : {v['scolaire']}</div>
                    <div class="dna-badge">Filière d'Étude : {v['filiere']}</div>
                    <div class="dna-badge">Grade Capital : {v['note']}/20</div>
                    <div class="dna-badge">Anglais : {student_eng}</div>
                    <div class="dna-badge">Français : {student_fr}</div>
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
        st.markdown("### 🔮 Universal Match Report & Entry Requirements")
        
        # Filtrer et afficher chaque domaine correspondant aux choix/mots-clés de l'élève
        matched_any = False
        for track in detected_tracks:
            if track in database:
                matched_any = True
                db = database[track]
                
                st.markdown(f"""
                    <div class="output-card prime">
                        <span class="prob-tag">Compatibilité Dossier : {chances_score}%</span>
                        <h4 style="margin:0; color:#059669 !important;">🎯 AXE DISCIPLINAIRE : {db['title']}</h4>
                        
                        <div style="margin-top:12px;">
                            <span style="font-size:12px; color:#60a5fa; font-weight:bold; text-transform:uppercase;">📋 FILIÈRES POSSIBLES POUR L'ÉLÈVE :</span>
                            <div style="font-size:14px; margin-top:5px; color:#e2e8f0 !important; line-height:1.5;">{"<br>".join(db['branches'])}</div>
                        </div>

                        <div style="margin-top:18px;">
                            <span style="font-size:12px; color:#34d399; font-weight:bold; text-transform:uppercase;">🌍 LISTE DES UNIVERSITÉS ET EXIGENCES INDIVIDUELLES (REQUIREMENTS) :</span>
                        </div>
                """, unsafe_allow_html=True)
                
                # Boucler sur TOUTES les universités de la base de données pour ce domaine spécifique
                for uni in db["unis"]:
                    # Analyse personnalisée de la situation de l'élève par rapport à l'université
                    status_color = "#34d399" if student_gpa >= 15.0 else "#fbbf24"
                    st.markdown(f"""
                        <div style="margin-top:12px; background: rgba(255,255,255,0.02); padding: 15px; border-radius: 8px; border: 1px solid #1e293b;">
                            <b style="font-size:15px; color:#ffffff;">🏛️ {uni['name']}</b> <span style="font-size:11px; color:#64748b;">({uni['type']})</span>
                            <div style="margin-top:8px; font-size:13.5px; line-height:1.6;">
                                <span style="color:#94a3b8;">• Exigence de Note (GPA) :</span> <span style="color:{status_color}; font-weight:600;">{uni['gpa']}</span><br>
                                <span style="color:#94a3b8;">• Exigence de Langue :</span> <span>{uni['lang']}</span><br>
                                <span style="color:#94a3b8;">• Documents Requis & Épreuves :</span> <span style="color:#e2e8f0;">{uni['docs']}</span><br>
                                <span style="color:#94a3b8;">• Période de Deadline de Candidature :</span> <span class="req-tag">⏰ {uni['deadline']}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                st.markdown(f"""
                        <div style="margin-top:15px;"><div class="salary-tag">Potentiel de Marché : {db['salary']}</div></div>
                    </div>
                """, unsafe_allow_html=True)
                
        if not matched_any:
            # Fallback adaptatif si aucun des choix n'est dans la base prédéfinie
            st.markdown("""
                <div class="output-card prime">
                    <h4 style="margin:0; color:#059669 !important;">🎯 RECHERCHE APPAREILLÉE DYNAMIQUE</h4>
                    <p style="font-size:14px; color:#e2e8f0;">L'analyse sémantique globale cible les universités mondiales du Groupe Ivy League (USA) et du Russell Group (UK). Les exigences de base pour ces filières d'élite imposent une moyenne au Bac > 16.5/20, un score IELTS minimum de 6.5 ou 7.0, ainsi que la soumission de lettres de recommandation de professeurs de matières principales (Maths/Sciences) avant la mi-janvier.</p>
                </div>
            """, unsafe_allow_html=True)

    # --- BOURSES D'ÉTUDES GLOBALES ET CRITÈRES ---
    st.markdown("### 🎓 Universal Scholarship Matching Engine & Application Deadlines")
    
    all_scholarships_html = []
    for track in detected_tracks:
        if track in database:
            all_scholarships_html.extend(database[track]["scholarships"])
            
    unique_scholarships = list(set(all_scholarships_html))
    li_bourses_html = "".join([f"<li style='margin-bottom:12px;'><b>{b.split(' : ')[0]}</b> : {b.split(' : ')[1] if len(b.split(' : ')) > 1 else ''}<br><span style='font-size:12px; color:#d97706;'>⏰ Critères d'Éligibilité : Moyenne d'Excellence + Dossier de motivation soumis entre Septembre et Mars selon le pays choisi. Accès prioritaire accordé aux profils d'impact concret.</span></li>" for b in unique_scholarships])

    st.markdown(f"""
        <div class="output-card scholarship">
            <h5 style="color:#2563eb !important; margin:0; font-size:16px;">✨ Programmes de Financement Accessibles ({len(unique_scholarships)} Programmes Détectés) :</h5>
            <p style="font-size:13px; color:#475569; margin-top:2px;">Filtre ajusté automatiquement selon le profil de ressources et l'ambition de l'étudiant.</p>
            <ul style="margin-top:15px; font-size:14px; padding-left:20px; line-height:1.7; color:#ffffff !important;">
                {li_bourses_html if li_bourses_html != '' else '<li>Analyse personnalisée requise pour ce profil croisé. Exigence générale : Excellence au dossier et validation des tests de langue avant Janvier.</li>'}
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # --- GPS ROADMAP PAR 3ALLAL ---
    st.markdown("### 🧭 GPS Diagnostic & Strategic Action Steps")
    st.markdown(f"""
        <div class="output-card warning">
            <h5 style="color:#d97706 !important; margin:0; font-size:16px;">🚨 AI Reality Check par 3allal :</h5>
            <p style="font-size:15px; margin-top:10px; color:#e2e8f0 !important; line-height:1.6;">
                "Ton dossier académique affiche une moyenne de <b>{student_gpa}/20</b>. C'est un excellent point de départ pour franchir les seuils automatiques des universités listées ci-dessus. Cependant, garde en tête que les universités d'élite rejettent des milliers de moyennes parfaites chaque année. La différence se fait sur ce que tu construis en dehors des cours.<br><br>
                <b>Ce qui manque à ton dossier actuel pour valider ces Requirements :</b><br>
                1. <b>Preuve d'Impact :</b> Tu dois documenter tes projets concrets, tes prototypes ou tes créations visuelles (comme un portfolio ou un site de démonstration fonctionnel) pour appuyer ta philosophie de 'Builder' qui teste, échoue et reconstruit.<br>
                2. <b>Validation des Tests de Langue :</b> Ton niveau auto-déclaré en Anglais (<b>{student_eng}</b>) et Français (<b>{student_fr}</b>) doit être validé par des certifications officielles (IELTS ou TOEFL, TCF ou DELF). Planifie ces examens dès cet automne pour ne pas rater les deadlines de candidatures internationales du cycle 2026-2027."
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    if st.button("🔄 Lancer une nouvelle simulation de profil"):
        st.session_state.current_level = 1
        st.session_state.dna_vault = {}
        st.rerun()
