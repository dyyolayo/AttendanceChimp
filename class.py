# Blueprint for all the people in the classroom

## This comment, I hope to use when I have something I want to add vs the regular # comment 
### Comment for personal reading, not to be pushed

# Everytime I add a student to a course, I want the course amount to update

# Each student has a first name, a last name, and a course 
## 


class Student:

    def __init__(self,first:str,last:str):
        self.first = first
        self.last = last 
        self.courses = [] ###read python doc, here we are 

    def add_course(self,*course):
        for courseItem in course:
            self.courses.append(courseItem)
        ## Make it so that there is a clickable that allows the person to add the course through JS and then populate it like that

    def full_name(self): #don't pass in first and last attr here because they are already init with self. (Stored with object)
        return f"{self.first} {self.last}"

class Teacher:
    def __init__(self,first,last,courses):
        self.first = first
        self.last = last
        self.courses = courses #each teacher teaches at least one course


firstStudent = Student("Jack","Swagger")
firstStudent.add_course("Math","Science")
print(firstStudent.full_name())
print(firstStudent.courses)