'''
Date: 2022-04-15 19:06:50
LastEditors: Azus
LastEditTime: 2022-05-24 16:53:15
FilePath: /DS/backend/timing.py
'''
from calendar import week
from threading import local
import time
import os
import json

# [m.start() for m in re.finditer('test', 'test test test test')]
FMT_FORMAT='%Y-%m-%d-%H:%M-%a'
STD_TIME = '2022-08-01-00:00-Mon'

def get_time_string(weekday=1, hour=00, minute=00):
    Week_dic=['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return "{0}{1}-{2:0>2d}-{3}".format(STD_TIME[:9], weekday, hour, Week_dic[weekday])
    
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
    # @return 当前虚拟时间戳
    def get_time_secs(self):
        crt_secs=time.time()
        secs_passed= crt_secs-self.init_stamp_secs
        virtual_secs=self.last_virtual_time+(secs_passed)*self.deltaT
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
        self.deltaT=deltaT
        # save seltaT settings
        self.save()
        pass
 
if __name__ == "__main__":
    # 初始化
    
    timer = timer()
    
    # 重制
    # timer.reset()

    # 设置虚拟时间
    timer.setdeltaT(1)
    
    print(timer.get_time_str())
    print(timer.get_time_secs())




    # 确定localtime时间

    # 请求当前时间的时候 return localtime

    # localtime能根据delta——t增长

    # 从字符串读入时间 -> 通用的时间 e w结构 struct_time
    # struct_time -> 字符串
    # alarm