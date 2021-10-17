import datetime as dt
import args_handler as ah

logFile = 'log.eslog'

def clearLog():
    # writes a blank string to the file therefor clearing it
    log = open(logFile, 'w')
    log.write('')
    log.close()

def writeLog(userinput):
    # apeends the command, input array and args to the log, this is usefull for debuging
    log = open(logFile, 'a')
    if not userinput:
        userinput = 'NAN'

    inputArray = str(userinput).split()
    command = inputArray[0]
    time = dt.datetime.now()

    log.write(str(time))
    log.write('\nInput Array: ')
    log.write(str(inputArray))
    log.write('\nCommand: ')
    log.write(str(command))
    log.write('\nArgs: ')
    log.write(str(ah.setArgs(inputArray)))
    log.write('\n\n')

    log.close()