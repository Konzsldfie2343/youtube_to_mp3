import requests
from bs4 import BeautifulSoup
from modules.sanitize_filename import sanitize_filename
from rich import print


async def get_video_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title").text.replace(" - YouTube", "").strip()
        return sanitize_filename(title)
    else:
        raise Exception("[red bold]Failed to fetch video title.[/red bold]")