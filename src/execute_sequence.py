import pyautogui
import time
from dotenv import load_dotenv
import os
import yaml
import sys
import readline
import platform
import glob
import pathlib
from util.delayed_hotkey import delayed_hotkey
from user_config import load_config
from util.colors import RED, RESET

CONFIG = load_config()

def print_error(message):
    """Print an error message in red."""
    print(f"{RED}Error: {message}{RESET}")

def execute_command(command):
    """Execute a single keyboard command."""
    if isinstance(command, dict):
        for cmd_type, value in command.items():
            if cmd_type == 'type':
                # Handle both simple string and [text, interval] format
                if isinstance(value, list):
                    if len(value) != 2:
                        print_error("Type with interval must be [text, interval_in_seconds]")
                        return
                    text, interval = value
                    for char in text:
                        pyautogui.write(char)
                        time.sleep(float(interval))
                else:
                    pyautogui.write(value)
            elif cmd_type == 'press':
                pyautogui.press(value)
            elif cmd_type == 'hotkey':
                if not isinstance(value, list):
                    print_error(f"Hotkey value must be a list of keys, got: {value}")
                    return
                # Use our custom implementation with configurable delays
                delayed_hotkey(value, press_delay=50, release_delay=2)
            elif cmd_type == 'pause':
                # Convert milliseconds to seconds for time.sleep
                time.sleep(float(value) / 1000)
            else:
                print_error(f"Unknown command type: {cmd_type}")

def execute_sequence(sequence):
    """Execute a sequence of keyboard commands."""
    print(f"Executing sequence...")
    # Initial pause to give user time to focus the correct window
    time.sleep(CONFIG['sequence_start_delay'])
    
    for command in sequence:
        execute_command(command)