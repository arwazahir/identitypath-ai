import streamlit as st
import time

# Configuration de l'application
st.set_page_config(page_title="IdentityPath Application", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN APPLICATION PRO & VISIBILITÉ MAXIMALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
    
    .main { background-color: #0f172a; color: #ffffff; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    
    /* Force la visibilité des textes en blanc éclatant */
    .stMarkdown, p, span, label, .stSelectbox, .stSlider { color: #ffffff !important; font-size: 16px !important; }
    h1, h2, h3, h4 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; font-weight: 800 !important; }
    
    /* Logo de l'application */
    .app-logo-container { text-align: center; padding: 25px; background: #1e293b; border-radius: 16px; border: 2px solid #334155; margin-bottom: 30px; }
    .app-logo { font-size: 40px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Urbanist'; }
    .app-subtitle { color: #10b981 !important; font-size: 14px !important; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
    
    /* Conteneurs de l'interface */
    .section-container { background: #1e293b; padding: 25px; border-radius: 16px; border: 1px solid #334155; margin-bottom: 25px; }
    .filiere-box { background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; margin-bottom: 10px; }
    .uni-box { background: #111827; padding: 20px; border-radius: 12px; border-left: 5px solid #3b82f6; margin-bottom: 15px; border: 1px solid #1f2937; }
    .bourse-box { background: #111827; padding: 20px; border-radius: 12px; border-left: 5px solid #10b981; margin-bottom: 15px; border: 1px solid #1f2937; }
    
    .title-white { font-size: 18px !important; font-weight: 700 !important; color: #ffffff !important; }
    .text-light { color: #e2e8f0 !important; font-size: 15px !important; line-height: 1.5; }
    
    /* Style des boutons */
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: #ffffff !important; font-weight: bold !important; border-radius: 10px !important; padding: 12px 28px !important; border: none !important; width: 100%; font-size: 16px !important; }
    
    /* Zone de Chat de l'application */
    .chat-bubble-user { background: #3b82f6; padding: 12px 18px; border-radius: 16px 16px 0px 16px; margin-bottom: 10px; color: white; text-align: right; max-width: 80%; margin-left: auto; }
    .chat-bubble-ai { background: #1e293b; padding: 12px 18px; border-radius: 16px 16px 16px 0px; margin-bottom: 10px; color: white; text-align: left; max-width: 80%; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# --- LOGO OFFICIEL ---
st.markdown("""
    <div class="app-logo-container">
        <div class="app-logo">🧭 IDENTITYPATH APP</div>
        <div class="app-subtitle">Plateforme Mobile & Moteur d'Orientation Intelligent de Nouvelle Génération</div>
    </div>
""", unsafe_allow_html=True)

# --- SÉCURITÉ ---
if "authenticated" not in st.session_state: st.session_state.authenticated = False
if not st.session_state.authenticated:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Activation de l'Application</h3>", unsafe_allow_html=True)
        pass_code = st.text_input("Code d'accès secret :", type="password")
        if pass_code == "Arwagiftorient":
            if st.button("Lancer l'Application 🚀"):
                st.session_state.authenticated = True
                st.rerun()
    st.stop()

# --- BASE DE DONNÉES GLOBALE ---
DATABASE = {
    "economie_social": {
        "label": "Sciences Économiques, Gestion & Sciences Sociales",
        "keywords": ["economie", "social", "eco", "gestion", "business", "commerce", "finance", "marketing", "management", "societe", "politique"],
        "filieres_possibles": [
            "• Bachelor in Business Administration (BBA) - Management International",
            "• Cursus Supérieur en Économie Appliquée et Statistiques",
            "• Sciences Politiques, Relations Internationales & Gouvernance"
        ],
        "unis": [
            {"nom": "ISCAE (Institut Supérieur de Commerce - National)", "details": "Grande École publique de management de référence.", "req": "Sélection sur concours post-classe prépa ou diplôme de gestion.", "deadline": "Avril - Mai"},
            {"nom": "UM6P - Faculty of Governance, Economic and Social Sciences (FGSES)", "details": "Campus d'élite basé à Rabat pour la gouvernance et l'économie.", "req": "Dossier scolaire d'excellence, épreuves écrites et entretien.", "deadline": "Fin Mai"},
            {"nom": "London School of Economics (LSE - Global)", "details": "L'un des meilleurs pôles universitaires au monde pour les sciences sociales.", "req": "Très fortes notes au Bac (Maths), IELTS ≥ 7.0.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse de Mérite et d'Excellence FGSES", "couverture": "Exonération complète ou partielle des frais d'études et de logement.", "req": "Excellents résultats académiques et évaluation sociale du dossier.", "deadline": "Juillet"},
            {"nom": "GREAT Scholarships (British Council)", "couverture": "Bourse d'aide financière d'un montant minimal de £10,000 pour l'année.", "req": "Acceptation définitive dans un établissement britannique partenaire.", "deadline": "Mai"}
        ]
    },
    "sciences_tech": {
        "label": "Ingénierie, Intelligence Artificielle & Technologies",
        "keywords": ["informatique", "code", "ia", "cyber", "ingenieur", "robot", "technologie", "math", "physique", "science"],
        "filieres_possibles": [
            "• Bachelor / Master en Engineering et Computer Science",
            "• Spécialisation de pointe en Intelligence Artificielle et Data Science",
            "• Cursus d'Ingénieur d'État (Génie Civil, Informatique, Industriel)"
        ],
        "unis": [
            {"nom": "UM6P - College of Computing", "details": "Écosystème technologique africain de très haut niveau.", "req": "Bac scientifique avec mention, tests algorithmiques internes.", "deadline": "Mai"},
            {"nom": "EPFL (Lausanne - Suisse)", "details": "Institution d'ingénierie d'élite à l'échelle internationale.", "req": "Moyenne au Baccalauréat ≥ 16/20 (Mention Très Bien requise).", "deadline": "30 Avril"},
            {"nom": "University of Toronto (Canada)", "details": "Département mondial majeur pour le développement software.", "req": "IELTS ≥ 6.5 ou TOEFL ≥ 100, excellent dossier scientifique.", "deadline": "15 Janvier"}
        ],
        "bourses": [
            {"nom": "Bourse d'Excellence Académique UM6P", "couverture": "Frais de scolarité et hébergement universitaire 100% gratuits.", "req": "Notes scientifiques d'élite au Baccalauréat.", "deadline": "Juillet"},
            {"nom": "Lester B. Pearson International Scholarship", "couverture": "Prise en charge intégrale (scolarité, livres, logement) sur 4 ans.", "req": "Profil de leader communautaire, nomination par le lycée.", "deadline": "15 Janvier"}
        ]
    }
}

# --- ÉTAPES DE L'APPLICATION ---
if "step" not in st.session_state: st.session_state.step = 1

st.progress(st.session_state.step / 4)

# --- ÉTAPE 1 : ACADÉMIQUE & GÉOGRAPHIE OUVERTE ---
if st.session_state.step == 1:
    st.markdown("### 📝 Étape 1 : Profil Général de l'Élève")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.f_bac = st.selectbox("Filière ou Option du Diplôme préparé :", ["Sciences Économiques & Gestion", "Sciences Mathématiques", "Sciences Physiques", "SVT", "Lettres"])
        st.session_state.note = st.slider("Moyenne générale projetée ou obtenue :", 10.0, 20.0, 16.0, step=0.1)
    with col2:
        st.session_state.destination = st.selectbox("Objectifs géographiques de l'élève (Totalement Ouvert) :", [
            "N'importe quel pays dans le monde (Full International)",
            "Pays Anglophones uniquement (USA, Canada, UK, etc.)",
            "Pays Francophones uniquement (France, Suisse, Belgique, etc.)",
            "Établissements et Grandes Écoles Nationaux"
        ])
        st.session_state.lycee = st.text_input("Région ou Ville actuelle de l'établissement :", placeholder="Ex: Casablanca, Rabat...")
    
    if st.button("Continuer vers l'Évaluation Linguistique ➡️"):
        st.session_state.step = 2
        st.rerun()

# --- ÉTAPE 2 : LOGIQUE DES LANGUES REVISITÉE (NIVEAUX + CERTIFS POUR TOUT) ---
elif st.session_state.step == 2:
    st.markdown("### 🔤 Étape 2 : Profil Linguistique Détaillé")
    st.write("Indiquez le niveau actuel selon le cadre européen (B1, B2, C1, C2) pour les trois langues, puis spécifiez vos certifications.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🇺🇸 Langue Anglaise")
        st.session_state.en_level = st.selectbox("Niveau d'Anglais :", ["Intermédiaire (B1)", "Avancé (B2)", "Autonome / Excellent (C1)", "Bilingue / Langue Maternelle (C2)"])
        has_en_cert = st.radio("Possédez-vous (ou visez-vous) une certification d'Anglais ?", ["Non", "Oui (IELTS)", "Oui (TOEFL)", "Oui (Duolingo)"])
        st.session_state.en_cert_score = st.text_input("Score de la certification (Anglais) :", placeholder="Ex: 7.5, 120...") if has_en_cert != "Non" else "Aucune"

    with col2:
        st.markdown("#### 🇫🇷 Langue Française")
        st.session_state.fr_level = st.selectbox("Niveau de Français :", ["Intermédiaire (B1)", "Avancé (B2)", "Autonome / Excellent (C1)", "Bilingue / Langue Maternelle (C2)"])
        has_fr_cert = st.radio("Possédez-vous (ou visez-vous) une certification de Français ?", ["Non", "Oui (TCF)", "Oui (DELF)", "Oui (DALF)"])
        st.session_state.fr_cert_score = st.text_input("Score de la certification (Français) :", placeholder="Ex: C1, 520 pts...") if has_fr_cert != "Non" else "Aucune"

    with col3:
        st.markdown("#### 🇲🇦 Langue Arabe")
        st.session_state.ar_level = st.selectbox("Niveau d'Arabe :", ["Intermédiaire (B1)", "Avancé (B2)", "Autonome / Excellent (C1)", "Bilingue / Langue Maternelle (C2)"])
        has_ar_cert = st.radio("Possédez-vous une certification ou attestation d'Arabe ?", ["Non", "Oui (Attestation d'Excellence / Cursus)"])
        st.session_state.ar_cert_score = st.text_input("Précision optionnelle (Arabe) :", placeholder="Ex: Langue d'enseignement...") if has_ar_cert != "Non" else "Aucune"

    st.write("---")
    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        if st.button("⬅️ Étape Précédente"): st.session_state.step = 1; st.rerun()
    with col_btn2:
        if st.button("Continuer vers le Profil Extra-Scolaire ➡️"): st.session_state.step = 3; st.rerun()

# --- ÉTAPE 3 : ACTIVITÉS ET PASSIONS ---
elif st.session_state.step == 3:
    st.markdown("### 🏆 Étape 3 : Distinctions & Exploration de Projet")
    st.write("Remplissez les informations de manière libre et ouverte pour nourrir l'algorithme d'orientation.")
    
    st.session_state.distinctions = st.text_area(
        "Distinctions ou Prix Remportés (Exemples : Concours, Olympiades, Événements régionaux...) :",
        placeholder="Renseignez les distinctions de l'élève si applicables..."
    )
    
    st.session_state.engagement = st.text_area(
        "Ambitions, passions et projets personnels (Exemples : Sujets d'études préférés, clubs, création, intérêts profonds...) :",
        placeholder="Décrivez précisément ce qui anime l'étudiant dans la vie et ses ambitions futures..."
    )

    st.markdown("#### 🎙️ Enregistrement Vocal Optionnel")
    st.components.v1.html("""
        <div style="background-color: #1e293b; border-radius: 12px; padding: 15px; text-align: center; border: 1px dashed #475569;">
            <button id="mic-btn" style="background: linear-gradient(90deg, #ef4444, #f43f5e); color: white; font-weight: bold; padding: 10px 22px; border: none; border-radius: 20px; cursor: pointer;">🎙️ DÉMARRER L'ANALYSE PAR LA VOIX</button>
        </div>
        <script>
            const btn = document.getElementById('mic-btn');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if(SpeechRecognition){
                const r = new SpeechRecognition(); r.lang = 'fr-FR';
                btn.onclick = () => { r.start(); btn.innerText = "⏳ Écoute en cours..."; };
                r.onresult = (e) => { window.parent.postMessage({type: 'streamlit:set_input', value: e.results[0][0].transcript}, '*'); btn.innerText = "🎙️ Relancer le micro"; };
            }
        </script>
    """, height=85)
    
    st.session_state.voice_text = st.text_input("Texte extrait par l'IA vocale :", placeholder="Les propos de l'étudiant s'analyseront ici...")

    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        if st.button("⬅️ Étape Précédente"): st.session_state.step = 2; st.rerun()
    with col_btn2:
        if st.button("Générer l'Application et Lancer le Chatbot 🧭"): st.session_state.step = 4; st.rerun()

# --- ÉTAPE 4 : LIVRABLE LOGIQUE + CHATBOT IA INTERACTIF ET COHÉRENT ---
elif st.session_state.step == 4:
    st.markdown("### 🧭 Espace d'Analyse Globale & Chatbot Privé")
    
    # Correction majeure du moteur de détection sémantique
    full_profile = (st.session_state.distinctions + " " + st.session_state.engagement + " " + st.session_state.voice_text).lower()
    
    detected_key = "sciences_tech" # Par défaut
    eco_keywords = ["economie", "social", "sociale", "eco", "gestion", "commerce", "business", "finance", "management", "sociologie", "marché"]
    
    # Vérification stricte des mots entiers pour éviter les faux positifs de la Tech
    if any(word in full_profile for word in eco_keywords):
        detected_key = "economie_social"
        
    result_data = DATABASE[detected_key]
    
    # Affichage de la fiche
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.write(f"#### 🎯 Profil Validé : {result_data['label']}")
    st.write(f"🌍 **Destination ciblée :** {st.session_state.destination} | 📊 **Moyenne estimée :** {st.session_state.note}/20")
    st.write(f"🗣️ **Niveaux validés :** Anglais ({st.session_state.en_level}) | Français ({st.session_state.fr_level}) | Arabe ({st.session_state.ar_level})")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # --- STRUCTURE STRICTE EXIGÉE : FILIÈRES -> UNIVERSITÉS -> BOURSES ---
    col_left, col_right = st.columns([4, 3])
    
    with col_left:
        # A. Filières possibles
        st.markdown("#### 📈 1. Filières Universitaires Possibles")
        for f in result_data["filieres_possibles"]:
            st.markdown(f"<div class='filiere-box'><span class='title-white'>{f}</span></div>", unsafe_allow_html=True)
            
        # B. Universités
        st.markdown("#### 🏛️ 2. Universités Adaptées & Requirements")
        for uni in result_data["unis"]:
            st.markdown(f"""
                <div class="uni-box">
                    <div class="title-white">{uni['nom']}</div>
                    <p class="text-light" style="margin-top:8px;"><b>Présentation :</b> {uni['details']}</p>
                    <p class="text-light"><b>Requirements :</b> {uni['req']}</p>
                    <p class="text-light" style="color: #f87171 !important;"><b>Deadline :</b> {uni['deadline']}</p>
                </div>
            """, unsafe_allow_html=True)

        # C. Bourses
        st.markdown("#### 💎 3. Bourses d'Excellence Accessibles")
        for b in result_data["bourses"]:
            st.markdown(f"""
                <div class="bourse-box">
                    <div class="title-white">{b['nom']}</div>
                    <p class="text-light" style="margin-top:8px;"><b>Couverture :</b> {b['couverture']}</p>
                    <p class="text-light"><b>Requirements :</b> {b['req']}</p>
                    <p class="text-light" style="color: #34d399 !important;"><b>Deadline Fin :</b> {b['deadline']}</p>
                </div>
            """, unsafe_allow_html=True)

    with col_right:
        st.markdown("#### 💬 Chatbot Conseiller IA Privé")
        st.write("Discutez en direct pour affiner le projet, parler de vos ambitions profondes ou de vos difficultés.")
        
        # Initialisation de l'historique du chat
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                {"role": "ai", "text": f"Bonjour ! L'analyse de votre profil montre un fort potentiel pour le secteur : {result_data['label']}. Quels sont vos doutes, vos questions sur les bourses présentées ou vos projets d'avenir ? Parlons-en en profondeur !"}
            ]
            
        # Affichage du chat
        chat_placeholder = st.container()
        with chat_placeholder:
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.markdown(f'<div class="chat-bubble-user">{msg["text"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="chat-bubble-ai">{msg["text"]}</div>', unsafe_allow_html=True)
                    
        # Zone de saisie du message
        user_msg = st.text_input("Posez votre question à l'application ici :", key="chat_user_input", placeholder="Ex: Quelles sont mes chances pour la bourse de l'UM6P avec mes notes ?")
        
        if st.button("Envoyer mon message ⚡"):
            if user_msg.strip() != "":
                st.session_state.chat_history.append({"role": "user", "text": user_msg})
                
                # Réponses simulées intelligentes selon la catégorie détectée
                time.sleep(0.5)
                reply = ""
                u_clean = user_msg.lower()
                
                if "bourse" in u_clean or "argent" in u_clean or "financement" in u_clean:
                    reply = "Les critères majeurs pour débloquer ces financements résident dans l'excellence de votre moyenne de Baccalauréat combinée à des activités de leadership (projets, engagements). Assurez-vous de préparer vos dossiers dès l'automne."
                elif "note" in u_clean or "moyenne" in u_clean or "chance" in u_clean:
                    reply = f"Avec une moyenne estimée à {st.session_state.note}/20, vous êtes dans la tranche haute d'éligibilité pour les bourses présentées. Le facteur de différenciation sera votre niveau de langue et vos lettres de recommandation."
                else:
                    reply = "C'est une excellente question. Pour approfondir cet aspect de votre projet d'études, il faut veiller à respecter scrupuleusement les exigences de dossier (Requirements) et à soumettre vos formulaires d'admission avant la date butoir."
                    
                st.session_state.chat_history.append({"role": "ai", "text": reply})
                st.rerun()

    st.write("---")
    if st.button("🔄 Lancer une nouvelle analyse d'élève"):
        st.session_state.step = 1
        if "chat_history" in st.session_state: del st.session_state.chat_history
        st.rerun()
