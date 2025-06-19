greeting="Hello"
name="John"

def greet():
    global greeting
    greeting="Goodbye"
    name="Rron"
    message=f"{greeting}, {name}"
    print(message)
greet()
message=f"{greeting}, {name}"
print(message)