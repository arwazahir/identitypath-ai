import streamlit as st
import time

# Configuration de l'application
st.set_page_config(page_title="IdentityPath Ecosystem", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN PREMIUM REVISITÉ : STRICT ACCESSIBILITY & HIGH-END UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #0f172a; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    
    /* Visibilité absolue des textes - Zéro compromis */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider { color: #ffffff !important; font-size: 16px !important; }
    h1, h2, h3, h4 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; font-weight: 800 !important; }
    
    /* Container Logo Moderne */
    .app-logo-container { text-align: center; padding: 30px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 20px; border: 2px solid #334155; margin-bottom: 35px; }
    .app-logo { font-size: 42px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Urbanist'; }
    .app-subtitle { color: #10b981 !important; font-size: 14px !important; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 8px; }
    
    /* Layout des blocs de résultats de l'analyse profonde */
    .section-container { background: #1e293b; padding: 25px; border-radius: 16px; border: 1px solid #334155; margin-bottom: 25px; }
    .filiere-card { background: linear-gradient(90deg, #1e3a8a 0%, #172554 100%); padding: 18px; border-radius: 12px; border: 1px solid #3b82f6; margin-bottom: 12px; }
    .uni-card { background: #111827; padding: 22px; border-radius: 14px; border-left: 6px solid #3b82f6; margin-bottom: 18px; border-top: 1px solid #1f2937; border-right: 1px solid #1f2937; border-bottom: 1px solid #1f2937; }
    .bourse-card { background: #111827; padding: 22px; border-radius: 14px; border-left: 6px solid #10b981; margin-bottom: 18px; border-top: 1px solid #1f2937; border-right: 1px solid #1f2937; border-bottom: 1px solid #1f2937; }
    
    .title-white { font-size: 19px !important; font-weight: 700 !important; color: #ffffff !important; }
    .text-light { color: #f1f5f9 !important; font-size: 15px !important; line-height: 1.6; }
    .badge-premium { background: #334155; color: #ffffff !important; padding: 5px 12px; border-radius: 6px; font-size: 12px !important; font-weight: bold; display: inline-block; text-transform: uppercase; }
    
    /* Boutons */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 10px !important; padding: 14px 30px !important; border: none !important; width: 100%; font-size: 16px !important; }
    
    /* Chatbot UI Components */
    .chat-box-user { background: #3b82f6; padding: 14px 20px; border-radius: 18px 18px 0px 18px; margin-bottom: 12px; color: white; text-align: right; max-width: 85%; margin-left: auto; font-size: 15px; }
    .chat-box-ai { background: #1e293b; padding: 14px 20px; border-radius: 18px 18px 18px 0px; margin-bottom: 12px; color: white; text-align: left; max-width: 85%; border: 1px solid #334155; font-size: 15px; line-height: 1.5; }
    </style>
""", unsafe_allow_html=True)

# --- LOGO & REBRANDING ---
st.markdown("""
    <div class="app-logo-container">
        <div class="app-logo">🧭 IDENTITYPATH APP</div>
        <div class="app-subtitle">Deep Analysis Matrix & Global Scholarship Connector</div>
    </div>
""", unsafe_allow_html=True)

# --- PORTAL SECURITY ---
if "app_lock" not in st.session_state: st.session_state.app_lock = False
if not st.session_state.app_lock:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Console d'Accès Sécurisée</h3>", unsafe_allow_html=True)
        token = st.text_input("Entrez la clé de licence produit :", type="password")
        if token == "Arwagiftorient":
            if st.button("Initialiser l'Environnement 🚀"):
                st.session_state.app_lock = True
                st.rerun()
    st.stop()

# --- REPERTOIRE DE DONNÉES MASSIVES ET ANALYTIQUES ---
MASTER_DB = {
    "medical_sante": {
        "label": "Sciences Médicales, Recherche Biomédicale & Santé Publique",
        "filieres": [
            "• Doctorat d'État en Médecine Générale (Parcours Hospitalo-Universitaire)",
            "• Spécialisation en Chirurgie, Neurosciences ou Oncologie Clinique",
            "• Industrie Pharmaceutique, Biotechnologies Médicales & Génie Biomédical",
            "• Global Health & Management des Systèmes de Santé Internationaux"
        ],
        "unis": [
            {"nom": "Facultés de Médecine et de Pharmacie (FMP - Réseau Public Marocain)", "desc": "Le parcours historique d'excellence pour l'accès aux carrières médicales nationales.", "req": "Moyenne de présélection extrêmement haute au Baccalauréat + Réussite au Concours National Écrit.", "deadline": "Fin Juillet"},
            {"nom": "Université Paris Cité - Faculté de Santé (France)", "desc": "Pôle d'élite européen offrant l'accès aux études de médecine via le parcours PASS / LAS hautement compétitif.", "req": "Classement d'excellence sur dossier Parcoursup, mention Très Bien au Bac fortement recommandée.", "deadline": "Début Mars"},
            {"nom": "King's College London - Faculty of Life Sciences & Medicine (Royaume-Uni)", "desc": "Une des meilleures universités médicales mondiales, pionnière en recherche clinique.", "req": "IELTS Academic ≥ 7.0 (minimum 6.5 dans chaque sous-catégorie), Examen d'aptitude clinique UCAT obligatoire.", "deadline": "15 Octobre"}
        ],
        "bourses": [
            {"nom": "Bourse Eiffel d'Excellence (Gouvernement Français)", "couv": "Prise en charge intégrale des frais de transport, couverture médicale de haut niveau et allocation mensuelle de vie.", "req": "Dossier scientifique d'exception présenté directement par une université française d'accueil.", "deadline": "Courant Janvier"},
            {"nom": "King's Medical International Scholarship Awards", "couv": "Réduction majeure de £10,000 par an sur les frais de scolarité obligatoires pendant toute la durée du cursus.", "req": "Avoir reçu une offre d'admission ferme, excellence académique et soumission d'un essai de recherche.", "deadline": "Fin Avril"}
        ]
    },
    "economie_social": {
        "label": "Sciences Économiques, Business International & Management Stratégique",
        "filieres": [
            "• Bachelor in Business Administration (BBA) - Finance, Stratégie & Data Analytics",
            "• Cursus Grande École - Master in Management & Économie Internationale",
            "• Sciences Politiques, Relations Internationales, Économie Publique & Gouvernance"
        ],
        "unis": [
            {"nom": "Groupe ISCAE (Institut Supérieur de Commerce et d'Administration des Entreprises)", "desc": "La Grande École publique de commerce la plus réputée du Royaume.", "req": "Admissibilité stricte sur concours écrit et oral après classes préparatoires économiques ou scientifiques.", "deadline": "Mai"},
            {"nom": "UM6P - Faculty of Governance, Economic and Social Sciences (FGSES Rabat)", "desc": "Campus ultra-moderne calqué sur les standards internationaux pour former les décideurs de demain.", "req": "Dossier scolaire d'excellence, épreuves écrites de logique/culture générale et Grand Oral.", "deadline": "Fin Mai"},
            {"nom": "London School of Economics and Political Science (LSE - Londres)", "desc": "L'institution mondiale de référence absolue pour l'analyse économique et les sciences de la société.", "req": "Dossier académique d'élite, notes maximales en Mathématiques au Bac, IELTS ≥ 7.5.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse de Mérite Académique et d'Excellence FGSES / UM6P", "couv": "Prise en charge à 100% ou 50% des frais de scolarité annuels ainsi que de l'hébergement au campus.", "req": "Excellence globale mesurée au Baccalauréat combinée à une étude personnalisée de la situation de l'élève.", "deadline": "Juillet"},
            {"nom": "GREAT Scholarships - British Council", "couv": "Financement d'études d'une valeur nette de £10,000 pour couvrir les frais universitaires de l'année.", "req": "Être titulaire d'un passeport marocain et détenir une offre d'admission d'une université britannique partenaire.", "deadline": "Mai"}
        ]
    },
    "sciences_tech": {
        "label": "Sciences Fondamentales, Computer Science & Intelligence Artificielle",
        "filieres": [
            "• Bachelor & Master of Computer Science - Ingénierie Logicielle & Cybersécurité",
            "• Cursus d'Ingénierie d'État - Intelligence Artificielle, Data Science & Robotique",
            "• Mathématiques Appliquées, Modélisation Stochastique & Physique Quantique"
        ],
        "unis": [
            {"nom": "UM6P - College of Computing (UM6P Benguerir)", "desc": "Le pôle technologique africain de référence pour la recherche en algorithmique et IA.", "req": "Baccalauréat Scientifique avec mention, suivi de tests de logique et de programmation internes.", "deadline": "Mai"},
            {"nom": "EPFL (École Polytechnique Fédérale de Lausanne - Suisse)", "desc": "L'un des plus grands pôles scientifiques mondiaux pour l'informatique et les technologies.", "req": "Moyenne générale au Baccalauréat ≥ 16/20 (Mention Très Bien exigée dans les filières SM ou PC).", "deadline": "30 Avril"},
            {"nom": "University of Toronto - Faculty of Applied Science & Engineering (Canada)", "desc": "Département nord-américain d'excellence absolue pour les sciences informatiques.", "req": "TOEFL iBT ≥ 100 ou IELTS ≥ 6.5, dossier scientifique d'élite (Maths et Physique).", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence Technologique de la Fondation UM6P", "couv": "Exonération totale des frais d'apprentissage et attribution d'un logement universitaire haut de gamme.", "req": "Classement majeur parmi les meilleures notes scientifiques au niveau national.", "deadline": "Juillet"},
            {"nom": "Lester B. Pearson International Scholarship (Canada)", "couv": "Bourse intégrale exceptionnelle : couvre scolarité, frais annexes, livres et résidence complète durant 4 ans.", "req": "Profil de leader mondial, impact communautaire hors-norme, nomination exclusive par le lycée.", "deadline": "15 Janvier"}
        ]
    }
}

# --- NAVIGATION APPLICATIVE ---
if "current_step" not in st.session_state: st.session_state.current_step = 1

st.progress(st.session_state.current_step / 3)

# --- ÉTAPE 1 : ACADÉMIQUE & GÉOGRAPHIE MONDIALE OUVERTE ---
if st.session_state.current_step == 1:
    st.markdown("### 📝 Étape 1 : Cartographie Académique de l'Étudiant")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.f_bac = st.selectbox("Filière / Option du Diplôme d'études secondaires :", ["Sciences Économiques & Gestion", "Sciences Mathématiques", "Sciences Physiques", "SVT", "Lettres"])
        st.session_state.note = st.slider("Moyenne générale estimée ou ciblée (sur 20) :", 10.0, 20.0, 16.0, step=0.1)
    with col2:
        st.session_state.destination = st.selectbox("Mobilité géographique de l'élève (Ouverture totale) :", [
            "Monde Entier / International Sans Restrictions",
            "Pays de Langue Anglophone (USA, Canada, UK, Asie...)",
            "Pays de Langue Francophone (France, Suisse, Belgique...)",
            "Institutions Nationales de Prestige & Grandes Écoles"
        ])
        st.session_state.lycee = st.text_input("Ville / Localisation de l'établissement actuel :", placeholder="Ex: Casablanca, Rabat, Fès...")
    
    if st.button("Passer au Profil Linguistique Global ➡️"):
        st.session_state.current_step = 2
        st.rerun()

# --- ÉTAPE 2 : NIVEAUX CEFR POUR LES 3 LANGUES ---
elif st.session_state.current_step == 2:
    st.markdown("### 🔤 Étape 2 : Matrice des Compétences Linguistiques")
    st.write("Évaluez le profil selon le cadre standardisé européen pour chaque langue de travail.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🇺🇸 Section Anglais**")
        st.session_state.en_lvl = st.selectbox("Niveau Cadre Européen (Anglais) :", ["B1 (Intermédiaire)", "B2 (Avancé)", "C1 (Autonome)", "C2 (Bilingue)"])
        en_cert = st.checkbox("Je possède ou je prépare une certification (IELTS / TOEFL / Duolingo)")
        st.session_state.en_score_txt = st.text_input("Indiquez le score visé ou obtenu :", placeholder="Ex: IELTS 7.5...") if en_cert else "Aucun test"
        
    with col2:
        st.markdown("**🇫🇷 Section Français**")
        st.session_state.fr_lvl = st.selectbox("Niveau Cadre Européen (Français) :", ["B1 (Intermédiaire)", "B2 (Avancé)", "C1 (Autonome)", "C2 (Bilingue)"])
        fr_cert = st.checkbox("Je possède ou je prépare une certification (TCF / DELF / DALF)")
        st.session_state.fr_score_txt = st.text_input("Indiquez le score ou diplôme :", placeholder="Ex: TCF C1...") if fr_cert else "Niveau Scolaire"

    with col3:
        st.markdown("**🇲🇦 Section Arabe**")
        st.session_state.ar_lvl = st.selectbox("Niveau de Maîtrise (Arabe) :", ["B1 (Intermédiaire)", "B2 (Avancé)", "C1 (Excellent)", "C2 (Maternelle / Bilingue)"])
        st.session_state.ar_details = st.text_input("Précisions (Optionnel) :", placeholder="Ex: Option Internationale...")

    st.write("---")
    col_b1, col_b2 = st.columns([1, 5])
    with col_b1:
        if st.button("⬅️ Retour"): st.session_state.current_step = 1; st.rerun()
    with col_b2:
        if st.button("Lancer la Matrice d'Orientation Dynamique ➡️"): st.session_state.current_step = 3; st.rerun()

# --- ÉTAPE 3 : ARCHITECTURE DE RECHERCHE PROFONDE ET EXPERT CHATBOT AVEC AUDIO INTEGRÉ ---
elif st.session_state.current_step == 3:
    st.markdown("### 🧭 Matrice d'Orientation Analytique & Espace Conversationnel")
    
    # Évaluation cognitive par pondération sémantique stricte pour éliminer les erreurs de filière
    # Initialisation des variables d'état du profil si inexistantes
    if "user_written_ambitions" not in st.session_state: st.session_state.user_written_ambitions = ""
    if "audio_transcription" not in st.session_state: st.session_state.audio_transcription = ""
    
    # Zone de collecte des ambitions (Option 1 : Écrit)
    st.markdown("#### ⚙️ Configuration des Intérêts de l'Élève")
    st.session_state.user_written_ambitions = st.text_area(
        "Saisissez ici les intérêts, passions ou domaines cibles de l'élève (Ex: médecine, sciences sociales, économie...) :",
        value=st.session_state.user_written_ambitions,
        placeholder="Décrivez précisément le profil pour alimenter l'analyse cognitive..."
    )
    
    # Calcul des scores sémantiques croisés pour verrouiller la bonne filière
    full_text_corpus = (st.session_state.user_written_ambitions + " " + st.session_state.audio_transcription).lower()
    
    # Dictionnaires de poids sémantiques exclusifs
    med_score = sum(full_text_corpus.count(w) for w in ["medecine", "médecine", "sante", "santé", "pharma", "dentaire", "chirurgie", "hopital", "biologie", "clinique", "docteur"])
    eco_score = sum(full_text_corpus.count(w) for w in ["economie", "économie", "social", "sociale", "gestion", "business", "commerce", "finance", "management", "politique", "société"])
    tech_score = sum(full_text_corpus.count(w) for w in ["informatique", "code", "ia", "cyber", "ingenieur", "ingénieur", "robot", "technologie", "math", "physique", "software"])
    
    # Logique d'arbitrage de l'IA de l'application
    final_key = "sciences_tech" # Base par défaut
    max_score = max(med_score, eco_score, tech_score)
    
    if max_score > 0:
        if max_score == med_score: final_key = "medical_sante"
        elif max_score == eco_score: final_key = "economie_social"
        elif max_score == tech_score: final_key = "sciences_tech"
        
    active_data = MASTER_DB[final_key]
    
    # --- AFFICHAGE DU LIVRABLE LOGIQUE : FILIÈRES -> UNIVERSITÉS -> BOURSES ---
    col_left, col_right = st.columns([4, 3])
    
    with col_left:
        st.markdown(f"### 🎯 Branche Diagnostiquée : **{active_data['label']}**")
        
        # 1. FILIERES
        st.markdown("#### 📈 1. Filières Universitaires Recommandées")
        for f in active_data["filieres"]:
            st.markdown(f"<div class='filiere-card'><span class='title-white'>{f}</span></div>", unsafe_allow_html=True)
            
        # 2. UNIVERSITES
        st.markdown("#### 🏛️ 2. Établissements & Universités de Prestige")
        for uni in active_data["unis"]:
            st.markdown(f"""
                <div class="uni-card">
                    <div class="title-white">{uni['nom']}</div>
                    <p class="text-light" style="margin-top:10px;"><b>Présentation :</b> {uni['desc']}</p>
                    <p class="text-light"><b>Requirements requis :</b> {uni['req']}</p>
                    <p class="text-light" style="color: #f87171 !important;"><b>Deadline d'inscription :</b> {uni['deadline']}</p>
                    <div class="badge-premium">Établissement Cible</div>
                </div>
            """, unsafe_allow_html=True)
            
        # 3. BOURSES
        st.markdown("#### 💎 3. Programmes de Bourses d'Études")
        for b in active_data["bourses"]:
            st.markdown(f"""
                <div class="bourse-card">
                    <div class="title-white">{b['nom']}</div>
                    <p class="text-light" style="margin-top:10px;"><b>Volume de couverture :</b> {b['couv']}</p>
                    <p class="text-light"><b>Requirements dossier :</b> {b['req']}</p>
                    <p class="text-light" style="color: #34d399 !important;"><b>Clôture des candidatures :</b> {b['deadline']}</p>
                    <div class="badge-premium">Financement Disponible</div>
                </div>
            """, unsafe_allow_html=True)

    with col_right:
        st.markdown("#### 💬 Assistant IA Conceptuel (Écrit & Vocal)")
        st.write("Utilisez le clavier ou le micro intégré pour exprimer vos ambitions profondes et ajuster le diagnostic.")
        
        # Le Micro Connecté Directement au Chatbot
        st.components.v1.html("""
            <div style="background-color: #1e293b; border-radius: 12px; padding: 12px; text-align: center; border: 1px dashed #475569;">
                <button id="chat-mic" style="background: linear-gradient(90deg, #ef4444, #f43f5e); color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer;">🎙️ PARLER À L'ASSISTANT VOCAL</button>
            </div>
            <script>
                const btn = document.getElementById('chat-mic');
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                if(SpeechRecognition){
                    const r = new SpeechRecognition(); r.lang = 'fr-FR';
                    btn.onclick = () => { r.start(); btn.innerText = "⚡ Écoute en cours..."; };
                    r.onresult = (e) => { 
                        window.parent.postMessage({type: 'streamlit:set_input', value: e.results[0][0].transcript}, '*'); 
                        btn.innerText = "🎙️ Micro Activé"; 
                    };
                }
            </script>
        """, height=75)
        
        # Récupération de la voix comme un message input alternatif
        voice_capture = st.text_input("Message dicté par la voix :", key="voice_bridge", placeholder="Votre enregistrement vocal se transformera ici en texte...")
        
        if "chat_matrix" not in st.session_state:
            st.session_state.chat_matrix = [
                {"role": "ai", "text": f"Analyse initiale terminée. Le profil montre des prédispositions pour : {active_data['label']}. Décrivez-moi vos doutes, vos contraintes financières ou vos rêves d'avenir par écrit ou avec le micro pour affiner notre feuille de route !"}
            ]
            
        # Rendu visuel du chat
        chat_container = st.container()
        with chat_container:
            for m in st.session_state.chat_matrix:
                if m["role"] == "user":
                    st.markdown(f'<div class="chat-box-user">{m["text"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="chat-box-ai">{m["text"]}</div>', unsafe_allow_html=True)
                    
        # Input écrit standard
        written_msg = st.text_input("Posez une question ou complétez vos ambitions :", key="written_chat_input")
        
        # Déclencheur d'envoi (soit le texte écrit, soit la voix capturée)
        if st.button("Envoyer à l'IA ⚡"):
            active_message = ""
            if written_msg.strip() != "":
                active_message = written_msg
            elif voice_capture.strip() != "":
                active_message = voice_capture
                st.session_state.audio_transcription += " " + voice_capture # Met à jour le corpus pour le moteur
                
            if active_message != "":
                st.session_state.chat_matrix.append({"role": "user", "text": active_message})
                
                # Réponse contextuelle basée sur l'analyse de profil
                time.sleep(0.4)
                text_clean = active_message.lower()
                
                if any(w in text_clean for w in ["bourse", "argent", "financer", "prix"]):
                    ai_reply = "Pour maximiser l'obtention des bourses listées à gauche, l'excellence des notes ne suffit pas. Nous devons packager vos activités extra-scolaires sous forme de projets d'impact. C'est ce que les comités de sélection (comme Eiffel ou Pearson) recherchent."
                elif any(w in text_clean for w in ["médecine", "medecine", "santé", "pharma"]):
                    ai_reply = "Le domaine médical impose des barrières à l'entrée très spécifiques. Si vous visez l'international (comme King's College), la préparation de l'UCAT doit débuter dès maintenant. Pour la France, l'accent doit être mis sur les matières scientifiques de spécialité."
                elif any(w in text_clean for w in ["éco", "eco", "gestion", "business"]):
                    ai_reply = "Le secteur Économie & Gestion demande de fortes compétences analytiques mais aussi une vraie culture générale. Des écoles comme l'UM6P (FGSES) ou l'ISCAE valorisent énormément l'aisance à l'oral et l'esprit critique lors des entretiens."
                else:
                    ai_reply = "Votre dossier possède des bases intéressantes. Pour affiner au mieux cette trajectoire, dites-moi quelles sont vos préférences en termes de langues d'études prioritaires ou vos plus grandes craintes concernant les dossiers."
                    
                st.session_state.chat_matrix.append({"role": "ai", "text": ai_reply})
                st.rerun()

    st.write("---")
    if st.button("🔄 Réinitialiser l'Application d'Orientation"):
        st.session_state.current_step = 1
        if "chat_matrix" in st.session_state: del st.session_state.chat_matrix
        st.session_state.user_written_ambitions = ""
        st.session_state.audio_transcription = ""
        st.rerun()
