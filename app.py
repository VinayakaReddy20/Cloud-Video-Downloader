import streamlit as st
from downloader import download_video
import os

st.set_page_config(page_title="Cloud Video Downloader", layout="centered")

# Premium UI styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f6f8;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #34495e;
        }
        .desc {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 2rem;
        }
        .footer {
            margin-top: 3rem;
            text-align: center;
            color: #95a5a6;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

# UI Title
st.markdown('<div class="title">📥 Cloud Video Downloader</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Download public YouTube videos in one click</div>', unsafe_allow_html=True)

# URL input
url = st.text_input("🔗 Enter Video Link (YouTube or Instagram):")

# Quality selector
quality = st.selectbox("🎞️ Select Video Quality", [
    "best",
    "worst",
    "best[height<=720]",
    "best[height<=480]"
])

# Download button
if st.button("Download"):
    if url:
        with st.spinner("Downloading... please wait..."):
            try:
                file_path, title = download_video(url, quality)
                with open(file_path, "rb") as f:
                    st.success(f"✅ Download complete: {title}")
                    st.download_button(
                        label="📥 Click to Download",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4"
                    )
            except Exception as e:
                st.error("❌ Failed to download. Make sure the link is valid and the Instagram video is public.")
    else:
        st.warning("⚠️ Please enter a video link.")

# Footer
st.markdown('<div class="footer">Built for educational use. Videos are not stored permanently.</div>', unsafe_allow_html=True)
