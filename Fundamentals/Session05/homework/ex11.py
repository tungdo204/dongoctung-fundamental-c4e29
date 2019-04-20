def is_inside(a,b):
    if a[0] >= b[0] and a[0] <= (b[0]+b[2]) and a[1] >= b[1] and a[1] <= (b[1]+b[3]):
        return True
    else:
        return False


n = is_inside([100,120],[140,60,100,200])
print(n)

m = is_inside([200,120],[140,60,100,200])
print(m)