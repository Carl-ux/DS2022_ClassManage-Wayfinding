'''
Date: 2022-04-07 22:28:19
LastEditors: Azus
LastEditTime: 2022-04-15 20:10:17
FilePath: /DS/backend/coursework.py
'''
import os
import time
import shutil

from debugpy import trace_this_thread
from DB_Classes import classes
from DB_Stu import students
import hashlib

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
    

#! --------to be done-----------
def zip(coursework_path:str, dst_dir:str, zip_name:str)->bool: # get the work then zip to the target folder
    
    # TODO: read file and zip
    # TODO: 从coursework_path读入文件，用某种方法压缩，还是放在coursework_path
    
    # mv the zipped file to the destination
    rn_path = os.path.join(os.path.dirname(coursework_path),zip_name)
    shutil.move(coursework_path,rn_path)
    shutil.move(rn_path, os.path.join(dst_dir, zip_name))
    return True

if __name__ == "__main__":
    print(submit_work(2020211550, 202201, "/Users/azus/Documents/Code/Py/DS/artifact.png", "example.jpeg" ))
    print(students.df.to_string())
    
