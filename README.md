# Keylogger Simulation with Discord Webhook (Educational)

This project is a **keylogger behavior simulation written in Python**, designed strictly for **educational, malware analysis, and defensive security research purposes**.

It demonstrates how keylogging malware typically captures keystrokes, maintains persistence, and exfiltrates data using external services such as webhooks.

> ⚠️ **Legal & Ethical Disclaimer**  
> This project is provided **for educational and research purposes only**.  
> The author does **not take responsibility** for any misuse, damage, or illegal activity resulting from this code.  
> Do **NOT** run this software on systems you do not own or have explicit permission to test.  
> Always use this project in **isolated lab environments or virtual machines**.

---

## Overview

The script runs silently in the background on a **Windows system**, captures keyboard input, and periodically sends the collected data to a **Discord webhook**.

Additionally, it demonstrates a common persistence technique by adding itself to the **Windows Registry**, ensuring execution on system startup.

This project is intended to help security professionals understand:
- How keyloggers operate
- How persistence mechanisms work on Windows
- How data exfiltration can be implemented
- How such threats can be detected and mitigated

---

## Features

- Captures keystrokes, including special keys (Enter, Backspace, etc.)
- Detects **Caps Lock** and **Num Lock** states for accurate logging
- Sends captured keystroke logs to a Discord webhook at fixed intervals
- Achieves persistence via **Windows Registry (Run key)**
- Runs silently in the background

---

## Requirements

- Windows operating system
- Python 3.x

---

## Required Python Modules

### `pynput`
- **Purpose**: Captures keyboard input events
- **Usage**: Monitors key presses and releases

Installation:
```bash
pip install pynput
dhooks
Purpose: Sends messages to Discord webhooks

Usage: Exfiltrates captured keystroke logs

Installation:

bash
pip install dhooks
Installation
Clone the repository:

bash
git clone <repository-url>
cd <repository-directory>
Install required dependencies:

bash
pip install pynput dhooks
How It Works (High-Level)
Keyboard Monitoring

Uses pynput to capture keystrokes globally

Records both regular and special keys

Key State Tracking

Tracks Caps Lock and Num Lock states

Ensures accurate character representation

Data Buffering

Keystrokes are stored temporarily in memory

Logs are grouped to avoid excessive network traffic

Data Exfiltration

Logs are sent to a Discord webhook at regular intervals

Demonstrates webhook-based C2-style communication

Persistence

Adds itself to the Windows Registry

Ensures execution on system startup

Persistence Mechanism
The script modifies the Windows Registry:

HKCU\Software\Microsoft\Windows\CurrentVersion\Run

This technique is commonly used by malware to survive reboots and is an important detection point for defenders.

Defensive Learning Outcomes
This project helps defenders understand:

How keyloggers capture user input

Why registry monitoring is critical

How outbound webhook traffic can indicate compromise

The importance of endpoint detection and response (EDR)

How simple malware achieves persistence

Safe Usage Guidelines
✔ Run only inside:

Virtual machines

Malware analysis labs

Controlled test environments

✖ Do NOT run on:

Personal computers

Corporate endpoints

Systems without explicit authorization

Project Structure
graphql
Kodu kopyala
.
├── keylogger.py   # Main keylogger simulation script
├── README.md     # Documentation
License
This project is licensed under the MIT License.
See the LICENSE file for details.

Final Note
Studying how keyloggers work is essential for building effective defenses.

Understanding attacker techniques is a prerequisite for strong endpoint security.
