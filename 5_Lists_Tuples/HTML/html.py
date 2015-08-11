#!/usr/bin/env python3

def main():
    output_list = [];
    with open('template.html', 'r') as f1, open('southPark.csv', 'r') as f2:
        lines = f1.readlines()
        content = f2.readline().strip().split(',')
        for i,l in enumerate(lines):
            if len(l) < 8 or i%2 != 0:
                output_list.append(l)
            else:
                output_list.append(l.replace('VALUE'+str(int(i/2)), content[int(i/2)-1]))
    with open('southPark.html', 'w') as f3:
        f3.write(''.join(output_list))

if __name__ == "__main__":
    main()
