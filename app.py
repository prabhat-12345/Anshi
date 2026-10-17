import streamlit as st

# Page setup and styling for a premium romantic theme
st.set_page_config(page_title="Happy Birthday Anshika! ❤️", page_icon="🎂", layout="centered")

# Custom CSS for gorgeous fonts, animated pulsing heart, and glowing shadows
st.markdown("""
    <style>
    /* Premium background gradient */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        font-family: 'Georgia', serif;
    }
    
    /* Main container styling */
    .main-container {
        text-align: center;
        padding: 30px;
        background: rgba(255, 255, 255, 0.45);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(255, 75, 75, 0.2);
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
    
    /* Title text styling */
    .gorgeous-title {
        font-size: 3.5rem !important;
        font-weight: bold;
        color: #d63031;
        text-shadow: 2px 2px 8px rgba(214, 48, 49, 0.3);
        margin-bottom: 5px;
        animation: fadeIn 2s ease-in-out;
    }
    
    .subtitle {
        font-size: 1.5rem;
        color: #e84393;
        font-style: italic;
        margin-bottom: 25px;
    }

    /* THE BIG BEATING HEART EFFECT */
    .heart-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 160px;
        margin: 20px 0;
    }

    .beating-heart {
        font-size: 100px;
        color: #d63031;
        display: inline-block;
        animation: beat .8s infinite alternate;
        transform-origin: center;
        filter: drop-shadow(0 0 15px rgba(214, 48, 49, 0.6));
        cursor: pointer;
    }

    @keyframes beat {
        to { transform: scale(1.3); }
    }
    
    /* Quote styling */
    .romantic-quote {
        font-size: 1.3rem;
        color: #4a4a4a;
        line-height: 1.6;
        background: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-left: 5px solid #d63031;
        border-radius: 10px;
        margin: 20px auto;
        max-width: 600px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Button redesign */
    div.stButton > button:first-child {
        background-color: #d63031 !important;
        color: white !important;
        font-size: 1.2rem !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(214, 48, 49, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.05) !important;
        background-color: #e84393 !important;
        box-shadow: 0 6px 20px rgba(232, 67, 147, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main structure
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="gorgeous-title">Happy Birthday, Anshika! ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">To the most special girl in my world...</p>', unsafe_allow_html=True)

# Big Beating Heart Section
st.markdown('<div class="heart-box"><span class="beating-heart">❤️</span></div>', unsafe_allow_html=True)

# Audio Player (Optional: YouTube or background link placeholder)
st.audio("https://soundhelix.com", start_time=0)
st.caption("🎵 Click play to add a romantic rhythm to this moment!")

st.markdown('</div>', unsafe_allow_html=True)

# Romantic & Beautiful Quotes Section (Interactive Carousel via buttons)
st.markdown("### 💌 Dil Ki Baatein (Special Wishes for You)")

quotes = [
    "“Anshika, tum sirf meri best friend nahi, meri duniya ka sabse khoobsurat hissa ho. Tumhaari smile se mera har din roshan hota hai. Happy Birthday, My Special One! 🌹”",
    "“Duniya ki sabse gorgeous girl ko janamdin ki dher saari mubarakbaad. Khuda kare tumhaari zindagi me har wo khushi ho jo tum chaaho, aur mera sath hamesha tumhaare sath rahe! 💝”",
    "“Kuch log zindagi me aakar use hamesha ke liye badal dete hain. Meri life me wo insaan tum ho. Meri best friend, meri guide aur sabse pyaari blessing. Happy Birthday, Anshika! 🥰”",
    "“Tumhaare sath bitaya har lamha premium hai. Aaj tumhaara din hai, ise khul kar jiyo aur hamesha aise hi muskurati raho. You deserve the best birthday in the universe! 🎂🥂”"
]

# Track quote state without page refresh issues
if 'quote_index' not in st.session_state:
    st.session_state.quote_index = 0

st.markdown(f'<div class="romantic-quote">{quotes[st.session_state.quote_index]}</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅️ Previous Wish"):
        st.session_state.quote_index = (st.session_state.quote_index - 1) % len(quotes)
        st.rerun()

with col2:
    if st.button("Next Surprise Wish ➡️"):
        st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)
        st.rerun()

# Surprise Confetti Trigger
if st.button("🎉 Click for Magical Birthday Surprise! 🎉"):
    st.balloons()
    st.snow()
    st.success("You are the most beautiful person, Anshika! Have an amazing year ahead! ✨❤️")
  
