import datetime as dt
import args_handler as ah

logFile = 'log.eslog'

def clearLog():
    log = open(logFile, 'w')
    log.write('')
    log.close()

def writeLog(userinput):
    log = open(logFile, 'a')

    inputArray = str(userinput).split()
    command = inputArray[0]
    time = dt.datetime.now()

    log.write(str(time))
    log.write('\nInput Array: ')
    log.write(str(inputArray))
    log.write('\nCommand: ')
    log.write(str(command))
    log.write('\nArgs: ')
    log.write(str(ah.setArgs(inputArray, command)))
    log.write('\n\n')

    log.close()