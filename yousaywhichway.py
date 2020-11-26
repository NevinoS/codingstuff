import sys, os, requests
import random as r
from time import sleep
from bs4 import BeautifulSoup

# Menu Stuff:

info = 'Welcome to You Say Which Way. This game is about chance and choice. Your character will explore across the world of Arnis, and you will have to do your best to protect them on their journey.'
'You will be tested upon morality, common knowledge and many other things. This game was created from an idea and nothing more. I, the creator [Billy], will personally see to it that you enjoy the game, thank you for playing!'

credits = ['Game Developer: Billy. B', 'Contributers: Faisal. M [for criticising me], Mr. Phillips [for teaching me ofc lol]']
credits = '\n'.join(credits)

# Class select stuff:

classes = ['Berserker', 'Mage', 'Healer', 'Archer', 'Tank']
health = 0
strength = 0
intelligence = 0
special = ['']

# Idk

prompt = '>>> '
pagenum1 = r.randint(1,10)
pagenum2 = r.randint(10,15)
pagenum3 = r.randint(15,20)
tries = 0

dateweb = requests.get('https://www.timeanddate.com/').text
soup1 = BeautifulSoup(dateweb, 'lxml')

date = soup1.find('span', {'id' : 'ij2'}).text

# --------------------------------------------------------------------------------------------------

def write(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.02)
    print()

def clear():
    os.system('cls')

def menu():
    clear()
    write('Welcome to You Say Which Way!')
    sleep(2)
    clear()
    print('---', '𝐘𝐨𝐮 𝐒𝐚𝐲 𝐖𝐡𝐢𝐜𝐡 𝐖𝐚𝐲', '---')
    print('1: Start')
    print('2: Info')
    print('3: Credits')
    print('--------------------------------')

menuStatus = True

while menuStatus:
    menu()
    opt = input('Please enter an option [1-3]: ').strip()
    try:
        opt in ['1', '2', '3']
    except ValueError:
        clear()
        menu()
        continue
    if opt == '1':
        menuStatus = False
        clear()
        write('Great... Shall we begin?')
        sleep(2)
        clear()
        break
    elif opt == '2':
        clear()
        write(info)
        sleep(10)
        clear()
        menu()
    elif opt == '3':
        write(credits)
        sleep(10)
        clear()
        menu()
    else:
        clear()
        sleep(0.5)
        write('Please enter an option [1-3] as intructed!')
        sleep(2)
        clear()
        continue





sleep(2)
write('Please enter your desired character name below.')
name = input(prompt).strip()
sleep(2)
clear()
write(f'Hello {name}!')
sleep(1.5)
clear()


def classMenu():
    sleep(0.5)
    print('----', '𝐂𝐥𝐚𝐬𝐬 𝐒𝐞𝐥𝐞𝐜𝐭', '----')
    print('1: Berserker')
    print('2: Mage')
    print('3: Healer')
    print('4: Archer')
    print('5: Tank')
    print('--------------------------------------------------------------')
    print(' >> TIP: Classes do not affect your performance in any way. << ')
    print('--------------------------------------------------------------')

def classSelect():
    classSelectStatus = True
    while classSelectStatus:
        classMenu()
        classopt = input('Please select your class [1-5]: ').strip()
        try:
            classopt in ['1', '2', '3', '4', '5']
        except ValueError:
            clear()
            write('Error: Please select a class [1-5] as instructed!')
            sleep(2.5)
            clear()
            classSelect()
        if classopt == '1':
            clear()
            write(f'You have selected {classes[0]}!')
            break
        elif classopt == '2':
            clear()
            write(f'You have selected {classes[1]}!')
            break
        elif classopt == '3':
            clear()
            write(f'You have selected {classes[2]}!')
            break
        elif classopt == '4':
            clear()
            write(f'You have selected {classes[3]}!')
            break
        elif classopt == '5':
            clear()
            write(f'You have selected {classes[4]}!')
            break
        else:
            sleep(0.5)
            clear()
            write('Error: Please select a class [1-5] as instructed!')
            sleep(2)
            clear()
            classSelect()

classSelect()




sleep(7)

correctAnsCount = 0

if pagenum1 == 1:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        oneans = input(prompt).lower().strip()
        if oneans in ['yes']:
            write(f'Correct! The answer was {oneans}')
            break
        elif oneans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 2:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        twoans = input(prompt).lower().strip()
        if twoans in ['yes']:
            write(f'Correct! The answer was {twoans}')
            break
        elif twoans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 3:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        threeans = input(prompt).lower().strip()
        if threeans in ['yes']:
            write(f'Correct! The answer was {threeans}')
            break
        elif threeans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 4:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        fourans = input(prompt).lower().strip()
        if fourans in ['yes']:
            write(f'Correct! The answer was {fourans}')
            break
        elif fourans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 5:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        fiveans = input(prompt).lower().strip()
        if fiveans in ['yes']:
            write(f'Correct! The answer was {fiveans}')
            break
        elif fiveans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 6:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        sixans = input(prompt).lower().strip()
        if sixans in ['yes']:
            write(f'Correct! The answer was {sixans}')
            break
        elif sixans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 7:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        sevenans = input(prompt).lower().strip()
        if sevenans in ['yes']:
            write(f'Correct! The answer was {sevenans}')
            break
        elif sevenans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 8:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        eightans = input(prompt).lower().strip()
        if eightans in ['yes']:
            write(f'Correct! The answer was {eightans}')
            break
        elif eightans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
elif pagenum1 == 9:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        nineans = input(prompt).lower().strip()
        if nineans in ['yes']:
            write(f'Correct! The answer was {nineans}')
            break
        elif nineans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
else:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        tenans = input(prompt).lower().strip()
        if tenans in ['yes']:
            write(f'Correct! The answer was {tenans}')
            break
        elif tenans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break

f = open('stats.txt', 'a')
