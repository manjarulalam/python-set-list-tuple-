class Human:
    def eat(self):
        print( "I can eat")

    def work(self):
        print("I can work")

class male:
    def eat(self):
        print( "I can eat")

    def work(self):
        print("I can work")

male1 = male()
male1.work()



class Human:
    def eat(self):
        print( "I can eat")

    def work(self):
        print("I can work")

class male(Human):
    pass

male1 = male()
male1.eat()





class Human:
    def eat(self):
        print( "I can eat")

    def work(self):
        print("I can work")

class male(Human):
    def flirt(self):
        print("I can flirt")

    def work(self):
        super().work()                  
        print("I can programm")

male1 = male()
male1.flirt()
male1.work()        






class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_nose = 1
        

    def eat(self):
        print( "I can eat")

    def work(self):
        print("I can work")

class male(Human):
    def flirt(self):
        print("I can flirt")

    def work(self):
        super().work()                  
        print("I can programm")

male1 = male()
male1.flirt()
male1.work()  
print(male1.num_eyes)
print(male1.num_nose)
