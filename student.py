'''
Date: 2022-04-05 00:24:27
LastEditors: Azus
LastEditTime: 2022-04-06 10:34:32
FilePath: /DS/student.py
'''
from asyncio import FastChildWatcher
from matplotlib.pyplot import switch_backend
import pandas as pd
# StudentNumber, Gender, Name, Class
import logging

COLUMNS = [
    'StudentNumber', 'Gender', 'Name', 'Class']
DB_PATH = './DB/student.csv'
ENV='production'

# df['证券名称'].str.contains('联通') ]

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# Load student DB
df = pd.DataFrame()
def load():
    global df 
    df = pd.read_csv(DB_PATH)
    df = df.set_index('StudentNumber')
    logger.info(f'STUDENT DB LOADED')
load()

# save to csv
def save():
    global df
    
    if ENV in 'production':
        df.to_csv(DB_PATH)

# add new student
def add_student(studentInfo: list):
    global df
    new_stu = pd.DataFrame(studentInfo, columns=[
        'StudentNumber', 'Gender', 'Name', 'Class'])
    new_stu.set_index('StudentNumber', inplace=True)
    df = pd.concat([df, new_stu])
    save()
    logger.info(f'NEW STUDENT ADDED:{df.loc[studentInfo[0][0]]["Name"]}')


    
def get_new_student() -> list:
    new_stu = []
    print('The classes of the new student are empty by default. Use add_class() to update.')
    new_stu = [[input("Student number:"), input(
        "Gender:"), input("Name:"), []]]
    print(new_stu)
    return new_stu


def add_class(student: int, classes: list) -> bool:
    global df
    try:
        df.loc[student]['Class'] = classes
    except KeyError:
        return False
    save()
    logger.info("Add class for {student} Successful")
    return True

def del_student(student: int) -> bool:
    global df
    load()
    try:
        df = df.drop(int(student))
    except KeyError:
        logger.info(f"Delete {student} failed: Not found")
        return False
    save()
    logger.info(f"Delete {student} Successful")
    return True
    
        

# classes = [101, 102]
# # assert add_class(2020211555, classes), 'Student Number Not Found'
# print(df.to_string())


# add_student(get_new_student())
# print(df.to_string())


def CLI():
    global df
    i = input(f'1: Add 2: Del 3. print all 4. Check Student\n')
    while(i!='q'):
        if i == '1':
            add_student(get_new_student())
        elif i == '2':
            del_student(input("Student Number:"))
            print(df.to_string())
        elif i == '3':
            print(df.to_string())
        elif i == '4':
            stunu = input("student number\n")
            try:
                # print(df.to_string())
                print(df.loc[stunu].to_string())
            except KeyError:
                print('not found')
        i = input(f'\n1: Add 2: Del 3. print all 4. Check Student\n')


print((df.loc[2020211555]).empty)

# print(df.to_string())


# df.append(series)

# print(df.to_string())
# print(get_new_student())


# print(df.index('ziyi'))
# df.to_string()

