#!/usr/bin/python3

while True:
    try:
        order = int(input("Please input the order of square:"))
        break
    except ValueError:
        print("Invalid input, please try again.")

while True:
    try:
        tl_num = int(input("Please input the top left number:"))
        break
    except ValueError:
        print("Invalid input, please try again.")

print("The Latin Square is:")
for i in range(0, order):
    for j in range(0, order):
        print( "%s " % (order-(order-tl_num-i-j)%order), end = "" )
    print()
