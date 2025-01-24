# PyAutoGUI Special Keys

*Updated As of 2025-01-24*

Below is a comprehensive list of special keys that can be used with PyAutoGUI's `press()` function.

## Navigation Keys
- `enter` (Return)
- `tab`
- `space`
- `home`
- `end`
- `pageup`
- `pagedown`
- `up` (Arrow key)
- `down` (Arrow key)
- `left` (Arrow key)
- `right` (Arrow key)

## Control Keys
- `esc` (Escape)
- `insert`
- `delete`
- `backspace`

## Function Keys
- `f1` through `f20`

## Lock Keys
- `capslock`
- `numlock`
- `scrolllock`
- `printscreen`

## Modifier Keys
- `ctrl` (Control)
- `alt`
- `shift`
- `win` (Windows key)
- `command` (Mac command key)

## Numeric Keypad
- `num0` through `num9`
- `numenter`
- `numdecimal`
- `numlock`
- `add` (+)
- `subtract` (-)
- `multiply` (*)
- `divide` (/)

## Media Control Keys
- `volumemute`
- `volumedown`
- `volumeup`
- `nexttrack`
- `prevtrack`
- `playpause`
- `stop`

## Browser Control Keys
- `browserback`
- `browserforward`
- `browserhome`
- `browserrefresh`
- `browsersearch`
- `browserstop`

## Application Control
- `pause`
- `help`
- `sleep`
- `menu` (Application key or right-click key)

## Notes
- Keys are case-insensitive (`ENTER` and `enter` work the same)
- Some special keys might not work on all systems or in all applications
- For combinations, use PyAutoGUI's `hotkey()` function instead of `press()`
- Not all keys may be recognized in a VM environment 