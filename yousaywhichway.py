import sys, os, requests
import random as r
from time import sleep
from bs4 import BeautifulSoup

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

print()
print()
print('তততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততত')
print('                                                                                               ')
print('                                                                                               ')
print('    ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧              ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧          ')
print('                                                                                               ')
print('                            Welcome to YouSayWhichWay!                              ')
print('                                                                                               ')
print('    ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧              ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧          ')
print('                                                                                               ')
print('                                                                                               ')
print('তততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততততত')
print()
print()


sleep(2)
write('Please enter your desired character name below.')
name = input(prompt).strip()
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
sleep(3)
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
    sleep(6)
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
    sleep(6)
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
    sleep(6)
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
    sleep(6)
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
    sleep(6)

print()
write('Here is your playercard!')
print()
print('Player Info:')
print(f'Name: {name}')
print(f'Class: {randclass}')
print(f'Current Health:  {health}')
print(f'Current Strength: {strength}')
print(f'Current Intelligence: {intelligence}')
print()
sleep(4)
write(f'Here we start our journey {name}. YouSayWhichWay is a combination of chance and choice. Your character explores for you, but you have to deal with what happens to that character on their way. Your journey begins here. You character finds a book. Please turn to page {pagenum1} of the YouSayWhichWay manual.')
print()

sleep(7)
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
f.write('--------------------------------------\n')
f.write('Player Info:\n')
f.write(f'Name: {name}\n')
f.write(f'Class: {randclass}\n')
f.write(f'Final Health:  {health}\n')
f.write(f'Final Strength: {strength}\n')
f.write(f'Final Intelligence: {intelligence}\n')
f.write('-\n')
f.write(f'Date completed: {date}.\n')
f.write('--------------------------------------\n')
