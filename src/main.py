import input_handler as ih
import log_handler as lh

def main():
    while True:
        userInput = input('>> ')
        
        ih.handleInput(userInput)
        lh.writeLog(userInput)

if __name__ == '__main__':
    lh.clearLog()

    main()
    