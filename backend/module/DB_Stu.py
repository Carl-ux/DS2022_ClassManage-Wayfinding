'''
Date: 2022-04-05 00:24:27
LastEditors: Azus
LastEditTime: 2022-06-15 14:26:19
FilePath: /DS/users/azus/documents/code/py/ds/backend/module/DB_Stu.py
'''

from select import select
import pandas as pd
from torch import true_divide
# StudentNumber, Gender, Name, Class
from logger import logger 
# TODO Multi-threading
import json

# For sync lock
import threading
import numpy
# class X:
#     #定义需要保证线程安全的方法
#     def m () :
#         #加锁
#         self.lock.acquire()
#         try :
#             #需要保证线程安全的代码
#             ＃...方法体
#         #使用finally 块来保证释放锁
#         finally :
#             #修改完成，释放锁
#             self.lock.release()

# Columns in student.csv
COLUMNS = [
    'StudentNumber', 'Gender', 'Name', 'Event']
DB_PATH = '/Users/azus/Documents/Code/Py/DS/DB/student.csv'
ENV='production'

# df['证券名称'].str.contains('联通') ]


# @use: students = db_students(DB_PATH)
class db_students(object):
    def __init__(self, DB_PATH=DB_PATH): # Load student DB
        self.save_path = DB_PATH
        self.load()

        #provide sync lock
        self.lock = threading.RLock()
    
    def load(self):
        self.df = pd.read_csv(self.save_path)
        self.df = self.df.set_index('StudentNumber')
        logger.info(f'STUDENT DB LOADED')

    def save(self):
        if ENV in 'production':
            self.df.to_csv(self.save_path)

    def add(self, studentInfo: list): # add new student
        self.load()
        studentInfo[0][0] = int(studentInfo[0][0])
        new_stu = pd.DataFrame(studentInfo, columns=COLUMNS)
        new_stu.set_index('StudentNumber', inplace=True)
        self.df = pd.concat([self.df, new_stu])
        self.save()
        logger.info(f'NEW STUDENT ADDED:{self.df.loc[studentInfo[0][0]]["Name"]}')
        
    def add_event(self, student: int, new_event: list) -> bool: # add class info to a student 
        self.load()
        if(self.if_conflict(int(student), new_event[0])==True):
            return False
        try:
            # self.df.loc[student]['Class'] = classes
            # df 读出来的内容为string，用json转化为list
            print(self.df.loc[student]['Event'])
            event=  json.loads(self.df.loc[student]['Event'])
            # print(type(ori_event))
            event.extend(new_event)
            self.df.loc[student]['Event'] = f'{event}'
        except KeyError:
            return False
        self.save()
        logger.info("Add class for {student} Successful")
        return True
    
    def drop(self, student: int) -> bool:   # delete student info
        self.load()
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
    def to_json(self):   
        return self.df.to_json()
    
    def query(self, studentNo:int)->pd.Series:  #query student by student number
        _target = pd.Series()
        logger.info(f'QUERY STUDENT {studentNo}')

        return self.df.loc[int(studentNo)]

        # TODO
    def get_db_as_list(self)->list: # ret df as list

        df = pd.read_csv(self.save_path)
        # data as array(numpy.ndarray)
        ary = df.values
        # info of the first student
        print(ary[0])
        # StudentNumber, Gender, Name, Class

        # the student number of the first student
        print(ary[0][0])
        # the name of the first student
        print(ary[0][2])
        return ary
    def if_conflict(self, stuNo, EvtNo):
        selected = self.query(int(stuNo)).to_dict()["Event"]
        if str(EvtNo) in selected:
            return True
        else:
            return False
        
# construct new studnet from stdin 
def get_new_student() -> list:
    new_stu = []
    print('The classes of the new student are empty by default. Use add_class() to update.')
    new_stu = [[input("Student number:"), input(
        "Gender:"), input("Name:"), []]]
    print(new_stu)
    return new_stu


def CLI(students:db_students):

    i = input(f'1: Add 2: Del 3. print all 4. Check Student\n')
    while(i!='q'):
        if i == '1':
            students.add(get_new_student())
            print(students.to_string())
        elif i == '2':
            students.drop(input("Student Number:"))
            print(students.to_string())
        elif i == '3':
            print(students.to_string())
        elif i == '4':
            stunu = input("student number\n")
            try:
                # print(df.to_string())
                print(students.query(stunu).to_string())
            except KeyError:
                print('Student not found')
        i = input(f'\n1: Add 2: Del 3. print all 4. Check Student\n')

# initialize students database 
students = db_students(DB_PATH)

# Testrun if run as main 
if __name__ == '__main__':
    # CLI(students)


    # students.get_db_as_list()
    # students.add_event(2020211554, [202251])
    print(students.if_conflict(2020211555, 55))
    


    
