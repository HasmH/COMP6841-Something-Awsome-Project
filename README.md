# COMP6841 Something Awsome Project
By HasmH  
Project Summary:

My Something Awesome Project was to create a keylogger, and cookie theft malware that is disguised as a simple video game. I decided to create this program using Python3 in a Windows environment, as I wanted to furhter flesh out my Python3 knowledge, as well as learn more about Windows OS at a deeper, lowe level - technical knowledge which I believe is very important in order to become a good security engineer. 


Another goal of this project was to step out of my comfort zone by creating a YouTube series. This YouTube series consists of videos which I uploaded weekly - I documented my  SA project progress. Along with explaining my progress to my YouTube audience, I also tried to relate my code/project with what we were learning in that particular week. For example - talking about Insiders and Malicious payloads in this YouTube video/Progress Checkin. 

Here is a link to a playlist of all videos that I have created so far for this project: [Playlist](https://www.youtube.com/playlist?list=PLWFGhqiHyIelLM40o_86uf88sSzfIQml3) 

Overall, considering the progress I made, I believe the final product for my SA Project deserves a DN grade. There were some pitfalls to my project and features I did not have time to implement and may have underestimated the difficulty of - this is something I will talk about in Project Scope and Project Reflection

Project Features: 

The scope of this project was to challenge my programming abilities, and to teach me relevant security concepts on the way. The project's work load and features was split up and and allocated particular weeks of the term to complete in. Here are the features of the SA Project: 

Keyloger ✔️

The keylogger was successfully implemented using Python's pynput package

One relevant concept I ran into when implementing this feature was the notion of "Security Through Obscurity" 

Since the keylogs were being stored as 'log' files, I had to find a way to obscure this from potential victims, as creating a 'log.txt' in the root of the install file might be too suspicious and the victim might realise they have something suspicious on their Windows PC. 

I addressed this issue in later weeks - see below


Cookie Thief ✔️

The cookie theft feature was successfully implemented using Python's browser_cookie3 package

Another relevant concept I came across when implementing this feature was "Session Hijacking" and "Encryption" - since it taught me the dangers and possibilities an attacker had if they were to steal a victim's cookie data. 

The cookie information was stored in runtime at this point of the implementation. 


Data Exfiltration/Stealing Data ✔️

At this stage of the project, I had ran into issues on trying to obscure the the keylogs and cookie data.

I attempted to store them in JSON objects, and as an attachment, but sending this via SMTP would be too time consuming for me, so I decided to store the key logs as a list, and the cookie's as a jsonified string, combining the two into a "payload" via a Python dictionary

I then sent this Python dictionary as plain text via SMTP 

Another hurdle in this stage was setting up a dummy account with gmail to send myself victim keylogs/cookies, as there were certain permissions that had to be tweaked in the gmail settings to be able to interact with their SMPT server. 


GUI/"Sneaky Video Game" ✔️

Straight forward process - using Python's tkinter and following a YouTube tutorial to create a random number guesser game that would be linked to my original sneaky.py file


Persistance  and combining the GUI with the Malware ❌

Unfourtanetly, this is where my SA Project took a turn. 

I had two independent files - a front-end interface game called "random_number_guesser.py" and my malware file that keylogs, cookie steals and data exfiltrates called "sneaky.py"

Although I was able to compile both of these seperately as their own Windows executables, I was unable to use Pyhton's os module, to spawn sneaky.py when random_number_guesser.py is run, and then put a timer on sending new keylogs to my email. 

I am aware of the method, however I do not have time unfourtauntely to reach the HD range for this project. 

My general understanding of how to achieve this, would be to first compile sneaky.py and random_number_guesser.py as standalone executables using pyinstallers "--onefile" parameter.

One this is done, I would create another Python script that simpley executes both of them at the same time, and add an internal timer to sneaky.py to resend keylogs every X hours or so. 
  
 

