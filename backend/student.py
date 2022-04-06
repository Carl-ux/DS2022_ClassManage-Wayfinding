'''
Date: 2022-04-05 00:24:27
LastEditors: Azus
LastEditTime: 2022-04-07 00:00:00
FilePath: /DS/student.py
'''

from asyncio import FastChildWatcher
from matplotlib.pyplot import switch_backend
import pandas as pd
# StudentNumber, Gender, Name, Class
from logger import logger

COLUMNS = [
    'StudentNumber', 'Gender', 'Name', 'Class']
DB_PATH = './DB/student.csv'
ENV='production'

# df['证券名称'].str.contains('联通') ]


class students(object):
    def __init__(self, DB_PATH=DB_PATH): # Load student DB
        self.save_path = DB_PATH
        self.df = pd.read_csv(self.save_path)
        self.df = self.df.set_index('StudentNumber')
        logger.info(f'STUDENT DB LOADED')
    
    def load(self):
        self.df = pd.read_csv(self.save_path)
        self.df = self.df.set_index('StudentNumber')
        logger.info(f'STUDENT DB LOADED')

    def save(self):
        if ENV in 'production':
            self.df.to_csv(self.save_path)

    def add(self, studentInfo: list): # add new student
        studentInfo[0][0] = int(studentInfo[0][0])
        new_stu = pd.DataFrame(studentInfo, columns=[
            'StudentNumber', 'Gender', 'Name', 'Class'])
        new_stu.set_index('StudentNumber', inplace=True)
        self.df = pd.concat([self.df, new_stu])
        self.save()
        logger.info(f'NEW STUDENT ADDED:{self.df.loc[studentInfo[0][0]]["Name"]}')
    
    def updateClass(self, student: int, classes: list) -> bool: # add class info to a student 
        try:
            self.df.loc[student]['Class'] = classes
        except KeyError:
            return False
        self.save()
        logger.info("Add class for {student} Successful")
        return True
    
    def drop(self, student: int) -> bool:   # delete student info
        try:
            self.df = self.df.drop(int(student))
        except KeyError:
            logger.info(f"Delete {student} failed: Not found")
            return False
        self.save()
        logger.info(f"Delete {student} Successful")
        return True
    
    def to_string(self):   
        return self.df.to_string()
    
    def query(self, studentNo:int)->pd.Series:  #query student by student number
        return self.df.loc[studentNo]
        
    

    
def get_new_student() -> list:
    new_stu = []
    print('The classes of the new student are empty by default. Use add_class() to update.')
    new_stu = [[input("Student number:"), input(
        "Gender:"), input("Name:"), []]]
    print(new_stu)
    return new_stu



def CLI():
    db = students(DB_PATH)
    i = input(f'1: Add 2: Del 3. print all 4. Check Student\n')
    while(i!='q'):
        if i == '1':
            db.add(get_new_student())
        elif i == '2':
            db.drop(input("Student Number:"))
            print(db.to_string())
        elif i == '3':
            print(db.to_string())
        elif i == '4':
            stunu = input("student number\n")
            try:
                # print(df.to_string())
                print(db.df.loc[int(stunu)].to_string())
            except KeyError:
                print('not found')
        i = input(f'\n1: Add 2: Del 3. print all 4. Check Student\n')

CLI()
