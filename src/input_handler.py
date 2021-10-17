import args_handler as ah

def handleInput(userinput):
    # gets all the stuff needed
    inputArray = str(userinput).split()
    command = inputArray[0]
    args = ah.setArgs(inputArray)