greeting="Hello"
def greet(name):
    global message
    message = f"{greeting} {name}!"
    print(message)
greet("John")
print(message)