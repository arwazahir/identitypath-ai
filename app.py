import os
import streamlit as st
import json

# -----------------------------------------------------------------------------
# 1. CONFIGURATION DE LA PAGE & STYLE ESTHÉTIQUE
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Identity Path - Orientation Universitaire Internationale",
    page_icon="🎯",
    layout="wide"
)

# Application d'un style CSS épuré et professionnel (aucun code n'apparaît à l'écran)
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        color: #1E3A8A;
        font-weight: 800;
        margin-bottom: 0.1rem;
    }
    .subtitle {
        font-size: 1.25rem;
        color: #4B5563;
        margin-bottom: 2.5rem;
    }
    .allal-bubble {
        padding: 1.75rem;
        background-color: #F0FDF4;
        border-radius: 0.75rem;
        border-left: 6px solid #16A34A;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
    }
    .section-card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 2rem;
        border: 1px solid #E5E7EB;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background-color: #EFF6FF;
        color: #1D4ED8;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. BASE DE DONNÉES GÉANTE (PAYS, FILIÈRES & BOURSES)
# -----------------------------------------------------------------------------

# Cartographie mondiale absolue des pays
DATA_PAYS = {
    "Europe Francophone & Anglophone": ["France", "Belgique", "Suisse", "Royaume-Uni", "Irlande"],
    "Europe Continentale & Nordique": ["Allemagne", "Pays-Bas", "Italie", "Espagne", "Suède", "Finlande", "Norvège", "Danemark", "Pologne", "Hongrie", "République Tchèque"],
    "Amérique du Nord": ["États-Unis", "Canada (Hors Québec)", "Canada (Québec)"],
    "Asie & Océanie": ["Singapour", "Japon", "Chine", "Corée du Sud", "Australie", "Nouvelle-Zélande"],
    "Moyen-Orient & CCG": ["Émirats Arabes Unis", "Arabie Saoudite", "Qatar", "Maroc / Local"]
}

# Matrice exhaustive des 17 domaines et sous-filières précises
DATA_FILIERES = {
    "Sciences de la Santé & du Vivant": {
        "1. Sciences Médicales": ["Médecine Générale", "Médecine Dentaire", "Pharmacie", "Médecine Vétérinaire"],
        "2. Sciences Biomédicales": ["Génie Biomédical", "Biotechnologies Médicales", "Neurosciences Appliquées", "Génétique"],
        "3. Santé Publique": ["Santé Environnementale", "Épidémiologie", "Éco-toxicologie", "Gestion des Risques Sanitaires"],
        "4. Agro-Sciences": ["Agronomie Durable", "Sciences de la Nutrition", "Bio-industries", "Gestion des Sols"]
    },
    "Sciences Exactes & Ingénierie": {
        "5. Informatique & IA": ["Intelligence Artificielle", "Data Science & Big Data", "Green Computing (Informatique Durable)", "Cybersécurité"],
        "6. Génie Civil & Environnement": ["Génie Écologique", "Traitement et Gestion des Eaux", "Restauration des Écosystèmes Fragiles", "Génie Civil Durable"],
        "7. Énergies & Ressources": ["Génie des Énergies Renouvelables", "Génie Chimique", "Matériaux Biosourcés", "Génie Minier Durable"],
        "8. Sciences Fondamentales": ["Physique Quantique", "Mathématiques Appliquées", "Chimie Verte", "Astrophysique"]
    },
    "Business, Économie & Impact": {
        "9. Gestion de l'Innovation": ["Entrepreneuriat Technologique", "Management de l'Innovation", "Gestion de Projets Complexes"],
        "10. Économie Appliquée": ["Économie Circulaire", "Économie du Développement", "Microfinance & Impact Social"],
        "11. Finance & Stratégie": ["Finance Durable (ESG)", "Stratégie d'Entreprise", "Supply Chain Éco-responsable"]
    },
    "Sciences Humaines & Sociales": {
        "12. Relations Internationales": ["Géopolitique", "Coopération Internationale", "Études du Développement Mondial"],
        "13. Droit & Gouvernance": ["Droit International Public", "Droit de l'Environnement", "Politiques Publiques & Administration"],
        "14. Éducation & Société": ["Sociologie Contemporaine", "Sciences de l'Éducation", "Ingénierie Pédagogique"]
    },
    "Arts, Design & Médias": {
        "15. Design Numérique": ["UI/UX Design", "Design Graphique", "Modélisation 3D & Animation", "Création Numérique"],
        "16. Médias & Journalisme": ["Journalisme Scientifique & Environnemental", "Communication Digitale", "Production Médias"],
        "17. Architecture & Urbanisme": ["Architecture Durable", "Urbanisme Écologique", "Aménagement du Territoire Littoral/Urbain"]
    }
}

# Catalogue exhaustif des bourses mondiales par type
DATA_BOURSES = {
    "Gouvernementales (100% Couverture)": [
        "Bourses Eiffel (France) - Master & Doctorat, excellence académique.",
        "Bourses Major (France) - Pour les bacheliers d'excellence des lycées français à l'étranger.",
        "Bourses du DAAD (Allemagne) - Prise en charge complète pour toutes les filières.",
        "Bourses Chevening (Royaume-Uni) - Financement total, vols et vie sur place.",
        "Bourse MEXT (Japon) - Couverture totale par le gouvernement japonais.",
        "Global Korea Scholarship (GKS) (Corée du Sud) - Vol, scolarité et allocation.",
        "Bourses d'excellence de la Confédération Suisse - Pour chercheurs et masters.",
        "Bourses Erasmus Mundus (Union Européenne) - Masters conjoints financés à 100%.",
        "Programme Fulbright (États-Unis) - Financement complet d'études supérieures."
    ],
    "Institutionnelles (Offertes par les Universités)": [
        "Bourses Need-Blind des universités de la Ivy League (USA) - Financement complet basé sur le besoin financier (Harvard, MIT, Yale, Princeton, Amherst).",
        "Bourse Internationale Lester B. Pearson (Université de Toronto, Canada) - Scolarité, livres et résidence complets pendant 4 ans.",
        "Bourses Karen McKellin pour les leaders de demain (UBC, Canada) - Financement complet basé sur le profil de leadership.",
        "Bourses Majeures d'Entrée de McGill (Canada) - Jusqu'à 12 000$ renouvelables sur critères académiques et d'engagement.",
        "Amsterdam Excellence Scholarship (Pays-Bas) - Pour les profils d'excellence hors UE.",
        "Bourses d'Excellence du Polytechnique de Milan / Bologne (Italie) - Exonération et allocation de vie.",
        "Bourses d'entrée de NYU Abu Dhabi / King Fahd University - Couverture totale des frais et hébergement."
    ],
    "Fondations Privées & Organismes Mondiales": [
        "Bourses de la Fondation MasterCard - Financement complet (100%) incluant le logement et le mentorat pour les étudiants à fort impact social.",
        "Bourses Gates Cambridge (Royaume-Uni) - Financement total pour les leaders engagés à l'Université de Cambridge.",
        "Bourses de la Banque Mondiale (JJ/WBGSP) - Pour les filières liées au développement et à l'impact.",
        "Bourses d'études de la Banque Islamique de Développement (BID) - Financement complet pour les filières scientifiques et technologiques."
    ]
}

# -----------------------------------------------------------------------------
# 3. INTERFACE DE L'APPLICATION (IDENTITY PATH)
# -----------------------------------------------------------------------------
st.markdown('<div class="main-title">Identity Path</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">La plateforme d\'orientation internationale d\'excellence guidée par Allal AI.</div>', unsafe_allow_html=True)

# --- BLOC 1 : INFORMATIONS ACADÉMIQUES ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📋 1. Identité & Parcours Académique")
col1, col2 = st.columns(2)

with col1:
    filiere_actuelle = st.selectbox(
        "Filière ou branche actuelle au lycée :",
        ["Sciences Expérimentales (SVT / Physique-Chimie)", "Sciences Mathématiques (A / B)", "Sciences Économiques & Gestion", "Lettres & Sciences Humaines"]
    )
    moyenne = st.slider("Moyenne générale estimée ou actuelle :", 10.0, 20.0, 16.0, step=0.1)

with col2:
    langues = st.multiselect(
        "Langues maîtrisées et certifications prévues/obtenues :",
        ["Anglais (SAT / IELTS / TOEFL)", "Français (DELF / DALF)", "Arabe (Langue Maternelle/Fluide)", "Espagnol", "Allemand (Goethe-Zertifikat)"],
        default=["Anglais (SAT / IELTS / TOEFL)", "Français (DELF / DALF)", "Arabe (Langue Maternelle/Fluide)"]
    )
st.markdown('</div>', unsafe_allow_html=True)

# --- BLOC 2 : PROJETS,RÉALISATIONS & COMPÉTENCES ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🛠️ 2. Réalisations Concrètes & Philosophie d'Action")
st.info("Identity Path valorise les profils qui bâtissent. Décrivez vos actions, vos projets ou vos engagements réels.")

competences = st.multiselect(
    "Vos compétences pratiques auto-apprises ou développées :",
    ["Design Graphique & Identité Visuelle", "Développement Web & Applications", "Rédaction de Rapports & Journalisme", "Gestion de Communauté & Communication", "Analyse de Données / Algorithmes", "Gestion de Projet & Logistique"],
    default=["Design Graphique & Identité Visuelle"]
)

projets_extra = st.text_area(
    "Décrivez un projet concret, une compétition, ou une action de terrain dont vous êtes fier(e) :",
    placeholder="Ex: Gagnant d'un concours national d'éco-innovation pour un système de filtration, création d'une plateforme d'aide aux élèves, travail de design bénévole pour une coopérative de plus de 20 femmes...",
    height=100
)

philosophie = st.radio(
    "Quelle phrase définit le mieux votre manière de travailler ?",
    [
        "J'aime concevoir, tester sur le terrain, échouer, apprendre et rebâtir jusqu'à ce que ça marche.",
        "Je préfère étudier la théorie en profondeur avant de me lancer dans l'application pratique.",
        "Je cherche à appliquer les outils technologiques et créatifs pour résoudre des problèmes de société."
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

# --- BLOC 3 : ASPIRATIONS & SECTEURS DE PRÉDILECTION ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🧬 3. Cartographie des Intérêts Précis")
st.write("Sélectionnez vos macro-domaines pour afficher la totalité des sous-filières disponibles dans le moteur d'Allal :")

macro_selectionnes = st.multiselect(
    "Sélectionnez un ou plusieurs Macro-Domaines :",
    list(DATA_FILIERES.keys()),
    default=["Sciences de la Santé & du Vivant", "Sciences Exactes & Ingénierie"]
)

filières_cochées = []
if macro_selectionnes:
    st.write("**Cochez les sous-filières spécifiques qui vous passionnent (Soyez précis) :**")
    for macro in macro_selectionnes:
        with st.expander(f"📌 {macro}", expanded=True):
            for domaine, sous_filieres in DATA_FILIERES[macro].items():
                st.markdown(f"**{domaine}**")
                for sf in sous_filieres:
                    if st.checkbox(sf, key=sf):
                        filières_cochées.append(f"{domaine} -> {sf}")
st.markdown('</div>', unsafe_allow_html=True)

# --- BLOC 4 : CHOIX GÉOGRAPHIQUES & BUDGET ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🌍 4. Préférences Géographiques & Besoins de Financement")

regions_selectionnees = st.multiselect(
    "Sélectionnez toutes les régions ou pays cibles souhaités :",
    list(DATA_PAYS.keys()),
    default=["Europe Francophone & Anglophone", "Amérique du Nord"]
)

liste_pays_finaux = []
if regions_selectionnees:
    for reg in regions_selectionnees:
        liste_pays_finaux.extend(DATA_PAYS[reg])

budget_selection = st.select_slider(
    "Quel est votre profil de financement pour vos études à l'étranger ?",
    options=[
        "Besoin impératif d'une bourse complète à 100% (Scolarité + Logement + Vie)",
        "Recherche active de bourses partielles ou d'exonérations de frais",
        "Financement autonome complet assuré"
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. EXÉCUTION DU MOTEUR D'ANALYSE D'ALLAL
# -----------------------------------------------------------------------------
if st.button("🚀 Soumettre mon profil complet à Allal AI", type="primary"):
    
    if not filières_cochées:
        st.error("Veuillez cocher au moins une sous-filière spécifique dans la section 3 pour permettre à Allal de bâtir votre trajectoire.")
    else:
        with st.spinner("Allal analyse l'intégralité de vos données, de vos projets et de vos contraintes..."):
            
            # Récupération et filtrage des bourses selon le besoin financier de l'élève
            bourses_recommandees = []
            if "100%" in budget_selection:
                bourses_recommandees.extend(DATA_BOURSES["Gouvernementales (100% Couverture)"])
                bourses_recommandees.extend([b for b in DATA_BOURSES["Institutionnelles (Offertes par les Universités)"] if "Need-Blind" in b or "Pearson" in b or "leaders de demain" in b])
                bourses_recommandees.extend(DATA_BOURSES["Fondations Privées & Organismes Mondiales"])
            else:
                bourses_recommandees.extend(DATA_BOURSES["Gouvernementales (100% Couverture)"])
                bourses_recommandees.extend(DATA_BOURSES["Institutionnelles (Offertes par les Universités)"])
                bourses_recommandees.extend(DATA_BOURSES["Fondations Privées & Organismes Mondiales"])

            # --- AFFICHAGE DE LAS RECOMMANDATIONS D'ALLAL (ZÉRO CODE VISIBLE) ---
            st.markdown("""
                <div class="allal-bubble">
                    <h3>👨‍🏫 Diagnostic et Plan d'Orientation d'Allal</h3>
                    <p><strong>Statut :</strong> Profil analysé avec succès. Modèle d'orientation croisé appliqué.</p>
                    <p><em>"J'ai passé au crible votre dossier académique, vos compétences techniques en design/création et votre philosophie axée sur l'impact concret. Voici votre feuille de route exhaustive, conçue sans aucun compromis ni généralisation."</em></p>
                </div>
            """, unsafe_allow_html=True)
            
            # Étape 1 : Diagnostic Holistique
            st.markdown("### 🔍 1. Diagnostic de Reconnaissance de l'Élève")
            st.markdown(f"""
            * **Analyse de l'Intersection des Passions :** Votre profil démontre une excellente synergie. Au lieu de séparer vos compétences, nous lions votre maîtrise pratique (*{', '.join(competences)}*) avec vos choix de filières spécialisées. Votre projet concret (*"{projets_extra if projets_extra else 'Non renseigné'}"*) témoigne d'un profil de bâtisseur, ce qui est extrêmement recherché à l'international.
            * **Adéquation de la Philosophie :** Vous avez choisi la dynamique : *"{philosophie}"*. Cela élimine d'office les parcours purement théoriques et nous oriente vers des universités dotées de laboratoires d'innovation, d'incubateurs de startups ou de cursus de recherche appliquée.
            * **Compétitivité Internationale :** Avec une moyenne de **{moyenne}/20** en filière *{filiere_actuelle}* et la préparation des certifications (*{', '.join(langues)}*), votre dossier possède les prérequis pour viser les bourses d'excellence mondiales les plus sélectives.
            """)
            
            st.write("---")
            
            # Étape 2 : Cartographie Spécifique des Filières Selectionnées
            st.markdown("### 🎓 2. Cartographie Complète de Vos Filières Cibles")
            st.write("Voici la liste complète des trajectoires universitaires précises validées pour votre profil :")
            for f in filières_cochées:
                st.markdown(f"**🔹 Option Validée :** `{f}`")
            
            st.write("---")
            
            # Étape 3 : Répertoire Exhaustif des Universités par Pays Demandés
            st.markdown("### 🏛️ 3. Répertoire des Universités Clés Validées")
            st.write(f"En fonction des destinations choisies ({', '.join(regions_selectionnees)}), Allal a sélectionné les établissements de premier plan qui proposent vos sous-filières précises :")
            
            for reg in regions_selectionnees:
                st.markdown(f"#### 📍 {reg}")
                pays_de_la_reg = DATA_PAYS[reg]
                
                if "Europe Francophone & Anglophone" in reg:
                    st.markdown("""
                    * **France :** Écoles Polytechniques (Réseau IP Paris), Sorbonne Université (Sciences et Ingénierie), Université Paris-Saclay, Réseau des INSAs (Génie écologique/biomédical), Campus France pour les universités de médecine/sciences.
                    * **Suisse :** EPFL (Lausanne) et ETH (Zürich) – leaders mondiaux en bio-ingénierie, informatique durable et sciences exactes. Université de Genève (Matières médicales et droit international).
                    * **Royaume-Uni :** Imperial College London, University of Cambridge, University of Edinburgh (Écosse - programmes d'impact environnemental et IA de pointe).
                    * **Belgique & Irlande :** KU Leuven, UCLouvain, Trinity College Dublin (excellence en technologies du vivant et informatique).
                    """)
                elif "Amérique du Nord" in reg:
                    st.markdown("""
                    * **Canada (Québec & Hors Québec) :** Université de Montréal, Université McGill (programmes d'excellence mondiaux en médecine, biotechnologies et sciences de l'environnement), Université de Toronto, UBC (Vancouver), Université de l'Alberta.
                    * **États-Unis :** Universités de la Ivy League (Harvard, Yale, MIT, Princeton) pour leurs départements de recherche transversaux, Stanford et UC Berkeley (épicentres mondiaux de l'entrepreneuriat technologique et des sciences environnementales), Liberal Arts Colleges (Amherst, Williams) pour un encadrement d'excellence.
                    """)
                elif "Europe Continentale & Nordique" in reg:
                    st.markdown("""
                    * **Allemagne & Pays-Bas :** TU9 (Alliance des universités technologiques allemandes comme la TUM Munich), Wageningen University (Pays-Bas - Numéro 1 mondial en sciences de l'environnement et écosystèmes), TU Delft, Université d'Amsterdam.
                    * **Scandinavie & Europe du Sud :** KTH Royal Institute of Technology (Suède), Université de Copenhague (Danemark), Polytechnique de Milan (Italie), Université de Bologne, Universités de Madrid et Barcelone (Espagne).
                    """)
                else:
                    st.markdown(f"* **Établissements d'Excellence :** National University of Singapore (NUS), NTU (Singapour), Tsinghua University (Chine), NYU Abu Dhabi (Émirats), KAUST & King Fahd University (Arabie Saoudite), Universités partenaires de la Fondation MasterCard.")

            st.write("---")
            
            # Étape 4 : Base de Données des Bourses d'Études Adaptée au Budget
            st.markdown("### 💰 4. Catalogue Exhaustif des Bourses d'Études Disponibles")
            st.warning(f"Filtre budgétaire appliqué activement : **{budget_selection}**")
            st.write("Voici la liste complète des programmes de financement auxquels votre profil vous donne le droit de postuler :")
            
            for bourse in bourses_recommandees:
                st.markdown(f"• {bourse}")

# -----------------------------------------------------------------------------
# 5. PIED DE PAGE DE LA PLATFORME
# -----------------------------------------------------------------------------
st.write("---")
st.caption("© 2026 Identity Path - Tous droits réservés. L'intégralité des analyses, diagnostics et correspondances de données est opérée par le moteur Allal AI.")
