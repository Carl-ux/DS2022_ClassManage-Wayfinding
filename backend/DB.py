'''
Date: 2022-04-16 15:13:07
LastEditors: Azus
LastEditTime: 2022-04-16 15:15:30
FilePath: /DS/backend/DB.py
'''
import pandas as pd
import logger

class db(object):
    def __init__(self, DB_PATH): # Load student DB
        self.save_path = DB_PATH
        self.load()
    
    def load(self):
        self.df = pd.read_csv(self.save_path)
        self.df = self.df.set_index('StudentNumber')
        logger.info(f'STUDENT DB LOADED')