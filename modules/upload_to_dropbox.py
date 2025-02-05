import dropbox
from dotenv import load_dotenv
import os
from rich import print
import asyncio
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")

async def upload_to_dropbox(file_path, file_name):
    if not DROPBOX_ACCESS_TOKEN:
        raise Exception("[red bold]Dropbox access token not found.[/red bold]")
    
    def upload_file():
        """同期的にDropboxにファイルをアップロードする関数"""
        try:
            dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
            with open(file_path, "rb") as f:
                dbx.files_upload(f.read(), f"/{file_name}")
        except dropbox.exceptions.AuthError as e:
            raise Exception(f"Dropbox authentication error: {e}")
    
    try:
        # 非同期に同期関数を実行
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            await loop.run_in_executor(executor, upload_file)
        print(f"[green bold]'{file_name}' uploaded to Dropbox.[/green bold]")
        return True
    except Exception as e:
        print(f"[red bold]Error: {e}[/red bold]")
        return False