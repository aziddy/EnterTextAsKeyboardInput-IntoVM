import pyautogui
import time
from dotenv import load_dotenv
import os
from key_handler import get_key_action

# Load environment variables
load_dotenv()

# Get all STRING* variables from .env file
strings_to_type = []
i = 1
while True:
    string_var = f"STRING{i}"
    if string_var in os.environ:
        strings_to_type.append(os.environ[string_var])
        i += 1
    else:
        break

# Get settings from .env
delay_before_start = float(os.getenv('DELAY_BEFORE_START', 5))
delay_between_strings = float(os.getenv('DELAY_BETWEEN_STRINGS', 1))
raw_key_after_string = os.getenv('KEY_AFTER_STRING', 'none')

if not strings_to_type:
    print("No strings found in .env file! Please add strings as STRING1, STRING2, etc.")
    exit(1)

# Delay before starting (gives you time to focus the VM window)
print(f"You have {delay_before_start} seconds to focus your VM window...")
time.sleep(delay_before_start)

# Type each string with the specified key action
for text in strings_to_type:
    pyautogui.write(text)
    
    # Check and handle key action for each iteration
    key_action = get_key_action(raw_key_after_string)
    if key_action is not None:
        pyautogui.press(key_action)
    
    time.sleep(delay_between_strings) 