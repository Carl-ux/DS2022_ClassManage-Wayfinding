'''
Description: 
Author: Carl
Date: 2022-06-14 20:09:13
LastEditTime: 2022-06-15 10:17:38
LastEditors: Azus
'''
import user 
import coursework as cw 
import pandas as pd
import map as mp
import timing as t
from logger import getLog
import DB_Classes
import DB_Stu
        
DB_PATH_CLASS = '/Users/azus/Documents/Code/Py/DS/DB/class.csv'
DB_PATH_STU = '/Users/azus/Documents/Code/Py/DS/DB/student.csv'

class apis():
    def __init__(self):
        """_summary_

        Args:
            OP_LEV1 (_type_): '1: Course 2: Activity 3: Guide 4. Virtual Time 5. Check System Log q: Quit'
            OP_LEV2 (_type_): _description_
        """
        # init Virtual time 
        timer = t.timer()
        # print(f'————当前时间（虚拟）：{timer.get_time_str()}————\n')
        #read class.csv into list    
        self.Info_Cou = user.get_db_as_list(DB_PATH_CLASS)
    #search_by_name
        #convert to Ascii
        self.INFO_NAME = user.ASCII_CONVERT_LIST(self.Info_Cou,1)
        #save in hash
        self.hash_name = user.HashTable(len(self.INFO_NAME))
        for i in self.INFO_NAME:
            self.hash_name.insert_hash(i)

    #search_by_time
        #convert to Ascii
        INFO_TIME = user.ASCII_CONVERT_LIST(self.Info_Cou,2)
        #save in hash
        hash_time = user.HashTable(len(INFO_TIME))
        for i in INFO_TIME:
            hash_time.insert_hash(i)

    def setID(self, id):
        self.ID = id
    def setOP1(self, op):
        self.OP_LEV1 = op
    def setOP2(self, op):
        self.OP_LEV2 = op
    def get_classes(self):
        return DB_Classes.classes.df.to_json(orient = 'records' , force_ascii=False)
    def get_student(self):
        return 
    def get(self):
        #USER_STU
        # OP_LEV1 (_type_): '1: Course 2: Activity 3: Guide 4. Virtual Time 5. Check System Log q: Quit'
        if self.OP_LEV1 == '1':
            # OP_LEV2_1 = input(f'1: Inquiry 2: Upload 3:Select Lesson  q: Return\n')
            if self.OP_LEV2 == '1':
                user.Course_sort(self.Info_Cou)
                user.Course_Inquiry(self.hash_name,self.hash_time,self.Info_Cou)
            elif  self.OP_LEV2 == '2':
            
                path = input("input work path:")
                courseNo =input("courseNo:")
                name = input("rename work:")
                cw.submit_work(self.ID, courseNo, path, name)
            elif  self.OP_LEV2 == '3':
                user.SelectCourse(self.ID)                    
            # for while loop     
        elif  self.OP_LEV1 == '2':
            # OP_LEV2_2 = input(f'1: Inquiry 2: Add Activity  3: Set Clock  q: Return\n')
            if  self.OP_LEV2 == '1':
                user.Activity_sort(self.Info_Cou)
                user.Activity_Inquiry(self.hash_name,self.hash_time,self.Info_Cou)
            elif  self.OP_LEV2 == '2':
                user.Addactivity(self.ID)
            elif  self.OP_LEV2 == '3':
                #TODO 闹钟
                # 2022,06,15,1,26,something
                # year, month, day, hour, minute = map(str, input("input year, month, day, hour, minute, info").split(','))
                year, month, day, hour, minute, info= map(str, input("input year, month, day, hour, minute, info\ne.g.. 2022,06,15,3,49,info").split(','))

                # print(f'{year}, {minute}')
                self.timer.setAlarm(year, month, day, hour, minute, info)
                    
            
        elif  self.OP_LEV1== '3':
            m = mp.map()
            method = int(input("select method: \n 1 : min dis; 2: min time; 3 : min time with transport "))
            start = input("input staring point. e.g.. 海淀南一教:")
            Endpattern = input(f'1: Location 2: CourseName  3: CourseTime\n')
            if Endpattern == '1':
                endpoint = input('Enter location:')
            elif Endpattern == '2':
                Name = input('Enter Course Name:')
                for row in self.Info_Cou:
                    if Name == row[1]:
                        endpoint = row[3]
                        break
            elif Endpattern == '3':
                Time = input('Enter Course Time:')
                for row in self.Info_Cou:
                    if Time == row[2]:
                        endpoint = row[3]
                        break
            #print(endpoint)
            m.findPath(start, endpoint, method)

        elif self.OP_LEV1 == '4':
            self.OP_LEV2 = input(f'1: Check Time 2: Set DeltaT 3. reset virtual time q: Return\n')
            if('1' ==  self.OP_LEV2):
                print(f'————当前时间（虚拟）：{self.timer.get_time_str()}————\n')
            if('2' ==  self.OP_LEV2):
                self.timer.setdeltaT(input(f"Previous deltaT:{self.timer.deltaT} \n   New deltaT:"))
            if('3' ==  self.OP_LEV2):
                # weekday=input("Weekday: e.g.. 1, 2, 3...")
                # hour =input("hour: e.g.. 8, 13, 19...")
                # minute =input("Weekday: e.g.. 00, 30, 50...")
                # info = input("Set Alarm info:")
                # timer.setAlarm(weekday, hour, minute, info)
                self.timer.reset()
                ...

        elif self.OP_LEV1 == '5':
            self.OP_LEV2 = input(f'1: Print System Log q: Return\n')
            if('1' ==  self.OP_LEV2):
                print(getLog())
                self.OP_LEV2 = input(f'1: Print System Log q: Return\n')




def Interface():
#login
    try:
        ID = int(input("Type your ID:"))
    except:
        print("Please type the right Format")
        ID = int(input("Type your ID:"))
    # init Virtual time 
    timer = t.timer()
    print(f'————当前时间（虚拟）：{timer.get_time_str()}————\n')
#read class.csv into list    
    Info_Cou = user.get_db_as_list(DB_PATH_CLASS)

#search_by_name
    #convert to Ascii
    INFO_NAME = user.ASCII_CONVERT_LIST(Info_Cou,1)
    #save in hash
    hash_name = user.HashTable(len(INFO_NAME))
    for i in INFO_NAME:
        hash_name.insert_hash(i)

#search_by_time
    #convert to Ascii
    INFO_TIME = user.ASCII_CONVERT_LIST(Info_Cou,2)
    #save in hash
    hash_time = user.HashTable(len(INFO_TIME))
    for i in INFO_TIME:
        hash_time.insert_hash(i)


    #USER_STU
    OP_LEV1 = input(f'1: Course 2: Activity 3: Guide 4. Virtual Time 5. Check System Log q: Quit\n')
    while(OP_LEV1 != 'q'):
        if OP_LEV1 == '1':
            OP_LEV2_1 = input(f'1: Inquiry 2: Upload 3:Select Lesson  q: Return\n')
            while(OP_LEV2_1 != 'q'):
                if OP_LEV2_1 == '1':
                    user.Course_sort(Info_Cou)
                    user.Course_Inquiry(hash_name,hash_time,Info_Cou)
                elif OP_LEV2_1 == '2':
                
                    path = input("input work path:")
                    courseNo =input("courseNo:")
                    name = input("rename work:")
                    cw.submit_work(ID, courseNo, path, name)
                elif OP_LEV2_1 == '3':
                    user.SelectCourse(ID)                    
                # for while loop
                OP_LEV2_1 = input(f'1: Inquiry 2: Upload 3:Select Lesson q: Return\n')       
        elif OP_LEV1 == '2':
            OP_LEV2_2 = input(f'1: Inquiry 2: Add Activity  3: Set Clock  q: Return\n')
            while OP_LEV2_2 != 'q':
                if OP_LEV2_2 == '1':
                    user.Activity_sort(Info_Cou)
                    user.Activity_Inquiry(hash_name,hash_time,Info_Cou)
                elif OP_LEV2_2 == '2':
                    user.Addactivity(ID)
                elif OP_LEV2_2 == '3':
                    #TODO 闹钟
                    # 2022,06,15,1,26,something
                    # year, month, day, hour, minute = map(str, input("input year, month, day, hour, minute, info").split(','))
                    year, month, day, hour, minute, info= map(str, input("input year, month, day, hour, minute, info\ne.g.. 2022,06,15,3,49,info\n").split(','))
                    recur = input(f"set if recur\n0: Single Timer\n1:Daily Timer\n2:Weekly Timer")
                    # print(f'{year}, {minute}')
                    timer.setAlarm(year, month, day, hour, minute, info, int(recur))
                    
                OP_LEV2_2 = input(f'1: Inquiry 2: Add Activity  3: Set Clock  q: Return\n')
            
        elif OP_LEV1 == '3':
            m = mp.map()
            method = int(input("select method: \n 1 : min dis; 2: min time; 3 : min time with transport "))
            start = input("input staring point. e.g.. 海淀南一教:")
            Endpattern = input(f'1: Location 2: CourseName  3: CourseTime\n')
            if Endpattern == '1':
                endpoint = input('Enter location:')
            elif Endpattern == '2':
                Name = input('Enter Course Name:')
                for row in Info_Cou:
                    if Name == row[1]:
                        endpoint = row[3]
                        break
            elif Endpattern == '3':
                Time = input('Enter Course Time:')
                for row in Info_Cou:
                    if Time == row[2]:
                        endpoint = row[3]
                        break
            #print(endpoint)
            m.findPath(start, endpoint, method)

        elif OP_LEV1 == '4':
            OP_LEV2_3 = input(f'1: Check Time 2: Set DeltaT 3. reset virtual time q: Return\n')
            while(OP_LEV2_3 != 'q'):
                if('1' == OP_LEV2_3):
                    print(f'————当前时间（虚拟）：{timer.get_time_str()}————\n')
                if('2' == OP_LEV2_3):
                    timer.setdeltaT(input(f"Previous deltaT:{timer.deltaT} \n   New deltaT:"))
                if('3' == OP_LEV2_3):
                    # weekday=input("Weekday: e.g.. 1, 2, 3...")
                    # hour =input("hour: e.g.. 8, 13, 19...")
                    # minute =input("Weekday: e.g.. 00, 30, 50...")
                    # info = input("Set Alarm info:")
                    # timer.setAlarm(weekday, hour, minute, info)
                    timer.reset()
                    ...
                OP_LEV2_3 = input(f'1: Check Time 2: Set DeltaT q: Return\n')

        elif OP_LEV1 == '5':
            OP_LEV2_4 = input(f'1: Print System Log q: Return\n')
            while(OP_LEV2_4 != 'q'):
                if('1' == OP_LEV2_4):
                    print(getLog())
                OP_LEV2_4 = input(f'1: Print System Log q: Return\n')

        OP_LEV1 = input(f'1: Course 2: Activity 3: Guide 4. Virtual Time 5. Check System Log q: Quit\n')




if __name__ == '__main__':
    Interface()