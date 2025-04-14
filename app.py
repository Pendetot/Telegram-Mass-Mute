import os
import time
import sys
from telethon import TelegramClient, sync
from telethon.tl.types import InputPeerNotifySettings
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from colorama import Fore, Style, init

init(autoreset=True)

def display_banner():
    banner = f"""
{Fore.CYAN}----------------------------------------
{Fore.YELLOW}        MasVen Telegram Mass Mute
{Fore.CYAN}----------------------------------------
{Fore.GREEN}    Automatic Mute for Groups, Channels & Bots
{Fore.CYAN}----------------------------------------
    """
    print(banner)

def loading_animation(message, progress, total):
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    idx = int(time.time() * 10) % len(spinner)
    percent = (progress / total) * 100
    bar_length = 20
    filled_length = int(bar_length * progress // total)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    sys.stdout.write(f"\r{Fore.YELLOW}{message} {spinner[idx]} [{bar}] {percent:.1f}% ({progress}/{total}) ")
    sys.stdout.flush()

def save_credentials(api_id, api_hash):
    with open('data.py', 'w') as f:
        f.write(f'API_ID = {api_id}\nAPI_HASH = "{api_hash}"')

def load_credentials():
    try:
        from data import API_ID, API_HASH
        return API_ID, API_HASH
    except ImportError:
        return None, None

def main():
    display_banner()
    
    api_id, api_hash = load_credentials()
    
    if api_id is None or api_hash is None:
        print(f"{Fore.CYAN}[*] Kredensial tidak ditemukan")
        api_id = int(input(f"{Fore.GREEN}[+] Masukkan API ID: "))
        api_hash = input(f"{Fore.GREEN}[+] Masukkan API Hash: ")
        save_credentials(api_id, api_hash)
        print(f"{Fore.GREEN}[√] Kredensial tersimpan di data.py")
    else:
        print(f"{Fore.GREEN}[√] Kredensial berhasil dimuat dari data.py")
    
    print(f"{Fore.CYAN}[*] Memulai sesi Telegram...")
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    
    settings = InputPeerNotifySettings(
        mute_until=2147483647
    )
    
    print(f"{Fore.CYAN}[*] Mengambil daftar dialog...")
    dialogs = list(client.iter_dialogs())
    count = 0
    total = len(dialogs)
    
    print(f"{Fore.CYAN}[*] Menemukan {total} dialog")
    print(f"{Fore.YELLOW}[*] Memulai proses mute...")
    
    for i, dialog in enumerate(dialogs):
        if dialog.is_group or dialog.is_channel or dialog.entity.bot:
            loading_animation("Sedang memproses", i+1, total)
            client(UpdateNotifySettingsRequest(
                peer=dialog.input_entity,
                settings=settings
            ))
            count += 1
            time.sleep(0.05)
    
    sys.stdout.write("\r" + " " * 70 + "\r")
    print(f"{Fore.GREEN}[√] Selesai! Total grup/channel/bot di mute: {count}")
    client.disconnect()

if __name__ == "__main__":
    main()