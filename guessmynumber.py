import random

num1 = random.randint(1, 10)

tries = 0

while True:
    while True:
        num = input("Guess my number, between 1 and 10: ").strip()
        try:
            num = int(num)
            if num in range(1, 11):
                break
            else:
                print('Please enter a number between 1 and 10.')
                continue
        except ValueError:
            print('Please enter a number between 1 and 10.')
            continue

    if num == num1:
        print("Correct! You guessed my number!")
        break
    elif tries == 3:
            print(f"You Failed! My number was {str(num1)}!")
            break
    else:
        print("Incorrect! Keep trying!")
        tries += 1
        print(f"You have {str(tries)}/3 tries remaining.")
