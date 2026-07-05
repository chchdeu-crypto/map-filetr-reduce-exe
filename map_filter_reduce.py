#mission 1
numbers=[3,7,10,15]
print(list(map(lambda num : num +10,numbers)))

#mission 2
prices = [100, 50, 200,80]
prices_with_tax=map(lambda price : price * 1.17,prices)
print(list(prices_with_tax))