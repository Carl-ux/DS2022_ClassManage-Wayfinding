import {
    CCol,
    CCard,
    CCardBody,
    CCardTitle,
    CCardSubtitle,
    CButton,
    CCardFooter,
    CCardText,
    CContainer,
    CRow,
    CCardHeader,
    CCardLink,
    CTableHead,
    CTableHeaderCell,
    CTableBody,
    CTable,
    CTableRow,
    CTableDataCell,

} from "@coreui/react";

import React, { useState, useEffect } from "react";
import axios from "axios";

import { useDispatch, useSelector } from "react-redux";

const SchoolCalender = () => {
    const isLogged = useSelector((state) => state.isLogged);
    const dispatch = useDispatch();
    const updateClass = (classes) => {
        dispatch({
            type: "set",
            classesinfo: classes,
        });
    };


    const weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"];
    const classes = [
        {
            Name: "高等数学",
            Time_Begin: "T0800",
            Location: "沙河北教学楼",
            Num: 20,
            classroom: "N116",
            ifClass: 1,
            info: "{'description':'暂无','QQ':'1234'}",
            Time_End: "T0955",
            Day: "星期一",
            index: 1,
            weekday: 1,
        },
        {
            Name: "数据结构",
            Time_Begin: "T1530",
            Location: "海淀南一教",
            Num: 5,
            classroom: "S201",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T1645",
            Day: "星期二",
            index: 4,
            weekday: 2,
        },
        {
            Name: "大学物理",
            Time_Begin: "T0930",
            Location: "沙河北教学楼",
            Num: 18,
            classroom: "N112",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T1120",
            Day: "星期三",
            index: 2,
            weekday: 3,
        },
        {
            Name: "Java",
            Time_Begin: "T1000",
            Location: "海淀北一教",
            Num: 26,
            classroom: "N134",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T1150",
            Day: "星期四",
            index: 2,
            weekday: 4,
        },
        {
            Name: "机器学习",
            Time_Begin: "T2100",
            Location: "沙河北教学楼",
            Num: 40,
            classroom: "N221",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T2125",
            Day: "星期五",
            index: 6,
            weekday: 5,
        },
        {
            Name: "计算机视觉",
            Time_Begin: "T2020",
            Location: "海淀南一教",
            Num: 18,
            classroom: "S114",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T2145",
            Day: "星期五",
            index: 6,
            weekday: 5,
        },
        {
            Name: "计算机网络",
            Time_Begin: "T0730",
            Location: "沙河北教学楼",
            Num: 60,
            classroom: "N134",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T0845",
            Day: "星期二",
            index: 1,
            weekday: 2,
        },
        {
            Name: "军事理论",
            Time_Begin: "T1400",
            Location: "沙河学生活动中心",
            Num: 70,
            classroom: "202",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T1700",
            Day: "星期三",
            index: 3,
            weekday: 3,
        },
        {
            Name: "R语言",
            Time_Begin: "T1800",
            Location: "沙河南教学楼",
            Num: 30,
            classroom: "S208",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "T1925",
            Day: "星期一",
            index: 5,
            weekday: 1,
        },
        {
            Name: "ios开发",
            Time_Begin: "T1020",
            Location: "海淀北二教",
            Num: 55,
            classroom: "N233",
            ifClass: 1,
            info: '{"description":"暂无"}',
            Time_End: "1225",
            Day: "星期三",
            index: 2,
            weekday: 3,
        },
        {
            Name: "天堂酒吧",
            Time_Begin: "T2300",
            Location: "沙河学生活动中心",
            Num: 100,
            classroom: "三楼",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T2400",
            Day: "星期六",
            index: 6,
            weekday: 6,
        },
        {
            Name: "心理建设",
            Time_Begin: "T2000",
            Location: "沙河学生活动中心",
            Num: 80,
            classroom: "二楼",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T2100",
            Day: "星期日",
            index: 6,
            weekday: 7,
        },
        {
            Name: "班会",
            Time_Begin: "T1930",
            Location: "沙河学生活动中心",
            Num: 30,
            classroom: "二楼",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T2010",
            Day: "星期一",
            index: 6,
            weekday: 1,
        },
        {
            Name: "聚餐",
            Time_Begin: "T1230",
            Location: "沙河一食堂",
            Num: 5,
            classroom: "三楼",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T1300",
            Day: "星期二",
            index: 2,
            weekday: 2,
        },
        {
            Name: "小组作业",
            Time_Begin: "T1900",
            Location: "海淀学一寝",
            Num: 3,
            classroom: "四楼",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T2400",
            Day: "星期三",
            index: 5,
            weekday: 3,
        },
        {
            Name: "锻炼",
            Time_Begin: "T2030",
            Location: "海淀足球场",
            Num: 1,
            classroom: "操场",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T2110",
            Day: "星期四",
            index: 6,
            weekday: 4,
        },
        {
            Name: "外出",
            Time_Begin: "T0700",
            Location: "海淀车站",
            Num: 1,
            classroom: "车站",
            ifClass: 0,
            info: '{"description":"暂无"}',
            Time_End: "T1720",
            Day: "星期六",
            index: 1,
            weekday: 6,
        },
    ];
    const cls = [
        {
            key: "1",
            name: "电子竞技科学与技术",
            weekday: "1",
            time: "8:00-10:30",
            index: "1",
            teacher: "白浩楠",

            loc: "郑州市",
        },
        {
            key: "2",

            name: "电子竞技科学与技术",
            weekday: "3",
            time: "8:00-10:30",
            index: "3",
            teacher: "白浩楠",

            loc: "郑州市",
        },
        {
            key: "3",

            name: "优雅男子",
            weekday: "2",
            time: "8:00-10:30",
            index: "1",
            teacher: "吕卓生",
            loc: "S101",
        },
    ];

    let REMOTE_URL = "http://127.0.0.1:5000/";
    const [info, setInfo] = useState();
    const [isOK, setOK] = useState(false);
    let data = {}
    useEffect(() => {
        axios
            .post(REMOTE_URL + "api/classes/", data, {
                headers: { "Access-Control-Allow-Origin": "*" },
            })
            .then((data) => {
                console.log("return data");
                // returned as html
                console.log(data.data);
                setInfo(JSON.parse(data.data));
                console.log(info);
                updateClass(JSON.parse(data.data));
                setOK(true);
            });
    }, []);

    // if(false==isOK){
    //   return (<>
    //         <CSpinner color="primary" />
    //     </>)
    // }

    // return <div>{info}</div>;

    const [timetable, setTimetable] = useState([[], [], [], [], [], [], []]);

    const getrows = (classes) => {
        let rows = [[], [], [], [], [], []];
        let a = 1;
        let day = 1;
        for (a = 1; a <= 6; a++) {
            const crtRow = classes.filter((element) => {
                return element.index == a;
            });
            for (day = 1; day <= 7; day++) {
                rows[a - 1].push(
                    crtRow.filter((element) => {
                        return element.weekday == day;
                    })[0]
                );
            }
        }
        console.log(rows);
        return rows;
    };
    // setTimetable(updateTimetable());
    const RenderTimetable = () => {
        // if (false == isOK) {
        //     return (
        //         <>
        //             <CSpinner color="primary" />
        //         </>
        //     );
        // }
        return (
            <CTableBody>
                {timetable.map((item, index) => {
                    return (
                        <CTableRow>
                            <CTableHeaderCell>{index}</CTableHeaderCell>
                            {item.map((subItem, subIndex) => {
                                return undefined == subItem ? (
                                    <CTableDataCell></CTableDataCell>
                                ) : (
                                    <CTableDataCell>
                                        <CCard width="20rem">
                                            <CCardBody>
                                                <CCardTitle>
                                                    <font size="2">
                                                        {subItem.Name}
                                                    </font>
                                                </CCardTitle>
                                                <CCardSubtitle className="mb-2 text-medium-emphasis">
                                                    <font size="2">
                                                        {subItem.EventNumber}
                                                    </font>
                                                </CCardSubtitle>
                                                <CCardText>
                                                    <font size="2">
                                                        {subItem.Location}
                                                    </font>
                                                    <font size="2">
                                                        {subItem.classroom}
                                                    </font>
                                                    <br />
                                                    <font size='1'>
                                                        {subItem.Time_Begin}-{subItem.Time_End}
                                                    </font>
                                                </CCardText>
                                            </CCardBody>
                                        </CCard>
                                    </CTableDataCell>
                                );
                            })}
                        </CTableRow>
                    );
                })}
            </CTableBody>
        );
    };
    return (
        <>
            {/* <CButton onClick={()=>{dispatch(
                {type:"set", isLogged:!isLogged}
            )}}>
                <font>Log in</font>
            </CButton> */}
            <CCard className="mb-4">
                <CCardHeader>
                    <CRow>
                        <CCol>
                            <h4>课程表</h4>
                        </CCol>
                        <CCol>
                            <div align="right">
                                <CButton
                                    onClick={() => {
                                        setTimetable(getrows(info));
                                    }}
                                    color="light"
                                    size="sm"
                                >
                                    <font size="1" color="grey">
                                        同步课程
                                    </font>
                                </CButton>
                            </div>
                        </CCol>
                    </CRow>
                </CCardHeader>

                <CTable hover bordered small responsive color="light">
                    <CTableHead>
                        <CTableRow>
                            <CTableHeaderCell>#</CTableHeaderCell>

                            <CTableHeaderCell scope="col">
                                周一
                            </CTableHeaderCell>
                            <CTableHeaderCell scope="col">
                                周二
                            </CTableHeaderCell>
                            <CTableHeaderCell scope="col">
                                周三
                            </CTableHeaderCell>
                            <CTableHeaderCell scope="col">
                                周四
                            </CTableHeaderCell>
                            <CTableHeaderCell scope="col">
                                周五
                            </CTableHeaderCell>
                            <CTableHeaderCell scope="col">
                                周六
                            </CTableHeaderCell>
                            <CTableHeaderCell scope="col">
                                周天
                            </CTableHeaderCell>
                        </CTableRow>
                    </CTableHead>
                    {RenderTimetable()}
                </CTable>
            </CCard>
        </>
    );
};

export default SchoolCalender;
