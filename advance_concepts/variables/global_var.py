x = 5 #global variable

def modify_global():
    global x
    x += 3
    print(f"modify value: {x}")

modify_global()
print(f"Global value: {x}")
