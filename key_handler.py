VALID_KEYS = {'enter', 'tab', 'esc'}

def get_key_action(key_after_string: str) -> str | None:
    """
    Validates and returns the key action if valid, None otherwise.
    
    Args:
        key_after_string (str): The key action to validate
        
    Returns:
        str | None: The validated key action or None if invalid/none
    """
    key = key_after_string.lower()
    return key if key in VALID_KEYS else None 