#!/usr/bin/python

import turtle as tt
import math

# drawing a rectangle fill with 'color'
def draw_rectangle(length, height, color):
    tt.fillcolor(color)
    tt.begin_fill()

    for d in [length, height]*2:
        tt.forward(d)
        tt.left(90)

    tt.end_fill()

# drawing a star filled with 'color' and 'size' is measured from its most left
# to most right
def draw_star(size, color):
    # from center move to left vertex
    tt.setpos(tt.xcor()-size/2.0, tt.ycor()+size/2.0/math.tan(math.radians(72.0))) 

    tt.fillcolor(color)
    tt.begin_fill()

    for i in range(5):
        tt.forward(size/2.0/(1+math.sin(math.radians(18))))
        tt.left(72)
        tt.forward(size/2.0/(1+math.sin(math.radians(18))))
	tt.right(180-36)

    tt.end_fill()

    # back to center
    tt.setpos(tt.xcor()+size/2.0, tt.ycor()-size/2.0/math.tan(math.radians(72.0)))


def draw_flag(height):
    tt.penup()

    # assign parameters defined from
    # https://en.wikipedia.org/wiki/Flag_of_the_United_States
    A = height
    B,C = 1.9*A, (7.0/13.0)*A
    D = 2.0*B/5.0
    E = C/10.0
    G = D/12.0
    L = A/13.0
    K = 4.0*L/5.0

    # draw the bottom 6 stripes
    for color in ['red','white']*3:
        draw_rectangle(B, L, color)
	tt.sety(tt.ycor()+L)

    # draw the top left blue rectangle
    draw_rectangle(D, C, 'blue')

    # draw the top right 7 stripes
    tt.setx(tt.xcor()+D)
    for color in ['red','white']*3:
        draw_rectangle(B-D, L, color)
	tt.sety(tt.ycor()+L)
    draw_rectangle(B-D, L, 'red')
    tt.sety(tt.ycor()+L)

    # draw the 50 stars
    tt.setx(G)
    tt.sety(tt.ycor()-E)
    nums_star = [6,5]*4
    nums_star.append(6)
    for nstar in nums_star:
        if (nstar == 5):
	    tt.setx(tt.xcor()+G)
	for i in range(nstar):
	    draw_star(K, 'white')
            tt.setx(tt.xcor()+2.0*G)
        tt.setx(G)
        tt.sety(tt.ycor()-E)


def main():
    tt.speed(10)
    draw_flag(300)
    tt.exitonclick()



if __name__ == "__main__":
    main()
