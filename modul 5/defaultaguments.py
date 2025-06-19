def greet_person(name, greetings="Hello"):
    message=f"{greetings}, {name}"
    return message
default_greetings=greet_person("Alice")
custom_greetings=greet_person("John", "Hi")
print(default_greetings)
print(custom_greetings)