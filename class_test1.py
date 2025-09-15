class Hablu:
    Name = ""
    Number = ""


Imtiaz = Hablu()
Imtiaz.Name = "Manjarul"
Imtiaz.Number = 37
print(Imtiaz.Name)
print(Imtiaz.Number)    


    

class Computer:
    def config(self):
        print("i5","16GB", "1TB")

Com1 = Computer()
Com2 = Computer()

Computer.config(Com1)
Computer.config(Com2)

Com1.config()
Com2.config()
