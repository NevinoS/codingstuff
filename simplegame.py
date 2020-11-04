import sys, os
import random as r
from time import sleep
# no i reading

classes = ['Mage', 'Berserker', 'Healer', 'Sniper', 'Tank']
classatr = ['has maximum intelligence, lowered strength and powerful magic weapons, such as Mage Staff', 'has maximum strength, high speed, but lowered intelligence wiith strong melee weapons!', ' will keep the team alive with healing abilities such as Aura and revive!', 'is the long ranged shooter. Pick a target, you shoot.', 'has very high Health Points, however lack in speed and weapon damage.']
prompt = '>>> '


def write(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    print()

def menu():
    write('{ Welcome to my game! }')
    print('  ===================  ')
    sleep(2)
    write('Please enter your desired character name below.')
    name = input(prompt)
    sleep(1)
    write(f'Hello {name}!')


def charclass():
    randclass = classes[r.randint(0,4)]
    write(f'>> Your randomly generated class is {randclass}! <<')
    if randclass == 'Mage':
        write(f'>> {randclass} {classatr[0]} <<')
    elif randclass == 'Berserker':
        write(f'>> {randclass} {classatr[1]} <<')
    elif randclass == 'Healer':
        write(f'>> {randclass} {classatr[2]} <<')
    elif randclass == 'Sniper':
        write(f'>> {randclass} {classatr[3]} <<')
    else:
        write(f'>> {randclass} {classatr[4]} <<')

def mainframe():
    print()
    write('I will now explain to you how to play the game.')
    print('====================================================================================================================')
    print()
    sleep(3)
    write('During stage 1, you will be asked a series of questions, if you answer correctly, you may progress.')
    print('====================================================================================================================')
    print()
    sleep(3)
    write('On to stage 2. Here, your class will now affect your performance. I will not tell you any more than that for now...')
    print('====================================================================================================================')
    print()
    sleep(3)
    write('Stage 3. If somehow, you make it here, you will truly be put to the test.')
    print('====================================================================================================================')
    print()
    sleep(3)
    while True:
        write('Do you wish to continue? (Yes/No)')
        yn = input('').lower().strip()
        if yn not in ['yes', 'no', 'y', 'n', 'ye', 'na', 'nah', 'nope', 'yeah']:
            write('Please enter either Y or N!')
        if yn in ['yes', 'y', 'ye', 'yeah']:
            write('Great! Lets continue.')
            break
        elif yn in ['no', 'n', 'na', 'nah', 'nope']:
            write('Game ended. Reason: Not wanting to play.')
            return False
    write('So, recollect yourself, and prepare to be put to the test!')
    sleep(4)
    print()
    print(' - - - - - - - - - ')
    print('|     Stage 1.    |')
    print(' - - - - - - - - - ')
    print()

    # Question 1 of stage 1.

    sleep(2)
    write('First question. Difficulty: Low')
    write('What is the Capital of Russia? (Enter your answer below.)')
    while True:
        q1 = input(prompt).lower().strip()
        if q1 not in ['moscow', 'moscoe', 'mosvow', 'noscow', 'mosciw', 'mosccow', 'mocow']:
            write('Incorrect! The answer was Moscow. Game ended. You died LMAO')
            return False
        else:
            write('Correct! The answer was Moscow. You may progress!')
            break

    # Question 2 of stage 1.        

    sleep(2)
    write('Second Question. Difficulty: Low')
    write('What is pi to 5 decimal places? (Enter your answer below.)')
    while True:
        q2 = input(prompt).strip()
        if q2 not in ['3.14159']:
            write('Incorrect! The answer was 3.14159. Game ended. You died LMAO')
            return True
        else:
            write('Correct! The answer was 3.14159. You may progress!')
            break

    # Question 3 of stage 1.        

    sleep(2)
    write('Third Question. Difficulty: Medium')
    write('Name ONE product of photosynthesis? (Enter your answer below.)')
    while True:
        q3 = input(prompt).lower().strip()
        if q3 not in ['glucose', 'oxygen', 'atp', 'energy']:
            write('Incorrect! The answer was either Glucose, Oxygen or ATP (Energy). Game ended. You died LMAO')
            return False
        else:
            write(f'Correct! The answer was {q3}!. You may progress!')
            break

    # Question 4 of stage 1.        

    sleep(2)
    write('Fourth Question. Difficulty: Medium')
    write('In a standard game of football, how many players are on each team? (Enter your answer below.)')
    while True:
        q4 = input(prompt).strip()
        if q4 not in ['11']:
            write('Incorrect! The answer was 11. Game ended. You died LMAO')
            return False
        else:
            write(f'Correct! The answer was 11!. You may progress!')
            break

    # Question 5 of stage 1.        

    sleep(2)
    write('Fifth Question. Difficulty: High')
    write('What are stars mainly comprised of? (Format: **** and ****)')
    while True:
        q5 = input(prompt).lower().strip()
        if q5 not in ['hydrogen and helium', 'h and he', 'hydrogen and heleum', 'hydrogen, helium', 'hydrogenhelium', 'hydrogen helium']:
            write('Incorrect! The answer was Hydrogen and Helium. Game ended. You died LMAO')
            return False
        else:
            write(f'Correct! The answer was Hydrogen and Helium!. You may progress!')
            break

    # Question 6 of stage 1.        

    sleep(2)
    write('Sixth Question. Difficulty: High')
    write('How many planets are in our solar system? (Enter your answer below.)')
    while True:
        q3 = input(prompt).strip()
        if q3 not in ['8']:
            write('Incorrect! The answer was 8. Game ended. You died LMAO')
            return False
        else:
            write(f'Correct! The answer was 8!. You may progress!')
            break

    write('Congrats, you have completed the game up to its highest current acheivable level!')
    write('The game is still under development, hopefully.')
    write('Contributers: Billy, Faisal.')

    
    



def initgame():
    menu()
    charclass()
    mainframe()

initgame()
