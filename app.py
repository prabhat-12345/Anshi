import streamlit as st
import os

# Custom canvas page configurations for an elite setup
st.set_page_config(page_title="Happy Birthday Anshika! ✨", page_icon="🎓", layout="centered")

# Trigger automatic beautiful runtime graphics on page load
st.snow()
st.balloons()

# 100% Pure Intense Liquid Red Canvas, Side-by-Side Frames & Heart Overlays
st.markdown("""
    <style>
    /* 1. LIQUID NEON SHIFTING BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #4d0005 0%, #a80011 25%, #ff1a3b 50%, #80000a 75%, #1f0002 100%) !important;
        background-size: 400% 400% !important;
        animation: gorgeousLiquidRed 8s ease infinite !important;
        font-family: 'Poppins', 'Helvetica', sans-serif;
        overflow-x: hidden;
    }

    @keyframes gorgeousLiquidRed {
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

    /* 2. MENTOR TOP SENDER TAG WITH PULSING AURA */
    .sender-tag {
        font-size: 1.15rem;
        font-weight: bold;
        color: #ff7675;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 20px;
        animation: textPulse 2s infinite alternate;
    }

    @keyframes textPulse {
        0% { opacity: 0.7; text-shadow: 0 0 5px #ff004c; }
        100% { opacity: 1; text-shadow: 0 0 15px #ff7675; }
    }

    /* 3. DYNAMIC EMERALD GREEN HAPPY BIRTHDAY HEADER WITH DYNAMIC COLOR WAVE */
    .giant-neon-birthday {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        line-height: 1.2;
        letter-spacing: 2px;
        background: linear-gradient(45deg, #00ff7f, #00eb00, #adff2f, #00ffaa, #ff004c);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: greenLightShine 4s linear infinite, greenExtremeGlow 2s ease-in-out infinite alternate;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    @keyframes greenLightShine {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    @keyframes greenExtremeGlow {
        0% { filter: drop-shadow(0 0 12px rgba(0, 255, 127, 0.6)); }
        100% { filter: drop-shadow(0 0 35px rgba(0, 235, 0, 0.9)); }
    }

    /* 4. PREMIUM DECORATED ROMANTIC PHOTO FRAME PACK */
    .stImage > img {
        border-radius: 20px !important;
        border: 4px solid #ff4d6d !important;
        box-shadow: 0 0 25px #ff004c, 0 15px 45px rgba(255, 0, 76, 0.8) !important;
        transition: transform 0.4s ease-in-out !important;
        animation: framePulse 3s infinite alternate !important;
    }

    @keyframes framePulse {
        0% { border-color: #ff004c; box-shadow: 0 0 15px #ff004c; }
        100% { border-color: #ffffff; box-shadow: 0 0 35px #ff4d6d; }
    }

    /* 5. GORGEOUS ROMANTIC SIDE PANEL STYLING WITH EMOJIS */
    .side-text-panel {
        background: rgba(35, 0, 5, 0.92);
        color: #ffffff;
        font-size: 1.35rem;
        font-weight: bold;
        padding: 25px 15px;
        border-radius: 20px;
        border: 2px solid #ff004c;
        box-shadow: 0 10px 30px rgba(255,0,76,0.5);
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        animation: panelShift 4s infinite alternate;
    }

    @keyframes panelShift {
        0% { border-color: #ff004c; box-shadow: 0 0 15px rgba(255,0,76,0.4); }
        100% { border-color: #ff7675; box-shadow: 0 0 30px rgba(255,118,117,0.6); }
    }

    .heart-bullet {
        color: #ff004c;
        font-size: 1.6rem;
        display: inline-block;
        animation: miniBeat 0.6s infinite alternate;
    }

    @keyframes miniBeat {
        to { transform: scale(1.15); }
    }

    /* 6. FAST REAL DHADAKTA HUA DIL ENGINE */
    .heart-engine-box {
        margin: 25px 0;
    }

    .ultimate-fast-heart {
        font-size: 110px;
        display: inline-block;
        animation: fastThrob 0.42s infinite alternate;
        filter: drop-shadow(0 0 35px #ff004c);
    }

    @keyframes fastThrob {
        0% { transform: scale(1); filter: drop-shadow(0 0 15px #ff004c); }
        100% { transform: scale(1.25) rotate(3deg); filter: drop-shadow(0 0 50px #ff0000); }
    }

    /* 7. CLASSY ACADEMIC MOTIVATIONAL BOARDS */
    .classy-scroll-card {
        background: rgba(30, 0, 4, 0.96);
        font-size: 1.25rem !important;
        font-weight: 500;
        line-height: 1.6;
        padding: 35px 25px;
        border-radius: 20px;
        border: 2px solid;
        margin-top: 30px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 12px 35px rgba(0,0,0,0.7);
        animation: cardColorShift 6s infinite alternate;
    }

    @keyframes cardColorShift {
        0% { border-color: #ff004c; color: #ffeaea; }
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
    }

    /* 8. HIGH-LEVEL TYPEWRITER ENGINE */
    .typewriter-box {
        margin: 35px 0;
        background: rgba(0, 0, 0, 0.4);
        padding: 25px 15px;
        border-radius: 15px;
        border: 1px dashed #ff4d6d;
    }

    .typewriter-text {
        font-size: 1.65rem;
        font-weight: bold;
        color: #ffffff;
        overflow: hidden;
        border-right: .15em solid #ff004c;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .05em;
        display: block;
        width: 25ch;
        animation: typing 4s steps(25, end) infinite, blink-caret .75s step-end infinite;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #ff004c; }
    }
    </style>
""", unsafe_allow_html=True)

# Main App execution shell
st.markdown('<div class="screenshot-layout-shell">', unsafe_allow_html=True)

# RESPECTFUL TAG
st.markdown('<p class="sender-tag">🎓 WISHING AN EXCEPTIONAL STUDENT ✨</p>', unsafe_allow_html=True)

# THE GRAND SHINY HAPPY BIRTHDAY BOLD TITLE
st.markdown('<h1 class="giant-neon-birthday">HAPPY BIRTHDAY<br>ANSHIKA 🌹</h1>', unsafe_allow_html=True)

# --- DECORATED SIDE-BY-SIDE FRAME ALIGNMENT ENGINE ---
col1, col2 = st.columns([1.1, 1])

with col1:
    # B&W Target photo automatically pulled from repository
    target_photo = "rotated_photo_only~2.jpg"
    if os.path.exists(target_photo):
        st.image(target_photo, use_container_width=True)
    else:
        st.image("https://unsplash.com", use_container_width=True)

with col2:
    # Side panel embedded with romantic glowing heart symbols & classy parameters
    st.markdown("""
        <div class="side-text-panel">
            <div><span class="heart-bullet">❤️</span> Pure Brilliance <span class="heart-bullet">❤️</span></div><br>
            <div><span class="heart-bullet">🌹</span> Outstanding Scholar 🎓</div><br>
            <div><span class="heart-bullet">✨</span> Absolute Grace 💘</div>
        </div>
    """, unsafe_allow_html=True)

# THE DYNAMIC FAST DHADAKTA HUA DIL ENGINE
st.markdown('<div class="heart-engine-box"><span class="ultimate-fast-heart">❤️</span></div>', unsafe_allow_html=True)

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

# --- FIXED TYPEWRITER AUTOMATIC LETTER MACHINE ---
st.markdown("""
    <div class="typewriter-box">
        <div class="typewriter-text">Happy Birthday Anshika! ✨</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
