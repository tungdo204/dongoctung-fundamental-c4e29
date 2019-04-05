n = input("your word: ")
z = sorted(n)
y={}
for c in z:
    y[c] = y.get(c,0)+1

for key, value in y.items():
    print("{} {}".format(key,value))
