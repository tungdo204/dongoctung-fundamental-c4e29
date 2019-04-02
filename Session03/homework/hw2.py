sheep = [5,7,300,90,24,50,75]
biggest = max(sheep)
print ("Hello, my name is Tung and these are my sheep sizes")
print(sheep, sep=' ,')
print("Now my biggest sheep has size {} let's shear it".format(biggest))
loop = True
while loop:
    for i in range(len(sheep)):
        if sheep[i] == biggest:
            loop = False
            sheep[i] = 8
        else:
            i += 1
print("After shearing, here is my flock")
print(sheep, sep=' ,')

n=3
for i in range(1,n+1):
    loop=True
    while loop:
        if i < n:
            print("MONTH {}".format(i))
            for i in range(len(sheep)):
                sheep[i] = sheep [i] + 50
            print("One month has passed, now here is my flock")
            print(sheep)
            biggest = max(sheep)
            print("Now my biggest sheep has size {} let's shear it".format(biggest))
            loop = True
            while loop:
                for i in range(len(sheep)):
                    if sheep[i] == biggest:
                        loop = False
                        sheep[i] = 8
                    else:
                        i += 1
            print("After shearing, here is my flock")
            print(sheep, sep=' ,')
        else:
            loop = False
            print("MONTH {}".format(i))
            for i in range(len(sheep)):
                sheep[i] = sheep [i] + 50
            print("One month has passed, now here is my flock")
            print(sheep)
            sum=0
            for i in sheep:
                sum = sum + i
            print("My flock has size in total: {}".format(sum))
            profit = sum*2
            print("I would get {} * 2$ = {}".format(sum,profit))
    i+=1




