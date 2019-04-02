import random
words = ["champion","hexagon","meticulous"]


game = random.choice(words)
character = list(game)
random.shuffle(character)
print (*character, sep='  ')
loop_2=True
while loop_2:
    answer=input("Your answer: ")
    if answer == game:
        print ("Hura")
        loop_2 = False
    else:
        print(":(")
    


