import yt_dlp
from rich import print
from rich import print

async def download_audio(url, title):
    ydl_opts = {
        "outtmpl": f".{title}.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"[green bold]Audio downloaded as '{title}.mp3'.[/green bold]")