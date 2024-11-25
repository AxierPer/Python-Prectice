def outer_function():
    x = 'enclosing'

    def inner_function():
        nonlocal x
        x = 'modified'
        print(f'Value in inner is: {x}')

    inner_function()
    print(f'Outer values is: {x}')

outer_function()
