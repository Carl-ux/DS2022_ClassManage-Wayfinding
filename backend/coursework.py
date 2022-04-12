'''
Date: 2022-04-07 22:28:19
LastEditors: Azus
LastEditTime: 2022-04-08 13:57:33
FilePath: /DS/backend/coursework.py
'''
import os
import time
import shutil

from debugpy import trace_this_thread
# from Database import students, classes
import Database as db
COURSEWORK_FOLDER='/Users/azus/Documents/Code/Py/DS/DB/coursework/'
def classdir(classNo)->bool:    #Make sure class dir exists. ret False if exists
    classpath=COURSEWORK_FOLDER+str(classNo)
    # isExist=os.path.exists(classpath)
    try:
        os.makedirs(classpath, exist_ok=False)
    except OSError:
        return False 
    finally:
        return True

def submit_work(studentNo:int, classNo:int, coursework_path, name:str)->bool:
    classdir(classNo)
    # student folder under class folder
    student_folder=str(COURSEWORK_FOLDER) + str(classNo)
    # make sure a dir for student
    try:
        os.makedirs(student_folder)
    except:
        pass
    date_time=time.strftime("%Y%m-%H%M")
    # upload workname 
    zip(coursework_path, student_folder, date_time+"-"+name)
    

#! --------to be done-----------
def zip(coursework_path:str, target_path:str, zip_name:str)->bool: # get the work then zip to the target folder
    shutil.move(target_path)
    return 

if __name__ == "__main__":
    submit_work(2020211550, 202201, "/Users/azus/Documents/Code/Py/DS/AllCatsGoToHeaven 2.jpeg", "example.jpeg" )
    print(db.students.df.to_string())
    
