'''
Date: 2022-04-12 10:51:31
LastEditors: Azus
LastEditTime: 2022-04-20 13:39:13
FilePath: /DS/backend/logger.py
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
