# ClassManage-Wayfinding
> Coursework of DataStructure of BUPT 2022. Created Apr 7 2022.




## ./backend/ structure
.
├── DB  
│   ├── class.csv   **Class DB**  
│   ├── coursework  **Coursework storage**  
│   │   └── 202201  
│   └── student.csv **Student DB**  
├── README.md  
├── backend       
│   ├── DB.py   **DB proto**  
│   ├── DB_Classes.py   **provide `classes` as db_class  **  
│   ├── DB_Stu.py   - **provide `students`  **  
│   ├── Server  **flask server**  
│   │   ├── app.py   
│   │   └── reverseProxy.py  
│   ├── coursework.py   **coursework upload and management**  
│   ├── log.txt     **sys log**   
│   ├── logger.py   **sys log module**  
│   ├── timing.py   **virtual time module**  
│   ├── user.py **CLI interface**  
│   ├── util.py - utils  
│   └── zip.py  **zip function for file upload**  
├── frontend    **npm env with react**  
│   ├── README.md  
│   ├── package-lock.json  
│   ├── package.json  
│   ├── public  
│   └── src  
├── log.txt  
├── settings.json  
├── test.ipynb   
└── time.json   **virtual time config**  
