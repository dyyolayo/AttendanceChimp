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

class Student:
    # each student may take multiple courses, many students in each course
    def __init__(self,first:str,last:str):
        self.first = first
        self.last = last 
        self.courses = [] ###read python doc, here we are 

    def add_course(self,*course):
        """Adds a course to the list of courses for each individual"""
        for courseItem in course:
            self.courses.append(courseItem)
        ## Make it so that there is a clickable that allows the person to add the course through JS and then populate it like that

    def full_name(self): #don't pass in first and last attr here because they are already init with self. (Stored with object)
        return f"{self.first} {self.last}"

class Teacher:
    # each teacher may teach multiple courses, there can be multiple teachers for a course
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.courses = [] #each teacher teaches at least one course

    def add_course(self,course):
        """Adds a course to the list of courses for each individual"""
        for courseItem in course:
            self.courses.append(courseItem)

class Course:
    ##Want to add a way to map each lecture time to the specific lecture days, i.e. MWF : 10-1, T,Th: 3-4
    # each Course can have multiple teachers, multiple enrolled and multiple lecture dates and times
    def __init__(self,subject:str,name:str,numLectures:int):
        self.subject = subject
        self.name = name
        self.numLectures = numLectures
        self.lectureDateTimes = {}

    def add_Lecture_DateTime(self,date,time):
        if verify_DOW(date):
            self.lectureDateTimes[date] = time
        # Check format for date addition is correct
        # condition for if it doesn't exist later

class Lecture:
    def __init__(self,course,time):
        self.course = course 
        self.time = time
        self.teachers = []

    # def add_teacher(self,teacher):


Math100 = Course("Math","Math100",2)

Math100.add_Lecture_DateTime("Monday","7:30")

print(Math100.lectureDateTimes)

# firstStudent = Student("Jack","Swagger")
# firstStudent.add_course("Math","Science")
# print(firstStudent.full_name())
# print(firstStudent.courses)
