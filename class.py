class Students:
    Student_name = "Manjarul Alam"
    student_roll = 679236
a = Students()
print(a.Student_name)

class Classname:
    name = "My 1st class"
b = Classname()
print(b.name)    

class Area:
    area1 = "Bangladesh"
    area2 = "Dhaka"
    area3 = "Cumilla"
    area4 = "Chandpur"
Ar = Area()
print(Ar.area1)
print(Ar.area2)
print(Ar.area3)
print(Ar.area4)



class Students:
    __student_name = "Manjarul"
    student_roll = 384823

    def function(self):
        return self.__student_name
    
st = Students()
print(st.function())
print(st.student_roll)


class Area:
    __area_name = "Dhaka"
    area_code = 7390

    def area(self):
        return self.__area_name
    
Ar = Area()
print(Ar.area())
print(Ar.area_code)    


class Subject:
    __subject_name = "Computer Science"
    subject_code = 839923
    def sub(self):
        return self.__subject_name
X = Subject()
print(X.sub())
print(X.subject_code)


# class Student:
#     def __init__(self, name: str, roll: int | None = None):
#         self.__name = name       
#         self.__roll = roll       

    
#     def get_name(self) -> str:
#         return self.__name

#     def get_roll(self) -> int | None:
#         return self.__roll

    
#     def set_roll(self, roll: int) -> None:
#         self.__roll = roll

    
#     def get_info(self) -> dict:
#         return {
#             "name": self.__name,
#             "roll": self.__roll
#         }

    
#     def __str__(self) -> str:
#         return f"Student(name={self.__name}, roll={self.__roll})"


