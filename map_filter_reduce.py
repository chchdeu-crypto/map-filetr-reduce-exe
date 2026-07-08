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

#part 2
#mission 1
numbers = [4, 7, 10, 13, 18, 21]
even_num=lambda num : True if num %2==0 else False
print(list(filter(even_num,numbers)))

#mission 2
grades = [100, 55, 70, 40, 88, 59]
print(list(filter(lambda grade : True if grade>=60 else False,grades)))

#misison 3
words = ["dog", "elephant", "cat", "computer", "sun"]
print(list(filter(lambda word : True if len(word)<=3 else False,words)))

#mission 4
names = ["Adam", "Dana", "Amit", "Noa", "Alon"]
print(list(filter(lambda name: True if name[0]=="A" else False,names)))

#mission 5
numbers = [-5, 3, 0, 12, -2, 8]
print(list(filter(lambda num : True if num >0 else False,numbers)))

#mission 6
products = [
    {"name": "Book", "price": 40},
    {"name": "Bag", "price": 120},
    {"name": "Pen", "price": 5},
    {"name": "Shirt", "price": 60}
]
prodact=lambda x : x["name"] if x["price"]>50 else False
print(list(filter(prodact,products)))

#mission 7
users = [
    {"name": "Dana", "active": True},
    {"name": "Ron", "active": False},
    {"name": "Maya", "active": True},
    {"name": "Gil", "active": False}
]
print(list(filter(lambda user : True if user["active"]==True else False,users)))

#mission 8
passwords = ["abc", "hello123", "Python2026", "pass", "GoodPass99"]
print(list(filter(lambda passw: True if len(passw)>=8 else False,passwords)))

#mission 9
tasks = [
    {"title": "Clean room", "done": True, "priority": 2},
    {"title": "Study Python", "done": False, "priority": 1},
    {"title": "Play game", "done": False, "priority": 5},
    {"title": "Send email", "done": True, "priority": 1}
]
print(list(filter(lambda task : True if task["done"]!=True and task["priority"]<=3 else False,tasks)))

#mission 10
students = [
    {"name": "Noa", "grade": 90, "attendance": 95},
    {"name": "Dan", "grade": 55, "attendance": 100},
    {"name": "Rina", "grade": 80, "attendance": 70},
    {"name": "Eli", "grade": 75, "attendance": 85}
]
print(list(filter(lambda student: True if student["grade"]>=70 and student["attendance"]>=80 else False,students)))



#part 4
#mission 1
#Because it takes the first two elements and adds them together, then adds the result to the next element, 
#until the entire list is reduced to a single final number.

#mission 2
#1.The function takes the first two numbers, 2 and 3, and multiplies them.
#2.It takes the result (6) and multiplies it by the next number in the list, which is 4
#3.and the result will be 24

#mission 3
#I’ll use `map` when I want to modify each element individually but keep the same number of elements
#I will use `reduce` when I want to combine all the elements and get a final result.

#mission 4
#Because it always performs an operation between two numbers, where x is the accumulated sum and y is the next element.

#mission 5
#`reduce` is preferable when I’m performing a simple operation on the entire list such as multiplying the elements together because it immediately clarifies the objective.
#I will use a for-loop when I want to perform several operations and check conditions, such as doubling only even numbers.

#part 5
#mission 1
from functools import reduce

numbers = [5, 10, 20, 15]
result = reduce(lambda x, y: x + y, numbers)

print(result)

#mission 2
numbers = [2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

#mission 3
words = ["cat", "elephant", "dog", "computer"]
longest = reduce(lambda x, y: x if len(x) >= len(y) else y, words)

print(longest)

#mission 4
words = ["Python", "is", "very", "useful"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)