def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def operate(func, x, y):
    return func(x, y)

result = operate(add, 10, 20)
print("Result:", result)

result = operate(sub, 20, 10)
print("Result:", result)
