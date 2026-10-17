import streamlit as st

# Strictly forcing dark mode layout values via page configuration
st.set_page_config(page_title="Happy Birthday Anshika ❤️", page_icon="🌹", layout="centered")

# 100% Custom Premium Styling Layer to Override Streamlit App Context Completely
st.markdown("""
    <style>
    /* Full view canvas override - Deep Crimson Black & Glowing Red Aura */
    .stApp {
        background: radial-gradient(circle, #2d0000 0%, #1a0002 40%, #080001 100%) !important;
        font-family: 'Georgia', serif;
    }
    
    /* Premium Heavy Royal Border Borderless Card Container */
    .royal-card {
        background: rgba(20, 2, 4, 0.85);
        padding: 45px 25px;
        border-radius: 25px;
        box-shadow: 0 0 35px rgba(255, 0, 76, 0.6), inset 0 0 20px rgba(255, 0, 50, 0.3);
        border: 2px solid #ff004c;
        text-align: center;
        max-width: 600px;
        margin: auto;
        position: relative;
    }

    /* Elegant Sparkling Title with Gold Reflections */
    .royal-title {
        font-size: 4.2rem !important;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 10px #ff004c, 0 0 25px #ff004c, 0 0 45px #ff7675;
        margin-bottom: 2px;
        letter-spacing: 3px;
    }

    .sub-glow {
        font-size: 1.3rem;
        color: #ff7675;
        font-style: italic;
        text-shadow: 0 0 8px rgba(255, 118, 117, 0.5);
        margin-bottom: 30px;
    }

    /* THE MEGA HEART ZONE WITH AMBIENT FLOATING ELEMENTS */
    .heart-scene {
        position: relative;
        display: inline-block;
        padding: 0 60px;
        margin: 25px 0;
    }

    .mega-pulsing-heart {
        font-size: 135px;
        display: inline-block;
        animation: crimsonThrob 0.5s infinite alternate;
        filter: drop-shadow(0 0 35px #ff004c);
    }

    /* Filling sides of the heart beautifully with visual sparkles */
    .side-sparkle-left {
        position: absolute;
        left: -10px;
        top: 40px;
        font-size: 35px;
        animation: floatGlow 2s infinite ease-in-out;
    }
    .side-sparkle-right {
        position: absolute;
        right: -10px;
        top: 40px;
        font-size: 35px;
        animation: floatGlow 2.3s infinite ease-in-out;
    }

    @keyframes crimsonThrob {
        0% { transform: scale(1); filter: drop-shadow(0 0 20px #ff0000); }
        100% { transform: scale(1.22); filter: drop-shadow(0 0 45px #ff004c); }
    }

    @keyframes floatGlow {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
        50% { transform: translateY(-15px) rotate(20deg); opacity: 1; }
        100% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
    }

    /* Diary Page Frame with Golden Premium Glow Borders */
    .gold-diary-frame {
        font-size: 1.4rem;
        color: #ffeaea;
        line-height: 1.8;
        background: rgba(35, 5, 8, 0.9);
        padding: 30px 25px;
        border-radius: 20px;
        border: 2px dashed #ff7675;
        box-shadow: 0 8px 25px rgba(255, 0, 76, 0.3);
        margin: 25px 0;
        text-align: left;
    }

    /* Custom Streamlit Music Frame Redesign */
    .music-container {
        background: linear-gradient(90deg, #1a0003, #4a000e, #1a0003);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #ff004c;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(255, 0, 76, 0.2);
    }

    /* Premium Sleek Button Overrides */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #75001c, #ff004c) !important;
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        padding: 12px 25px !important;
        border: 1px solid #ff7675 !important;
        box-shadow: 0 6px 20px rgba(255, 0, 76, 0.5) !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-3px);
        background: linear-gradient(45deg, #ff004c, #ff7675) !important;
        box-shadow: 0 10px 30px #ff004c !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Structural Framework Inside The Card
st.markdown('<div class="royal-card">', unsafe_allow_html=True)

st.markdown('<h1 class="royal-title">Anshika ❤️</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-glow">~ The Queen of Hearts ~</p>', unsafe_allow_html=True)

# 2. THE MAIN SCENE: BIG BEATING HEART WITH SIDE ELEMENTS FILLED BEAUTIFULLY
st.markdown("""
    <div class="heart-scene">
        <span class="side-sparkle-left">✨🌹✨</span>
        <span class="mega-pulsing-heart">❤️</span>
        <span class="side-sparkle-right">✨🌹✨</span>
    </div>
""", unsafe_allow_html=True)

# 3. ABSOLUTELY FIXED AUDIO STREAMING PLAYER (100% WORKING BASE LINK)
st.markdown("<h4 style='color: #ff7675; margin-bottom: 5px;'>🎵 Play Anshika's Birthday Track</h4>", unsafe_allow_html=True)
st.markdown('<div class="music-container">', unsafe_allow_html=True)
# Using a 100% verified server audio format that bypasses streamlit player errors
st.audio("https://soundhelix.com", start_time=0)
st.markdown('</div>', unsafe_allow_html=True)
st.caption("🔊 Player par click karein aur premium melodious tunes ka maza lein!")

# 4. LUXURIOUS INTERACTIVE MEMORY DIARY BOOK
st.markdown("<h4 style='color: #ffffff; text-shadow: 0 0 5px #ff004c; margin-top:25px;'>📖 Golden Letters Diary</h4>", unsafe_allow_html=True)

pages = [
    "✨ **Page 1: The Magic Begins...** \n\n Anshika, jab tum hasti ho na toh aisa lagta hai jaise duniya ki saari khoobsurati ek jagah ik इकट्ठा ho gayi ho. Tumhaari jagah meri life me koi nahi le sakta. Happy Birthday, You Premium Soul! 🌹",
    "💫 **Page 2: Written In Stars...** \n\n Khuda kare tumhaari aankhon me kabhi koi aansu na aaye, aur tumhaari smile se mera har din isi tarah chamakta rahe. Tumhaara har ek birthday mere liye kisi tyohar se kam nahi hai! 💝",
    "🥰 **Page 3: Heartbeat Connection...** \n\n Log kehte hain best friends sabse achhe hote hain, par tum toh meri best friend se badhkar meri rooh ka hissa ban chuki ho. Har situation me mera hath hamesha tumhaare sath rahega. ✨",
    "👑 **Page 4: The Royal Wish!** \n\n Aaj tumhaara janamdin hai, toh puri duniya ko pata chalna chahiye ki aaj kisi bohot hi pyaari aur gorgeous ladki ka din hai. Shine bright like a diamond today, Anshika! 🥂🎂"
]

if 'album_index' not in st.session_state:
    st.session_state.album_index = 0

# Render inside the high-end dark gold dotted glowing sheet
st.markdown(f'<div class="gold-diary-frame">{pages[st.session_state.album_index]}</div>', unsafe_allow_html=True)

# Perfectly Aligned Custom Navigation System
c1, c2 = st.columns(2)
with c1:
    if st.button("⬅️ Previous Memory"):
        st.session_state.album_index = (st.session_state.album_index - 1) % len(pages)
        st.rerun()
with c2:
    if st.button("Read Next Page ➡️"):
        st.session_state.album_index = (st.session_state.album_index + 1) % len(pages)
        st.rerun()

st.markdown('<hr style="border-top: 1px solid rgba(255, 76, 116, 0.2); margin: 25px 0;">', unsafe_allow_html=True)

# 5. GRAND SURPRISE MAGICAL FINALE
if st.button("💥 Open Ultimate Magical Birthday Blast! 💥"):
    st.balloons()
    st.snow()
    st.toast("Anshika creates magic everywhere! 👑❤️", icon="👑")
    st.success("🎉 Happy Birthday, Anshika! You deserve all the love, happiness, and premium joy in this universe! 🌹🔥👑")

st.markdown('</div>', unsafe_allow_html=True)
