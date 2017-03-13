#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:21:52 2017

@author: xinyezhang
"""

"""lec 10"""
import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    def __str__(self):
        """return self's name"""
        return self.name
    def setBirthday(self, month, day, year):
        """set self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """return True if self's name is lexicographically less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        
class MITPerson(Person):
    nextIDNum = 0 #next id number to assign 
    def __init__(self, name):
        Person.__init__(self, name) #initiate Person attributes
        self.idNum = MITPerson.nextIDNum #add MITPerson unique attribute: idNum
        MITPerson.nextIDNum += 1
    def getIdNum(self):
        return self.idNum
    #sort MITPerson using idNum not name
    def __lt__(self, other):
        return self.idNum < other.idNum
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

# for student
class Student(MITPerson):
    pass

# for undergraduate
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

#for graduate
class Grad(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

class TransferStudent(Student):
    pass

# for professor
class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    def lecture (self, topic):
        return self.speak('It is obvious that' + topic)

# gradebook
class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to gradebook"""
        if student in self.students:
            raise  ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in gradebook')
    def getGrade(self, student):
        """Return a list of grades for the student"""
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in gradebook')
    def allStudents(self):
        """Return all the students in gradebook"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        #return copy of list of students
def gradeReport(course):
    """Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrade = 0
        for g in course.getGrade(s):
            tot += g
            numGrade += 1
        try:
            average = tot/numGrade
            report.append(str(s) + '\'s mean is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    