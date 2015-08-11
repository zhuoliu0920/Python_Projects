#!/usr/bin/python3

class Error(Exception):
    """Base class for other exceptions"""
    pass

def checkInput(word):
    if (not word.isdigit()) or (len(word) != len(set(word))) or (len(word) != 4):
        return(False)
    else:
        return(True)

def printResult(total_results):
    for r in total_results:
        print("{0}: exist:{1}, position:{2}".format(r[0],r[1],r[2]))
    print()

def main():
    while True:
        try:
            key = str(input("What is the key:"))
            print()
            if checkInput(key):
                chance = 12
                bingo = False
                total_results = []
                while (chance > 0) and (not bingo):
                    while True:
                        try:
                            guess = str(input("Guess:"))
                            if checkInput(guess):
                                exist = 0
                                position = 0
                                for (i,l) in enumerate(guess):
                                    if l in key:
                                        exist += 1
                                    if guess[i] == key[i]:
                                        position += 1
                                result = (guess, exist, position)
                                total_results.append(result)
                                printResult(total_results)
                                chance -= 1
                                if position == 4:
                                    bingo = True
                            else:
                                raise Error
                            break
                        except Error:
                            print("****Please enter a valid guess, 4 digits only, without duplicate.")
                            printResult(total_results)
                if bingo == True:
                    print("Bingo! It took you {} guesses".format(12-chance))
                else:
                    print("Ops! You are out of chances")
            else:
                raise Error
            break
        except Error:
                print("****Please enter a valid key, 4 digits only, without duplicate.")


if __name__ == "__main__":
    main()

