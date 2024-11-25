x =  'global' # global variable

# outer function
def outer_function():
    x = 'enclosing'
    
    # inner function
    def inner_funtion():
        x = 'local' #local variable 
        print(x)
    
    inner_funtion()
    print(x)

outer_function()
print(x)
