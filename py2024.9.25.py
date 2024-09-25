import re
import math
class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def show(self):
        print(self.name,"age::",self._age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
stu=Student("aaa",666,100)
stu.show()