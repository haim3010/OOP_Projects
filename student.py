#!/usr/bin/env python3


class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade # between 0-100
    
    def get_grade(self):
        return self.grade

    
class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade # same as value = value + student.get_grade
        
        avg_grade = value / len(self.students)
        return avg_grade
    

s1 = Student("Hai",27,61)
s2 = Student("Nevo",24,100)
s3 = Student("Ofir",28,100)
s4 = Student("Daniel",25,100)

course = Course("Devops",3) # name of the cousre and the maximum student. 
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.add_student(s4))
print(course.get_avg_grade())

