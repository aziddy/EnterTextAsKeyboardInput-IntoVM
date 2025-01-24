# How to Run

## Setup

1. Create a Python virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a `.env` file from the example `.env.example`:
```bash
cp .env.example .env
```

3. Edit your `.env` file with your strings and settings:
```bash
# Strings to type
STRING1=your_first_string
STRING2=your_second_string
STRING3=your_third_string

# Settings
DELAY_BEFORE_START=5
DELAY_BETWEEN_STRINGS=1
KEY_AFTER_STRING=enter  # Options: enter, tab, esc, none
```

## Running the Program

1. Make sure your virtual environment is activated:
```bash
source venv/bin/activate
```

2. Run the script:
```bash
python3 vm_keyboard_input.py # Or python (without the 3 on your system)
```

3. When prompted, switch to your VM window within the specified delay time.

## Notes

- The program will type each string in sequence with your specified delay between them
- If `KEY_AFTER_STRING` is set to a valid key (enter, tab, esc), that key will be pressed after each string
- If `KEY_AFTER_STRING` is set to 'none' or any invalid value, no key will be pressed
- Move your mouse to any corner of the screen to force-stop the program
- For a complete list of available special keys, see [Special Keys List](SPECIALKEYLIST.md)
