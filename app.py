import streamlit as st
import time

st.set_page_config(page_title="IdentityPath AI", page_icon="🚀", layout="centered")

st.title("🚀 IdentityPath AI")
st.subheader("Explore ton potentiel et trace ton orientation à la voix.")

# --- SYSTÈME DE PAIEMENT & CODE PROMO ---
if "payment_done" not in st.session_state:
    st.session_state.payment_done = False

if not st.session_state.payment_done:
    st.write("---")
    st.warning("🔒 L'accès complet à IdentityPath AI est réservé aux membres premium.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Tarif Premium", value="8 USD", delta="Accès à vie")
        st.button("💳 Payer 8$ avec Stripe / Carte", disabled=True, help="Mode simulation activé")
    
    with col2:
        promo_input = st.text_input("🎟️ Tu as un Code Promo ?", placeholder="Entre ton code ici...")
        if promo_input:
            if promo_input == "Arwagiftorient":
                st.success("🎉 Code 'Arwagiftorient' activé ! Accès 100% Gratuit accordé.")
                if st.button("🚀 Entrer dans l'application"):
                    st.session_state.payment_done = True
                    st.rerun()
            else:
                st.error("Code promo invalide. Réessaie !")
    st.stop() # Arrête le code ici tant que le paiement ou code n'est pas validé
# --- FIN DU SYSTÈME DE PAIEMENT ---

# Le reste de l'application s'affiche uniquement si payment_done est True
st.sidebar.success("🎉 Mode Premium Activé !")
voice_active = st.sidebar.checkbox("🔊 Activer la voix du robot", value=True)

if "step" not in st.session_state:
    st.session_state.step = 0

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bienvenue sur IdentityPath AI Premium. Commençons par le début : dans quelle ville ou lycée étudies-tu, et quelle est ta filière ou spécialisation actuelle (Sciences Maths, PC, SVT...) ?"}
    ]

RESPONSES = [
    "C'est une excellente filière ! Avec des notes solides entre 17 et 18, tu as un dossier très prometteur. En dehors des cours, as-tu des projets ou des passions particulières ? Par exemple du graphisme, du bénévolat, ou des concours ?",
    "C'est un profil impressionnant ! L'alliance entre tes compétences de création et ton parcours scientifique est parfaite pour des bourses internationales. Aimerais-tu t'orienter vers l'entrepreneuriat, les nouvelles technologies ou le business management ?",
    "Parfait ! Pour viser ces parcours d'excellence à l'international à la rentrée prochaine, il faudra préparer ton dossier dès octobre/novembre (lettres de recommandation de tes profs, tests de langue ou SAT). Tu es prête à découvrir tes opportunités ?"
]

# --- AUDIO ---
if voice_active and len(st.session_state.messages) > 0:
    last_msg = st.session_state.messages[-1]
    if last_msg["role"] == "assistant":
        clean_text = last_msg["content"].replace("'", "\\'")
        st.components.v1.html(f"""
            <script>
                var msg = new SpeechSynthesisUtterance('{clean_text}');
                msg.lang = 'fr-FR';
                window.speechSynthesis.speak(msg);
            </script>
        """, height=0, width=0)

st.write("### 🎙️ Commande Vocale")
st.components.v1.html("""
    <div style="text-align: center; padding: 10px;">
        <button id="mic-btn" style="padding: 12px 24px; font-size: 16px; font-weight: bold; background-color: #FF4B4B; color: white; border: none; border-radius: 20px; cursor: pointer; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
            🛑 Cliquez ici pour PARLER (Micro)
        </button>
        <p id="status" style="font-family: sans-serif; color: gray; margin-top: 8px;">Cliquez sur le bouton pour commencer à parler...</p>
    </div>
    <script>
        const btn = document.getElementById('mic-btn');
        const status = document.getElementById('status');
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {
            status.innerText = "Navigateur non supporté.";
        } else {
            const recognition = new SpeechRecognition();
            recognition.lang = 'fr-FR';
            btn.addEventListener('click', () => {
                recognition.start();
                btn.style.backgroundColor = "#2b2b2b";
                btn.innerText = "🎙️ Écoute en cours...";
            });
            recognition.onresult = (event) => {
                const text = event.results[0][0].transcript;
                window.parent.postMessage({type: 'streamlit:set_input', value: text}, '*');
                btn.style.backgroundColor = "#FF4B4B";
                btn.innerText = "🛑 Cliquez ici pour PARLER (Micro)";
            };
        }
    </script>
""", height=120)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Tape ou parle pour répondre..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        time.sleep(1)
        if st.session_state.step < len(RESPONSES):
            ai_text = RESPONSES[st.session_state.step]
            st.session_state.step += 1
        else:
            ai_text = "Merci ! Ton profil IdentityPath est complété. Nous analysons tes réponses pour bâtir ton plan vers les bourses internationales."
        response_placeholder.write(ai_text)
    st.session_state.messages.append({"role": "assistant", "content": ai_text})
    st.rerun()
