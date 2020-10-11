import pyautogui as p
import time as t

t.sleep(5) #Waits for the user to go onto the selected platform to spam.
f = open('script.txt', 'r') #Opens the file with the spam script in
for word in f: #Runs for every word in the file
    p.typewrite(word) #Writes the word
    p.press('enter') #Presses enter after every word.
