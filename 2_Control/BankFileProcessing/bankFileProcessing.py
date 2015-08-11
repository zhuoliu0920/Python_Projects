#!/usr/bin/python3

import sys

def get_number(line):
    word = line.split()
    number = int(word[0])
    return(number)

def get_balance(line):
    word = line.split()
    balance = float(word[1])
    return(balance)

def get_name(line):
    word = line.split(None, 2)
    name = str(word[2])
    return(name)
    
def equal_floats(x,y):
    if(abs(x-y) < 1.0e-8):
        return(True)
    else:
        return(False)


def main():
    with open('./master.new.txt', 'w') as output_file, open('./sample.master.old.txt', 'r') as master_file, open('./user.inputs.txt', 'r') as user_file:

        m_all_lines = master_file.read().splitlines()
        user_file_lines = user_file.read().splitlines()
        i = 0 # line index of the user file
        for m_line in m_all_lines:
            if get_number(m_line) == 999999:
                output_file.write( "{0:06d} \n".format(get_number(m_line)) )
                break
            else:
                close_flag = False  # in default, account is not closed
                new_balance = get_balance(m_line)
                while i < len(user_file_lines):
                    if user_file_lines[i] == 'w':  # customer withdrawed money
                        new_balance -= float(user_file_lines[i+1])
                        i += 2
                        continue
                    elif user_file_lines[i] == 'd': # customer deposited money
                        new_balance += float(user_file_lines[i+1])
                        i += 2
                        continue
                    elif user_file_lines[i] == 'a': # next customer
                        i += 1
                        break
                    elif user_file_lines[i] == 'c': # customer closed account
                        close_flag = True
                        i += 1
                        continue
                    else:
                        print("Error user input file.")
                        sys.exit(1)
                if close_flag == False:
                    output_file.write( "{0:06d} {1:>10} {2}\n".format(get_number(m_line),new_balance,get_name(m_line)) )
    
if __name__ == "__main__":
    main()
