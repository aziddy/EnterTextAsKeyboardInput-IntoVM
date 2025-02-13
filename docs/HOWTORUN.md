# How to Run

## Setup

1. Create a Python virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```


## Running the Program

1. Make sure your virtual environment is activated:
    ```bash
    source venv/bin/activate
    ```

2. Run the script:
    ```bash
    python3 src/main.py # Or python (without the 3 on your system)
    ```

3. Select a sequence to run. (TAB Complete is available)
    ```bash
    (venv) EnterTextAsKeyboardInput-IntoVM % python src/main.py

    Loading sequences...
    ✓ Loaded user_sequences/example_sequence_3.yml
    ✓ Loaded user_sequences/example_sequence_2.yml
    ✓ Loaded user_sequences/example_sequence_1.yml

    All sequences loaded successfully!

    Available sequences:
    - example_sequence_3
    - example_sequence_2
    - example_sequence_1

    Tip: Use TAB key to autocomplete sequence names

    Enter the sequence name to execute (or 'quit' to exit): 
    ```

4. Refocus to your window within the specified delay time.
    ```bash
    Preparing to execute 'example_sequence_2'...
    Please focus the target window within '3' seconds...
    Executing sequence...
    Sequence completed!
    ```

## Making a New Sequence

1. Create a new `.yml` file in the `user_sequences` directory.
2. Reference the provided `example_sequence_*.yml` files for **syntax and ideas!**
3. Run the program and select your new sequence.

## Configure Program
1. If `user_config/config.yml` is not present, run the program atleast once to generate it
2. Edit the `user_config/config.yml` file to to change the following:
    - `sequence_start_delay`: Number of seconds to wait before starting a sequence
    - `show_example_sequences`: Boolean to show example sequences in the program

## Notes
- Move your mouse to any corner of the screen to force-stop the program
- For a complete list of available special keys, see [Special Keys List](SPECIALKEYLIST.md)
