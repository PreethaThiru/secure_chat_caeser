import streamlit as st
import os
from datetime import datetime

# ---------- Caesar Cipher ----------
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---------- Storage ----------
MESSAGE_FILE = "messages.txt"
os.makedirs(os.path.dirname(MESSAGE_FILE) or ".", exist_ok=True)
if not os.path.exists(MESSAGE_FILE):
    with open(MESSAGE_FILE, "w", encoding="utf-8") as f:
        pass

# ---------- Page / Meta ----------
st.set_page_config(
    page_title="Secure Caesar Chat",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- Global Styles ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #F5A8B8, #F28BAF, #D8CBB5);
        font-family: 'Poppins', 'Segoe UI', Roboto, Arial, sans-serif;
        color: #3B4979 !important;
    }

    html, body, [class*="css"] {
        color: #3B4979 !important;
    }

    /* Title */
    .app-title {
        font-weight: 800;
        font-size: clamp(28px, 4vw, 40px);
        color: #3B4979 !important;
        margin-bottom: 0.5rem;
    }

    .app-subtitle {
        color: #9B6ABA !important;
        font-weight: 500;
        margin-bottom: 1.2rem;
    }

    /* Card Styling */
    .glass {
        background: rgba(255,255,255,0.85);
        border-radius: 18px;
        padding: 1rem 1rem 0.8rem;
        border: 1px solid rgba(155, 106, 186, 0.2);
        box-shadow: 0 6px 18px rgba(59,73,121,0.2);
    }

    /* Tabs */
    [data-testid="stTabs"] button[role="tab"] {
        border-radius: 999px !important;
        padding: 0.5rem 1rem !important;
        margin-right: .4rem;
        background: #D8CBB5 !important;
        color: #3B4979 !important;
        font-weight: 600;
        border: none;
    }
    [data-testid="stTabs"] button[aria-selected="true"] {
        background: #9B6ABA !important;
        color: #fff !important;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 999px;
        padding: .7rem 1.2rem;
        font-weight: 700;
        background: #3B4979 !important;
        color: #fff !important;
        box-shadow: 0 6px 18px rgba(59,73,121,0.3);
        border: none;
    }

    /* Inputs */
    .stTextInput > div > div > input,
    .stTextArea textarea {
        border-radius: 14px !important;
        border: 1px solid rgba(155, 106, 186, 0.4) !important;
        background: #fff !important;
        color: #3B4979 !important;
    }

    /* Chat bubbles */
    .bubble {
        border-radius: 14px;
        padding: .8rem 1rem;
        margin-bottom: .6rem;
        color: #3B4979 !important;
        box-shadow: 0 4px 12px rgba(59,73,121,0.15);
    }
    .bubble-left { background: #F5A8B8; }
    .bubble-right { background: #F28BAF; }
    .bubble .meta { font-size: .78rem; opacity: .8; }
    </style>
    """,
    unsafe_allow_html=True
)



# ---------- Header ----------
st.markdown('<div class="app-title">🔐 Secure Chat with Caesar Cipher</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">A playful encrypted notepad with a refined look.</div>', unsafe_allow_html=True)

# ---------- Tabs ----------
tab1, tab2 = st.tabs(["💬 Send Message", "📜 View Messages"])

with tab1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("Send Encrypted Message", anchor=False)
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        username = st.text_input("Your Name", placeholder="e.g., Preetha")
    with col2:
        shift = st.slider("Caesar Cipher Shift", min_value=1, max_value=25, value=3, help="How many letters to shift by.")

    message = st.text_area("Message", placeholder="Type your secret message here...")

    send = st.button("Send Securely ✨")
    if send:
        if username.strip() and message.strip():
            encrypted_message = caesar_encrypt(message, shift)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            # format: name:encrypted:shift:time\n
            with open(MESSAGE_FILE, "a", encoding="utf-8") as f:
                f.write(f"{username}:{encrypted_message}:{shift}:{timestamp}\n")
            st.success("Message sent securely! 🎉")
            st.balloons()
        else:
            st.warning("Please fill in all fields.")

    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass pad">', unsafe_allow_html=True)
    st.subheader("View Messages (Decrypted)", anchor=False)

    # Safe read + parsing (allow colons in encrypted text by limiting splits)
    try:
        with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f.readlines() if ln.strip()]
    except Exception as e:
        lines = []
        st.error(f"Error reading storage: {e}")

    if not lines:
        st.info("No messages yet.")
    else:
        st.caption(f"Total messages: **{len(lines)}**")
        for i, line in enumerate(lines):
            try:
                # Expect at least 3 fields; if timestamp present, we grab it too
                # name : encrypted : shift [: timestamp]
                parts = line.split(":", 3)  # <= key fix compared to split(":")
                if len(parts) == 4:
                    name, encrypted_text, shift_val, ts = parts
                else:
                    name, encrypted_text, shift_val = parts[:3]
                    ts = "—"

                decrypted = caesar_decrypt(encrypted_text, int(shift_val))
                side_class = "bubble-right" if i % 2 else "bubble-left"
                st.markdown(
                    f"""
                    <div class="bubble {side_class}">
                        <strong>{name}</strong>: {decrypted}
                        <div class="meta"><code>Encrypted:</code> {encrypted_text} &nbsp;•&nbsp; <code>Shift:</code> {shift_val} &nbsp;•&nbsp; <code>Time:</code> {ts}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"Error reading message: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
