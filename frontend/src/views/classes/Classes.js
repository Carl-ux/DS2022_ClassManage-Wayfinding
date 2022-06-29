/*
 * @Date: 2022-06-15 13:06:34
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-15 14:22:41
 * @FilePath: /DS/frontend/src/views/classes/Classes.js
 */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useForm } from "react-hook-form";

import { useDispatch, useSelector } from "react-redux";
import CIcon from "@coreui/icons-react";
import SHAHE from "./../../assets/images/SHAHE.png";
import HAIDIAN from "./../../assets/images/HANDIAN.png";
import { CToast, CToastHeader, CToastBody } from "@coreui/react";

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
    CForm,
    CTableDataCell,
    CImage,
    CInputGroup,
    CInputGroupText,
    CFormInput,
} from "@coreui/react";
import {
    cibCcAmex,
    cibCcApplePay,
    cibCcMastercard,
    cibCcPaypal,
    cibCcStripe,
    cibCcVisa,
    cibGoogle,
    cibFacebook,
    cibLinkedin,
    cifBr,
    cifEs,
    cifFr,
    cifIn,
    cifPl,
    cifUs,
    cibTwitter,
    cilCloudDownload,
    cilPeople,
    cilLockLocked,
    cilUser,
    cilUserFemale,
} from "@coreui/icons";

const Classes = () => {
    let REMOTE_URL = "http://127.0.0.1:5000/";
    const [info, setInfo] = useState();
    const username = useSelector((data) => data.username);
    const [isOK, setOK] = useState(false);
    const classesinfo = useSelector((data) => data.classesinfo);
    const storedata = useSelector((data) => data);
    console.log(storedata);
    // debugger;

    // return( <div>username: {info.json}</div>)

    // if (false == isOK) {
    //     return (
    //         <>
    //             <CSpinner color="primary" />
    //         </>
    //     );
    // }
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
    } = useForm();

    // const onSubmit = async () => {
    //     const loginFormData = new FormData();
    //     loginFormData.append("username", formValue);
    //     // TODO
    // };

    const onSubmit = async (data) => {
        let payload = {
            username: username,
            EventNumber: data.EventNumber,
        };
        axios
            .post(REMOTE_URL + "api/classes/add", payload, {
                headers: { "Access-Control-Allow-Origin": "*" },
            })
            .then((data) => {
                debugger
                console.log("return data");
                console.log(data.data);
                // returned as html
                setInfo(data.data);
                console.log(info)
                console.log(data.data["result"]);
                setOK(true);
            });
        // apis.getStudentInfo(data.username);
    };

    return (
        <div>
            <CCard>
                <CCardHeader>
                    <h2>课程管理</h2>
                </CCardHeader>
                <CCardBody>
                    <CRow>
                        <CCol>
                            <CTable
                                align="middle"
                                className="mb-0 border"
                                hover
                                responsive
                            >
                                <CTableHead color="light">
                                    <CTableRow>
                                        <CTableHeaderCell className="text-center">
                                            编号
                                        </CTableHeaderCell>
                                        <CTableHeaderCell className="text-center">
                                            名称
                                        </CTableHeaderCell>
                                        <CTableHeaderCell className="text-center">
                                            时间
                                        </CTableHeaderCell>

                                        <CTableHeaderCell>
                                            地点
                                        </CTableHeaderCell>
                                    </CTableRow>
                                </CTableHead>
                                <CTableBody>
                                    {classesinfo.map((item, index) => (
                                        <CTableRow
                                            v-for="item in tableItems"
                                            key={index}
                                        >
                                            <CTableDataCell className="text-center">
                                                <div>{item.EventNumber}</div>
                                            </CTableDataCell>
                                            <CTableDataCell className="text-center">
                                                <div>{item.Name}</div>
                                            </CTableDataCell>
                                            <CTableDataCell className="text-center">
                                                <div>
                                                    <strong>{item.Day}</strong>
                                                    {""}
                                                    {item.Time_Begin}-
                                                    {item.Time_End}
                                                </div>
                                            </CTableDataCell>
                                            <CTableDataCell>
                                                <strong>
                                                    {item.Location}{" "}
                                                    {item.classroom}
                                                </strong>
                                            </CTableDataCell>
                                        </CTableRow>
                                    ))}
                                </CTableBody>
                            </CTable>
                        </CCol>
                    </CRow>
                    <br />
                    <CCard>
                        <CCardHeader center>选课</CCardHeader>
                        <CForm onSubmit={handleSubmit(onSubmit)}>
                            <br />
                            <CRow>
                                <CCol xs={6} center>
                                    <CInputGroup className="mb-4">
                                        <CInputGroupText>
                                            <font size="3" heavy>
                                                编号
                                            </font>
                                        </CInputGroupText>
                                        <CFormInput
                                            {...register("EventNumber")}
                                            type="text"
                                            placeholder="202201"
                                        />
                                    </CInputGroup>
                                </CCol>
                                <CCol xs={6} center>
                                    <CButton
                                        type="submit"
                                        color="primary"
                                        className="px-4"
                                    >
                                        选课
                                    </CButton>
                                </CCol>
                            </CRow>
                        </CForm>
                        {isOK ? (
                            <CToast autohide={false} visible={true}>
                                <CToastHeader closeButton>
                                    <svg
                                        className="rounded me-2"
                                        width="20"
                                        height="20"
                                        xmlns="http://www.w3.org/2000/svg"
                                        preserveAspectRatio="xMidYMid slice"
                                        focusable="false"
                                        role="img"
                                    >
                                        <rect
                                            width="100%"
                                            height="100%"
                                            fill="#007aff"
                                        ></rect>
                                    </svg>
                                    <strong className="me-auto">
                                        课程辅助系统
                                    </strong>
                                    <small>now</small>
                                </CToastHeader>
                                <CToastBody>
                                    {(info["result"].indexOf("Conflicted") == -1)
                                    ? (
                                        <>选课成功！！！</>
                                    ) : (
                                        <>选课失败！课程冲突！</>
                                    )}
                                </CToastBody>
                            </CToast>
                        ) : (
                            <br />
                        )}
                    </CCard>
                </CCardBody>
            </CCard>
        </div>
    );
};
export default Classes;
