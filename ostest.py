import sys, os
import time

def write(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

write('Hello, I am not a human.')
