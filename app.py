import streamlit as st

# --- CONFIGURATION PREMIUM ---
st.set_page_config(page_title="IdentityPath AI | Global Master Engine", page_icon="🧭", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    body, [data-testid="stAppViewContainer"] { background-color: #060a12; color: white; font-family: 'Plus Jakarta Sans', sans-serif; }
    .stButton>button { background: linear-gradient(90deg, #2563eb, #059669); color: white; border-radius: 12px; width: 100%; font-weight: 700; padding: 15px; border: none; }
    .card { background: #0b111e; padding: 20px; border-radius: 16px; border: 1px solid #1e293b; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES GLOBALE EXHAUSTIVE ---
DB = {
    "Santé & Vivant": {
        "filières": ["Médecine", "Biotechnologies", "Neurosciences", "Éco-toxicologie", "Agronomie Durable"],
        "unis": ["Wageningen University (Pays-Bas)", "Karolinska Institutet (Suède)", "McGill (Canada)", "FMP (Maroc)", "KAUST (Arabie)"],
        "bourses": ["Bourse Eiffel (France)", "DAAD (Allemagne)", "MasterCard Foundation", "Bourses MEXT (Japon)"]
    },
    "Tech, IA & Ingénierie": {
        "filières": ["IA & Data Science", "Génie Civil & Environnement", "Énergies Renouvelables", "Informatique Quantique"],
        "unis": ["MIT (USA)", "EPFL (Suisse)", "NUS (Singapour)", "1337 (Maroc)", "TU Delft (Pays-Bas)", "Tsinghua (Chine)"],
        "bourses": ["SINGA (Singapour)", "KAUST Fellowships", "Bourse d'Excellence EPFL", "Türkiye Bursları"]
    },
    "Business & Stratégie": {
        "filières": ["Management de l'Innovation", "Finance Durable", "Supply Chain", "Entrepreneuriat"],
        "unis": ["HEC Paris (France)", "LSE (UK)", "Wharton (USA)", "ABS UM6P (Maroc)", "Rotterdam School of Mgmt"],
        "bourses": ["Bourse Eiffel", "Fondation Al Ghurair", "Bourse Érasmus+", "Bourses Lester B. Pearson"]
    },
    "Design, Arts & Archi": {
        "filières": ["Architecture Durable", "UI/UX Design", "Design Industriel", "Urbanisme"],
        "unis": ["Politecnico di Milano (Italie)", "UAL (UK)", "Parsons (USA)", "ENA (Maroc)", "SAP+D UM6P"],
        "bourses": ["Bourse DSU (Italie)", "Bourse d'Excellence SAP+D", "British Council GREAT", "Türkiye Bursları"]
    }
}

# --- LOGIQUE DE L'APP ---
st.title("🧭 IdentityPath AI - Global Engine")

if "step" not in st.session_state: st.session_state.step = 1

if st.session_state.step == 1:
    st.subheader("Authentification Premium")
    token = st.text_input("Code Promo / Token ($0) :", type="password")
    if token == "Arwagiftorient":
        if st.button("Démarrer le Profilage"):
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.subheader("Générateur de Trajectoire")
    domaine = st.selectbox("Choisir le Macro-Domaine :", list(DB.keys()))
    note = st.slider("Moyenne au Bac :", 10.0, 20.0, 16.0)
    besoin = st.selectbox("Besoin de financement :", ["100% Bourse", "Partiel", "Autonomie"])
    
    if st.button("Générer mon Mapping Universel"):
        st.session_state.res = DB[domaine]
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    data = st.session_state.res
    st.subheader("Ton Mapping Stratégique")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='card'><h3>🎓 Filières</h3>{', '.join(data['filières'])}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><h3>🏛️ Universités</h3>{', '.join(data['unis'])}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><h3>💰 Bourses & Requirements</h3>{', '.join(data['bourses'])}<br><br><b>Requirements :</b><br>• IELTS/TOEFL<br>• Lettre de motivation<br>• Relevés de notes officiels</div>", unsafe_allow_html=True)
    
    if st.button("Relancer une analyse"):
        st.session_state.step = 2
        st.rerun()
