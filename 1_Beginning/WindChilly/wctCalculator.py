#!/usr/bin/python3

while True:
    try:
        num_str_temp = input( "Please enter the degree:")
        temp = float(num_str_temp)
        break
    except ValueError:
        print("Please enter a number, try again!\n")

while True:
    try:
        num_str_speed = input( "Please enter the MPH:")
        speed = float(num_str_speed)
        break
    except ValueError:
        print("Please enter a number, try again!\n")

wct_index = 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16
print ("The WCT index is:", wct_index)
