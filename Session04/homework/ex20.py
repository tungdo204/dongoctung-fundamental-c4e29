n = input("your word: ")
y={}
for c in n:
    y[c] = y.get(c,0)+1

for key, value in y.items():
    print("{} {}".format(key,value))
