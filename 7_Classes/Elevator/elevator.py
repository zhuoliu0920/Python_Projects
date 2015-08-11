#!/usr/bin/env python3

import random

class Building(object):
    """ A Building class has variables: num_of_floors, customer_list, elevator(Elevator class)
        methods: run() and output().
    """
    def __init__(self, nfloor, cus, elev):
        self.num_of_floors = nfloor
        self.customer_list = cus
        self.elevator = elev

    def run(self):
        """ The method to operate the elevator for Building.
        """
        if self.elevator.direction == 'up':
            max_cur_floor = max([x.cur_floor for x in self.customer_list]) # max floor where customer is waiting
            max_dst_floor = max([x.dst_floor for x in self.customer_list]) # max floor where customer needs to reach
            max_floor = max(max_cur_floor, max_dst_floor)
            while len([y for y in self.customer_list if y.finished == False]) > 0: # elevator keeps moving if there is still customer not finished
                print("At floor {}, going {}, customers in elevator: {}, customers finished: {}".format(self.elevator.cur_floor, self.elevator.direction, [x.ID for x in self.elevator.register_list], [y.ID for y in self.customer_list if y.finished == True]))
                for x in [y for y in self.customer_list if y.finished == False]: # check all customers who are not finished
                    if (x.finished == False) and (x.cur_floor == self.elevator.cur_floor): # customer enters elevator at his current floor
                        self.elevator.register_customer(x)
                        x.in_elevator = True
                    if (x.in_elevator == True) and (x.dst_floor == self.elevator.cur_floor): # customer leaves elevator if elevator reaches the floor
                        self.elevator.cancel_customer(x)
                        x.in_elevator = False
                        x.finished = True
                if self.elevator.cur_floor == max_floor:
                   self.elevator.direction = 'down' # arriving top floor, changing direction and going down
                self.elevator.move()

    def output(self):
        print("Total number of floors for the building: {}".format(self.num_of_floors))
        print("Total number of customers in the building: {}".format(len(self.customer_list)))
        print("Customer information:")
        for x in self.customer_list:
            print("{}: at floor {}, go to floor {}".format(x.ID, x.cur_floor, x.dst_floor))

class Elevator(object):
    """ A Elevator class has varibles: num_of_floors, register_list, cur_floor, direction
        methods: move(), register_customer(customer), cancel_customer(customer)
    """
    def __init__(self, nfloor, reg, cur, dirct):
        if (type(nfloor) != int) or (nfloor < 1):
            raise ValueError
        else:
            self.num_of_floors = nfloor
        if (type(cur) != int) or (cur > nfloor) or (cur < 1):
            raise ValueError
        else:
            self.cur_floor = cur

        self.register_list = reg
        if dirct.lower() not in ['up', 'down']:
            raise ValueError
        else:
            self.direction = dirct

    def move(self):
        """ Method to move elevator by one floor.
        """
        if self.direction == 'up':
            if self.cur_floor == self.num_of_floors: # cannot move up when at top
                raise ValueError
            else:
                self.cur_floor += 1
        elif self.cur_floor == 1: # cannot move down when at bottom
            raise ValueError
        else:
            self.cur_floor -= 1

    def register_customer(self, customer):
        """ A customer goes into elevator.
        """
        self.register_list.append(customer)

    def cancel_customer(self, customer):
        """ A customer goes out of elevator.
        """
        self.register_list.remove(customer)

class Customer(object):
    """ A Customer class has variables: cur_floor, dst_floor, ID, in_elevator, finished.
    """
    def __init__(self, cfloor, dfloor, ID, inele, finished):
        self.cur_floor = cfloor
        self.dst_floor = dfloor
        self.ID = ID
        self.in_elevator = inele
        self.finished = finished

def main():
    c1 = Customer(1,5,1,False,False)
    c2 = Customer(2,4,2,False,False)
    c3 = Customer(6,3,3,False,False)

    e = Elevator(6, [], 1, 'up')

    b = Building(6, [c1,c2,c3], e)
    b.output()
    b.run()

if __name__ == "__main__":
    main()

