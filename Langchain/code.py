import streamlit as st
import time
import random

# Page Setup
st.set_page_config(
    page_title="AI Scanner",
    page_icon="📸",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp{
    background: black;
    color: white;
}

.title{
    font-size:60px;
    text-align:center;
    font-weight:bold;
    color:#00ffcc;
    text-shadow:0px 0px 25px #00ffcc;
}

.scan-box{
    border:2px solid #00ffcc;
    padding:20px;
    border-radius:20px;
    background:rgba(0,255,200,0.05);
    box-shadow:0px 0px 30px #00ffcc;
}

.result{
    font-size:28px;
    text-align:center;
    color:#00ffcc;
    font-weight:bold;
    animation: glow 1s infinite alternate;
}

@keyframes glow{
    from{
        text-shadow:0 0 10px #00ffcc;
    }
    to{
        text-shadow:0 0 30px #00ffcc;
    }
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">⚡ AI FACE SCANNER ⚡</div>', unsafe_allow_html=True)

# Upload Image
uploaded = st.file_uploader(
    "Upload Your Photo",
    type=["jpg", "png", "jpeg"]
)

if uploaded:

    st.image(uploaded, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="scan-box">', unsafe_allow_html=True)

    scan = st.progress(0)

    scan_text = st.empty()

    effects = [
        "Scanning Face...",
        "Detecting Emotions...",
        "Reading Brain Signals...",
        "Analyzing Personality...",
        "Accessing AI Database...",
        "Generating Future Prediction..."
    ]

    for i in range(100):

        scan.progress(i + 1)

        if i % 15 == 0:
            scan_text.markdown(
                f"## {random.choice(effects)}"
            )

        time.sleep(0.03)

    st.markdown("</div>", unsafe_allow_html=True)

    # Funny Viral Results
    results = [
        "🔥 Main Character Energy",
        "🚀 Future Millionaire",
        "😈 Dangerous Mind Detected",
        "🧠 Genius Level: 99%",
        "💀 Too Cool For Reality",
        "👑 Viral Creator Identified",
        "⚡ Anime Hero Vibes"
    ]

    st.markdown(
        f'<div class="result">{random.choice(results)}</div>',
        unsafe_allow_html=True
    )

    st.balloons()