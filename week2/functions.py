def my_adidas(x):
    x +=10
    print(x)

my_adidas(5)  # prints 15

def function_part_two(y):
    y *= 3
    return (y)

z = 100

def z_function():
    global z # this is required for the function to work if you are referencing a global variable. This isn't recommended; better to pass parameters to function (ex: def z_function() (...) print(z_function(100)))
    z += 20
    return z

function_part_two(17) # this will save the value of y (51) and further actions can be taken on it
print(function_part_two(17)) # just prints 51 to the console
print(z_function())
