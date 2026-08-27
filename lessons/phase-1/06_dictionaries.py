car = {
    "brand": "Toyota",
    "model": "camry",
    "year": 2020
}
print(car["brand"]) #Toyota
car["year"] = 2023 
print(car["year"]) #'year': 2023
car["color"] = "black"
print(car) #{'brand': 'Toyota', 'model': 'camry', 'year': 2023, 'color': 'black'}
del car["model"]
print(car) #{'brand': 'Toyota', 'year': 2023, 'color': 'black'}
print(len(car)) #3
