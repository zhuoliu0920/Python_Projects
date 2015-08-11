#!/usr/bin/env python3

def get_input_data():
    while True:
        try:
            file_name = str(input("Open what file:"))
            f = open(file_name, 'r')
            f.close()
            return(file_name)
            break
        except (IOError,NameError):
            print("Bad file name, try again")
            pass

def get_data_list(file_object, column_number):
    with open(file_object, 'r') as f:
        lines = f.readlines()
        list_of_tuples = [( (l.strip().split(','))[0], float((l.strip().split(','))[column_number]) ) for l in lines[1:]]
    return(list_of_tuples)

def average_data(list_of_tuples):
    new_lt = []
    count_month = 0
    for i,t in enumerate(sorted(list_of_tuples)):
        month = t[0][5:7]+'-'+t[0][:4]
        if new_lt == []:
            new_lt.append([t[1], month])
            count_month += 1
        elif month == new_lt[-1][1]:
            new_lt[-1][0] += t[1]
            count_month += 1
        else:
            new_lt[-1][0] = new_lt[-1][0]/count_month
            new_lt.append([t[1], month])
            count_month = 1
    new_lt[-1][0] = new_lt[-1][0]/count_month
    return(new_lt)
        




def main():
    filename = get_input_data()
    column = int(input("What column (1-6):"))
    data_with_date = get_data_list(filename, column)
    month_average = sorted(average_data(data_with_date))
    print("Lowest 6 for column {}".format(column))
    for i in range(6):
        print("Date:{0}, Value:{1:.2f}".format(month_average[i][1], month_average[i][0]))
    print("\nHighest 6 for column {}".format(column))
    for i in range(1,7):
        print("Date:{0}, Value:{1:.2f}".format(month_average[-i][1], month_average[-i][0]))

if __name__ == "__main__":
    main()

