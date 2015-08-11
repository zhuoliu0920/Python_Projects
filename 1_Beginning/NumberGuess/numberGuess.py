#!/usr/bin/python3


print ("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!\n")

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueNotInRangeError(Error):
    """Raised when the value is not in required range"""
    pass

class ValueNotAnIntegerError(Error):
    """Raised when the value is not an integer"""
    pass

while True:
    try:    
        ans_str = input("*You* This will be the answer. Select a number 10-49:")
        if not ans_str.isdigit():
            raise ValueNotAnIntegerError()
        else:
            ans = int(ans_str)
            if (ans > 49) or (ans < 10):
                raise ValueNotInRangeError()
        break
    except ValueNotInRangeError:
        print("This value is not in required range. Try again!")
        print()
    except ValueNotAnIntegerError:
        print("This value is not an interger. Try again!")
        print()

while True:
    try:
        num_str = input("*Player* Pick any number 50-99:")
        if not num_str.isdigit():
            raise ValueNotAnIntegerError()
        else:
            num = int(num_str)
            if (num > 99) or (num < 50):
                raise ValueNotInRangeError()
        break
    except ValueNotInRangeError:
        print("This value is not in required range. Try again!")
        print()
    except ValueNotAnIntegerError:
        print("This value is not an interger. Try again!")
        print()

tmp1 = (99-ans) + num

tmp2 = tmp1//100 + tmp1%100


guessed_ans = num-tmp2

print ("I said the answer was", ans, "and the calculation result is", guessed_ans,"\n")
