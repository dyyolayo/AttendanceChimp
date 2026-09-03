# Blueprint for all the people in the classroom

## This comment, I hope to use when I have something I want to add vs the regular # comment 
### Personal comments


############TODO############ : Look through code and note necessary edits here 

## Review Changes
## Docstrings
## Add verification for teachers
## Incorporate SQL
## Separate helper functions from here
## To keep things small, may need to isolate People and Course, Lecture models

############ CHANGES ############

import itertools

class StudentManager:
    all_students = {}
    @classmethod
    def add_student(cls,studentId, studentObj):
        cls.all_students[studentId] = studentObj

    @classmethod
    def get_student(cls,studentId):
        if studentId in cls.all_students:
            return cls.all_students.get(studentId)

    @classmethod
    def del_student(cls,studentId):
        return cls.all_students[studentId], cls.all_students.pop(studentId,None)
    
class TeacherManager :
    all_teachers = {}
    @classmethod
    def add_teacher(cls,teacherName, teacherObj):
        cls.all_teachers[teacherName] = teacherObj

    @classmethod
    def get_teacher(cls,teacherName):
        return cls.all_teachers.get(teacherName)

    @classmethod
    def del_teacher(cls,teacherName):
        return cls.all_teachers.pop(teacherName)
    


class Person:
    def __init__(self, fName:str , lName:str ):
        self.firstName = fName
        self.lastName = lName
        self.fullName = f"{self.firstName} {self.lastName}"
    
    def print_name(self):
        print(self.firstName, self.lastName)

class Student(Person):
    # each student may take multiple courses, many students in each course
    # Each student has a first and a last name
    idIter = itertools.count(1)

    def __init__(self, fName:str, lName:str, year:int):
        super().__init__(fName, lName)
        self.year = year
        self.sections = []
        self.qrcode_section = {}
        self.idNum = next(self.idIter)
        StudentManager.add_student(self.idNum,self)

    
    def add_sections(self, courseName, sectionNum):
        section = get_section(courseName,sectionNum)

        if section is None:
            print("Section does not exist")
            return None
        
        if check_student_in_section(self.idNum,section):
            self.sections.append(section)
            print("You've successfully added section")
            return True
        
        print("Make sure you are added to the section before you add it to your list")
        return None

        
    def upload_qrcode(self,section,code,date):
        self.qrcode_section[date] = [section, code]


class Teacher(Person):
    idIter = itertools.count()
    def __init__(self, fName, lName):
        super().__init__(fName, lName)
        self.idNum = next(self.idIter)
        TeacherManager.add_teacher(self.fullName,self)



class CourseManager:
    availableCourses = {}

    @classmethod
    def add_course(cls,courseName,courseObj):
        cls.availableCourses[courseName] = courseObj

    @classmethod
    def get_course(cls,courseName):
        return cls.availableCourses.get(courseName)

    @classmethod
    def del_course(cls,courseName):
        return cls.availableCourses.pop(courseName)

class Course:
    idIter = itertools.count()

    def __init__(self,cName:str ,subject:str):
        self.idNum = next(self.idIter)
        self.courseName = cName
        self.subject = subject
        self.sectionList = []

        CourseManager.add_course(self.courseName,self)

    def add_section(self, *sections):
            self.sectionList.extend(sections)
    
class Section():
    def __init__(self, course, sectionNum):
        self.course = course 
        self.sectionNum = sectionNum
        self.classTime = {}
        self.students = []
        self.teachers = []

    def add_classTime(self,day,startTime,endTime):
        self.classTime[day] = [startTime,endTime]

    def add_teachers(self, *teachers):
        for teacher in teachers:
            self.teachers.append(teacher)

    def add_students(self, *students):

        nonExistentStudents = []
        for studentId in students:
            if check_student_exists(studentId):
                if studentId not in self.students:
                    self.students.append(studentId)
            else:
                nonExistentStudents.append(studentId)



class QRcode:
    def __init__(self,qrcode,date,section):
        self.qrcode = qrcode
        self.date = date
        self.section = section
    pass

def create_section(courseName, sectionNum):
    courseDict = CourseManager.availableCourses

    if courseName in courseDict.keys():
        courseObj = courseDict[courseName]
        section = Section(courseObj,sectionNum)
        courseObj.add_section(section)

        return section
    
    else:
        return "course does not exist"


def get_section(courseName, sectionNum):
    if courseName not in CourseManager.availableCourses:
        return None
    

    courseObj = CourseManager.availableCourses[courseName]

    for section in courseObj.sectionList:
        if sectionNum == section.sectionNum:
            return section
    
    return None

def check_student_exists(studentId):
    if studentId in StudentManager.all_students:
        return True
    return False

def check_student_in_section(studentId,section):
    return studentId in section.students

############################################################ Test area ############################################################

math100 = Course("Math100", "Math")
literature100 = Course("Lit100", "Literature")

MrL = Teacher("Mannor", "Louis")
math100Section1 = create_section("Math100", 1)

mya = Student("Mya","Williams",4)

math100Section1.add_students(1) #need to assign unique Id later

mya.add_sections("Math100", 1)

print(math100Section1.students)


############################################################ Extra Code  ############################################################