import yaml
from pathlib import Path

# Default configuration values
DEFAULT_CONFIG = {
    'sequence_start_delay': 3,  # seconds
    'show_example_sequences': True
}

def ensure_config_dir():
    """Create the user_config directory if it doesn't exist."""
    config_dir = Path('user_config')
    config_dir.mkdir(exist_ok=True)
    return config_dir

def create_default_config():
    """Create the default configuration file if it doesn't exist."""
    config_path = ensure_config_dir() / 'config.yml'
    
    if not config_path.exists():
        with open(config_path, 'w') as f:
            yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False, sort_keys=False)
        print(f"Created default configuration file at {config_path}")
    
    return config_path

def load_config():
    """Load the configuration from file, creating default if needed."""
    config_path = create_default_config()
    
    try:
        with open(config_path, 'r') as f:
            user_config = yaml.safe_load(f)
        
        # Ensure all required keys are present
        for key, default_value in DEFAULT_CONFIG.items():
            if key not in user_config:
                user_config[key] = default_value
        
        return user_config
    
    except Exception as e:
        print(f"Error loading config, using defaults: {str(e)}")
        return DEFAULT_CONFIG.copy() 