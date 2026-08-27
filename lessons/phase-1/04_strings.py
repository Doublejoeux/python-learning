sentence = "calculate" 
print (sentence[0]) #c
print (sentence[-1]) #e
print (len(sentence))

phrase = "I am JoJo"
print (phrase[2]) #a
print (phrase[-2]) #J
print (len(phrase))

#string slicing
my_string = 'I love python programming'
print (my_string[2:6]) #love
print (my_string[7:]) #python to the end
print (my_string[0:6]) #I love

# string methods
text = "  Learning Python is FUN  "
print (text.upper()) # LEARNING PYTHON IS FUN
print (text.lower()) # learning python is fun
print (text.strip()) # "Learning Python is FUN"
print (text.replace("FUN","exciting")) # Learning Pythong is exciting

# String Concatenation
name = "JoJo"
age = 27
hobby = "Football"
print (f"My name is {name}, I am {age} and I love playing {hobby}")

a = 9
b = 6
print (f"the sum of {a} and {b} is {a + b}")