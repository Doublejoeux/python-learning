#try/except
def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    except TypeError:
        print("Both inputs must be numbers.")
        return None
    else:
        print(result)
        return result
safe_divide(10,2)
safe_divide(10,0)
safe_divide(10,"a")
safe_divide("r",5)