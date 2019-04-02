from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
a = 180
edge = 3
for i in range(len(colors)):
    n = colors[i]
    pencolor(n)
    for i in range(edge):
        forward(150)
        left(180-((180*(edge-2))/edge))
    edge = edge + 1
mainloop()