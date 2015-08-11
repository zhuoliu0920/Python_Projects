#!/usr/bin/python3

import sys

class Error(Exception):
    """Base class for other exceptions"""
    pass

class InputError(Error):
    """Raised when the value is not in required range"""
    pass






def main():
    #initial amount of coins
    nk = 25
    dm = 25
    qt = 25
    on = 0
    fv = 0

    print( "Welcome to the vending machine change maker program Change maker initialized. Stock contains:\n  %s nickels\n  %s dimes\n  %s quarters\n  %s ones\n  %s fives \n" % (nk, dm, qt, on, fv) )

    while True:
        while True:
            try:
                price = input("Enter the purchase price (xx.xx) or `q' to quit:")
                if price == 'q':
                    sys.exit(0)
                else:
                    init_due = round(float(price)*100)
                    if init_due%5 != 0:
                        raise InputError
                    else:
                        due = init_due
                        print("\nMenu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill\n  'c' - cancel the purchase \n")
                        print("Payment due:", due//100, "dollars and", due%100, "cents")
                        change = -1
                        while due > 0:
                            pay_code = str(input("Indicate your deposit:"))
                            if pay_code == 'n':
                                due -= 5
                                nk += 1
                            elif pay_code == 'd':
                                due -= 10
                                dm += 1
                            elif pay_code == 'q':
                                due -= 25
                                qt += 1
                            elif pay_code == 'o':
                                due -= 100
                                on += 1
                            elif pay_code == 'f':
                                due -= 500
                                fv += 1
                            elif pay_code == 'c':
                                change = init_due-due
                                break
                            else:
                                print("Illegal selection:", pay_code)
                        nk_out, dm_out, qt_out = (0, 0, 0)
                        if change == -1:
                            change = -due
                        if change > 0:
                            print("\nPlease take the change below.")
                            qt_out = change//25
                            change = change%25
                            print("  %s quarters" % qt_out)
                            dm_out = change//10
                            change = change%10
                            print("  %s dimes" % dm_out)
                            nk_out = change//5
                            print("  %s nickel" % nk_out)
                        print( "\nStock contains:\n  %s nickels\n  %s dimes\n  %s quarter\n  %s ones\n  %s fives\n" % (nk-nk_out, dm-dm_out, qt-qt_out, on, fv) )
                        break
            except (InputError, ValueError):
                print("Illegal price: Must be a non-negative multiple of 5 cents.")

if __name__ == "__main__":
    main()
