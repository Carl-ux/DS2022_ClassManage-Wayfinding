'''
Date: 2022-04-07 22:28:19
LastEditors: Azus
LastEditTime: 2022-06-15 05:36:29
FilePath: /DS/backend/module/coursework.py
'''
import os
import time
import shutil
from logger import logger 
from debugpy import trace_this_thread
from DB_Classes import classes
from DB_Stu import students
import hashlib
import zip as zp
import math
import jieba
import jieba.analyse

COURSEWORK_FOLDER='/Users/azus/Documents/Code/Py/DS/DB/coursework/'

def isDirExist(classNo)->bool:    #Make sure class dir exists. ret False if exists
    classpath=COURSEWORK_FOLDER+str(classNo)
    # isExist=os.path.exists(classpath)
    try:
        os.makedirs(classpath, exist_ok=False)
    except OSError:
        return False 
    return True

def submit_work(studentNo:int, classNo:int, coursework_path, name:str)->bool:
    """submit student work, auto compressed 

    Args:
        studentNo (int): student number     
        classNo (int): class number 
        coursework_path (_type_): the absolute path of the work you wanted to upload 
        name (str): work name 

    Returns:
        bool: if success 
    """

    # if(classes.query())
    isDirExist(classNo)
    classpath=COURSEWORK_FOLDER+str(classNo)

    # student folder under class folder
    student_folder=os.path.join(classpath, str(studentNo))
    # make sure a dir for student
    try:
        os.makedirs(student_folder)
    except:
        pass
    submit_date=time.strftime("%Y%m%H%M")
    # filehash before zipping
    filehash = hash_file(coursework_path)[-5:-1]
    # check if exist using hash paring
    for root, dirs, files in os.walk(student_folder):
        for file in files:
            if 'DS_Store' not in file:
                if filehash in file.split('-')[-1]:
                    # if exist with equal hashvalue 
                    return False
    
    zip(coursework_path, student_folder, submit_date+"_"+filehash+os.path.splitext(coursework_path)[-1])
    logger.info(f'{studentNo} uploaded {name} to class {classNo}.')


def hash_file(file_path, Bytes=1024):    # ret hex hash of file
    # new md5 object
    _MD5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        # read in first batch
        data=f.read(Bytes)
        # until empty
        while(data):
            _MD5.update(data)
            data=f.read(Bytes)
    ret = _MD5.hexdigest()
    return ret
    


def zip(coursework_path:str, dst_dir:str, zip_name:str)->bool: # get the work then zip to the target folder
    
    # TODO: read file and zip
    # TODO: 从coursework_path读入文件，用某种方法压缩，还是放在coursework_path
    rn_path = os.path.join(os.path.dirname(coursework_path),zip_name)
    # zipping
    zp.compress(coursework_path, rn_path)
    # mv the zipped file to the destination
    # shutil.move(coursework_path,rn_path)
    shutil.move(rn_path, os.path.join(dst_dir, zip_name))
    return True

if __name__ == "__main__":
    # print(submit_work(2020211550, 202201, "/Users/azus/Documents/Code/Py/DS/EXAMPLE.png", "example" ))
    # print(students.df.to_string())
    # print(classes.df.to_string())
    # zp.decompress('/Users/azus/Documents/Code/Py/DS/DB/coursework/202201/2020211550/2022040138_b535.png', '/Users/azus/Documents/Code/Py/DS/exp.png')
    logger.info(f"test info")

# -*- encoding:utf-8 -*-

# Partial similarity check based on hamming distance
class SimHash(object):
    def getBinStr(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            return str(x)
    def getWeight(self, source):
        return ord(source)
    def unwrap_weight(self, arr):
        ret = ""
        for item in arr:
            tmp = 0
            if int(item) > 0:
                tmp = 1
            ret += str(tmp)
        return ret
    def sim_hash(self, rawstr):
        seg = jieba.cut(rawstr)
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=100, withWeight=True)
        ret = []
        for keyword, weight in keywords:
            binstr = self.getBinStr(keyword)
            keylist = []
            for c in binstr:
                weight = math.ceil(weight)
                if c == "1":
                    keylist.append(int(weight))
                else:
                    keylist.append(-int(weight))
            ret.append(keylist)
        # 降维
        rows = len(ret)
        cols = len(ret[0])
        result = []
        for i in range(cols):
            tmp = 0
            for j in range(rows):
                tmp += int(ret[j][i])
            if tmp > 0:
                tmp = "1"
            elif tmp <= 0:
                tmp = "0"
            result.append(tmp)
        return "".join(result)
    def distince(self, hashstr1, hashstr2):
        length = 0
        for index, char in enumerate(hashstr1):
            if char == hashstr2[index]:
                continue
            else:
                length += 1
        return length
if __name__ == "__main__":
    simhash = SimHash()
    str1 = '例子文本1'
    str2 = '例子文本2'
    hash1 = simhash.sim_hash(str1)
    # print(hash1)
    hash2 = simhash.sim_hash(str2)
    distince = simhash.distince(hash1, hash2)
    value = 5
    print("simhash", distince, "距离：", value, "是否相似：", distince<=value)
    
    

    
