import streamlit as st

# 1. CONFIGURATION ET STYLE PREMIUM
st.set_page_config(page_title="Identity Path", layout="wide", page_icon="🎯")

st.markdown("""
    <style>
    /* Design global moderne */
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color: #F1F5F9; }
    .main-title { font-size: 3.5rem; color: #FFFFFF; font-weight: 900; text-align: center; margin-bottom: 2rem; }
    .allal-guide { background: rgba(30, 58, 138, 0.4); border-left: 6px solid #3B82F6; padding: 25px; border-radius: 15px; margin-bottom: 30px; }
    .card { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 20px; }
    h2 { color: #60A5FA; }
    </style>
""", unsafe_allow_html=True)

# 2. BASE DE DONNÉES MASSIVE
DATA_UNIVERSITES = {
    "Europe Francophone & Anglophone": {
        "France": ["École Polytechnique", "Sorbonne Université", "INSA Lyon", "Sciences Po"],
        "Suisse": ["EPFL", "ETH Zürich", "Université de Genève"],
        "UK": ["Imperial College London", "University of Cambridge", "University of Edinburgh"]
    },
    "Amérique du Nord": {
        "Canada": ["Université McGill", "Université de Toronto", "UBC (Vancouver)", "Université de Montréal"],
        "États-Unis": ["MIT", "Stanford", "Harvard", "UC Berkeley", "Amherst College"]
    },
    "Europe Continentale & Nordique": {
        "Pays-Bas": ["Wageningen University", "TU Delft", "Université d'Amsterdam"],
        "Allemagne": ["TU München", "RWTH Aachen", "LMU Munich"],
        "Scandinavie": ["KTH Royal Institute (Suède)", "Université de Copenhague"]
    }
}

# 3. INTERFACE
st.markdown('<div class="main-title">Identity Path</div>', unsafe_allow_html=True)
st.markdown('<div class="allal-guide"><strong>👨‍🏫 Allal :</strong> Je suis ton guide dédié. J\'ai intégré l\'exhaustivité de notre base de données mondiale pour tracer ton chemin. Dis-moi qui tu es, je te dirai où aller.</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    filiere = st.selectbox("Ta filière :", ["Sciences Exp", "Sciences Math", "Économie"])
with col2:
    budget = st.selectbox("Besoin financier :", ["Bourse Complète (100%)", "Bourse Partielle", "Autonome"])

# 4. MOTEUR D'ANALYSE
if st.button("🚀 Allal, génère mon analyse complète"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Ton Diagnostic Allal")
    st.write(f"Analyse approfondie pour : **{filiere}**")
    
    st.write("### 🏛️ Universités cibles (Top-Tier) :")
    for region, pays_list in DATA_UNIVERSITES.items():
        st.write(f"#### {region}")
        for pays, unis in pays_list.items():
            st.write(f"**{pays} :** {', '.join(unis)}")
            
    st.write("### 💰 Bourses recommandées :")
    st.write("✅ **Gouvernementales :** Eiffel (FR), DAAD (DE), Chevening (UK), Fulbright (USA)")
    st.write("✅ **Institutionnelles :** Lester B. Pearson (Toronto), Need-Blind (Ivy League)")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("© 2026 Identity Path - Propulsé par Allal AI")
