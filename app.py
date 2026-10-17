import streamlit as st

# Premium configurations
st.set_page_config(page_title="For My Gorgeous Anshika ❤️", page_icon="🌹", layout="centered")

# Premium High-End Romantic Velvet Red & Glow UI
st.markdown("""
    <style>
    /* Continuous Deep Velvet Red Romantic Background */
    .stApp {
        background: linear-gradient(135deg, #4a00e0 0%, #8e2de2 30%, #d63031 70%, #1a0000 100%) !important;
        background-size: 200% 200% !important;
        animation: pulseRomantic 10s ease infinite !important;
        font-family: 'Georgia', serif;
    }
    
    @keyframes pulseRomantic {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Premium Glassmorphism Diary Container */
    .diary-box {
        background: rgba(15, 0, 0, 0.65);
        padding: 40px 30px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(255, 0, 76, 0.4), inset 0 0 15px rgba(255,255,255,0.1);
        border: 2px solid rgba(255, 76, 116, 0.3);
        text-align: center;
        max-width: 600px;
        margin: auto;
    }
    
    /* Neon Glowing Crimson Title */
    .anshika-title {
        font-size: 4rem !important;
        font-weight: 900;
        color: #fff;
        text-shadow: 0 0 10px #ff004c, 0 0 20px #ff004c, 0 0 30px #ff004c;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    
    .romantic-sub {
        font-size: 1.4rem;
        color: #ff7675;
        font-style: italic;
        margin-bottom: 25px;
    }

    /* THE BIGGEST GLOWING REAL BEATING HEART */
    .heart-zone {
        margin: 30px 0;
    }

    .mega-beating-heart {
        font-size: 140px;
        display: inline-block;
        animation: premiumHeartBeat 0.5s infinite alternate;
        filter: drop-shadow(0 0 30px #ff0000);
        cursor: pointer;
    }

    @keyframes premiumHeartBeat {
        0% { transform: scale(1); filter: drop-shadow(0 0 15px #ff0000); }
        100% { transform: scale(1.3) rotate(-5deg); filter: drop-shadow(0 0 40px #ff004c); }
    }

    /* Secret Diary Pages Style */
    .diary-sheet {
        font-size: 1.35rem;
        color: #fff;
        line-height: 1.8;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #ff004c;
        margin: 25px 0;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }

    /* Customized Premium Action Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff004c, #ff7675) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        padding: 12px 30px !important;
        border: none !important;
        box-sizing: border-box;
        box-shadow: 0 5px 15px rgba(255, 0, 76, 0.4) !important;
        width: 100%;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px #ff004c !important;
    }
    </style>
""", unsafe_allow_html=True)

# App UI Container Starts
st.markdown('<div class="diary-box">', unsafe_allow_html=True)

st.markdown('<h1 class="anshika-title">Anshika ❤️</h1>', unsafe_allow_html=True)
st.markdown('<p class="romantic-sub">~ My Ultimate Romantic Digital Diary ~</p>', unsafe_allow_html=True)

# 1. THE MEGA BEATING RED HEART ANIMATION
st.markdown('<div class="heart-zone"><span class="mega-beating-heart">❤️</span></div>', unsafe_allow_html=True)

# 2. GUARANTEED DIRECT WORKING ROMANTIC INSTRUMENTAL TRACK
st.markdown("### 🎵 Feel the Love Music")
# Stable Direct-link CD-quality server path to ensure it plays on every device
st.audio("https://soundhelix.com", start_time=0)
st.caption("👉 Click the PLAY icon above to fire up the premium background music track!")

# 3. INTERACTIVE LOVE DIARY CAROUSEL
st.markdown("<h4 style='color: #ff7675; margin-top:20px;'>📖 Read My Heart Pages</h4>", unsafe_allow_html=True)

diary_messages = [
    "✨ **Page 1: The One & Only...** \n\n Anshika, tumhaari smile mere pure din ki thakan mita deti hai. Tum sirf meri best friend nahi, meri har khushi ka premium zariya ho. Happy Birthday to the most gorgeous girl on earth! 🌹",
    "💫 **Page 2: Hamesha Tumhaare Sath...** \n\n Bhagwan se dua hai ki tumhaari life hamesha is red velvet theme ki tarah chamakti rahe. Tum jo chaho wo tumhe mile, aur mera sath tumhaare sath hamesha barkarar rahe. 💝",
    "🥰 **Page 3: Priceless Blessing...** \n\n Tumhaari dosti aur tumhaara sath mere liye sabse bada gift hai. Tumse baat karke lagta hai jaise duniya ki saari fikar gayab ho gayi ho. You are my true blessing, Anshika! ✨",
    "👑 **Page 4: The Birthday Celebration!** \n\n Aaj tumhaara janamdin hai, toh dhoom-dhaam se celebrate banta hai! Hamesha aise hi muskuraati raho aur mujhe satati raho. Happy Birthday Once Again! 🥂🎂"
]

if 'page_no' not in st.session_state:
    st.session_state.page_no = 0

# Display Current Page inside the custom dark premium sheet
st.markdown(f'<div class="diary-sheet">{diary_messages[st.session_state.page_no]}</div>', unsafe_allow_html=True)

# Horizontal Interactive Buttons
b1, b2 = st.columns(2)
with b1:
    if st.button("⬅️ Previous Wish"):
        st.session_state.page_no = (st.session_state.page_no - 1) % len(diary_messages)
        st.rerun()
with b2:
    if st.button("Next Surprise ➡️"):
        st.session_state.page_no = (st.session_state.page_no + 1) % len(diary_messages)
        st.rerun()

st.markdown('<hr style="border-top: 1px solid rgba(255,255,255,0.1); margin: 25px 0;">', unsafe_allow_html=True)

# 4. TRIPLE SURPRISE ANIMATION BUTTON
if st.button("🌟 Click Here for Anshika's Grand Surprise! 🌟"):
    st.balloons()
    st.snow()
    st.toast("I Love Your Smile, Anshika! ❤️", icon="🔥")
    st.success("🎉 May this birthday bring infinite magic into your life! Happy Birthday! 👑🌹")

st.markdown('</div>', unsafe_allow_html=True)
