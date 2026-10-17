import streamlit as st
import os

# Custom canvas page configurations for an elite setup
st.set_page_config(page_title="Happy Birthday Anshika! ✨", page_icon="🎓", layout="centered")

# Continuous automatic snowfall & balloons animation trigger instantly
st.snow()
st.balloons()

# Intense Shifting Red Canvas & Rigid HTML Table Grid Formatting
st.markdown("""
    <style>
    /* 1. LIQUID NEON SHIFTING INTENSE RED BACKGROUND */
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
        padding: 5px;
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

    /* 3. DYNAMIC GLOW HAPPY BIRTHDAY TITLE WITH INTENSE GREEN MATRIX SHIFT */
    .giant-neon-birthday {
        font-size: 3.5rem !important;
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

    /* 4. HARD-LOCKED HTML TABLE ALIGNMENT PACK (Prevents center stacking) */
    .rigid-layout-table {
        width: 100% !important;
        border-collapse: collapse !important;
        margin: 20px 0 !important;
        border: none !important;
    }

    .photo-td-cell {
        width: 50% !important;
        padding-right: 8px !important;
        vertical-align: middle !important;
        text-align: left !important;
    }

    .decor-td-cell {
        width: 50% !important;
        padding-left: 8px !important;
        vertical-align: middle !important;
        text-align: right !important;
    }

    /* 5. ROMANTIC DECORATED RED NEON PHOTO FRAME */
    .photo-td-cell img {
        width: 100% !important;
        max-width: 280px !important;
        border-radius: 20px !important;
        border: 4px solid #ff004c !important;
        box-shadow: 0 0 20px #ff004c, 0 10px 30px rgba(255,0,76,0.6) !important;
        animation: romanticFramePulse 3s infinite alternate !important;
        display: block;
    }

    @keyframes romanticFramePulse {
        0% { border-color: #ff004c; filter: drop-shadow(0 0 5px #ff004c); }
        100% { border-color: #ffffff; filter: drop-shadow(0 0 20px #ff7675); }
    }

    /* 6. ROMANTIC DECORATIVE INNER CONTAINER IN RIGHT COLUMN */
    .dynamic-love-board {
        background: rgba(30, 0, 4, 0.95) !important;
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        padding: 22px 12px !important;
        border-radius: 15px !important;
        border: 2px solid #ff004c !important;
        box-shadow: 0 8px 25px rgba(255, 0, 76, 0.5) !important;
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 15px !important;
        animation: panelGlowWave 4s infinite alternate !important;
    }

    @keyframes panelGlowWave {
        0% { border-color: #ff004c; box-shadow: 0 0 10px rgba(255,0,76,0.4); }
        100% { border-color: #ff7675; box-shadow: 0 0 25px rgba(255,118,117,0.6); }
    }

    .heart-bullet {
        color: #ff004c;
        font-size: 1.3rem;
        display: inline-block;
        animation: throbEffect 0.5s infinite alternate;
    }

    @keyframes throbEffect {
        to { transform: scale(1.15); }
    }

    /* 7. CONTINUOUS FAST DHADAKTA HUA DIL ENGINE */
    .heart-engine-box {
        margin: 30px 0;
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

    /* 8. ELITE ENGLISH MOTIVATIONAL SCROLL CARDS */
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

    /* 9. TYPEWRITER BOX ENGINE */
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

# Main App execution framework shell
st.markdown('<div class="screenshot-layout-shell">', unsafe_allow_html=True)

# RESPECTFUL TOP TAG
st.markdown('<p class="sender-tag">🎓 WISHING AN EXCEPTIONAL STUDENT ✨</p>', unsafe_allow_html=True)

# THE GRAND SHINY HAPPY BIRTHDAY BOLD TITLE
st.markdown('<h1 class="giant-neon-birthday">HAPPY BIRTHDAY<br>ANSHIKA 🌹</h1>', unsafe_allow_html=True)

# --- STRICT MULTI-COLUMN TABLE ENGINE (No center reset allowed) ---
target_photo = "rotated_photo_only~2.jpg"

st.markdown(f"""
    <table class="rigid-layout-table">
        <tr>
            <td class="photo-td-cell">
                <img src="https://githubusercontent.com{target_photo}" onerror="this.src='https://unsplash.com'">
            </td>
            <td class="decor-td-cell">
                <div class="dynamic-love-board">
                    <div><span class="heart-bullet">❤️</span> Pure Brilliance <span class="heart-bullet">❤️</span></div>
                    <div><span class="heart-bullet">🌹</span> Outstanding Scholar 🎓</div>
                    <div><span class="heart-bullet">✨</span> Absolute Grace 💘</div>
                </div>
            </td>
        </tr>
    </table>
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
