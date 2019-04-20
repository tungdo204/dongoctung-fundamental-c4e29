prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3,
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15,
}

for key in prices.keys():
    print(key)
    print("price: {}".format(prices[key]))
    print("stock: {}".format(stock[key]))
    print()

total=0
for key in prices.keys():
    n = prices[key]*stock[key]
    total += n

print(total)
