user_ages = []
user_names = []

for i in range(5):
    try:
        age = int(input("Age: "))
        name = input("Name: ")
        user_ages.append(age)
        user_names.append(name)
    except ValueError:
        print("❌ Invalid age. Please enter a number.")
        continue

user_ages = list(dict.fromkeys(user_ages))
user_names = list(dict.fromkeys(user_names))

users = {}

def a(ages, names, dictionary):
    for name, age in zip(names, ages):
        dictionary[name] = {"age": age}

a(user_ages, user_names, users)
print(users)

for name, info in users.items():
    if info["age"] > 18:
        print(name, info["age"])


def average_age(dictionary):
    try:
        ages = [info["age"] for info in dictionary.values()]
        return sum(ages) / len(ages)
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print("Error calculating average age:", e)
        return None

print("Average age:", average_age(users))
