# Blueprint for all the people in the classroom

## This comment, I hope to use when I have something I want to add vs the regular # comment 
### Personal comments

# Everytime I add a student to a course, I want the course amount to update

############TODO############
#Look through code and note necessary edits here 
## Look into DB design to verify if a teacher is in a course, start working on SQL
## Might want to change the design so that 
## Separate helper functions from here

import itertools

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
        self.sections = []
    
    def add_sections(self,course, section):
        # if student in this lecture, add lecture to the student list of lectures

        if course in Course.courseName():
            pass

mya = Student("Mya","Williams",4)
# mya.add_lectures("Math100", {"Monday":"8:30"})

class Teacher(Person):
    pass

class Course:
    idIter = itertools.count()
    availableCourses = {}

    def __init__(self,cName:str ,subject:str):
        self.idNum = next(self.idIter)
        self.courseName = cName
        self.subject = subject
        self.sections = []
        self.availableCourses[self.courseName] = self

    def add_section(self, *sections):
        for section in sections:
            self.sections.append(section)
    
class Section():
    def __init__(self, course, sectionNum):
        # each lecture has multiple qrcodes, a new one generated each day
        self.course = course 
        self.sectionNum = sectionNum
        self.classTime = {}
        self.students = []
        self.teachers = []

    def add_classTime(self,day,startTime,endTime):
        self.classTime[day] = [startTime,endTime]


    # def add_dayTime(self, **dayTimes):
    #     """Function designed to add a day and a time-slot for each lecture. 
    #     This way we can have Math100 on monday at 8-9 and add 10-11"""
    #     for x,y in dayTimes.items():
    #         if x in self.dayTime.keys():
    #             if self.dayTime[x] == dayTimes[x]:
    #                 return True
    #             else: 
    #                 [self.dayTime[x].append(y) for y in dayTimes[x] if y not in self.dayTime[x]] 
    #                 return "updated"
    #         else:
    #             self.dayTime[x] = y
    #             return "updated"

    def add_teachers(self, *teachers):
        for teacher in teachers:
            self.teachers.append(teacher)

    def add_students(self, *students):
        for student in students:
            self.students.append(student)



math100 = Course("Math100", "Math")
literature100 = Course("Lit100", "Literature")



# print(Course.availableCourses)
def create_section(courseName, sectionNum):
    courseDict = Course.availableCourses

    if courseName in courseDict.keys():
        courseObj = courseDict[courseName]
        section = Section(courseName,sectionNum)
        courseObj.add_section(section)

        return section
    
    else:
        return "course does not exist"


math100Section1 = create_section("Math100",1)

print(math100Section1.course)