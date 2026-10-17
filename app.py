import streamlit as st

# High-level page setup
st.set_page_config(page_title="For Someone Very Special: Anshika", page_icon="💖", layout="centered")

# Advanced Premium UI/UX CSS styling
st.markdown("""
    <style>
    /* Full page premium color palette */
    .stApp {
        background: linear-gradient(135deg, #ff4e50 0%, #f9d423 50%, #e84393 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Poppins', 'Georgia', serif;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Diary/Album Card Style */
    .diary-card {
        background: rgba(255, 255, 255, 0.92);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3), inset 0 0 20px rgba(232, 67, 147, 0.2);
        border: 4px solid #fff;
        text-align: center;
        max-width: 650px;
        margin: auto;
        position: relative;
        overflow: hidden;
    }
    
    /* Glowing Animated Title */
    .gorgeous-header {
        font-size: 3.8rem !important;
        font-weight: 900;
        background: -webkit-linear-gradient(#d63031, #e84393);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        margin-bottom: 5px;
    }
    
    .romantic-sub {
        font-size: 1.6rem;
        color: #636e72;
        font-style: italic;
        margin-bottom: 30px;
    }

    /* MEGA DIAL-DHADAKTA HEART ANIMATION */
    .heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 25px 0;
    }

    .giant-pulsing-heart {
        font-size: 130px;
        color: #d63031;
        display: inline-block;
        animation: heartPulse 0.6s infinite alternate;
        filter: drop-shadow(0 0 25px #ff4e50);
        cursor: pointer;
    }

    @keyframes heartPulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.25) rotate(5deg); }
    }

    /* Diary Page Text Container */
    .diary-page-text {
        font-size: 1.4rem;
        color: #2d3436;
        line-height: 1.8;
        background: #fff8f8;
        padding: 25px;
        border-radius: 20px;
        border: 2px dashed #ff7675;
        margin: 25px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        min-height: 120px;
    }

    /* Premium Custom Audio Player Box */
    .audio-box {
        background: linear-gradient(90deg, #e84393, #ff7675);
        padding: 15px;
        border-radius: 50px;
        margin: 20px auto;
        max-width: 90%;
        box-shadow: 0 8px 20px rgba(232, 67, 147, 0.4);
    }
    
    /* Custom Streamlit Buttons override */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #d63031, #e84393) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 12px 35px !important;
        border: none !important;
        box-shadow: 0 6px 20px rgba(214, 48, 49, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-3px) scale(1.03) !important;
        box-shadow: 0 10px 25px rgba(232, 67, 147, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# App Container initialized as a Diary Album layout
st.markdown('<div class="diary-card">', unsafe_allow_html=True)

st.markdown('<h1 class="gorgeous-header">Anshika ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="romantic-sub">My Diary of Special Memories & Wishes</p>', unsafe_allow_html=True)

# 1. MEGA DHADAKTA HUA DIL
st.markdown('<div class="heart-container"><span class="giant-pulsing-heart">❤️</span></div>', unsafe_allow_html=True)

# 2. HIGH-QUALITY ROMANTIC INSTRUMENTAL AUDIO LAYER
st.markdown('<div class="audio-box">', unsafe_allow_html=True)
# Pixabay high-quality direct streaming romantic instrumental audio track 
st.audio("https://soundhelix.com", start_time=0)
st.markdown('</div>', unsafe_allow_html=True)
st.caption("✨ Pyaari music shuru karne ke liye upar play button par click karein! ✨")

# 3. DIARY PAGES / STORYBOOK CAROUSEL STATE MANAGEMENT
diary_pages = [
    "📖 **Page 1: The Magic of You...** \n\n Anshika, tumhaari smile me wo jadoo hai jo meri puri duniya ko ek hi pal me roshan kar deta hai. Tum sirf meri best friend nahi ho, tum meri life ki sabse pyaari aadat ho! Happy Birthday to the most gorgeous girl! 🌹",
    "💌 **Page 2: Dil Se Dua...** \n\n Bhagwan se bas yahi dua hai ki tumhaari life ka har ek pal is canvas ki tarah colourful aur sparkling ho. Tumhe duniya ki har wo khushi mile jiski tum khwaahish rakhti ho. Mera sath hamesha tumhaare sath rahega! 💝",
    "💫 **Page 3: My Best Blessing...** \n\n Kuch log life me itne special hote hain ki unke bina zindagi adhuri lagti hai. Mere liye wo tum ho. Tumhaari baatein, tumhaara support aur tumhaari dosti mere liye premium aur priceless hain. 🥰",
    "🎂 **Page 4: The Ultimate Celebration!** \n\n Aaj tumhaara janamdin hai, isliye udasi ki koi jagah nahi honi chahiye. Tumhe duniya ka sabse best aur happy status milna chahiye kyunki tum sach me pure gold ho. Happy Birthday, Anshika! 🥂"
]

if 'current_page' not in st.session_state:
    st.session_state.current_page = 0

# Display the colorful text block like a real diary sheet
st.markdown(f'<div class="diary-page-text">{diary_pages[st.session_state.current_page]}</div>', unsafe_allow_html=True)

# Navigation elements formatted in beautiful alignment columns
c1, c2 = st.columns(2)
with c1:
    if st.button("⬅️ Turn Page Back"):
        st.session_state.current_page = (st.session_state.current_page - 1) % len(diary_pages)
        st.rerun()

with c2:
    if st.button("Turn Page Next ➡️"):
        st.session_state.current_page = (st.session_state.current_page + 1) % len(diary_pages)
        st.rerun()

st.markdown('<hr style="border-top: 2px solid #ff7675; opacity: 0.3;">', unsafe_allow_html=True)

# 4. PREMIUM MAGICAL SURPRISE CONFETTI BUTTON
if st.button("🎁 Open Anshika's Birthday Surprise Box! 🎁"):
    st.balloons()
    st.snow()
    st.success("🎉 You are the most beautiful star of my life! Happy Birthday Once Again! ✨👑❤️")

st.markdown('</div>', unsafe_allow_html=True)
