import streamlit as st

# Setup page config for an absolute premium layout
st.set_page_config(page_title="Happy Birthday Anshika ❤️", page_icon="👑", layout="centered")

# 100% Pure Custom CSS for Giant Fonts, Neon Birthdays, and Color Changing Aura
st.markdown("""
    <style>
    /* 1. DYNAMIC ROYAL VELVET BACKGROUND WITH DENSE GLOW */
    .stApp {
        background: linear-gradient(135deg, #1f0003 0%, #4a000e 25%, #630225 50%, #2d0015 75%, #0f0003 100%) !important;
        background-size: 400% 400% !important;
        animation: premiumAura 10s ease infinite !important;
        font-family: 'Playfair Display', 'Georgia', serif;
        overflow-x: hidden;
    }
    
    @keyframes premiumAura {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. THE GRAND ROMANTIC CARD SHELL */
    .royal-shell {
        text-align: center;
        max-width: 650px;
        margin: auto;
        padding: 10px;
    }

    /* 3. SABSE BADA, BOLD AUR DYNAMIC HAPPY BIRTHDAY STATUS */
    .giant-birthday-text {
        font-size: 4.8rem !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        line-height: 1.1;
        background: linear-gradient(45deg, #ff004c, #ffd700, #ff7675, #ffffff);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite, headingGlow 2s ease-in-out infinite alternate;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    @keyframes textShine {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    @keyframes headingGlow {
        0% { filter: drop-shadow(0 0 15px rgba(255, 0, 76, 0.6)); }
        100% { filter: drop-shadow(0 0 35px rgba(255, 215, 0, 0.9)); }
    }

    /* 4. GORGEOUS GOLDEN NAME STATUS */
    .queen-name {
        font-size: 3.8rem !important;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 15px #ff004c, 0 0 30px #ff7675;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    /* 5. FAST REAL DHADAKTA HUA DIL ENGINE */
    .heart-box {
        position: relative;
        display: inline-block;
        margin: 20px 0;
    }

    .infinite-throb-heart {
        font-size: 160px;
        display: inline-block;
        animation: megaThrob 0.42s infinite alternate;
        filter: drop-shadow(0 0 40px #ff004c);
    }

    @keyframes megaThrob {
        0% { transform: scale(1); filter: drop-shadow(0 0 20px #ff0000); }
        100% { transform: scale(1.28) rotate(4deg); filter: drop-shadow(0 0 55px #ff004c); }
    }

    .side-sparkle {
        position: absolute;
        font-size: 45px;
        top: 40px;
        animation: danceSparkle 2s infinite ease-in-out;
    }
    .left-s { left: -40px; }
    .right-s { right: -40px; animation-delay: 0.4s; }

    @keyframes danceSparkle {
        0%, 100% { transform: translateY(0) scale(1); opacity: 0.8; }
        50% { transform: translateY(-20px) scale(1.2); opacity: 1; }
    }

    /* 6. TWO DYNAMIC BIG & BOLD PREMIUM QUOTES PANEL */
    .dynamic-big-quote {
        background: rgba(20, 0, 5, 0.75);
        color: #ffffff;
        font-size: 1.8rem !important; /* Bold Big Font size */
        font-weight: bold;
        line-height: 1.7;
        padding: 35px 30px;
        border-radius: 25px;
        border: 2px solid;
        margin-top: 35px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        animation: dynamicBorder &Glow 6s infinite alternate;
        transition: transform 0.4s ease;
    }

    .dynamic-big-quote:hover {
        transform: scale(1.03) translateY(-5px);
    }

    @keyframes dynamicBorder {
        0% { border-color: #ff004c; box-shadow: 0 0 25px rgba(255, 0, 76, 0.4), inset 0 0 15px rgba(255, 0, 76, 0.2); color: #ffeaea; }
        50% { border-color: #ffd700; box-shadow: 0 0 35px rgba(255, 215, 0, 0.5), inset 0 0 15px rgba(255, 215, 0, 0.2); color: #fffde6; }
        100% { border-color: #e84393; box-shadow: 0 0 25px rgba(232, 67, 147, 0.4), inset 0 0 15px rgba(232, 67, 147, 0.2); color: #mfeff5; }
    }

    .quote-badge {
        display: block;
        font-size: 1rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #ffd700;
        margin-bottom: 15px;
        text-shadow: 0 0 5px rgba(255,215,0,0.5);
    }

    /* 7. BLOCKBUSTER CELEBRATION BUTTON AT BOTTOM */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff004c, #ffd700, #e84393) !important;
        color: #000000 !important;
        font-size: 1.4rem !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 12px 35px rgba(255, 0, 76, 0.7) !important;
        width: 100%;
        margin-top: 25px;
        margin-bottom: 60px;
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 20px 50px #ff004c !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Structural Shell Starts
st.markdown('<div class="royal-shell">', unsafe_allow_html=True)

# THE GIANT BOLD BIRTHDAY BANNER
st.markdown('<h1 class="giant-birthday-text">HAPPY BIRTHDAY</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="queen-name">ANSHIKA ❤️</h2>', unsafe_allow_html=True)

# THE NON-STOP REAL BEATING HEART ENGINE
st.markdown("""
    <div class="heart-box">
        <span class="side-sparkle left-s">👑🌹</span>
        <span class="infinite-throb-heart">❤️</span>
        <span class="side-sparkle right-s">🌹👑</span>
    </div>
""", unsafe_allow_html=True)

# TWO DYNAMIC BIG & BOLD CLASSY QUOTES PANEL (Single vertical page scroll)
st.markdown("""
    <div class="dynamic-big-quote">
        <span class="quote-badge">✧ FIRST CHARMING LETTER ✧</span>
        "Anshika, tumhaari smile me wo jadoo hai jo meri puri duniya ko ek hi pal me roshan kar deta hai. Tum sirf meri sabse achhi dost nahi ho, tum meri zindagi ka sabse khoobsurat aur premium hissa ho! Happy Birthday to the most gorgeous girl in the universe! 🌹✨"
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="dynamic-big-quote">
        <span class="quote-badge">✧ ETERNAL WISH FOR YOU ✧</span>
        "Khuda kare tumhaari zindagi ka har ek lamha is canvas ki tarah hamesha sparkling aur colorful rahe. Tumhe zindagi ki har wo premium khushi mile jo tum chaaho, aur mera sath tumhaare sath hamesha aise hi barkarar rahe! Hamesha chamakti raho! 💝💫👑"
    </div>
""", unsafe_allow_html=True)

# THE ULTIMATE DYNAMIC MAGIC SURPRISE FINALE BUTTON
if st.button("🎁 CLICK FOR ANSHIKA'S ULTIMATE CELEBRATION BLAST! 🎁"):
    st.balloons()
    st.snow()
    st.toast("Anshika is absolute royalty! 👑❤️", icon="👑")
    st.success("🎉 Happy Birthday, Anshika! May your life be as gorgeous, grand, and premium as you are! 🌹🔥👑")

st.markdown('</div>', unsafe_allow_html=True)
