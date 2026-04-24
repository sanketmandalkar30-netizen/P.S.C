import streamlit as st
import re

# ── Page Config ───────────────────────────────
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────
st.markdown("""
    <style>
        .main { max-width: 600px; margin: auto; }
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #f44336, #ff9800, #4caf50);
        }
        .tip-box {
            background-color: #fff8e1;
            border-left: 4px solid #ffc107;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            margin-bottom: 0.4rem;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# ── Title ────────────────────────────────────
st.title("🔐 Password Strength Checker")
st.write("Check how strong your password is and get suggestions to improve it.")

# ── Password Input ───────────────────────────
password = st.text_input("Enter your password", type="password", placeholder="Type your password here...")

# ── Strength Checker Function ─────────────────
def check_strength(pwd: str) -> tuple[int, list[str]]:
    """
    Evaluates password strength on 5 criteria.
    Returns (score: int 0-5, feedback: list of improvement tips).
    """
    score = 0
    feedback = []

    if len(pwd) >= 8:
        score += 1
    else:
        feedback.append("👉 Use at least **8 characters**.")

    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        feedback.append("👉 Add at least one **uppercase letter** (A–Z).")

    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        feedback.append("👉 Add at least one **lowercase letter** (a–z).")

    if re.search(r"[0-9]", pwd):
        score += 1
    else:
        feedback.append("👉 Include at least one **number** (0–9).")

    if re.search(r"[!@#$%^&*()\-_=+\[\]{};:'\",.<>?/\\|`~]", pwd):
        score += 1
    else:
        feedback.append("👉 Add at least one **special character** (e.g. `!@#$%`).")

    return score, feedback

# ── Result Display ────────────────────────────
if password:
    score, feedback = check_strength(password)

    st.subheader("🔍 Password Analysis")

    # Strength label
    if score <= 2:
        st.error("❌ **Weak Password** — This password is easy to crack.")
    elif score in (3, 4):
        st.warning("⚠️ **Medium Strength** — Getting there, but can be stronger.")
    else:
        st.success("✅ **Strong Password** — Great job!")

    # Progress bar (clamp between 0.0 and 1.0)
    st.progress(max(0.0, min(score / 5, 1.0)))
    st.caption(f"Strength score: {score}/5")

    # Tips
    if feedback:
        st.subheader("💡 Suggestions to Improve:")
        for tip in feedback:
            st.markdown(f'<div class="tip-box">{tip}</div>', unsafe_allow_html=True)
    else:
        st.balloons()
        st.success("🎉 Your password meets all strength criteria!")

else:
    st.info("⬆️ Enter a password above to see its strength analysis.")

# ── Footer ───────────────────────────────────
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")