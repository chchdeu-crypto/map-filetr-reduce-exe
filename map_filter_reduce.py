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

#mission 7
grades = [95, 40, 67, 88, 52]
pass_grades=map(lambda grade : "pass" if grade>=60 else "fail",grades)
print(list(pass_grades))

#mission 8
products = [
    {"name": "Bread", "price": 8},
    {"name": "Milk", "price": 6},
    {"name": "Eggs", "price": 15}
]
cost=lambda prodact : f"{prodact["name"]} cost {prodact["price"]}"
print(list(map(cost,products)))

#mission 9
players = [
    {"name": "Dana", "score": 70},
    {"name": "Yoni", "score": 85},
    {"name": "Rami", "score": 40}
]
new_players=lambda x :{"name": x["name"], "score": x["score"]+5}
print(list(map(new_players,players)))

#mission 10
orders = [
    {"id": 1, "item": "Book", "amount": 3, "price": 40},
    {"id": 2, "item": "Pen", "amount": 10, "price": 5},
    {"id": 3, "item": "Bag", "amount": 1, "price": 120}
]
result=lambda order : f"order {order["id"]}: {order["item"]} total is {order["amount"] * order["price"]}"
print(list(map(result,orders)))