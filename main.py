import asyncio
from rich import print

from modules.get_args import get_args
from modules.download_thumbnail import download_thumbnail
from modules.crop_image import crop_image
from modules.download_audio import download_audio
from modules.get_video_title import get_video_title
from modules.set_cover import set_cover
from modules.upload_to_dropbox import upload_to_dropbox
from modules.cleanup import cleanup

import os


# Dropbox workaround
async def dropbox_workaround(title):
    if os.path.exists(f".thumbnail.jpg"):
        os.remove(".thumbnail.jpg")
    if os.path.exists(f".{title}.mp3"):
        os.rename(f".{title}.mp3", f"{title}.mp3")
    print("[blue bold]Dropbox workaround completed.[/blue bold]")


async def youtube_to_mp3(url):
    try:
        await download_thumbnail(url)
        await crop_image()
        title = await get_video_title(url)
        await download_audio(url, title)
        await set_cover(title)
        upload_status = await upload_to_dropbox(f".{title}.mp3", f"{title}.mp3")
        if upload_status:
            await cleanup(title)
        else:
            await dropbox_workaround(title)

    except Exception as e:
        print(f"[red bold]Error: {e}[/red bold]")


async def main():
    YOUTUBE_URLs = get_args()
    for url in YOUTUBE_URLs:
        await youtube_to_mp3(url)


if __name__ == "__main__":
    asyncio.run(main())
