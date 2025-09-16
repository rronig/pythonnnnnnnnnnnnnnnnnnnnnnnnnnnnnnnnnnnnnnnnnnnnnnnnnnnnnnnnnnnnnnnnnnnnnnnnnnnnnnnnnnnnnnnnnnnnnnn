def add(x,y):
    return x+y
def concatenate(x,y):
    return str(x)+str(y)

def operate(operation,x,y):
    return operation(x,y)

result_concat=operate(concatenate, "Hello, ", "World")
print(result_concat)
result_sum=operate(add,34, 66)
print(result_sum)