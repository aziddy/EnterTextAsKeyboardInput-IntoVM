import pyautogui
import time

def delayed_hotkey(keys, press_delay=50, release_delay=50):
    """
    Different Implementation of PyAutoGUI's Hotkey Function that 
    in order KeyDown/Holds a Key, delays and then KeyDown/Holds 
    the following key untill all keys have been KeyDown/Held, 
    where we at the end release all keys

    Made this because the PyAutoGUI's Hotkey Function, Presses
    all defined keys as fast as possible, that most operating 
    systemscant keep up with
    
    Args:
        keys (list): List of keys to press in sequence
        press_delay (int): Delay in milliseconds between pressing each key
        release_delay (int): Delay in milliseconds between releasing each key
    """
    try:
        # Convert delays to seconds
        press_delay_sec = press_delay / 1000
        release_delay_sec = release_delay / 1000
        
        # Press each key in sequence with delay
        for key in keys:
            pyautogui.keyDown(key)
            time.sleep(press_delay_sec)
        
        # Small delay before starting to release
        time.sleep(press_delay_sec)
        
        # Release keys in reverse order with delay
        for key in reversed(keys):
            pyautogui.keyUp(key)
            time.sleep(release_delay_sec)
            
    except Exception as e:
        # If anything goes wrong, make sure to release all keys
        for key in keys:
            try:
                pyautogui.keyUp(key)
            except:
                pass
        raise e 