from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(len(colors)):
    setx(100*i)
    n = colors[i]
    pencolor(n)
    begin_fill()
    fillcolor(n)
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    end_fill()
    
    
    
mainloop()