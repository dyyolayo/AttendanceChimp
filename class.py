# Blueprint for all the people in the classroom

## This comment, I hope to use when I have something I want to add vs the regular # comment 
### Personal comments

# Everytime I add a student to a course, I want the course amount to update

############TODO############
#Look through code and note necessary edits here 
## Look into DB design to verify if a teacher is in a course, start working on SQL
## Might want to change the design so that 
## Separate helper functions from here

daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def verify_DOW(day:str):
    """This function is meant to verify if a proposed class date is one of the 
    days of the week"""

    try:
        if day in daysOfTheWeek:
            return True
        
        raise ValueError(
            f"The day you entered, {day} is not one of the available days of the week"
                         ) #replace with logs
    
    except ValueError:
        return False
    
    except TypeError:
        raise TypeError (
            "Day must be a string"
            )

class Person:
    def __init__(self, fName:str , lName:str ):
        self.firstName = fName
        self.lastName = lName
    
    def print_name(self):
        print(self.firstName, self.lastName)

class Student(Person):
    # each student may take multiple courses, many students in each course
    # Each student has a first and a last name
    def __init__(self, fName:str, lName:str, year:int):
        super().__init__(fName, lName)
        self.year = year
        self.lectures = []
    
    def add_lectures(self):
        # if student in this lecture, add lecture to the student list of lectures
        pass

class Teacher(Person):
    pass

class Courses:
    def __init__(self,cName:str ,subject:str):
        self.courseName = cName
        self.subject = subject
        self.lectures = []

    def add_lecture(self, *lectures):
        for lecture in lectures:
            self.lectures.append(lecture)
    
class Lectures():
    def __init__(self, course, day, timePeriod):
        # each lecture has multiple qrcodes, a new one generated each day
        self.course = course 
        self.day = day
        self.timePeriod = timePeriod
        self.students = []
        self.teachers = []

    def add_teachers(self, *teachers):
        for teacher in teachers:
            self.teachers.append(teacher)

    def add_students(self, *students):
        for student in students:
            self.teachers.append(student)



Math100 = Courses("Math100", "math")
Math100.add_lecture({"Monday":"7:30"})
print(Math100.courseName, Math100.subject)
print(Math100.lectures)

# class Teacher:
#     # each teacher may teach multiple courses, there can be multiple teachers for a course
#     ls_of_teachers = []

#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#         self.courses = [] #each teacher teaches at least one course
#         self.lectures = [] #each teacher has a lecture time period
#         Teacher.ls_of_teachers.append(self)

#     # def __repr__(self):
#     #     return f"{self.first!r}"
#     def add_course(self,*course):
#         """Adds a course to the list of courses for each individual"""
#         for courseItem in course:
#             self.courses.append(courseItem)

# class Course:
#     ##Want to add a way to map each lecture time to the specific lecture days, i.e. MWF : 10-1, T,Th: 3-4
#     # each Course can have multiple teachers, multiple enrolled and multiple lecture dates and times
#     def __init__(self,subject:str,name:str,numLectures:int):
#         self.subject = subject
#         self.name = name
#         self.numLectures = numLectures
#         self.lectureDateTimes = {}
#         self.teachers = []

#     def add_Lecture_DateTime(self,date,time):
#         if verify_DOW(date):
#             self.lectureDateTimes[date] = time
#         # Check format for date addition is correct
#         # condition for if it doesn't exist later

# class Lecture:
#     def __init__(self,course,time):
#         self.course = course 
#         self.time = time
#         self.teachers = []
#         self.students = []

#     def add_teacher(self,*lsofTeachers):
#         for teacher in lsofTeachers:
#             if teacher in Teacher.ls_of_teachers:
#                 self.teachers.append(teacher)


# Math100 = Course("Math","Math100",2)

# # Math100.add_Lecture_DateTime("Monday","7:30")

# # print(Math100.lectureDateTimes)

# msM = Teacher("Amy", "Mansour")
# mrL = Teacher("Terry", "Lewis")

# # print(Teacher.ls_of_teachers)
# print(msM)

# # firstStudent = Student("Jack","Swagger")
# # firstStudent.add_course("Math","Science")
# # print(firstStudent.full_name())
# # print(firstStudent.courses)
