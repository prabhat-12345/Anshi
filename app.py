import streamlit as st

# Strictly pushing high-end canvas settings
st.set_page_config(page_title="Happy Birthday Anshika ❤️", page_icon="👑", layout="centered")

# 100% Responsive CSS to match the premium screenshot blueprint
st.markdown("""
    <style>
    /* Full view canvas configuration - Fluid Crimson and Deep Burgundy */
    .stApp {
        background: radial-gradient(circle at center, #3d0006 0%, #1a0003 60%, #050001 100%) !important;
        font-family: 'Poppins', 'Georgia', serif;
        overflow-x: hidden;
    }

    /* Core Content Shell Wrapper */
    .screenshot-layout-shell {
        text-align: center;
        max-width: 600px;
        margin: auto;
        padding: 10px;
    }

    /* 1. TOP SENDER & RECEIVER BANNER SETTING */
    .sender-tag {
        font-size: 1.4rem;
        font-weight: bold;
        color: #ff7675;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 15px;
        text-shadow: 0 0 8px rgba(255, 118, 117, 0.4);
    }

    /* 2. SABSE BADA GLOWING BOLD HAPPY BIRTHDAY HEADER */
    .giant-neon-birthday {
        font-size: 4.8rem !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        line-height: 1.1;
        letter-spacing: 2px;
        background: linear-gradient(45deg, #ff004c, #ffd700, #ff7675, #ffffff);
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

    /* 3. DYNAMIC LIFELINE RIBBON BADGES (Changes color dynamically) */
    .love-ribbon-badge {
        background: rgba(255, 0, 76, 0.15);
        color: #ffd700;
        font-size: 1.4rem !important;
        font-weight: bold;
        letter-spacing: 3px;
        padding: 12px 25px;
        border-radius: 50px;
        display: inline-block;
        border: 2px solid;
        margin: 20px auto;
        box-shadow: 0 0 20px rgba(255, 0, 76, 0.4);
        animation: borderShift 6s infinite alternate;
    }

    @keyframes borderShift {
        0% { border-color: #ff004c; color: #ffd700; box-shadow: 0 0 20px #ff004c; }
        50% { border-color: #ffd700; color: #ffffff; box-shadow: 0 0 30px #ffd700; }
        100% { border-color: #e84393; color: #ffcccc; box-shadow: 0 0 20px #e84393; }
    }

    /* 4. THE MASTERPIECE PHOTO FRAME BOX WITH SOLID NEON REFLECTION */
    .photo-frame-outer {
        position: relative;
        max-width: 320px;
        margin: 25px auto;
        border-radius: 25px;
        padding: 8px;
        background: linear-gradient(45deg, #ff004c, #ffd700, #e84393);
        box-shadow: 0 15px 45px rgba(255, 0, 76, 0.6);
        animation: rotationGlow 4s linear infinite;
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
        transition: transform 0.5s ease;
    }

    .photo-frame-inner img:hover {
        transform: scale(1.05);
    }

    /* 5. DYNAMIC CLASSY BIG QUOTES CONTAINER DOWN THE PAGE */
    .classy-scroll-card {
        background: rgba(30, 2, 6, 0.85);
        color: #ffffff;
        font-size: 1.85rem !important;
        font-weight: bold;
        line-height: 1.7;
        padding: 40px 30px;
        border-radius: 25px;
        border: 3px solid;
        margin-top: 40px;
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.8);
        animation: cardColorShift 5s infinite alternate;
    }

    @keyframes cardColorShift {
        0% { border-color: #ff004c; box-shadow: 0 0 25px #ff004c; color: #ffeaea; }
        50% { border-color: #ffd700; box-shadow: 0 0 35px #ffd700; color: #fffde6; }
        100% { border-color: #ff3333; box-shadow: 0 0 25px #ff3333; color: #ffcccc; }
    }

    .chapter-tag {
        display: block;
        font-size: 1.1rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #ffd700;
        margin-bottom: 20px;
        text-shadow: 0 0 8px #ff004c;
    }

    /* 6. ULTIMATE ROYAL CELEBRATION BUTTON */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #d63031, #ff004c, #ffd700) !important;
        color: #000000 !important;
        font-size: 1.4rem !important;
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

# Main Application Execution Framework
st.markdown('<div class="screenshot-layout-shell">', unsafe_allow_html=True)

# SENDER & TOP RECEIVER CAPTION
st.markdown('<p class="sender-tag">👑 FROM PRABHAT TO HIS LIFELINE 👑</p>', unsafe_allow_html=True)

# THE MEGA BOLD HAPPY BIRTHDAY HEADER BANNER
st.markdown('<h1 class="giant-neon-birthday">HAPPY BIRTHDAY<br>ANSHIKA ❤️</h1>', unsafe_allow_html=True)

# TOP BADGE 1
st.markdown('<div class="love-ribbon-badge">💝 YOU ARE MY LIFE 💝</div>', unsafe_allow_html=True)

# --- THE PREMIUM NEON PHOTO FRAME SECTION ---
# NOTE: Replace the link below with Anshika's actual uploaded image link!
image_url = "https://unsplash.com"

st.markdown(f"""
    <div class="photo-frame-outer">
        <div class="photo-frame-inner">
            <img src="{image_url}" alt="Anshika's Special Birthday Frame">
        </div>
    </div>
""", unsafe_allow_html=True)

# MID BADGE 2
st.markdown('<div class="love-ribbon-badge">✨ YOU ARE MY EVERYTHING ✨</div>', unsafe_allow_html=True)

# --- TWO LARGE HIGH-LEVEL ROMANTIC DYNAMIC QUOTE CARDS ---
st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">✨ MY ULTIMATE CONFESSION ✨</span>
        "Anshika, tumhaari smile me wo jadoo hai jo meri puri duniya ko ek hi pal me roshan kar deta hai. Tum sirf meri sabse achhi dost nahi ho, tum meri zindagi ka sabse khoobsurat aur premium hissa ho! Happy Birthday to the most gorgeous girl in the universe! 🌹👑✨"
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="classy-scroll-card">
        <span class="chapter-tag">👑 ETERNAL WISH FOR YOU 👑</span>
        "Khuda kare tumhaari zindagi ka har ek lamha is red velvet canvas ki tarah hamesha sparkling aur colorful rahe. Tumhe zindagi ki har wo premium khushi mile jo tum chaaho, aur mera sath tumhaare sath hamesha aise hi barkarar rahe! Hamesha chamakti raho! 💝💫🔥"
    </div>
""", unsafe_allow_html=True)

# GRAND CELEBRATION BLAST TRIGGER
if st.button("🎈 CLICK FOR ANSHIKA'S ROYAL BIRTHDAY BLAST! 🎈"):
    st.balloons()
    st.snow()
    st.toast("Anshika belongs to pure royalty! 👑🔥", icon="❤️")
    st.success("🎉 Happy Birthday, Anshika! May your year ahead be as passionate, premium, and stunningly gorgeous as this layout! 🌹🔥👑")

st.markdown('</div>', unsafe_allow_html=True)
