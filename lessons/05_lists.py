#list
colors = ["red", "green", "blue"]
print (colors[0]) # red
print (colors[-1]) # blue
colors [1] = "yellow"
print (colors) # ['red', 'yellow', 'blue']
colors.append("purple")
print (colors) # ['red', 'yellow', 'blue', 'purple']
colors.remove("red")
print (colors) # ['yellow', 'blue', 'purple']
print (len(colors)) #3
# tuple
dimensions = ("width", "height", "depth")
print (dimensions[0]) # width
print (dimensions[-1]) # depth
print (len(dimensions)) #3
dimensions [0] = "length" #TypeError:'tuple' object does not support item assignment
# python refused to change 'width' to 'length' cause tuples are not mutable, hence, cannot be changed. 