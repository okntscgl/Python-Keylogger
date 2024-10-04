# Keylogger with Discord Webhook Integration

This project is a simple keylogger that captures keystrokes on a Windows machine and sends the captured logs to a specified Discord webhook URL. The keylogger runs in the background and is set to execute on system startup.

## Features

- Captures keystrokes, including special keys (e.g., Enter, Backspace).
- Detects the state of Caps Lock and Num Lock to accurately log characters.
- Sends captured logs to a Discord webhook at regular intervals.
- Automatically adds itself to the Windows Registry for persistence.

## Requirements

- Python 3.x

### Required Modules

1. **pynput**
   - **Description**: A Python library that allows you to monitor and control input devices. It is used to capture keyboard events in this project.
   - **Installation**:
     ```bash
     pip install pynput
     ```

2. **dhooks**
   - **Description**: A simple library to send messages to Discord webhooks. It is used to send captured keystroke logs to a Discord channel.
   - **Installation**:
     ```bash
     pip install dhooks
     ```

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
