import streamlit as st
import os

# Custom canvas page configurations for an elite setup
st.set_page_config(page_title="Happy Birthday Anshika! ✨", page_icon="🎓", layout="centered")

# Automatic background animations on page load
st.snow()
st.balloons()

# 100% Exact Replica of the Laser Neon Light Heart via HTML5 Canvas JavaScript Engine
st.markdown("""
    <style>
    /* Full view dark neon canvas background override */
    .stApp {
        background: #050508 !important;
        font-family: 'Poppins', 'Helvetica', sans-serif;
        overflow-x: hidden;
    }

    /* Core Content Wrapper Shell */
    .screenshot-layout-shell {
        text-align: center;
        max-width: 600px;
        margin: auto;
        padding: 5px;
    }

    /* MENTOR TOP SENDER TAG WITH PULSING AURA */
    .sender-tag {
        font-size: 1.15rem;
        font-weight: bold;
        color: #ff4d6d;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 20px;
        text-shadow: 0 0 10px #ff004c;
    }

    /* DYNAMIC GLOW HAPPY BIRTHDAY TITLE WITH INTENSE GREEN MATRIX SHIFT */
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

    /* HIGH-LEVEL NEON LASER HEART MATRIX CONTAINER */
    .laser-heart-frame {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 25px 0;
        background: #000;
        border-radius: 20px;
        border: 2px solid #ff004c;
        box-shadow: 0 0 30px rgba(255, 0, 76, 0.5);
        padding: 10px;
    }

    /* ELITE ENGLISH MOTIVATIONAL SCROLL CARDS */
    .classy-scroll-card {
        background: rgba(15, 15, 25, 0.95);
        font-size: 1.25rem !important;
        font-weight: 500;
        line-height: 1.6;
        padding: 35px 25px;
        border-radius: 20px;
        border: 2px solid #ff004c;
        margin-top: 30px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 0 20px rgba(255, 0, 76, 0.3);
        color: #ffffff;
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

    /* TYPEWRITER BOX ENGINE */
    .typewriter-box {
        margin: 35px 0;
        background: rgba(255, 255, 255, 0.05);
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

# --- SIDE-BY-SIDE FIXED LAYOUT GRID FOR PHOTO AND BOARD ---
target_photo = "rotated_photo_only~2.jpg"

col1, col2 = st.columns(2)

with col1:
    if os.path.exists(target_photo):
        st.image(target_photo, use_container_width=True)
    else:
        st.image("https://unsplash.com", use_container_width=True)

with col2:
    st.markdown("""
        <div style="background: rgba(15,15,25,0.95); border: 2px solid #ff004c; border-radius: 15px; padding: 22px 12px; color: white; font-weight: bold; font-size: 1.15rem; text-align: center; display: flex; flex-direction: column; gap: 15px; box-shadow: 0 8px 25px rgba(255,0,76,0.4);">
            <div>❤️ Pure Brilliance ❤️</div>
            <div>🌹 Outstanding Scholar 🎓</div>
            <div>✨ Absolute Grace 💘</div>
        </div>
    """, unsafe_allow_html=True)

# --- THE MATRIX NEON LASER HEART LIGHT SHOW ENGINE ---
st.markdown('<div class="laser-heart-frame">', unsafe_allow_html=True)
st.components.v1.html("""
    <canvas id="laserHeartCanvas" width="400" height="400" style="background:#000; max-width:100%;"></canvas>
    <script>
    const canvas = document.getElementById('laserHeartCanvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width;
    let height = canvas.height;
    let time = 0;

    function getHeartPoint(t) {
        // Core parametric heart equation variables mapping
        let x = 16 * Math.pow(Math.sin(t), 3);
        let y = 13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t);
        return { x: x * 8 + width/2, y: -y * 8 + height/2 - 10 };
    }

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        ctx.fillRect(0, 0, width, height);
        
        time += 0.02;
        let points = [];
        
        // Generating core structural points on the outer boundary
        for (let t = 0; t < Math.PI * 2; t += 0.05) {
            points.push(getHeartPoint(t));
        }
        
        // Drawing the brilliant radiant laser beam lines from the epicenter
        for (let i = 0; i < points.length; i++) {
            let p = points[i];
            let hue = (i * 5 + time * 50) % 360;
            ctx.beginPath();
            ctx.moveTo(width/2, height/2 - 10);
            ctx.lineTo(p.x, p.y);
            ctx.strokeStyle = `hsla(${hue}, 100%, 60%, 0.35)`;
            ctx.lineWidth = 1.5;
            ctx.stroke();
        }

        // Drawing the outer boundary sparkling flower star nodes replica
        for (let i = 0; i < points.length; i++) {
            let p = points[i];
            let hue = (i * 6 - time * 60) % 360;
            ctx.beginPath();
            ctx.arc(p.x, p.y, 4 + Math.sin(time + i)*2, 0, Math.PI * 2);
            ctx.fillStyle = `hsla(${hue}, 100%, 70%, 1)`;
            ctx.shadowColor = `hsla(${hue}, 100%, 60%, 1)`;
            ctx.shadowBlur = 15;
            ctx.fill();
        }
        
        requestAnimationFrame(draw);
    }
    draw();
    </script>
""", height=420)
st.markdown('</div>', unsafe_allow_html=True)

# --- ELITE ENGLISH MOTIVATIONAL BOARDS ---
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
