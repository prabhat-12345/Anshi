import streamlit as st

# Custom canvas page configurations
st.set_page_config(page_title="Happy Birthday Anshika! ✨", page_icon="🎓", layout="centered")

# 100% Pure Royal Crimson Red & Gold Classy Style Overwrite
st.markdown("""
    <style>
    /* Full view intense premium dark red velvet gradient */
    .stApp {
        background: radial-gradient(circle at center, #8a000c 0%, #4a0005 50%, #210002 100%) !important;
        font-family: 'Poppins', 'Georgia', serif;
        overflow-x: hidden;
    }

    /* Core Content Wrapper Shell */
    .screenshot-layout-shell {
        text-align: center;
        max-width: 600px;
        margin: auto;
        padding: 10px;
    }

    /* 1. ELITE TOP SENDER TAG */
    .sender-tag {
        font-size: 1.3rem;
        font-weight: bold;
        color: #ffd700;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 15px;
        text-shadow: 0 0 10px #ff004c;
    }

    /* 2. SABSE BADA GLOWING BOLD HAPPY BIRTHDAY HEADER */
    .giant-neon-birthday {
        font-size: 4.5rem !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        line-height: 1.1;
        letter-spacing: 2px;
        background: linear-gradient(45deg, #ff3366, #ffd700, #ff7675, #ffffff);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: lightShine 3s linear infinite, extremeGlow 1.8s ease-in-out infinite alternate;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    @keyframes lightShine {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    @keyframes extremeGlow {
        0% { filter: drop-shadow(0 0 15px #ff004c); }
        100% { filter: drop-shadow(0 0 35px #ffd700); }
    }

    /* 3. DYNAMIC STATUS RIBBON BADGES */
    .love-ribbon-badge {
        background: rgba(255, 215, 0, 0.1);
        color: #ffffff;
        font-size: 1.3rem !important;
        font-weight: bold;
        letter-spacing: 2px;
        padding: 12px 25px;
        border-radius: 50px;
        display: inline-block;
        border: 2px solid;
        margin: 20px auto;
        box-shadow: 0 0 20px rgba(255, 0, 76, 0.4);
        animation: borderShift 5s infinite alternate;
    }

    @keyframes borderShift {
        0% { border-color: #ff004c; box-shadow: 0 0 20px #ff004c; }
        50% { border-color: #ffd700; box-shadow: 0 0 30px #ffd700; }
        100% { border-color: #ff3366; box-shadow: 0 0 20px #ff3366; }
    }

    /* 4. THE MASTERPIECE PHOTO FRAME BOX WITH SOLID NEON REFLECTION */
    .photo-frame-outer {
        position: relative;
        max-width: 320px;
        margin: 25px auto;
        border-radius: 25px;
        padding: 6px;
        background: linear-gradient(45deg, #ff004c, #ffd700, #ff3366);
        box-shadow: 0 15px 45px rgba(255, 0, 76, 0.7);
    }

    .photo-frame-inner {
        background: #120002;
        border-radius: 20px;
        overflow: hidden;
        display: block;
    }

    .photo-frame-inner img {
        width: 100%;
        display: block;
    }

    /* 5. CLASSY & HIGH-LEVEL DYNAMIC ENGLISH TEXT BOARDS */
    .classy-scroll-card {
        background: rgba(40, 2, 6, 0.95);
        color: #ffffff;
        font-size: 1.75rem !important;
        font-weight: bold;
        line-height: 1.7;
        padding: 40px 30px;
        border-radius: 25px;
        border: 3px solid;
        margin-top: 35px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.8);
        animation: cardColorShift 6s infinite alternate;
    }

    @keyframes cardColorShift {
        0% { border-color: #ff004c; color: #ffeaea; }
        50% { border-color: #ffd700; color: #fffde6; }
        100% { border-color: #ff3366; color: #ffcccc; }
    }

    .chapter-tag {
        display: block;
        font-size: 1.1rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #ffd700;
        margin-bottom: 25px;
        text-shadow: 0 0 8px #ff004c;
    }

    /* 6. ULTIMATE ROYAL CELEBRATION BUTTON */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff004c, #ffd700) !important;
        color: #000000 !important;
        font-size: 1.35rem !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 12px 40px rgba(255, 0, 76, 0.8) !important;
        width: 100%;
        margin-top: 25px;
        margin-bottom: 60px;
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 20px 60px #ff0000 !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main App execution shell
st.markdown('<div class="screenshot-layout-shell">', unsafe_allow_html=True)

# SENDER DECENT TAG
st.markdown('<p class="sender-tag">⭐ TO A BRILLIANT STUDENT & DEAR FRIEND ⭐</p>', unsafe_allow_html=True)

# THE MEGA BOLD HAPPY BIRTHDAY HEADER
st.markdown('<h1 class="giant-neon-birthday">HAPPY BIRTHDAY<br>ANSHIKA ✨</h1>', unsafe_allow_html=True)

# TOP BADGE 1
st.markdown('<div class="love-ribbon-badge">🌟 INDEPENDENT & BRIGHT 🌟</div>', unsafe_allow_html=True)

# --- THE PREMIUM NEON PHOTO FRAME SECTION ---
# Yahan Anshika ki online uploaded photo ka direct link paste karein
image_url = "https://unsplash.com"

st.markdown(f"""
    <div class="photo-frame-outer">
        <div class="photo-frame-inner">
            <img src="{image_url}" alt="Anshika's Special Birthday Frame">
        </div>
    </div>
""", unsafe_allow_html=True)

# MID BADGE 2
st.markdown('<div class="love-ribbon-badge">🎓 SUCCESS & EXCELLENCE 🎓</div>', unsafe_allow_html=True)

# --- TWO LARGE CLASSY & ELITE ENGLISH BOARDS ---
st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">✧ AN INSPIRING MENTORSHIP ✧</span>
        "Anshika, having a student and a friend as dedicated and brilliant as you is truly exceptional. Your intellect, hard work, and positive energy light up every room you walk into. May your beautiful mind achieve wonders. Happy Birthday! 🎓🌟✨"
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">✧ THE VISION OF SUCCESS ✧</span>
        "May this year unlock unparalleled growth, endless opportunities, and the highest peaks of academic excellence for you. Stay focused, stay unstoppable, and keep shining like the star you are. Have a phenomenal birthday! 🚀🏆🔥"
    </div>
""", unsafe_allow_html=True)

# GRAND CELEBRATION BLAST TRIGGER
if st.button("🎉 CLICK FOR ANSHIKA'S GRAND BIRTHDAY SURPRISE! 🎉"):
    st.balloons()
    st.snow()
    st.toast("Anshika is pure excellence! 🎓✨", icon="⭐")
    st.success("🎉 Happy Birthday, Anshika! Wishing you infinite professional success, joy, and grand milestones! 🎓🚀🌟")

st.markdown('</div>', unsafe_allow_html=True)
