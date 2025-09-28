def say_hello():
    print('Hello Python!')
say_hello()

# Function e argument bebohar
def great(name):
    print('Hello',name)
great('Manajrul')  

# # Function e মান return kora
def add(a, b):
    return(a+b)
result = add(20, 50)
print(result)


def calculate(a,b):
    A = a+b
    B = a-b
    return a, b
X,y = calculate(10,5)
print(X,y)


def calculate(a, b):
    sum_result = a + b
    sub_result = a - b
    return sum_result, sub_result

x, y = calculate(10, 5)
print("Sum:", x)
print("Sub:", y)


# *args
def add_all(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(add_all(1,2,3,4,5))

def add_all(*numbers):
    total = 0
    for i in numbers:
        total -= i
    return total
print(add_all(1,2,3,4,5))


