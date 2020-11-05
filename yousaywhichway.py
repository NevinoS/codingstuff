import sys, os
import random as r
from time import sleep

classes = ['Mage', 'Berserker', 'Healer', 'Archer', 'Tank']
prompt = '>>> '
health = 0
strength = 0
intelligence = 0
special = ['']
pagenum1 = r.randint(1,10)
pagenum2 = r.randint(10,15)
pagenum3 = r.randint(15,20)
tries = 0

# --------------------------------------------------------------------------------------------------

def write(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    print()

print('তততততততততততততততততততততততততততততততততত')
print('                                                ')
print('                                                ')
print('    ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧          ')
print('                                                ')
print('    Welcome to YouSayWhichWay!            ')
print('                                                ')
print('    ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧          ')
print('                                                ')
print('                                                ')
print('তততততততততততততততততততততততততততততততততত')


sleep(2)
write('Please enter your desired character name below.')
name = input(prompt)
print()
sleep(2)
write(f'Hello {name}!')
print()



randclass = classes[r.randint(0,4)]
write(f'Generating random class...')
sleep(2)
print()
write(f'Your generated class is {randclass}!')
print()
if randclass == 'Mage':
    health += 85
    strength += 25
    intelligence += 125
    special.append('MageStaff')
    write(f'{randclass}:')
    write('Health: 85')
    write('Strength: 25')
    write('Intelligence: 125')
    write('Special: Mage Staff')
    print()
    sleep(4)
elif randclass == 'Berserker':
    health += 115
    strength += 75
    intelligence += 15
    special.append('Me Smash Head')
    write(f'{randclass}:')
    write('Health: 115')
    write('Strength: 75')
    write('Intelligence: 15')
    write('Special: Me Smash Head')                                      # It works!!! Now health can be depleted, or added to throughout the program, just like other player stats.
    print()
    sleep(4)
elif randclass == 'Healer':
    health += 105
    strength += 35
    intelligence += 65
    special.append('Wish')
    write(f'{randclass}:')
    write('Health: 105')
    write('Strength: 35')
    write('Intelligence: 65')
    write('Special: Wish')
    print()
    sleep(4)
elif randclass == 'Archer':
    health += 95
    strength += 35
    intelligence += 50
    special.append('Extreme Focus')
    write(f'{randclass}:')
    write('Health: 95')
    write('Strength: 35')
    write('Intelligence: 50')
    write('Special: Extreme Focus')
    print()
    sleep(4)
else:
    health += 185
    strength += 45
    intelligence += 25
    special.append('Fortify')
    write(f'{randclass}:')
    write('Health: 185')
    write('Strength: 45')
    write('Intelligence: 25')
    write('Special: Fortify')
    print()
    sleep(4)


def playercard():
    print()
    print('Player Info:')
    print(f'Name: {name}')                    # They should be able to ask for their playercard at any point throughout the program!
    print(f'Class: {randclass}')
    print(f'Current Health:  {health}')
    print(f'Current Strength: {strength}')
    print(f'Current Intelligence: {intelligence}')

print()
write('Here is your playercard. You can view it at any point by entering "playercard" into the terminal!')
print()
playercard()
print()
write(f'Here we start our journey {name}. YouSayWhichWay is a combination of chance and choice. Your character explores for you, but you have to deal with what happens to that character on their way. Your journey begins here. You character finds a book. Please turn to page {pagenum1} of the YouSayWhichWay manual.')
print()

sleep(5)
if pagenum1 == 1:
    write(f'You have turned to page {pagenum1}! Enter your solution to the page below.')
    while True:
        oneans = input(prompt).lower().strip()
        if oneans in ['yes']:
            write(f'Correct! The answer was {oneans}')
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
        elif tenans not in ['yes']:
            tries += 1
            write(f'Incorrect! You have used {tries}/3 tries.')
            if tries == 3:
                write('Oh No! It is the end of the road for you friend. Game ended, You Died.')
                break
