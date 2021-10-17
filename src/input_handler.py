import args_handler as ah
from os import *

def handleInput(userinput):
    # gets all the stuff needed
    inputArray = str(userinput).split()
    command = inputArray[0]
    args = ah.setArgs(inputArray)

    if command == 'cls' or command == 'clear':
        # depending on os name will run a seperate clear command
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    elif command == 'do':
        print(eval(' '.join(args)))
            

    else:
        print(command + ' is a invalid command')
