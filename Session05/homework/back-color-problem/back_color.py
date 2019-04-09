from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    color=[]
    text=[]
    for i in range(len(shapes)):
        color.append(shapes[i]['color'])
        text.append(shapes[i]['text'])
    color_1 = choice(color)
    text_1 = choice(text)
    quiztype = [0,1]
    quiztype_1 = choice(quiztype)
    return [
                text_1,
                color_1,
                quiztype_1 # 0 : meaning, 1: color
            ]
def is_inside(a,b):
    if a[0] >= b[0] and a[0] <= (b[0]+b[2]) and a[1] >= b[1] and a[1] <= (b[1]+b[3]):
        return True
    else:
        return False
def mouse_press(x, y, text, color, quiz_type):
    a=[x,y]
    text_l=None
    color_l=None
    for i in range(len(shapes)):
        if shapes[i]['text'] == text:
            text_l = (shapes[i]['rect'])
    for i in range(len(shapes)):
        if shapes[i]['color'] == color:
            color_l = (shapes[i]['rect'])
    if quiz_type == 0:
        is_inside(a,text_l)
    elif quiz_type == 1:
        is_inside(a,color_l)
