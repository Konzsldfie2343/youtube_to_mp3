import requests
from rich import print

async def download_thumbnail(url):
    video_id = url.split("watch?v=")[-1]
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        with open(".thumbnail.jpg", "wb") as f:
            f.write(response.content)
        print("[green bold]Thumbnail downloaded successfully.[/green bold]")
    else:
        raise Exception("[red bold]Failed to download thumbnail.[/red bold]")