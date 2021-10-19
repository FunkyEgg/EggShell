import input_handler as ih
import log_handler as lh

def main():
    while True:
        userInput = input('>> ')

        lh.writeLog(userInput)
        ih.handleInput(userInput)

if __name__ == '__main__':
    lh.clearLog()
    main()
