'''
Description:
Author: Carl
Date: 2022-06-11 15:09:39
LastEditTime: 2022-06-15 12:14:37
LastEditors: Azus
'''


from collections import deque
from json.encoder import INFINITY
from re import S



class map:

    V_walk = 1.25
    V_bicycle = 5                 #m/s

    Hmapdict = {}  # 字典存储有向图
    Smapdict = {}  # 字典存储有向图

    H_Build_List = [
        '海淀北一教',
        '海淀北二教',
        '海淀南一教',
        '海淀南二教',
        '海淀北办公楼',
        '海淀东办公楼',
        '海淀学一寝',
        '海淀学二寝',
        '海淀学三寝',
        '海淀学四寝',
    ]

    H_Service_List = [
        '海淀图书馆',
        '海淀车站',
        '海淀医务室',
        '海淀物美超市',
        '海淀篮球场',
        '海淀银行',
        '海淀一食堂',
        '海淀二食堂',
        '海淀洗衣房',
        '海淀足球场',
    ]

    S_Build_List = [
        '沙河北教学楼',
        '沙河南教学楼',
        '沙河东配楼',
        '沙河行政办公楼',
        '沙河南一寝',
        '沙河南二寝',
        '沙河南三寝',
        '沙河南四寝',
        '沙河北一寝',
        '沙河北二寝',
    ]

    S_Service_List = [
        '沙河图书馆',
        '沙河车站',
        '沙河医务室',
        '沙河超市',
        '沙河篮球场',
        '沙河学生活动中心',
        '沙河教工食堂',
        '沙河学生食堂',
        '沙河公园',
        '沙河足球场',
    ]

    def __init__(self):
        self.loadHEAD()  # 载入头结点
        self.addDirectLine()

    def loadHEAD(self):
        for building in self.H_Build_List:
            self.addVertex(building,1)
        for building in self.H_Service_List:
            self.addVertex(building,1)
        for building in self.S_Build_List:
            self.addVertex(building,2)
        for building in self.S_Service_List:
            self.addVertex(building,2)

    def addVertex(self, key: str,i):
        if i == 1:
            self.Hmapdict[key] = []
        elif i ==2:
            self.Smapdict[key] = []

    def addDirectLine(self):  # 添加有向边
        start = '海淀北一教'
        end = [['海淀北二教', 50, 0.2], ['海淀北办公楼', 500, 0.3], ['海淀学一寝', 200, 0.4]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀北二教'
        end = [['海淀北一教', 50, 0.2], ['海淀北办公楼', 500, 0.5], ['海淀学一寝', 180, 0.4],
               ['海淀篮球场', 300, 0.3]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀南一教'
        end = [['海淀南二教', 50, 0.2], ['海淀银行', 500, 0.2], ['海淀物美超市', 480, 0.4],
               ['海淀足球场', 1000, 0.5], ['海淀车站', 1500, 0.5]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀南二教'
        end = [['海淀南一教', 50, 0.2], ['海淀银行', 480, 0.2]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀北办公楼'
        end = [['海淀北一教', 500, 0.2], ['海淀北二教', 500, 0.4], ['海淀篮球场', 200, 0.1],
               ['海淀图书馆', 400, 0.3], ['海淀东办公楼', 600, 0.1]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀东办公楼'
        end = [['海淀北办公楼', 600, 0.4], ['海淀医务室', 200, 0.4], ['海淀车站', 300, 0.7],
               ['海淀图书馆', 300, 0.6], ['海淀足球场', 400, 0.7]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀学一寝'
        end = [['海淀北一教', 200, 0.5], ['海淀北二教', 180, 0.4], ['海淀篮球场', 400, 0.2],
               ['海淀学二寝', 100, 0.2], ['海淀一食堂', 200, 0.7], ['海淀洗衣房', 200, 0.3]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀学二寝'
        end = [['海淀学一寝', 100, 0.2], ['海淀学三寝', 100, 0.3], ['海淀足球场', 400, 0.7],
               ['海淀洗衣房', 150, 0.3], ['海淀一食堂', 250, 0.7]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀学三寝'
        end = [['海淀学二寝', 100, 0.3], ['海淀学四寝', 100, 0.2], ['海淀二食堂', 150, 0.5],
               ['海淀足球场', 300, 0.4], ['海淀洗衣房', 150, 0.3]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀学四寝'
        end = [['海淀学三寝', 100, 0.2], ['海淀物美超市', 500, 0.4], ['海淀银行', 550, 0.2],
               ['海淀足球场', 300, 0.4], ['海淀洗衣房', 200, 0.3], ['海淀二食堂', 280, 0.7]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀图书馆'
        end = [['海淀篮球场', 300, 0.8], ['海淀北办公楼', 400, 0.2], ['海淀东办公楼', 300, 0.5],
               ['海淀医务室', 150, 0.4], ['海淀一食堂', 100, 0.6]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀车站'
        end = [['海淀足球场', 700, 0.6], ['海淀东办公楼', 300, 0.5], ['海淀南一教', 1500, 0.5]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀医务室'
        end = [['海淀一食堂', 200, 0.4], ['海淀二食堂', 180, 0.3], ['海淀图书馆', 150, 0.5],
               ['海淀足球场', 300, 0.4], ['海淀东办公楼', 200, 0.3]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀物美超市'
        end = [['海淀足球场', 700, 0.3], ['海淀学四寝', 500, 0.4], ['海淀银行', 100, 0.2],
               ['海淀南一教', 480, 0.1]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀篮球场'
        end = [['海淀北二教', 300, 0.5], ['海淀学一寝', 400, 0.3], ['海淀一食堂', 300, 0.5],
               ['海淀北办公楼', 200, 0.2], ['海淀图书馆', 300, 0.6]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀银行'
        end = [['海淀物美超市', 100, 0.3], ['海淀学四寝', 550, 0.4], ['海淀南一教', 500, 0.4],
               ['海淀南二教', 480, 0.4]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀一食堂'
        end = [['海淀篮球场', 300, 0.6], ['海淀学一寝', 200, 0.8], ['海淀学二寝', 250, 0.7],
               ['海淀医务室', 200, 0.4], ['海淀二食堂', 50, 0.6], ['海淀图书馆', 100, 0.3],
               ['海淀学二寝', 250, 0.7]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀二食堂'
        end = [['海淀学三寝', 150, 0.8], ['海淀足球场', 200, 0.3], ['海淀医务室', 180, 0.4],
               ['海淀一食堂', 50, 0.6], ['海淀学四寝', 280, 0.7]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀洗衣房'
        end = [['海淀学一寝', 200, 0.3], ['海淀学二寝', 150, 0.3], ['海淀学三寝', 150, 0.3],
               ['海淀学四寝', 200, 0.3]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '海淀足球场'
        end = [['海淀二食堂', 200, 0.3], ['海淀医务室', 300, 0.3], ['海淀学三寝', 3000, 0.5],
               ['海淀学四寝', 300, 0.4], ['海淀车站', 700, 0.6], ['海淀南一教', 1000, 0.2],
               ['海淀物美超市', 700, 0.1], ['海淀东办公楼', 400, 0.7]]
        for row in end:
            self.Hmapdict[start].append(row)

        start = '沙河北教学楼'
        end = [['沙河南教学楼', 50, 0.2], ['沙河图书馆', 100, 0.4], ['沙河南一寝', 500, 0.8],
               ['沙河公园', 200, 0.8]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河南教学楼'
        end = [['沙河北教学楼', 50, 0.2], ['沙河公园', 250, 0.8], ['沙河南四寝', 550, 0.8]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河东配楼'
        end = [['沙河图书馆', 50, 0.2], ['沙河学生活动中心', 80, 0.2], ['沙河行政办公楼', 60, 0.4],
               ['沙河医务室', 200, 0.5]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河行政办公楼'
        end = [['沙河图书馆', 100, 0.2], ['沙河学生活动中心', 50, 0.3],
               ['沙河学生食堂', 100, 0.2], ['沙河教工食堂', 60, 0.2], ['沙河医务室', 40, 0.5],
               ['沙河东配楼', 60, 0.4]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河南一寝'
        end = [['沙河北教学楼', 500, 0.8], ['沙河公园', 350, 0.6], ['沙河南二寝', 30, 0.5],
               ['沙河车站', 3000, 0.7], ['沙河学生食堂', 150, 0.2], ['沙河北二寝', 90, 0.6],
               ['沙河足球场', 140, 0.7], ['沙河超市', 150, 0.6]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河南二寝'
        end = [['沙河南一寝', 30, 0.5], ['沙河公园', 250, 0.6], ['沙河南三寝', 30, 0.5],
               ['沙河足球场', 120, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河南三寝'
        end = [['沙河南二寝', 30, 0.5], ['沙河公园', 250, 0.6], ['沙河南四寝', 30, 0.5],
               ['沙河足球场', 100, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河南四寝'
        end = [['沙河南三寝', 30, 0.5], ['沙河公园', 300, 0.6], ['沙河南教学楼', 550, 0.8],
               ['沙河足球场', 130, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河北一寝'
        end = [['沙河医务室', 250, 0.5], ['沙河教工食堂', 100, 0.2], ['沙河学生食堂', 150, 0.2],
               ['沙河北二寝', 50, 0.4], ['沙河超市', 100, 0.4], ['沙河篮球场', 150, 0.3]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河北二寝'
        end = [['沙河北一寝', 50, 0.4], ['沙河教工食堂', 150, 0.2], ['沙河学生食堂', 100, 0.2],
               ['沙河南一寝', 90, 0.6], ['沙河超市', 80, 0.4], ['沙河篮球场', 200, 0.3],
               ['沙河车站', 3200, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河图书馆'
        end = [['沙河学生活动中心', 50, 0.3], ['沙河行政办公楼', 100, 0.2], ['沙河东配楼', 50, 0.2],
               ['沙河北教学楼', 100, 0.4]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河车站'
        end = [['沙河篮球场', 2700, 0.7], ['沙河超市', 2800, 0.7], ['沙河北二寝', 3200, 0.7],
               ['沙河南一寝', 3000, 0.7],
               ['沙河足球场', 2500, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河医务室'
        end = [['沙河北一寝', 250, 0.5], ['沙河教工食堂', 80, 0.5], ['沙河行政办公楼', 40, 0.5],
               ['沙河东配楼', 200, 0.5]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河超市'
        end = [['沙河篮球场', 100, 0.4], ['沙河北一寝', 100, 0.4], ['沙河北二寝', 80, 0.4],
               ['沙河南一寝', 150, 0.6], ['沙河车站', 2800, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河篮球场'
        end = [['沙河车站', 2700, 0.7], ['沙河超市', 100, 0.4], ['沙河北一寝', 200, 0.3],
               ['沙河北二寝', 150, 0.3]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河学生活动中心'
        end = [['沙河教工食堂', 110, 0.2], ['沙河行政办公楼', 50, 0.3], ['沙河东配楼', 80, 0.2],
               ['沙河图书馆', 50, 0.3], ['沙河公园', 150, 0.8], ['沙河学生食堂', 50, 0.2]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河教工食堂'
        end = [['沙河学生食堂', 30, 0.1], ['沙河北二寝', 150, 0.2], ['沙河北一寝', 100, 0.2],
               ['沙河医务室', 80, 0.5], ['沙河行政办公楼', 60, 0.2],
               ['沙河学生活动中心', 110, 0.2]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河学生食堂'
        end = [['沙河教工食堂', 30, 0.1], ['沙河北二寝', 100, 0.2], ['沙河北一寝', 150, 0.2],
               ['沙河南一寝', 150, 0.2], ['沙河行政办公楼', 100, 0.2],
               ['沙河学生活动中心', 50, 0.2], ['沙河公园', 180, 0.8]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河公园'
        end = [['沙河学生食堂', 180, 0.8], ['沙河学生活动中心', 150, 0.8],
               ['沙河北教学楼', 200, 0.8], ['沙河南教学楼', 250, 0.8], ['沙河南一寝', 350, 0.6],
               ['沙河南二寝', 250, 0.6], ['沙河南三寝', 250, 0.6], ['沙河南四寝', 300, 0.6]]
        for row in end:
            self.Smapdict[start].append(row)

        start = '沙河足球场'
        end = [['沙河车站', 2500, 0.7], ['沙河南一寝', 140, 0.7], ['沙河南二寝', 120, 0.7],
               ['沙河南三寝', 100, 0.7], ['沙河南四寝', 130, 0.7]]
        for row in end:
            self.Smapdict[start].append(row)

    def showMap(self):
        for key in self.Hmapdict:
            print(key, '-->', self.Hmapdict[key])
        for key in self.Smapdict:
            print(key, '-->', self.Smapdict[key])

    def arcNum(self):
        i = 0
        for key in self.Hmapdict:
            for arc in self.Hmapdict[key]:
                i = i + 1
        for key in self.Smapdict:
            for arc in self.Smapdict[key]:
                i = i + 1
        print(i)


    def toString(self,queue):
        str = queue[0]
        for i in range(1,len(queue)):
            str = str + ' --> ' + queue[i]
        return str

    def method3_pf(self,deque,chart):
        for i in range(1,len(deque)):
            for arc in chart[deque[i-1]]:
                if arc[0] == deque[i]:
                    if arc[1] > 150:
                        print('{0}到{1} 选择骑行，耗时{2}s'.format(deque[i-1],deque[i],int(self.method_3(arc)[1])) + '\n')
                    elif arc[1] <= 150 and arc[1] >= 0:
                        print('{0}到{1} 选择步行，耗时{2}s'.format(deque[i-1],deque[i],int(self.method_3(arc)[1])) + '\n')


    def printPath(self,start:str,end:str,campus:int,method:int):
        if method == 1:
            returned_path, returned_distance = self.dijkstra(start,end,campus,method)
            print('目的地，终点: {0} -> {1}'.format(start, end))
            print('距离最短路径: {0}'.format(self.toString(returned_path)))
            print('距离: {0}m'.format(returned_distance))

        elif method == 2:
            returned_path, returned_distance = self.dijkstra(start,end,campus,method)
            print('目的地，终点: {0} -> {1}'.format(start, end))
            print('时间最短路径: {0}'.format(self.toString(returned_path)))
            print('步行预估耗时: {0}s'.format(returned_distance))

        elif method == 3:
            returned_path,returned_adj, returned_distance = self.dijkstra(start,end,campus,method)
            print('目的地，终点: {0} -> {1}'.format(start, end))
            self.method3_pf(returned_path,returned_adj)
            print('预估总耗时: {0}s'.format(returned_distance))

    def GetPathStr(self,start:str,end:str,campus:int,method:int):
        ret = ''
        # print(start)
        # print(end)
        # print(campus)

        if method == 1:
            returned_path, returned_distance = self.dijkstra(start,end,campus,method)
            ret = ret +'目的地，终点: {0} -> {1}\n'.format(start, end)
            ret = ret +'距离最短路径: {0}\n'.format(self.toString(returned_path))
            ret = ret +'距离: {0}m \n'.format(returned_distance)

        elif method == 2:
            returned_path, returned_distance = self.dijkstra(start,end,campus,method)
            ret = ret +'目的地，终点: {0} -> {1}\n'.format(start, end)
            ret = ret +'时间最短路径: {0}\n'.format(self.toString(returned_path))
            ret = ret +'步行预估耗时: {0}s \n'.format(returned_distance)

        elif method == 3:
            returned_path,returned_adj, returned_distance = self.dijkstra(start,end,campus,method)
            ret = ret +'目的地，终点: {0} -> {1} \n'.format(start, end)
            self.method3_pf(returned_path,returned_adj)
            ret = ret +'预估总耗时: {0}s \n'.format(returned_distance)
        return ret

    def findPath(self,start:str,end:str,method:int):
        """main function of finding path

        Args:
            start (str): start point, strict string pairing 
            end (str): end point, strict string pairing 
            method (int): path-finding strategy:
            1 : min dis; 2: min time; 3 : min time with transport 
        """
        if(start[0:2] == '海淀' and end[0:2] == '海淀'):
            self.printPath(start,end,1,method)
            
        if(start[0:2] == '沙河' and end[0:2] == '沙河'):
            self.printPath(start,end,2,method)

        if(start[0:2] == '海淀'  and end[0:2] == '沙河'):
            self.printPath(start,'海淀车站',1,method)
            # print('\n' + '目的地，终点: {0} -> {1}'.format('海淀车站','沙河车站') + '\n')
            self.printPath('沙河车站',end,2,method)

        if(start[0:2] == '沙河'  and end[0:2] == '海淀'):
            self.printPath(start,'沙河车站',2,method)
            print('\n' + '目的地，终点: {0} -> {1}'.format('沙河车站','海淀车站') + '\n')            
            self.printPath('海淀车站',end,1,method)
    def get_str_Path(self,start:str,end:str,method:int):
        """main function of finding path

        Args:
            start (str): start point, strict string pairing 
            end (str): end point, strict string pairing 
            method (int): path-finding strategy:
            1 : min dis; 2: min time; 3 : min time with transport 
        """
        ret =""
        if(start[0:2] == '海淀' and end[0:2] == '海淀'):
            ret = ret + self.GetPathStr(start,end,1,method)
            
        if(start[0:2] == '沙河' and end[0:2] == '沙河'):
            ret = ret + self.GetPathStr(start,end,2,method)

        if(start[0:2] == '海淀'  and end[0:2] == '沙河'):
            ret = ret + self.GetPathStr(start,'海淀车站',1,method)
            # print(self.GetPathStr(start,'海淀车站',1,method))
            ret = ret +('\n' + '目的地，终点: {0} -> {1}'.format('海淀车站','沙河车站') + '\n')
            ret = ret + self.GetPathStr('沙河车站',end,2,method)
            # print(self.GetPathStr('沙河车站',end,2,method))

        if(start[0:2] == '沙河'  and end[0:2] == '海淀'):
            ret = ret + self.GetPathStr(start,'沙河车站',2,method)
            ret = ret +('\n' + '目的地，终点: {0} -> {1}'.format('沙河车站','海淀车站') + '\n')            
            ret = ret + self.GetPathStr('海淀车站',end,1,method)
        # print(f"get_str_path {ret}")
        print(ret)
        return ret


    def method_3(self,arc:list):
        if arc[1] > 150:                                        #大于150距离的路可以骑行
            return arc[0],arc[1]/(arc[2] * self.V_bicycle)
        elif arc[1] <= 150 and arc[1] >=0:
            return arc[0],arc[1]/(arc[2] * self.V_walk)


    def dijkstra(self,start:str,end:str,campus,method,path = []):
        if campus == 1:          #表示海淀校区
            mapdict = self.Hmapdict.copy()
        elif campus == 2:        #表示沙河校区
            mapdict = self.Smapdict.copy()
        
        nodes = {key for key in mapdict.keys()}
        #表
        adjacency_list = {node: set() for node in nodes}
        if method == 1:
            for key in mapdict:
                for arc in mapdict[key]:
                    adjacency_list[key].add((arc[0],arc[1]))
        elif method == 2:
             for key in mapdict:
                for arc in mapdict[key]:
                    adjacency_list[key].add((arc[0],arc[1]/(arc[2] * self.V_walk)))
        elif method == 3:
            return_adj = {node: set() for node in nodes}
            for key in mapdict:
                for arc in mapdict[key]:
                    return_adj[key].add((arc[0],arc[1],arc[2]))
                    adjacency_list[key].add(self.method_3(arc))
                    
        #创建一个字典表示每个点到起始点的距离，每个点先初始化为inf除了点本身初始化为0
        #当我们找到一个更短路径的时候更新这个字典所对应的值，数据结构为 节点：距离
        distance_from_start = {
            node: (0 if node == start else INFINITY) for node in nodes
        }

        #节点其中后面的节点是前面的前置节点，由此可以一步步找到路径，如果找到更短路径就更新这个字典
        previous_node = {node: None for node in nodes}
        #创造一个未访问节点的集合初始化为所有节点
        unvisited_nodes = nodes.copy()

        while unvisited_nodes:
            #将当前节点设置为到目前为止在未访问节点这个字典中路径最短的节点
            current_node = min(
                #从unvisited_nodes中找到键值最小的节点作为当前节点
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            #从未访问的节点中，移除当前节点
            unvisited_nodes.remove(current_node)
            #如果当前节点的距离为无穷大，则其余未访问的节点不会连接到开始节点，停止
            if distance_from_start[current_node] == INFINITY:
                break
 
            #遍历每个当前节点的邻居，检查一下从起始节点到当前节点再到邻居节点的距离的大小
            #与distance_form_start中的比较看看是否更小，是讲究更新distance中所对应的值
            for neighbor, distance in adjacency_list[current_node]:
                #新的路径的距离
                new_path = distance_from_start[current_node] + int(distance)
                if new_path < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = new_path#更新值
                    previous_node[neighbor] = current_node#更新路径，将当前节点作为邻居的前置节点
 
        #为了找到我们所建立的最短路径，使用迭代器遍历每个点的前置节点即可找到路径
        #并且把他存入一个队列中之所以可以保证找得到前置节点，是因为算法完成时候每个点的前置节点都代表着
        #到起始点的最短路径
        path = deque()
        current_node = end
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start)
        if method == 1 or method == 2:
            return path, distance_from_start[end]
        elif method == 3:
            return path,return_adj,distance_from_start[end]











def main():
    m = map()
    #m.showMap()
    #m.arcNum()
    #用户输入起点 终点 和 策略
    
    #start = input()
    #end = input()
    #method = int(input())
    

    #m.findPath(start,end,method)

    # m.findPath('海淀南二教','海淀学一寝',1)
    # m.findPath('海淀南二教','海淀学一寝',2)
    # m.findPath('海淀南二教','海淀学一寝',3)
    # print(m.GetPathStr("沙河车站", "沙河南教学楼", 2, 1))

    # data ={
    #     "from_data": f'{form_data}',
    #     "json": f'{json}'
    # }
    # print(json)
    # print(json["departure"])
    result = m.get_str_Path("沙河车站", "沙河南教学楼", 1)

    

if __name__ == '__main__':
    main()
