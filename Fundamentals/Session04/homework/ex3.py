x=8
z="4*(x+3)"
y=eval(z)
answer = {
    1:35,
    2:36,
    3:40,
    4:44,
}

loop = True
while loop:
    print ("If x={}, then what is the value of {} ?".format(x,z))
    for key, value in answer.items():
        print("{}. {}".format(key,value))

    choice = int(input("Your Choice: "))

    if answer[choice] == y:
        loop = False
        print("Bingo")
    else:
        print(":(")
            