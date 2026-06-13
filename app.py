import streamlit as st
import time

# Configuration de la page avec un titre et une mise en page large
st.set_page_config(page_title="IdentityPath AI | L'Orientation du Futur", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN & BRANDING PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
    
    /* Global Styles */
    .main { background-color: #0f172a; color: #f8fafc; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #0f172a; font-family: 'Inter', sans-serif; }
    
    /* Headers & Typography */
    h1, h2, h3 { font-family: 'Urbanist', sans-serif; color: #ffffff !important; }
    
    /* Custom Brand Header */
    .brand-header { text-align: center; padding: 40px 20px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 24px; border: 1px solid #334155; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .brand-logo { font-size: 46px; font-weight: 800; background: linear-gradient(90deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .brand-tagline { color: #94a3b8; font-size: 18px; margin-top: 10px; font-weight: 500; }
    
    /* Professional Cards for Results */
    .uni-card { background: #1e293b; padding: 25px; border-radius: 16px; border-left: 6px solid #10b981; margin-bottom: 20px; border-top: 1px solid #334155; border-right: 1px solid #334155; border-bottom: 1px solid #334155; }
    .uni-title { font-size: 22px; font-weight: 700; color: #ffffff; margin-bottom: 10px; font-family: 'Urbanist'; }
    .uni-det { color: #cbd5e1; font-size: 16px; line-height: 1.6; }
    .badge { background: #334155; color: #10b981; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; display: inline-block; margin-top: 10px; }
    
    /* Form & Input Adjustments */
    .stTextInput>div>div>input { background-color: #1e293b !important; color: white !important; border: 1px solid #334155 !important; border-radius: 12px !important; padding: 12px !important; }
    .stButton>button { background: linear-gradient(90deg, #3b82f6, #10b981) !important; color: white !important; font-weight: bold !important; border: none !important; border-radius: 12px !important; padding: 12px 30px !important; transition: all 0.3s ease; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4); }
    </style>
""", unsafe_allow_stdio=True)

# --- HEADER DE MARQUE ---
st.markdown("""
    <div class="brand-header">
        <div class="brand-logo">🧭 IDENTITYPATH AI</div>
        <div class="brand-tagline">Transformez vos aspirations en itinéraire universitaire d'excellence</div>
    </div>
""", unsafe_allow_html=True)

# --- CONFIGURATION DU LIEN PRÉ-REQUIS & PREMIUM ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<h3 style='text-align: center;'>🔒 Déverrouiller la Plateforme</h3>", unsafe_allow_html=True)
        st.write("Veuillez entrer votre pass d'accès étudiant pour activer le moteur de filtrage mondial.")
        access_code = st.text_input("Code d'accès / Code Promo", type="password", placeholder="Entre ton code d'accès ici...")
        if access_code == "Arwagiftorient":
            st.success("🎉 Accès Premium Activé avec succès ! Bienvenue sur IdentityPath AI.")
            if st.button("Lancer mon diagnostic d'orientation 🚀"):
                st.session_state.authenticated = True
                st.rerun()
        elif access_code:
            st.error("Code incorrect. Veuillez vérifier vos identifiants.")
    st.stop()

# --- BASE DE DONNÉES GÉANTE D'ORIENTATION ---
UNIVERSAL_DATABASE = {
    "sante": {
        "filiere": "Sciences de la Santé & Médecine",
        "keywords": ["medecine", "sante", "docteur", "dentaire", "pharma", "biologie", "clinique", "chirurgie", "soin"],
        "desc": "Votre profil démontre une vocation pour les sciences du vivant, le diagnostic et l'impact social direct à travers le soin.",
        "institutions": [
            {"nom": "Facultés de Médecine et de Pharmacie (FMP/FMD - Public Maroc)", "details": "Accessible sur concours après un bac scientifique (SM/PC). Formations de 6 à 7 ans.", "badge": "National - Excellence"},
            {"nom": "Universités de Santé Privées (UIASS, UM6SS)", "details": "Cursus d'excellence avec infrastructures hospitalières modernes au Maroc. Sélection sur dossier et entretien.", "badge": "Partenaire National"},
            {"nom": "Parcours PASS / LAS (France)", "details": "Voie d'accès aux études de santé en France. Requiert un excellent dossier académique et une forte autonomie.", "badge": "International - Europe"},
            {"nom": "Pre-Med Tracks (USA / Canada)", "details": "4 ans de Bachelor en sciences suivis du MCAT pour intégrer les prestigieuses Medical Schools américaines.", "badge": "International - Bourses Disponibles"}
        ]
    },
    "tech": {
        "filiere": "Engineering, Intelligence Artificielle & Computer Science",
        "keywords": ["tech", "informatique", "code", "ia", "cyber", "ordinateur", "software", "data", "jeux video", "robot"],
        "desc": "Vous êtes attiré par l'innovation technologique, l'architecture des logiciels, l'analyse de données et la résolution de problèmes algorithmiques complexes.",
        "institutions": [
            {"nom": "UM6P / École 1337 & Green Tech Valley", "details": "Écosystème de pointe en Afrique axé sur le codage en autonomie et la recherche technologique avancée.", "badge": "Fleuron National"},
            {"nom": "Réseau des ENSA / ENSEM / INPT", "details": "Grandes écoles d'ingénieurs publiques marocaines accessibles via prépa intégrée ou concours national.", "badge": "Public - Haut Niveau"},
            {"nom": "EPFL (Suisse) / Polytechnique (France)", "details": "Le sommet mondial de l'ingénierie francophone. Exige une mention Très Bien au Bac (filière SM de préférence).", "badge": "Élite Internationale"},
            {"nom": "MIT / Stanford / Bourses d'Excellence USA", "details": "Programmes de Computer Science majeurs. Nécessite la préparation d'un dossier incluant SAT, IELTS et activités extra-scolaires.", "badge": "Monde - Impact Global"}
        ]
    },
    "business": {
        "filiere": "Business, Management, Entrepreneuriat & Finance",
        "keywords": ["business", "management", "entreprendre", "commerce", "finance", "marketing", "start", "bourse", "gestion"],
        "desc": "Vous possédez une fibre de leader, un esprit stratégique, et une volonté de piloter des projets, de manager des équipes ou de créer vos propres entreprises.",
        "institutions": [
            {"nom": "ISCAE (Institut Supérieur de Commerce et d'Administration des Entreprises)", "details": "La business school publique de référence au Maroc. Accès post-classe prépa ou sur concours sélectif.", "badge": "Élite Nationale"},
            {"nom": "Réseau des ENCG (Écoles Nationales de Commerce et de Gestion)", "details": "Parcours en 5 ans très complets, ouverts aux bacs Éco, Physique et Maths.", "badge": "Public - Grande Insertion"},
            {"nom": "HEC Paris / ESSEC Business School (France)", "details": "Meilleures écoles de management d'Europe. Possibilité d'intégrer après une prépa ECS/ECT ou en admission parallèle.", "badge": "Top Europe"},
            {"nom": "Wharton / London School of Economics (LSE)", "details": "Le pôle d'excellence anglo-saxon pour la finance globale et l'économie politique.", "badge": "Monde - Réseau d'Influence"}
        ]
    },
    "art": {
        "filiere": "Architecture, Art, Design Visuel & Urbanisme",
        "keywords": ["art", "design", "architecture", "dessin", "graphisme", "mode", "urbanisme", "creatif", "cinema"],
        "desc": "Votre profil met en avant une forte sensibilité esthétique, une pensée créative disruptive et un intérêt pour la communication visuelle et la structuration de l'espace.",
        "institutions": [
            {"nom": "ENA (École Nationale d'Architecture - Maroc)", "details": "Le parcours public officiel pour devenir architecte au Maroc. Sélection hyper sélective sur note de bac et concours.", "badge": "Public - Régulé"},
            {"nom": "Écoles Supérieures des Beaux-Arts & EAC", "details": "Spécialisations en arts visuels, design produit et scénographie.", "badge": "Création"},
            {"nom": "Parsons School of Design (New York) / Central Saint Martins (Londres)", "details": "Les références mondiales absolues pour le design et les industries créatives.", "badge": "International - Prestige"},
            {"nom": "Écoles d'Architecture Spécialisées (Belgique / France - ENSA)", "details": "Cursus européens reconnus internationalement avec de fortes composantes en design durable.", "badge": "Europe"}
        ]
    },
    "droit": {
        "filiere": "Droit, Sciences Politiques & Diplomatie",
        "keywords": ["droit", "justice", "avocat", "politique", "diplomatie", "international", "juge", "relations"],
        "desc": "Idéal pour les profils ayant une excellente expression écrite et orale, un esprit critique aiguisé et une passion pour la gouvernance, les lois ou les relations internationales.",
        "institutions": [
            {"nom": "FSJES - Cursus de Droit (Maroc)", "details": "Filières en français ou en arabe débouchant sur les concours de la magistrature, du barreau et de l'administration.", "badge": "Public - Universitaire"},
            {"nom": "Sciences Po Paris (Réseau des IEP)", "details": "La grande école des leaders politiques, diplomates et cadres dirigeants mondiaux.", "badge": "Élite Européenne"},
            {"nom": "Sorbonne / Université Paris-Panthéon-Assas", "details": "Le berceau historique du droit civil. Excellente préparation pour le droit international des affaires.", "badge": "Prestige France"}
        ]
    }
}

# --- PROCESSUS DE L'APPLICATION ---
if "current_step" not in st.session_state:
    st.session_state.current_step = 1

# Barre de progression dynamique et professionnelle
steps = ["1. Informations Académiques", "2. Passions & Exploration", "3. Filtrage & Recommandations"]
st.progress(st.session_state.current_step / 3)

# --- ÉTAPE 1 : ACADÉMIQUE ---
if st.session_state.current_step == 1:
    st.markdown("### 📝 Étape 1 : Votre Profil Académique Actuel")
    st.write("Ces données nous permettent d'éliminer les critères impossibles et de cibler uniquement les établissements viables.")
    
    col1, col2 = st.columns(2)
    with col1:
        filiere_bac = st.selectbox("Quelle est votre filière actuelle (ou visée) ?", ["Sciences Mathématiques (SM)", "Sciences Physiques (PC)", "Sciences de la Vie et de la Terre (SVT)", "Sciences Économiques & Gestion", "Lettres & Sciences Humaines"])
        ville = st.text_input("Dans quelle ville ou lycée étudies-tu ?", placeholder="Ex: Casablanca, Rabat...")
    with col2:
        ambition = st.selectbox("Quel est votre objectif géographique ?", ["Études au Maroc (Public & Privé d'Excellence)", "Études à l'Étranger (Europe, France, Suisse)", "Études Internationales Anglophones (USA, UK, Canada, Asie)", "Peu importe, je vise les meilleures bourses mondiales"])
        note_estimee = st.slider("Quelle est votre moyenne générale actuelle (ou visée) ?", 10.0, 20.0, 15.0, step=0.1)
        
    if st.button("Continuer vers l'analyse des passions ➡️"):
        st.session_state.filiere_bac = filiere_bac
        st.session_state.ville = ville
        st.session_state.ambition = ambition
        st.session_state.note_estimee = note_estimee
        st.session_state.current_step = 2
        st.rerun()

# --- ÉTAPE 2 : EXPLORATION LIBRE (VOCALE OU TEXTE) ---
elif st.session_state.current_step == 2:
    st.markdown("### 🎙️ Étape 2 : Vos Passions & Domaines de Rêve")
    st.write("Ici, pas de case à cocher restrictive. Parlez ou écrivez comme vous le feriez avec un mentor privé. Racontez-nous ce que vous aimez faire (créer, calculer, diriger, soigner, débattre...) et ce qui vous inspire.")
    
    # Intégration du composant d'écoute vocale HTML5 avancé
    st.components.v1.html("""
        <div style="background-color: #1e293b; border-radius: 16px; padding: 20px; text-align: center; border: 1px dashed #3b82f6;">
            <button id="record-btn" style="background: linear-gradient(90deg, #ef4444, #f43f5e); color: white; font-family: sans-serif; font-size: 16px; font-weight: bold; border: none; padding: 12px 28px; border-radius: 50px; cursor: pointer; box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);">
                🔴 CLIQUEZ POUR PARLER (Micro)
            </button>
            <p id="rec-status" style="color: #94a3b8; font-family: sans-serif; margin-top: 12px; font-size: 14px;">Votre navigateur enverra directement votre voix au transcripteur intelligent.</p>
        </div>
        <script>
            const btn = document.getElementById('record-btn');
            const status = document.getElementById('rec-status');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if(!SpeechRecognition) {
                status.innerText = "La commande vocale n'est pas supportée sur ce navigateur. Utilisez la zone de texte ci-dessous !";
                btn.style.display = 'none';
            } else {
                const rec = new SpeechRecognition();
                rec.lang = 'fr-FR';
                btn.addEventListener('click', () => {
                    rec.start();
                    btn.innerText = "⏳ Écoute en cours... Parlez librement.";
                    btn.style.background = "#334155";
                });
                rec.onresult = (e) => {
                    const text = e.results[0][0].transcript;
                    window.parent.postMessage({type: 'streamlit:set_input', value: text}, '*');
                    btn.innerText = "🔴 CLIQUEZ POUR PARLER (Micro)";
                    btn.style.background = "linear-gradient(90deg, #ef4444, #f43f5e)";
                };
                rec.onerror = () => {
                    btn.innerText = "🔴 Recommencer";
                    btn.style.background = "linear-gradient(90deg, #ef4444, #f43f5e)";
                    status.innerText = "Erreur de capture. Veuillez réactiver le micro.";
                };
            }
        </script>
    """, height=130)
    
    user_expression = st.text_area("Votre texte capturé ou écrit à la main :", placeholder="Exemple : J'ai toujours adoré le design, faire de la création de contenu graphique et j'aime aussi beaucoup l'informatique ou l'entrepreneuriat...", height=150)
    
    col_b1, col_b2 = st.columns([1, 5])
    with col_b1:
        if st.button("⬅️ Retour"):
            st.session_state.current_step = 1
            st.rerun()
    with col_b2:
        if st.button("Analyser mon profil & Filtrer les universités mondiales 🧭"):
            if user_expression.strip() == "":
                st.error("Veuillez vous exprimer via le micro ou la zone de texte avant de lancer le filtrage.")
            else:
                st.session_state.user_expression = user_expression
                st.session_state.current_step = 3
                st.rerun()

# --- ÉTAPE 3 : MOTEUR DE FILTRAGE INTELLIGENT & RÉSULTATS ---
elif st.session_state.current_step == 3:
    st.markdown("### 🧭 Vos Itinéraires d'Avenir Personnalisés")
    st.write("Notre moteur d'intelligence a analysé vos propos et a filtré l'ensemble des domaines mondiaux pour retenir la meilleure adéquation.")
    
    text_clean = st.session_state.user_expression.lower()
    matches_found = 0
    
    # Balayage de la base de données universelle
    for key, data in UNIVERSAL_DATABASE.items():
        # Vérification si l'un des mots-clés est présent dans le texte de l'élève
        if any(keyword in text_clean for keyword in data["keywords"]):
            matches_found += 1
            
            # Affichage de la catégorie détectée
            st.markdown(f"#### ✨ Secteur Identifié : {data['filiere']}")
            st.info(data["desc"])
            
            st.write("**🏛️ Établissements & Universités Recommandés :**")
            
            # Génération des cartes d'universités dynamiques
            cols_uni = st.columns(2)
            for idx, inst in enumerate(data["institutions"]):
                target_col = cols_uni[idx % 2]
                with target_col:
                    st.markdown(f"""
                        <div class="uni-card">
                            <div class="uni-title">{inst['nom']}</div>
                            <div class="uni-det">{inst['details']}</div>
                            <div class="badge">{inst['badge']}</div>
                        </div>
                    """, unsafe_allow_html=True)
            st.write("---")
            
    # Si aucun mot-clé ultra-spécifique n'a été intercepté, le robot propose une analyse transversale d'excellence
    if matches_found == 0:
        st.warning("🧐 Votre profil est d'une grande richesse transversale. Aucun pôle unique n'a été restrictif. Voici notre recommandation pour les profils polyvalents :")
        st.markdown("""
            <div class="uni-card" style="border-left-color: #3b82f6;">
                <div class="uni-title">Cursus Pluridisciplinaires & Bourses Mondiales</div>
                <div class="uni-det">Vu votre flexibilité, les filières comme les <b>Classes Préparatoires Commerciales (ECG)</b>, les Bachelors en <b>Sciences Politiques</b> ou les filières <b>Arts & Technologies</b> à l'international sont optimales pour vous laisser le temps de choisir.</div>
                <div class="badge">Recommandation Spéciale IdentityPath</div>
            </div>
        """, unsafe_allow_html=True)
        
    # Section Plan d'Action Dossier d'Excellence
    st.markdown("### 📈 Votre Feuille de Route Stratégique")
    st.write(f"En tant qu'étudiant visant l'excellence depuis votre filière (**{st.session_state.filiere_bac}**), avec une projection de moyenne de **{st.session_state.note_estimee}/20** :")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.metric(label="Statut Dossier", value="Éligible Bourses" if st.session_state.note_estimee >= 16 else "Dossier Standard")
        st.caption("Basé sur vos prévisions de notes et vos ambitions.")
    with col_f2:
        st.metric(label="Prochaine Étape", value="IELTS / SAT" if "Anglophones" in st.session_state.ambition else "Concours Nationaux")
        st.caption("Exigence requise pour votre cible géographique.")
    with col_f3:
        st.metric(label="Optimisation Profil", value="Extra-Scolaire", delta="Prioritaire")
        st.caption("Valorisez vos projets d'innovation et vos engagements.")

    if st.button("🔄 Refaire un nouveau diagnostic d'orientation"):
        st.session_state.current_step = 1
        st.session_state.authenticated = True
        st.rerun()
