'''
Date: 2022-04-07 00:28:27
LastEditors: Azus
LastEditTime: 2022-04-07 00:54:02
FilePath: /DS/backend/DB_Classes.py
'''

import pandas as pd
# classesNumber, Gender, Name, Class
from logger import logger
import threading


# Columns in classes.csv
COLUMNS = [
    'ClassNumber', 'Time', 'Name', 'Location']
DB_PATH = '../DB/class.csv'
ENV='production'

# df['证券名称'].str.contains('联通') ]


class db_classes(object):
    def __init__(self, DB_PATH=DB_PATH):
        self.save_path = DB_PATH
        self.load()
        #provide sync lock
        self.lock = threading.RLock()
        
    def load(self):
        self.df = pd.read_csv(self.save_path)
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
        return self.df.loc[classNO]
    
    def filter_by_name(name:str)->int: # search name in classes and ret classid
        # df['证券名称'].str.contains('联通') ]
        classid=0
        return classid
    def filter_by_time(time:str)->int: # search time in classes and ret classid
        # df['证券名称'].str.contains('联通') ]
        classid=0
        return classid
    
classes = db_classes(DB_PATH)
