class Student:
    roll = ""
    gpa = ""


Manjarul = Student()
print(isinstance(Manjarul,Student))
Manjarul.roll = 679236
Manjarul.gpa = 3.63
print(f"Roll: {Manjarul.roll} , GPA: {Manjarul.gpa}")

Siam = Student()
Siam.roll = 764290
Siam.gpa = 3.58
print(f"Roll: {Siam.roll} , GPA: {Siam.gpa}")

Milon = Student()
Milon.roll = 639720
Milon.gpa = 3.34
print(f"Roll:{Milon.roll}, GPA:{Milon.gpa}")