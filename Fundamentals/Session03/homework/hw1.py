product = ["T-Shirt","Sweater"]

loop = True
while loop:
    answer = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if answer == "R":
        print("Our items: ", end='')
        print(*product, sep = ", ")
        done = input("Are you done?")
        if done == "Y":
            loop=False  
        else:
            loop=True
    elif answer == "C":
        n = str(input("Enter new items: "))
        product.append(n)
        print("Our items: ", end='')
        print(*product, sep = ", ")
        done = input("Are you done?")
        if done == "Y":
            loop=False  
        else:
            loop=True
    elif answer == "U":
        i = int(input("Update position?"))
        item = input("New item?")
        product[i-1]=item
        print("Our items: ", end='')
        print(*product, sep = ", ")
        done = input("Are you done?")
        if done == "Y":
            loop=False  
        else:
            loop=True
    elif answer == "D":
        i = int(input("Delete position?"))
        del product[i-1]
        print("Our items: ", end='')
        print(*product, sep = ", ")
        done = input("Are you done?")
        if done == "Y":
            loop=False  
        else:
            loop=True
    else:
        print("please response correctly")
    