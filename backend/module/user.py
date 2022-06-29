'''
Description: 
Author: Carl
Date: 2022-04-18 19:58:12
LastEditTime: 2022-06-15 03:24:32
LastEditors: Azus
'''


import pandas as pd
from  DB_Stu import students
DB_PATH_CLASS = '/Users/azus/Documents/Code/Py/DS/DB/class.csv'
DB_PATH_STU = '/Users/azus/Documents/Code/Py/DS/DB/student.csv'

# @use: Hash for search        
class HashTable:
    def __init__(self, size):
        self.elem = [[0,0] for i in range(size)]
        self.count = size
 
    def hash(self, key):
        return key % self.count
 
    def insert_hash(self, key):
        address = self.hash(key[0])
        while self.elem[address][0]:
            address = (address + 1) % self.count
        self.elem[address] = key
 
    def search_hash(self, str)->int:
        key = ASCII_CONVERT_STR(str)
        star = address = self.hash(key)
        while self.elem[address][0] != key:
            address = (address + 1) % self.count
            if not self.elem[address][0] or address == star:
                return 0
        return (self.elem[address][1] + 1)

def get_db_as_list(DB_PATH)->list: # ret df as list
    df = pd.read_csv(DB_PATH)
    # data as array(numpy.ndarray)
    ary = df.values
    return ary


#@use : return a list that carries the ascii and the index of the str
def ASCII_CONVERT_LIST(list,col)->list:
    val = [0]*len(list)
    ary =[]
    for i in range(0,len(list)):
        for charc in list[i][col]:
            val[i] += ord(charc)
    for i in range(0,len(list)):
        ary.append([val[i],i])
    return ary

#@use : enter str to search
def ASCII_CONVERT_STR(str)->int:
    num = 0
    for charc in str:
        num += ord(charc)
    return num


def Course_Inquiry(hash_name:HashTable,hash_time:HashTable,list:list):
    pat = input(f'1: search by name 2: search by time q:Return\n')
    while(pat != 'q'):
        if pat == '1':
            str = input("Enter name:")
            loc = hash_name.search_hash(str)
            if loc == 0:
                print("No such course found")
            else:
                loc -= 1
                if list[loc][6] == 1:
                    print("Course Number:%d"%(list[loc][0]))
                    print("Course Name:%s"%(list[loc][1]))
                    print("Course Time:%s"%(list[loc][2][1:3]) + "点" + "%s"%(list[loc][2][3:5]))
                    print("Course Location:%s"%(list[loc][3]))
                    print("Course selection:%d"%(list[loc][4]))
                    print("Course Classroom:%s"%(list[loc][5]))
                    print("Course Information:%s"%(list[loc][7]))
        elif pat == '2':
            str = input("Enter time:")
            loc = hash_time.search_hash(str)
            if loc == 0:
                print("No such course found")
            else:
                loc -= 1
                if list[loc][6] == 1:
                    print("Course Number:%d"%(list[loc][0]))
                    print("Course Name:%s"%(list[loc][1]))
                    print("Course Time:%s"%(list[loc][2][1:3]) + "点" + "%s"%(list[loc][2][3:5]))
                    print("Course Location:%s"%(list[loc][3]))
                    print("Course selection:%d"%(list[loc][4]))
                    print("Course Classroom:%s"%(list[loc][5]))
                    print("Course Information:%s"%(list[loc][7]))                
        pat = input(f'1: search by name 2: search by time q:Return\n')

#quicksort
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

#quicksort
def partition(arr,low,high): 
    i = low - 1
    pivot = arr[high][4]     
  
    for j in range(low , high): 
        if   arr[j][4] <= pivot: 
            i = i + 1 
            #arr[i],arr[j] = arr[j],arr[i] 
            tmp = arr[i].copy()
            arr[i] = arr[j].copy()
            arr[j] = tmp.copy()

    #arr[i+1],arr[high] = arr[high],arr[i+1]
    tmp = arr[i+1].copy()
    arr[i+1] = arr[high].copy()
    arr[high] = tmp.copy() 
    
    return ( i+1 )


def Course_sort(List:list):
    list = List.copy()
    print("Choose the way of sorting")
    pat = input(f'1: sort by number 2: sort by name 3: skip\n')
    if pat == '1':
        quickSort(list,0,len(list)-1)
        for i in range(0,len(list)):
            if list[i][6] == 1:
                print("%s : %d students selected"%(list[i][1],list[i][4]))
    elif pat == '2':
        arr_sorted = []
        for i in range(0,len(list)):
            if list[i][6] == 1:
                arr_sorted.append(list[i][1])
        arr_sorted.sort()
        for name in arr_sorted:
                print(name)

def Activity_Inquiry(hash_name:HashTable,hash_time:HashTable,list:list):
    pat = input(f'1: search by name 2: search by time q:Return\n')
    while(pat != 'q'):
        if pat == '1':
            str = input("Enter name:")
            loc = hash_name.search_hash(str)
            if loc == 0:
                print("No such activity found")
            else:
                loc -= 1
                if list[loc][6] == 0:
                    print("Activity Number:%d"%(list[loc][0]))
                    print("Activity Name:%s"%(list[loc][1]))
                    print("Activity Time:%s"%(list[loc][2][1:3]) + "点" + "%s"%(list[loc][2][3:5]))
                    print("Activity Location:%s"%(list[loc][3]))
                    print("Activity selection:%d"%(list[loc][4]))
                    print("Activity Classroom:%s"%(list[loc][5]))
                    print("Activity Information:%s"%(list[loc][7]))
        elif pat == '2':
            str = input("Enter time:")
            loc = hash_time.search_hash(str)
            if loc == 0:
                print("No such activity found")
            else:
                loc -= 1
                if list[loc][6] == 0:
                    print("Activity Number:%d"%(list[loc][0]))
                    print("Activity Name:%s"%(list[loc][1]))
                    print("Activity Time:%s"%(list[loc][2][1:3]) + "点" + "%s"%(list[loc][2][3:5]))
                    print("Activity Location:%s"%(list[loc][3]))
                    print("Activity selection:%d"%(list[loc][4]))
                    print("Activity Classroom:%s"%(list[loc][5]))
                    print("Activity Information:%s"%(list[loc][7]))                
        pat = input(f'1: search by name 2: search by time q:Return\n')




def Activity_sort(List:list):
    list = List.copy()
    print("Choose the way of sorting")
    pat = input(f'1: sort by number 2: sort by name 3: skip\n')
    if pat == '1':
        quickSort(list,0,len(list)-1)
        for i in range(0,len(list)):
            if list[i][6] == 0:
                print("%s : %d students selected"%(list[i][1],list[i][4]))
    elif pat == '2':
        arr_sorted = []
        for i in range(0,len(list)):
            if list[i][6] == 0:
                arr_sorted.append(list[i][1])
        arr_sorted.sort()
        for name in arr_sorted:
                print(name)




def SelectCourse(ID):
    CourseNo = input("Enter the course number you want to select:")
    students.add_event(ID,[int(CourseNo)])


def Addactivity(ID):
    ActivityNo = input("Enter the activity number you want to select:")
    students.add_event(ID,[int(ActivityNo)])

def CLI_STU():
#login
    try:
        ID = int(input("Type your ID:"))
    except:
        print("Please type the right Format")
        ID = int(input("Type your ID:"))
    
#read class.csv into list    
    Info_Cou = get_db_as_list(DB_PATH_CLASS)
    Info_STU = get_db_as_list(DB_PATH_STU)

#search_by_name
    #convert to Ascii
    INFO_NAME = ASCII_CONVERT_LIST(Info_Cou,1)
    #save in hash
    hash_name = HashTable(len(INFO_NAME))
    for i in INFO_NAME:
        hash_name.insert_hash(i)

#search_by_time
    #convert to Ascii
    INFO_TIME = ASCII_CONVERT_LIST(Info_Cou,2)
    #save in hash
    hash_time = HashTable(len(INFO_TIME))
    for i in INFO_TIME:
        hash_time.insert_hash(i)


    #USER_STU
    OP_LEV1 = input(f'1: Course 2: Activity 3: Guide q: Quit\n')
    while(OP_LEV1 != 'q'):
        if OP_LEV1 == '1':
            OP_LEV2_1 = input(f'1: Inquiry 2: Upload q: Return\n')
            while(OP_LEV2_1 != 'q'):
                if OP_LEV2_1 == '1':
                    Course_sort(Info_Cou)
                    Course_Inquiry(hash_name,hash_time,Info_Cou)
                    '''
                elif OP_LEV2_1 == '2':
                    #TODO: Upload
                    '''
                OP_LEV2_1 = input(f'1: Inquiry 2: Upload q: Return\n')
                    
        '''             
        elif OP_LEV1 == '2':
            #TODO: Activity
        elif OP_LEV1 == '3':
            #TODO: Guide
        '''
        OP_LEV1 = input(f'1: Course 2: Activity 3: Guide q: Quit\n')


# Testrun if run as main 
if __name__ == '__main__':
    OP_LEV0 = input(f'A: Admin U: User\n')
    if OP_LEV0 == 'U':  
        CLI_STU()