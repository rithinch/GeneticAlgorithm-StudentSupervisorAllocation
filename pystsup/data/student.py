"""
    An AI Tool for Student-Supervisor Allocation.
    
    Package: pystsup
    Module: data
    File: student.py
    
    Purpose:  Contains Student class, which structures and holds data of a particular student.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 21/7/17
    
"""


class Student:

    def __init__(self,stuID,keywords,realID=None,name=None):
        
        """
        Initialize the Student object.

        Parameters:
        
            stuID (string) -  is the internal ID (eg. "student1") given to a student generated by this program,
                              this id is also a key in the students data dictionary.
                              
            keywords (dictionary) -  contains all the preferences of a student along with their paths in ACM tree.
                                     
            realID (string) - is the actual id of the student in university records.
            
            name (string) -  is the name of the student in university records.
        
        """
        
        self._keywords = keywords
        self._stuID = stuID
        self._realID = realID
        self._name = name
        

    def getStudentID(self):
        """ Function to get the Student ID (temporary)"""
        
        return self._stuID

    def getStudentName(self):
        """ Function to the get the Student Name"""
        
        return self._name

    def getRealID(self):
        """Function to get the real Student ID"""
        
        return self._realID
    
    def getKeywords(self):
        """Function to get the keywords dictionary"""
        
        return self._keywords

