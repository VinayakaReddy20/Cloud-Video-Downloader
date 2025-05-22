import streamlit as st
from downloader import download_video
import os
import shutil
from datetime import datetime

# Set up page config
st.set_page_config(page_title="☁️ Cloud Video Downloader", page_icon="☁️", layout="centered")

# Custom styles for Batman dark theme
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #0f0f0f, #1a1a1a);
            font-family: 'Segoe UI', sans-serif;
            color: #f5f5f5;
        }
        .title {
            text-align: center;
            font-size: 3.2em;
            font-weight: bold;
            color: #f1c40f;
            padding-top: 20px;
        }
        .desc {
            text-align: center;
            font-size: 1.2em;
            color: #bdc3c7;
            margin-bottom: 30px;
        }
        .footer {
            margin-top: 3rem;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
        }
        .css-1aumxhk {
            background-color: #2c3e50 !important;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            color: #ecf0f1 !important;
        }
        .stButton>button {
            background-color: #f1c40f;
            color: black;
            font-weight: bold;
            border-radius: 8px;
        }
        .stTextInput>div>div>input {
            background-color: #34495e;
            color: #ecf0f1;
        }
        .stSelectbox>div>div>div>div {
            background-color: #34495e;
            color: #ecf0f1;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">☁️ Cloud Video Downloader</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Download public YouTube and Instagram videos from the shadows</div>', unsafe_allow_html=True)

# Input form
with st.form("download_form"):
    url = st.text_input("🔗 Video URL", placeholder="https://www.youtube.com/watch?v=xyz or https://www.instagram.com/p/abc")
    quality = st.selectbox("🎞️ Choose Video Quality", ["best", "best[height<=1080]", "best[height<=720]", "best[height<=480]", "worst"])
    submit = st.form_submit_button("Download")

if submit:
    if url:
        with st.spinner(" Downloading from the Cloud... please wait..."):
            try:
                file_path, title = download_video(url, quality)

                st.success(f"✅ Download complete: {title}")
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Click here to download",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4"
                    )

                # Auto cleanup (optional)
                now = datetime.now()
                for file in os.listdir("temp"):
                    path = os.path.join("temp", file)
                    if os.path.isfile(path):
                        if (now - datetime.fromtimestamp(os.path.getmtime(path))).seconds > 600:
                            os.remove(path)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}. Ensure the link is public and valid.")
    else:
        st.warning("⚠️ Please enter a valid link.")

st.markdown('<div class="footer">Built in the dark. For educational purposes only. Videos are not stored and are auto-deleted periodically.</div>', unsafe_allow_html=True)
