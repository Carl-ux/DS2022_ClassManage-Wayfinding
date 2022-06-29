'''
Date: 2022-04-12 10:51:31
LastEditors: Azus
LastEditTime: 2022-06-14 22:08:09
FilePath: /DS/backend/module/logger.py
'''
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def getLog():
    with open("./log.txt", "r+") as log:
        return log.read()
