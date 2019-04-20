from turtle import *
def draw_square(length,color):
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)
    
speed(100)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()