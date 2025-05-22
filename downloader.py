import yt_dlp
import os

def download_video(url, quality="best", output_path="temp"):
    os.makedirs(output_path, exist_ok=True)

    # Output file path
    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename, info.get('title', 'Video')
