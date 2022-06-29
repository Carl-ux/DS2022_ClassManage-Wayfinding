'''
Date: 2022-04-15 19:06:50
LastEditors: Azus
LastEditTime: 2022-06-15 09:38:27
FilePath: /DS/backend/module/timing.py
'''
from ast import arg
from calendar import week
from datetime import datetime
from threading import local, Timer
from logger import logger
import threading
import time
import datetime 

import os
import json

# [m.start() for m in re.finditer('test', 'test test test test')]
FMT_FORMAT='%Y-%m-%d-%H:%M-%a'
STD_TIME = '2022-08-01-00:00-Mon'
'''
time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, 
tm_hour=10, tm_min=3, tm_sec=27, tm_wday=3, 
tm_yday=98, tm_isdst=0)
'''


    
class timer(object):
    def __init__(self):
        self.load()

    def load(self):
        if os.path.getsize('time.json')!=0:
            with open('time.json', 'r+') as fp:
                self.log=json.load(fp)
                self.deltaT = self.log['deltaT']
                self.init_stamp_secs=self.log['init_stamp_secs']
                self.init_stamp_tuple=self.log['init_stamp_tuple']
                self.last_virtual_time=self.log['last_virtual_time']
                print('time.json loaded.')
        else:
            # self.__init__()
            self.deltaT=1
            self.init_stamp_secs=time.time()
            self.init_stamp_tuple=time.localtime(self.init_stamp_secs)
            self.last_virtual_time=self.init_stamp_secs
            self.save()
            print('time.json newed.')

    def save(self):
        self.log={
            'init_stamp_secs':self.init_stamp_secs,
            'init_stamp_tuple':self.init_stamp_tuple,
            'last_virtual_time':self.last_virtual_time,
            'deltaT':self.deltaT
        }
        with open('time.json', 'w') as fp:
            json.dump(self.log, fp)
        pass
    
    def reset(self):
        with open('time.json', 'w') as fp:
            fp.seek(0)
            fp.truncate()
        self.load()
    def strptime(self, time:str):
        """get time string and convert to time tuple

        Args:
            time (str): seting 

        Returns:
            _type_: time tuple
        """
        return time.strptime(time,FMT_FORMAT)

    def get_next_event_time(self, weekday=1, hour=00, minute=00):
        Week_dic=['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        now_year = self.get_time_str()[0:4]
        now_day = self.get_time_str()[8:10]
        now_month= self.get_time_str()[5:7]
        print(now_month)
        dt = datetime.datetime.strptime()
        return "{0}{1}-{2:0>2d}-{3}".format(STD_TIME[:9], weekday, hour, Week_dic[weekday])

    # @return 当前虚拟时    
    def get_time_secs(self):
        crt_secs=time.time()
        secs_passed= crt_secs-self.init_stamp_secs
        virtual_secs=self.last_virtual_time+secs_passed*float(self.deltaT)
        return virtual_secs

    def get_time_str(self):
        time_tuple=time.localtime(self.get_time_secs())
        return time.strftime(FMT_FORMAT, time_tuple)
        
    # @breif 设置当前deltaT: 每真实世界一秒虚拟时间增加量
    def setdeltaT(self, deltaT):
        # memorize virtual time
        self.last_virtual_time=self.get_time_secs()
        self.init_stamp_secs=time.time()
        self.init_stamp_tuple=time.localtime(self.init_stamp_secs)
        # reset deltaT
        self.deltaT=float(deltaT)
        # save seltaT settings
        self.save()
        pass

    def setAlarm(self, year, month, day:int, hour, minute,  info:str, recur):
        """_summary_

        Args:
            year (_type_): _description_
            month (_type_): _description_
            day (int): _description_
            hour (_type_): _description_
            minute (_type_): _description_
            info (str): _description_
            recur (_type_): if recur. 0 no recur, 1 recur every day, 2 recur every week 
        """
        setTime = time.strptime(f'{year}-{month}-{day}-{hour}-{minute}', "%Y-%m-%d-%H-%M")
        interval = time.mktime(setTime) - self.get_time_secs()
        print(interval)
        # Timer(interval, lambda:print(f"Timer: {info}")).start()
        logger.info(f"Timer set for {time.strftime(FMT_FORMAT, setTime)}")
        print(f"Timer set for {time.strftime(FMT_FORMAT, setTime)}")
        thread = threading.Thread(target=self.handleAlarm, args=[time.mktime(setTime), info, recur])
        thread.start()

    def handleAlarm(self, TimeSecs, info, recur):
        while(1):
            time.sleep(1)
            if(TimeSecs - self.get_time_secs()<=0):
                # ! modify alarm behavior 
                logger.info(f"Timer {info} goes off.")
                print(f"Timer: {info}\n")
                if(recur == 1):
                    thread = threading.Thread(target=self.handleAlarm, args=[TimeSecs+86400, info, recur])
                    thread.start()
                elif(recur == 2):
                    thread = threading.Thread(target=self.handleAlarm, args=[TimeSecs+604800, info, recur])
                    thread.start()
                break
                
        
 
if __name__ == "__main__":
    # 初始化
    
    timer = timer()
    # 重制

    # timer.reset()

    # 设置虚拟时间

    # timer.reset()
    print(timer.get_time_str())
    # timer.setdeltaT(1000)
    # timer.setdeltaT(1000)
    # timer.reset()
    timer.setAlarm("2022", "06", "15", "09", "39", "Daily Alarm", recur=1)
    timer.setdeltaT(1000)
    while(1):
        print(timer.get_time_str())
        time.sleep(1)
    # print(timer.get_time_secs())





    # 确定localtime时间

    # 请求当前时间的时候 return localtime

    # localtime能根据delta——t增长

    # 从字符串读入时间 -> 通用的时间 e w结构 struct_time
    # struct_time -> 字符串
    # alarm