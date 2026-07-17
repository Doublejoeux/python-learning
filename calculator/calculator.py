#calculator
history = []
def is_decimal(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def warning():
    print("must be a number or decimal")
def add_numbers():
    aa = input("For 'a + b' input a: ")
    if is_decimal(aa):
        a = float(aa)
        bb = input("input b: ")
        if is_decimal(bb):
            b = float(bb)
            c = a + b 
            print(c)
            history.append(c)
        else:
            warning()
    else:
        warning()
def minus():
    aa = input("For 'a - b' input a: ")
    if is_decimal(aa):
        a = float(aa)
        bb = input("input b: ")
        if is_decimal(bb):
            b = float(bb)
            c = a - b
            print(c)
            history.append(c)
        else:
            warning()
    else:
        warning()
def multiply():
    aa = input("For 'a * b' input a: ")
    if is_decimal(aa):
        a = float(aa)
        bb = input("input b: ")
        if is_decimal(bb):
            b = float(bb)
            c = a * b
            print(c)
            history.append(c)
        else:
            warning()
    else:
        warning()
def division():
    aa = input("For 'a / b' input a: ")
    if is_decimal(aa):
        a = float(aa)
        bb = input("input b: ")
        if is_decimal(bb):
            b = float(bb)
            try:
                c = a / b
                print(c)
                history.append(c)
            except ZeroDivisionError:
                print("Cannot divide by zero(0)")                
        else:
            warning()
    else:
        warning()
def mod():
    aa = input("For 'a mod b' input a: ")
    if is_decimal(aa):
        a = float(aa)
        bb = input("input b: ")
        if is_decimal(bb):
            b = float(bb)
            try:
                c = a % b
                print(c)
                history.append(c)
            except ZeroDivisionError:
                print("Cannot divide by zero(0)")
        else:
            warning()
    else:
        warning()
def exp():
    aa = input("For 'a exp b' input a: ")
    if is_decimal(aa):
        a = float(aa)
        bb = input("input b: ")
        if is_decimal(bb):
            b = float(bb)
            c = a ** b
            print(c)
            history.append(c)
        else:
            warning()
    else:
        warning()
def running():
    options = ["add", "subtract", "divide", "multiply","modulus", "exponent", "history", "quit"]
    start = input("Add, Subtract, Multiply, Divide, Modulus, Exponent, History or Quit: ").lower()
    if start not in options:
        print("Invalid Option")
        return True
    elif start == "add":
        add_numbers()
        return True
    elif start == "subtract":
        minus()
        return True
    elif start == "multiply":
        multiply()
        return True
    elif start == "divide":
        division()
        return True
    elif start == "modulus":
        mod()
        return True
    elif start == "exponent":
        exp()
        return True
    elif start == "history":
        for i in history:
            print(i)
            return True
    else:
        print("End!")
        return False
def begin():
    begin = True
    while begin == True:
        begin = running()
begin()