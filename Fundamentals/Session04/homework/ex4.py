x=8
z="4*(x+3)"
y=eval(z)
answer = {
    1:35,
    2:36,
    3:40,
    4:44,
}
answer_2 = {
    1:10,
    2:12,
    3:14,
    4:16,
}
mean = (10+12+14+16+18)/5
count = 0
print ("If x={}, then what is the value of {} ?".format(x,z))
for key, value in answer.items():
    print("{}. {}".format(key,value))
choice = int(input("Your Choice: "))
if answer[choice] == y:
    print("Bingo")
    count += 1
else:
    print(":(")
print("Mean of 10, 12, 14, 16, 18?")
for key, value in answer_2.items():
    print("{}. {}".format(key,value))
choice = int(input("Your Choice: "))
if answer_2[choice] == mean:
    print("Bingo")
    count+=1
else:
    print(":(")
print("You correctly answer {} out of 2 questions".format(count))