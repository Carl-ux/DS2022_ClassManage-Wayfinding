'''
Date: 2022-04-07 00:28:27
LastEditors: Azus
LastEditTime: 2022-04-15 19:41:39
FilePath: /DS/backend/DB_Classes.py
'''

import pandas as pd
# classesNumber, Gender, Name, Class
import threading
import json
import sys
sys.path.append('..')
from logger import logger



# to_file = open('.../path.json')


# Columns in classes.csv
COLUMNS = [
    'ClassNumber', 'Time', 'Name', 'Location']
DB_PATH = '/Users/azus/Documents/Code/Py/DS/DB/class.csv'
ENV='production'


# df['证券名称'].str.contains('联通') ]

class db_classes(object):
    def __init__(self, DB_PATH=DB_PATH):
        self.save_path = DB_PATH
        self.load()
        #provide sync lock
        self.lock = threading.RLock()
        
    def load(self):
        try:
            self.df = pd.read_csv(self.save_path)
        except pd.errors.EmptyDataError:
           self.df = pd.DataFrame(columns=COLUMNS)
        self.df = self.df.set_index('ClassNumber')
        logger.info(f'CLASSES DB LOADED')

    def save(self):
        if ENV in 'production':
            self.df.to_csv(self.save_path)

    def add(self, Info: list): # add new class
        Info[0][0] = int(Info[0][0])
        new_class = pd.DataFrame(Info, columns=COLUMNS)
        new_class.set_index(COLUMNS[0], inplace=True)
        self.df = pd.concat([self.df, new_class])
        self.save()
        logger.info(f'NEW CLASS ADDED:{self.df.loc[Info[0][0]]["Name"]}')


    def drop(self, classes: int) -> bool:   # delete classes info
        try:
            self.df = self.df.drop(int(classes))
        except KeyError:
            logger.info(f"Delete {classes} failed: Not found")
            return False
        self.save()
        logger.info(f"Delete {classes} Successful")
        return True
    
    def query(self, classNO:int)->pd.Series:  #query class by class number
        _target = pd.Series()
        try:
            _target = self.df.loc[classNO]
        except:
            return False
        return _target
    
    def filter_by_name(name:str)->list: # search name in classes and ret classid
        # df['证券名称'].str.contains('联通') ]
        classid=[]
        return classid
    def filter_by_time(time:str)->list: # search time in classes and ret classid
        # df['证券名称'].str.contains('联通') ]
        classid=[]
        return classid
    def to_string(self):
        return self.df.to_string()
    
classes = db_classes(DB_PATH)

if __name__ == "__main__":
    print(classes.to_string())
    classes.add([[202201, "MON0800", "MATH", 0000]])

    
    