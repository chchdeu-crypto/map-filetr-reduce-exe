#mission 1
numbers=[3,7,10,15]
print(list(map(lambda num : num +10,numbers)))

#mission 2
prices = [100, 50, 200,80]
prices_with_tax=map(lambda price : price * 1.17,prices)
print(list(prices_with_tax))

#mission 3
words = ["cat", "elephant", "dog", "python"]
langth=lambda word :len(word)
print(list(map(langth,words)))

#mission 4
names = ["dan", "maya", "ron", "lea"]
upper_names=map(lambda name : name.upper(),names)
print(list(upper_names))

#mission 5
users=["Noa", "Adam", "Lior", "Tamar"]
user_messege=map(lambda name : f"hello {name}",users)
print(list(user_messege))

#mission 6
meters = [1.5, 2, 0.75, 3.2]
centimeters=map(lambda meter : meter*100,meters)
print(list(centimeters))