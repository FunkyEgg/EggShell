import args_handler as ah

def handleInput(userinput):
    inputArray = str(userinput).split()
    command = inputArray[0]
    args = ah.setArgs(inputArray, command)