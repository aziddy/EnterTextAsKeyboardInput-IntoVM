from user_config import load_config
from load_sequences import load_sequences
from automcomplete import setup_autocomplete
from execute_sequence import execute_sequence
from util.colors import ORANGE, RESET

# Load configuration
CONFIG = load_config()


def main():
    # Load all sequences
    sequences = load_sequences()
    
    # If no sequences found
    if not sequences:
        print("No sequences found in user_sequences directory!")
        print("Please add .yml files to the user_sequences directory.")
        print("You can use example_sequence.yml as a template.")
        return

    # Set up tab completion
    setup_autocomplete(sequences.keys())

    # Print available sequences
    print("\nAvailable sequences:")
    for seq_name in sequences.keys():
        print(f"- {seq_name}")

    print("\nTip: Use TAB key to autocomplete sequence names")
    
    # Get sequence name from user
    sequence_name = input("\nEnter the sequence name to execute (or 'quit' to exit): ")
    
    while sequence_name.lower() != 'quit':
        if sequence_name in sequences:
            print(f"\nPreparing to execute '{sequence_name}'...")
            print(f"{ORANGE}Please focus the target window within '{CONFIG['sequence_start_delay']}' seconds...{RESET}")
            execute_sequence(sequences[sequence_name])
            print("Sequence completed!")
        else:
            print(f"Sequence '{sequence_name}' not found!")
        
        sequence_name = input("\nEnter another sequence name (or 'quit' to exit): ")

if __name__ == "__main__":
    main()