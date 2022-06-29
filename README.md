# ClassManage-Wayfinding
> Coursework of DataStructure of BUPT 2022. Created Apr 7 2022. Dev on React with Redux and Python with Flask.


## How to start
1. Client side web server
```sh
cd frontend && npm install #install node modules
npm start #start local web server
cd ./../backend/module && python app.py  # start flask server 
```
2. CLI Interface 
```sh
cd ./../backend/module && python interface.py  # start CLI 
```

## 模块结构
```

.
├── DB     
│   ├── class.csv               **课程数据库**  
│   ├── coursework              **作业文件储存**  
│   │   ├── 202201    
│   │   └── 202205  
│   └── student.csv             **学生数据库**  
├── README.md  
├── backend  
│   ├── client.py               **前端模拟接口脚本**  
│   ├── module  
│   │   ├── DB.py               **数据操作原型**  
│   │   ├── DB_Classes.py       **课程信息数据操作**  
│   │   ├── DB_Stu.py           **学生信息数据操作**  
│   │   ├── __init_.py          **Module __init__**  
│   │   ├── app.py              **Flask APP Http服务器**  
│   │   ├── coursework.py       **作业文件处理模块**  
│   │   ├── interface.py        **CLI/API交互接口**  
│   │   ├── log.txt             **日志文件**  
│   │   ├── logger.py           **日志模块**  
│   │   ├── map.py              **寻路模块**  
│   │   ├── reverseProxy.py     **Flask反向代理脚本**  
│   │   ├── time.json       **虚拟时间储存文件**  
│   │   ├── timing.py       **虚拟时间、闹钟模块**  
│   │   ├── user.py         **课内外交互管理**  
│   │   ├── util.py       
│   │   └── zip.py          **压缩功能模块**  
├── frontend
│   ├── build
│   ├── node_modules
│   ├── package.json
│   ├── public
│   ├── src                 **React源文件**
│   │   ├── App.js  
│   │   ├── App.test.js
│   │   ├── _nav.js         **navbar对象**
│   │   ├── apis.js         **接口函数**
│   │   ├── assets
│   │   ├── components      **react组件**
│   │   │   ├── ...
│   │   ├── index.js        **入口文件**
│   │   ├── layout  
│   │   ├── reportWebVitals.js
│   │   ├── routes.js       **react-router配置**
│   │   ├── scss            **scss样式文件**
│   │   ├── store.js        **Redux配置**
│   │   └── views           **渲染页面**
├── log.txt                 **日志保存**
├── settings.json
├── time.json               **虚拟时间储存**
└── tree.txt                

861 directories, 57 files
```




## TODO
1. 单个课程展示界面（资料？）

> 课程信息？【课程资料、当前进度、已交作业、待交作业、课程群、考试时间和考试地点等信息】）
作业（是否已交）

输入课程名称(时间）查询

系统可以检测个人活动、集体活动和课程的时间冲突，并给出提示。


### 提交内容

整个系统的架构、完成的所有功能、设计和使用的各种算法、算法性能的分析、系统测试结果、运行效果截图展示等内容；报告中最好能够突出自己所做功能如何更好地满足实际用户的需求，以及采用算法的理由和优缺点；每个小组交一份报告，但是在报告中要明确详细的阐述所有组员的分工和贡献；此报告作为评分的主要依据； 

可执行代码（可运行的系统，包括环境配置说明）

功能需求报告、总体方案设计报告、数据结构说明报告、各模块设计报告、测试报告、评价和改进意见报告、用户使用说明报告