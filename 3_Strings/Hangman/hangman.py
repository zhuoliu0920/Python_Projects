#!/usr/bin/python3

class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidInputError(Error):
    """Raised when the value is not valid"""
    pass
class DuplicateInputError(Error):
    """Raised when the value is duplicate"""
    pass

def reminder(chance, letters, result):
    print("Changces Remaining : {}".format(chance))
    print("Missed Letters/Digits : {}".format(letters))
    for r in result:
        print(r, end=" ")
    print("\n\n")

def main():
    word = str(input("Please enter phrase to guess:"))
    
    chance = 6
    missed_letters = ''
    result = ['_'] * len(word)
    for (i,l) in enumerate(word):
        if not l.isalpha():
            result[i] = l
    reminder(chance, missed_letters, result)

    while chance > 0 and ('_' in result):
        while True:
            try:
                guess = str(input("Your guess (letters only):"))
                if (len(guess) != 1) or (not guess.isalpha()):
                    raise InvalidInputError
                elif (guess.lower() in missed_letters) or (guess.lower() in result) or (guess.upper() in result):
                    raise DuplicateInputError
                else:
                    correct_flag = False
                    for (i,l) in enumerate(word):
                        if not l.isalpha():
                            result[i] = l
                        elif l.lower() == guess.lower():
                            result[i] = l
                            correct_flag = True
                        else:
                            pass

                    if correct_flag == False:
                        missed_letters += guess.lower()
                        chance -= 1
                    reminder(chance, missed_letters, result)                 
                break
            except InvalidInputError:
                print("Not a valid character. Please enter a letter.\n")
            except DuplicateInputError:
                print("You have already tried this letter or digit. Guess again!\n")


if __name__ == "__main__":
    main()

