x = ['Hello', 'Hello again', 'Hey'] # Array/List

for index, word in enumerate(x): #Iterates through the list
    if index == len(word) - 1: #If its the last value...
        print(word) #Print the word only
    else:
        print(word + ', ', end='') #Prints the word and a comma and a space! (Instead of going line by line, it replaces it with nothing)
