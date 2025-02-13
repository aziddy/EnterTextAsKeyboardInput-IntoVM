import readline
import platform


class SequenceCompleter:
    """Handles tab completion for sequence names."""
    def __init__(self, sequences):
        self.sequences = sequences
        self.matches = []

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.sequences 
                              if s.startswith(text)]
            else:
                self.matches = list(self.sequences)
        
        # Return match indexed by state (0, 1, 2, ...)
        try:
            return self.matches[state]
        except IndexError:
            return None

def setup_autocomplete(sequences):
    """Set up readline with tab completion for sequences."""
    completer = SequenceCompleter(sequences)
    readline.set_completer(completer.complete)
    
    # Handle different readline configurations for different operating systems
    if platform.system() == 'Darwin':  # macOS
        readline.parse_and_bind('bind ^I rl_complete')
    else:  # Linux, Windows, etc.
        readline.parse_and_bind('tab: complete')
    
    # Set word delimiters - we want to treat the entire input as one word
    readline.set_completer_delims('')