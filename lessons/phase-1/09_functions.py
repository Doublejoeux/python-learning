#function
#Question 1
def greet_user(name):
    print(f"Welcome, {name}!")
greet_user("JoJo")
#question 2
def subtract(a, b):
    return a - b 
result = subtract(7, 2)
print(result)
#question 3
def is_even(number):
    return True if number % 2 == 0 else False
test = is_even(8)
print(test)
#question 4 - bonus
def get_age():
    age = input("Enter your age: ")
    age = int(age)
    return age
rio_age = get_age()
print(f"Rio is {rio_age}")