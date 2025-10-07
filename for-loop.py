for i in range(6):
    print(i)

for i in range(5,20):
    print(i)    

for i in range(20,50,2):
    print(i)

for i in range(20,50,3):
    print(i)


fruits = ['apple','banana','mango']
for Fruit in fruits:
    print(Fruit)


total = 0
for i in range(1,20):
    total += i
print('TOTAL=',total)


total = 0
for i in range(1,20):
    total += i
    print('TOTAL=',total)


Number = 5
for i in range(1,11):
    print(Number*i)


Number = 5
for i in range(1,11):
    print(f'{Number}*{i} = {Number*i}')  


Num = [37,38,94,192,65,654,8,98]
maximum = Num[0]

for i in Num:
    if i > maximum:
        maximum = i

print("max:", maximum)

Number = 23
prime = True
for i in range(2, Number):
    if Number % i == 0:
        prime = False
        break
    if prime:
        print(Number, "Its prime number")
    else:
        print(Number, "Its not prime number")
    