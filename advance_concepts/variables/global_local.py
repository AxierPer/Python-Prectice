x = 100

def local_function():
    x = 10
    print(f"The value of variable is : {x}")

def show_global():
    print(f"The values of global variable is {x}")

# local_function()
# Print x and generate error if print x outside the function

print(x)
# Print the value in global function
