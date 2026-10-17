import streamlit as st

# Setup page config for a premium responsive layout
st.set_page_config(page_title="Happy Birthday Anshika ❤️", page_icon="🌹", layout="centered")

# 100% Pure Custom CSS for Dynamic Color Changing, Non-stop Heartbeat, and Floating Hearts
st.markdown("""
    <style>
    /* 1. DYNAMIC COLOR CHANGING BACKGROUND */
    .stApp {
        background: linear-gradient(45deg, #1a0002, #4a000e, #2d0015, #1a0002) !important;
        background-size: 400% 400% !important;
        animation: romanticGradient 12s ease infinite !important;
        font-family: 'Georgia', serif;
        overflow-x: hidden;
    }
    
    @keyframes romanticGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. THE GRAND ROMANTIC CONTAINER */
    .premium-container {
        text-align: center;
        max-width: 650px;
        margin: auto;
        padding: 20px;
    }

    /* 3. GLOWING ANIMATED TITLE */
    .gorgeous-name {
        font-size: 4.5rem !important;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 15px #ff004c, 0 0 30px #ff004c;
        margin-bottom: 2px;
        letter-spacing: 3px;
        animation: titleGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes titleGlow {
        0% { text-shadow: 0 0 10px #ff004c, 0 0 20px #ff004c; }
        100% { text-shadow: 0 0 25px #ff7675, 0 0 50px #ff004c; }
    }

    .subtitle-love {
        font-size: 1.4rem;
        color: #ff7675;
        font-style: italic;
        margin-bottom: 20px;
    }

    /* 4. NON-STOP MEGA DHADAKTA HUA DIL WITH FLOATING SIDE ROSES */
    .heart-wrapper {
        position: relative;
        display: inline-block;
        margin: 30px 0;
        padding: 0 50px;
    }

    .eternal-heart {
        font-size: 150px;
        display: inline-block;
        animation: fastHeartBeat 0.45s infinite alternate;
        filter: drop-shadow(0 0 35px #ff004c);
    }

    @keyframes fastHeartBeat {
        0% { transform: scale(1); filter: drop-shadow(0 0 20px #ff0000); }
        100% { transform: scale(1.25) rotate(-3deg); filter: drop-shadow(0 0 50px #ff004c); }
    }

    .rose-decor-left, .rose-decor-right {
        position: absolute;
        font-size: 40px;
        top: 45px;
        animation: floatDecor 2.5s infinite ease-in-out;
    }
    .rose-decor-left { left: -20px; }
    .rose-decor-right { right: -20px; animation-delay: 0.5s; }

    @keyframes floatDecor {
        0% { transform: translateY(0px) scale(1); opacity: 0.7; }
        50% { transform: translateY(-15px) scale(1.1); opacity: 1; }
        100% { transform: translateY(0px) scale(1); opacity: 0.7; }
    }

    /* 5. ALL QUOTES DISPLAYED VERTICALLY WITH AUTOCONTEXT COLOR CHANGING SHADOWS */
    .diary-headline {
        color: #ffffff;
        font-size: 2rem;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        text-shadow: 0 0 10px #ff7675;
    }

    .romantic-card-scroll {
        background: rgba(255, 255, 255, 0.06);
        color: #ffeaea;
        font-size: 1.35rem;
        line-height: 1.8;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 0, 76, 0.3);
        margin-bottom: 25px;
        text-align: left;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        animation: borderPulse 8s infinite alternate;
        transition: transform 0.3s ease;
    }
    
    .romantic-card-scroll:hover {
        transform: scale(1.02);
        background: rgba(255, 255, 255, 0.09);
    }

    @keyframes borderPulse {
        0% { border-color: #ff004c; box-shadow: 0 8px 25px rgba(255, 0, 76, 0.2); }
        50% { border-color: #ffd700; box-shadow: 0 8px 25px rgba(255, 215, 0, 0.2); }
        100% { border-color: #e84393; box-shadow: 0 8px 25px rgba(232, 67, 147, 0.2); }
    }

    .page-tag {
        font-size: 0.9rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #ff7675;
        margin-bottom: 8px;
        display: block;
    }

    /* 6. ULTIMATE CELEBRATION BUTTON OVERRIDE */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff004c, #ffd700) !important;
        color: #000000 !important;
        font-size: 1.3rem !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(255, 0, 76, 0.6) !important;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 50px;
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 40px #ff004c !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main App Shell Container
st.markdown('<div class="premium-container">', unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="gorgeous-name">Anshika ❤️</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-love">~ You Are The Most Beautiful Chapters Of My Life ~</p>', unsafe_allow_html=True)

# THE SUPER BEATING HEART (Sides filled with gorgeous roses and sparkles)
st.markdown("""
    <div class="heart-wrapper">
        <span class="rose-decor-left">✨🌹</span>
        <span class="eternal-heart">❤️</span>
        <span class="rose-decor-right">🌹✨</span>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="diary-headline">📖 My Golden Letters Diary For You</div>', unsafe_allow_html=True)

# ALL QUOTES DISPLAYED VERTICALLY IN ONE CONTINUOUS PREMIUM SCROLL
quotes_list = [
    {
        "tag": "Chapter 1: The Magic of You",
        "text": "Anshika, tumhaari smile me wo jadoo hai jo meri puri duniya ko ek hi pal me roshan kar deta hai. Tum sirf meri best friend nahi ho, tum meri life ki sabse khoobsurat blessing ho! Happy Birthday to the most gorgeous girl! 🌹✨"
    },
    {
        "tag": "Chapter 2: Dil Se Dua",
        "text": "Bhagwan se bas yahi dua hai ki tumhaari zindagi ka har ek lamha is premium canvas ki tarah hamesha sparkling aur colorful rahe. Tumhe duniya ki har wo khushi mile jo tum chaaho, aur mera sath hamesha tumhaare sath rahe! 💝💫"
    },
    {
        "tag": "Chapter 3: Connection of Hearts",
        "text": "Kuch log life me itne special hote hain ki unke bina zindagi bilkul adhuri lagti hai. Mere liye wo tum ho. Tumhaari baatein, tumhaara support aur tumhaari dosti mere liye sabse zyaada precious hain. Stay blessed always! 🥰🌸"
    },
    {
        "tag": "Chapter 4: The Royal Birthday Wish",
        "text": "Aaj tumhaara janamdin hai, toh puri duniya ko pata chalna chahiye ki aaj kisi bohot hi pyaari aur special ladki ka din hai! Hamesha aise hi muskurati raho, chamakti raho aur mujhe satati raho. Happy Birthday, Anshika! 🥂🎂👑"
    }
]

# Rendering each quote beautifully down the page
for q in quotes_list:
    st.markdown(f"""
        <div class="romantic-card-scroll">
            <span class="page-tag">{q['tag']}</span>
            {q['text']}
        </div>
    """, unsafe_allow_html=True)

# GRAND SURPRISE MAGICAL FINALE BUTTON AT THE BOTTOM
if st.button("🎁 CLICK FOR ANSHIKA'S GRAND SURPRISE BLAST! 🎁"):
    st.balloons()
    st.snow()
    st.toast("Anshika is pure magic! 👑❤️", icon="👑")
    st.success("🎉 Happy Birthday, Anshika! May your year ahead be as premium, gorgeous, and full of love as you are! 🌹🔥👑")

st.markdown('</div>', unsafe_allow_html=True)
