import streamlit as st

# Custom canvas page configurations for a respectful, brilliant setup
st.set_page_config(page_title="Happy Birthday Anshika! ✨", page_icon="🎓", layout="centered")

# 100% Pure Intense Crimson Red Fluid Style Overwrite - No Frames, Elite Responsive Text
st.markdown("""
    <style>
    /* Full view intense premium dark red velvet gradient shifting continuously */
    .stApp {
        background: radial-gradient(circle at center, #9e000e 0%, #4a0005 50%, #1c0002 100%) !important;
        background-size: 200% 200% !important;
        animation: fluidRedAura 8s ease infinite !important;
        font-family: 'Poppins', 'Helvetica', sans-serif;
        overflow-x: hidden;
    }

    @keyframes fluidRedAura {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Core Content Wrapper Shell */
    .screenshot-layout-shell {
        text-align: center;
        max-width: 600px;
        margin: auto;
        padding: 10px;
    }

    /* 1. MENTOR TOP SENDER TAG IN PURE RED GLOW */
    .sender-tag {
        font-size: 1.1rem;
        font-weight: bold;
        color: #ff4d6d;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 20px;
        text-shadow: 0 0 10px #ff004c;
    }

    /* 2. GLOWING BOLD HAPPY BIRTHDAY HEADER - ONLY RED & WHITE SHINE */
    .giant-neon-birthday {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        line-height: 1.2;
        letter-spacing: 2px;
        background: linear-gradient(45deg, #ff004c, #ff4d6d, #ff7675, #ffffff);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: lightShine 3s linear infinite, extremeGlow 1.8s ease-in-out infinite alternate;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    @keyframes lightShine {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    @keyframes extremeGlow {
        0% { filter: drop-shadow(0 0 15px #ff004c); }
        100% { filter: drop-shadow(0 0 35px #ff4d6d); }
    }

    /* 3. DYNAMIC STATUS RIBBON BADGES - PURE CRIMSON AURA */
    .love-ribbon-badge {
        background: rgba(255, 0, 76, 0.15);
        color: #ffffff;
        font-size: 1.2rem !important;
        font-weight: bold;
        letter-spacing: 2px;
        padding: 10px 22px;
        border-radius: 50px;
        display: inline-block;
        border: 2px solid;
        margin: 15px auto;
        box-shadow: 0 0 20px rgba(255, 0, 76, 0.5);
        animation: borderShift 5s infinite alternate;
    }

    @keyframes borderShift {
        0% { border-color: #ff004c; box-shadow: 0 0 20px #ff004c; }
        50% { border-color: #ff4d6d; box-shadow: 0 0 35px #ff4d6d; }
        100% { border-color: #ff7675; box-shadow: 0 0 20px #ff7675; }
    }

    /* 4. REFINED CLASSY CHOTA DYNAMIC ENGLISH BOARDS */
    .classy-scroll-card {
        background: rgba(35, 0, 5, 0.95);
        color: #ffeaea;
        font-size: 1.25rem !important; /* Fixed to small, elegant size */
        font-weight: 500;
        line-height: 1.6;
        padding: 30px 25px;
        border-radius: 20px;
        border: 2px solid;
        margin-top: 30px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        animation: cardColorShift 6s infinite alternate;
    }

    @keyframes cardColorShift {
        0% { border-color: #ff004c; color: #ffeaea; }
        50% { border-color: #ff4d6d; color: #fff5f5; }
        100% { border-color: #ff7675; color: #ffcccc; }
    }

    .chapter-tag {
        display: block;
        font-size: 0.95rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #ff4d6d;
        margin-bottom: 15px;
        text-shadow: 0 0 8px #ff004c;
    }

    /* 5. ULTIMATE ROYAL RED MENTORSHIP CELEBRATION BUTTON */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff004c, #ff4d6d) !important;
        color: #ffffff !important;
        font-size: 1.25rem !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 12px 35px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 12px 40px rgba(255, 0, 76, 0.7) !important;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 60px;
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 50px #ff0000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main App execution shell
st.markdown('<div class="screenshot-layout-shell">', unsafe_allow_html=True)

# RESPECTFUL MENTOR IDENTIFIER TAG
st.markdown('<p class="sender-tag">🎓 WISHING AN EXCEPTIONAL STUDENT 🎓</p>', unsafe_allow_html=True)

# THE GRAND SHINY HAPPY BIRTHDAY BOLD TITLE
st.markdown('<h1 class="giant-neon-birthday">HAPPY BIRTHDAY<br>ANSHIKA 🌹</h1>', unsafe_allow_html=True)

# TOP BADGE
st.markdown('<div class="love-ribbon-badge">❤️ DEDICATION & EXCELLENCE ❤️</div>', unsafe_allow_html=True)

# --- TWO REFINED ELITE ENGLISH MOTIVATIONAL BOARDS ---
st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">✧ ACADEMIC APPRECIATION ✧</span>
        "Anshika, having a student as dedicated, focused, and intellectually driven as you is a true privilege. Your hard work, academic consistency, and sharp analytical mind set a stellar example for everyone. May you keep conquering new academic milestones. Happy Birthday! 🎓🌹"
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">✧ THE VISION OF SUCCESS ✧</span>
        "May this special day bring you great inspiration and open new avenues for your growth and research. Stay relentless in your pursuit of knowledge, and may you reach the absolute pinnacle of success in your future career. Have a wonderful birthday! 🚀🏆"
    </div>
""", unsafe_allow_html=True)

# GRAND MENTOR CELEBRATION TRIGGER
if st.button("🌹 CLICK FOR ANSHIKA'S SUCCESS CELEBRATION! 🌹"):
    st.balloons()
    st.snow()
    st.toast("Wishing Anshika excellence! 🎓✨", icon="❤️")
    st.success("🎉 Happy Birthday, Anshika! Wishing you outstanding career breakthroughs, wisdom, and phenomenal milestones ahead! 🎓🚀🌟")

st.markdown('</div>', unsafe_allow_html=True)
