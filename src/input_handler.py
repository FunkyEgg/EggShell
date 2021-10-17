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
        if not args:
            print('you need to supply a math equation')
            return

        invalidChars = [
            '!', '@', '#', '$', '%', '^', '&', '_',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'W', 'Z',
            ',', '.', ';', "'", '[', ']', '\\',
            '<', '>', '?', ':', '"', '{', '}', '|'
        ]

        argStr = ''.join(args)
        errorCheck = list(argStr)
        invalidCharDetected = False

        for i in errorCheck:
            for x in invalidChars:
                if x in i:
                    invalidCharDetected = True
                else:
                    continue
        
        if invalidCharDetected == True:
            print(' '.join(args) + ' is invalid math')
        elif ' '.join(args).endswith('*') or ' '.join(args).endswith('+') or ' '.join(args).endswith('-') or ' '.join(args).endswith('/'):
            print('math cannot end with a operator')
        else:
            try:
                print(eval(' '.join(args)))
            except:
                print('invalid math make sure you typed it right')

    else:
        print(command + ' is a invalid command')
