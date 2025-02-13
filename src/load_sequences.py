import os
import yaml
import glob
import pathlib
from user_config import load_config
from util.colors import GREEN, RED, RESET

# Load configuration
CONFIG = load_config()

USER_SEQ_PATH = "user_sequences"

def load_sequences(directory=USER_SEQ_PATH):
    """Load all sequence files from the specified directory."""
    sequences = {}
    had_errors = False
    
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created {directory} directory")
        return sequences

    # Load all .yml files from the directory
    yaml_files = glob.glob(os.path.join(directory, '*.yml'))
    
    # Filter out example sequences if configured
    if not CONFIG['show_example_sequences']:
        yaml_files = [f for f in yaml_files if not os.path.basename(f).startswith('example_sequence_')]
    
    if not yaml_files:
        print("No .yml files found in user_sequences directory")
        return sequences

    print("\nLoading sequences...")
    for filepath in yaml_files:
        sequence = load_sequence_file(filepath)
        if sequence:
            sequences[sequence['name']] = sequence['commands']
            print(f"{GREEN}✓{RESET} Loaded {filepath}")
        else:
            had_errors = True
    
    if had_errors:
        print(f"\n{RED}Some sequences failed to load. See errors above.{RESET}")
    else:
        print(f"\n{GREEN}All sequences loaded successfully!{RESET}")
    
    return sequences



def load_sequence_file(filepath):
    """Load a single sequence file."""
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
            if not data:
                print_error(f"{filepath} is empty or has invalid YAML syntax")
                return None
            if not isinstance(data, dict):
                print_error(f"{filepath} must contain a YAML dictionary/object")
                return None
            if 'commands' not in data:
                print_error(f"{filepath} is missing required 'commands' field")
                return None
            if not isinstance(data['commands'], list):
                print_error(f"{filepath} 'commands' must be a list")
                return None
            
            # Validate each command
            for i, cmd in enumerate(data['commands']):
                if not isinstance(cmd, dict):
                    print_error(f"{filepath} command #{i+1} must be a dictionary/object")
                    return None
                if len(cmd) != 1:
                    print_error(f"{filepath} command #{i+1} must have exactly one action type")
                    return None
                cmd_type = list(cmd.keys())[0]
                if cmd_type not in ['type', 'press', 'hotkey', 'pause']:
                    print_error(f"{filepath} command #{i+1} has invalid type '{cmd_type}'")
                    return None
                
            return {
                'name': data.get('name', pathlib.Path(filepath).stem),
                'commands': data['commands']
            }
    except yaml.YAMLError as e:
        print_error(f"{filepath} has invalid YAML syntax:")
        print(f"{RED}  {str(e)}{RESET}")
        return None
    except Exception as e:
        print_error(f"Error loading {filepath}:")
        print(f"{RED}  {str(e)}{RESET}")
        return None