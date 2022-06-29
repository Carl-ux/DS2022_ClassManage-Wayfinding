'''
Date: 2022-06-13 16:46:24
LastEditors: Azus
LastEditTime: 2022-06-15 03:04:08
FilePath: /DS/backend/handleStudents.py
'''
from module import DB_Stu as stu

students = stu.students

def handleStudents(mode:int, studentNo, students:stu.db_students = students ):
    """hendle Student-related requests 

    Args:
        mode (int): 1~4. 
            1: Add new student
            2. delete student 
            3. get all students 
            4. get single student info
        students (stu.db_students, optional): _description_. Defaults to students.
    """
    i = mode
    if i == '1':
        students.add(stu.get_new_student())
        return 0
    elif i == '2':
        students.drop(studentNo)
        return (students.to_json())
    elif i == '3':
        return(students.df.to_html())
    elif i == '4':
        try:
            print(students.query(studentNo).to_string())
            return(students.query(studentNo).to_html())
        except KeyError:
            return 1

if __name__ =="__main__":
    print(students.df.to_html())