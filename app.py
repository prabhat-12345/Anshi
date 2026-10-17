import streamlit as st

# Custom canvas page configurations for a respectful, brilliant setup
st.set_page_config(page_title="Happy Birthday Anshika! ✨", page_icon="🎓", layout="centered")

# 100% Pure Intense Shifting Red Canvas & Typewriter Effects
st.markdown("""
    <style>
    /* 1. DYNAMIC FLUID SHIFTING BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #7a0006, #4a0002, #b50014, #3d0004) !important;
        background-size: 400% 400% !important;
        animation: fluidRedAura 10s ease infinite !important;
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

    /* 2. MENTOR TOP SENDER TAG WITH PULSING SHINE */
    .sender-tag {
        font-size: 1.15rem;
        font-weight: bold;
        color: #ff4d6d;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 20px;
        animation: textPulse 2s infinite alternate;
    }

    @keyframes textPulse {
        0% { opacity: 0.7; text-shadow: 0 0 5px #ff004c; }
        100% { opacity: 1; text-shadow: 0 0 15px #ff4d6d; }
    }

    /* 3. GLOWING BOLD HAPPY BIRTHDAY HEADER WITH DYNAMIC TEXT COLOR SHIFT */
    .giant-neon-birthday {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        line-height: 1.2;
        letter-spacing: 2px;
        background: linear-gradient(45deg, #ff004c, #ff4d6d, #ff7675, #ffffff, #ff004c);
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
        0% { filter: drop-shadow(0 0 10px #ff004c); }
        100% { filter: drop-shadow(0 0 30px #ff7675); }
    }

    /* 4. DYNAMIC SHIFTING BORDERS FOR STATUS RIBBON */
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
        animation: borderShift 4s infinite alternate;
    }

    @keyframes borderShift {
        0% { border-color: #ff004c; box-shadow: 0 0 15px #ff004c; color: #ffeaea; }
        50% { border-color: #ff4d6d; box-shadow: 0 0 25px #ff4d6d; color: #ffffff; }
        100% { border-color: #ff7675; box-shadow: 0 0 15px #ff7675; color: #ffcccc; }
    }

    /* 5. FAST REAL DHADAKTA HUA DIL ENGINE */
    .heart-engine-box {
        margin: 20px 0;
    }

    .ultimate-fast-heart {
        font-size: 100px;
        display: inline-block;
        animation: fastThrob 0.45s infinite alternate;
        filter: drop-shadow(0 0 35px #ff004c);
    }

    @keyframes fastThrob {
        0% { transform: scale(1); filter: drop-shadow(0 0 15px #ff004c); }
        100% { transform: scale(1.22) rotate(-3deg); filter: drop-shadow(0 0 45px #ff0000); }
    }

    /* 6. REFINED CLASSY CHOTA DYNAMIC BOARDS (Text colors change dynamically) */
    .classy-scroll-card {
        background: rgba(35, 0, 5, 0.95);
        font-size: 1.25rem !important;
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
        0% { border-color: #ff004c; color: #ffeaea; box-shadow: 0 0 20px rgba(255,0,76,0.3); }
        50% { border-color: #ff4d6d; color: #fff5f5; box-shadow: 0 0 30px rgba(255,77,109,0.4); }
        100% { border-color: #ff7675; color: #ffcccc; box-shadow: 0 0 20px rgba(255,118,117,0.3); }
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
        animation: tagColor 4s infinite alternate;
    }

    @keyframes tagColor {
        0% { color: #ff004c; }
        100% { color: #ffffff; }
    }

    /* 7. CLASSY TYPEWRITER ANIMATION ENGINE (Letters write down one by one) */
    .typewriter-box {
        margin: 30px 0;
        background: rgba(0, 0, 0, 0.3);
        padding: 20px;
        border-radius: 15px;
        border: 1px dashed #ff4d6d;
    }

    .typewriter-text {
        font-size: 1.6rem;
        font-weight: bold;
        color: #ffffff;
        overflow: hidden;
        border-right: .15em solid #ff004c;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .15em;
        display: inline-block;
        animation: typing 4s steps(30, end) infinite, blink-caret .75s step-end infinite;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #ff004c; }
    }

    /* 8. ULTIMATE CELEBRATION BUTTON */
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

# RESPECTFUL MENTOR IDENTIFIER TAG WITH PYARA EMOJI
st.markdown('<p class="sender-tag">🎓 WISHING AN EXCEPTIONAL STUDENT ✨</p>', unsafe_allow_html=True)

# THE GRAND SHINY HAPPY BIRTHDAY BOLD TITLE
st.markdown('<h1 class="giant-neon-birthday">HAPPY BIRTHDAY<br>ANSHIKA 🌹</h1>', unsafe_allow_html=True)

# THE DYNAMIC FAST DHADAKTA HUA DIL ENGINE
st.markdown('<div class="heart-engine-box"><span class="ultimate-fast-heart">❤️</span></div>', unsafe_allow_html=True)

# TOP BADGE WITH CLASSY EMOJIS
st.markdown('<div class="love-ribbon-badge">✨ DEDICATION & EXCELLENCE 🎓</div>', unsafe_allow_html=True)

# --- REFINED ELITE ENGLISH MOTIVATIONAL BOARDS ---
st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">✨ ACADEMIC APPRECIATION ✨</span>
        "Anshika, having a student as dedicated, focused, and intellectually driven as you is a true privilege. Your hard work, academic consistency, and sharp analytical mind set a stellar example for everyone. May you keep conquering new academic milestones. Happy Birthday! 🎓🌹"
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">🚀 THE VISION OF SUCCESS 🏆</span>
        "May this special day bring you great inspiration and open new avenues for your growth and research. Stay relentless in your pursuit of knowledge, and may you reach the absolute pinnacle of success in your future career. Have a wonderful birthday! 🚀🏆"
    </div>
""", unsafe_allow_html=True)

# --- THE TYPEWRITER AUTOMATIC LETTER MACHINE ---
st.markdown("""
    <div class="typewriter-box">
        <div class="typewriter-text">✨ Happy Birthday Anshika! 🎓</div>
    </div>
""", unsafe_allow_html=True)

# GRAND MENTOR CELEBRATION TRIGGER
if st.button("🌹 CLICK FOR ANSHIKA'S SUCCESS CELEBRATION! 🌹"):
    st.balloons()
    st.snow()
    st.toast("Wishing Anshika excellence! 🎓✨", icon="❤️")
    st.success("🎉 Happy Birthday, Anshika! Wishing you outstanding career breakthroughs, wisdom, and phenomenal milestones ahead! 🎓🚀🌟")

st.markdown('</div>', unsafe_allow_html=True)
