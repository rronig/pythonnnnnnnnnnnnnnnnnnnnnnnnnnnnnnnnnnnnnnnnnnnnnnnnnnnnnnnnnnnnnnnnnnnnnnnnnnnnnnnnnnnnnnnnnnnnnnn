from traceback import print_tb
age = int(input("How old are you: "))
if age >= 18:
    print("You can vote")
else:
    print("You can not vote")
if (age//2)*2==age:
    print("Your age is an even number")
else:
    print("Your age is an odd number")

temperature=int(input("What is the temperature where you live: "))
if temperature>30:
    print("It's hot")
elif 20<=temperature<=30:
    print("It's around room temperature")
else:
    print("It's cold")