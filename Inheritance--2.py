class Animal():
    def __init__(self,name):
        self.name = name
        print(self.name + "Was adopted")

    def speak(self):
        print("Speaking")

class Dog(Animal):
    def speak(self):
        print(self.name + "Is Barking :dog:")        

class Cat(Animal):
    def speak(self):
        print(self.name + "mewing :cat:")

romio = Dog('Romio')
romio.speak() 

kalu = Cat('Kaluuu')
kalu.speak()


        