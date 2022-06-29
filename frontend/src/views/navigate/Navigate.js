/*
 * @Date: 2022-06-14 01:26:25
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-15 13:13:26
 * @FilePath: /DS/frontend/src/views/navigate/navigate.js
 */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useForm } from "react-hook-form";

import { useDispatch, useSelector } from "react-redux";
import CIcon from "@coreui/icons-react";
import SHAHE from "./../../assets/images/SHAHE.png";
import HAIDIAN from "./../../assets/images/HANDIAN.png";

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

const Navigate = () => {
    let REMOTE_URL = "http://127.0.0.1:5000/";
    const [info, setInfo] = useState();
    const [isOK, setOK] = useState(false);
    let data = {};
    useEffect(() => {
        axios
            .post(REMOTE_URL + "api/navigate/", data, {
                headers: { "Access-Control-Allow-Origin": "*" },
            })
            .then((data) => {
                console.log("return data");
                console.log(data.data.json);
                // returned as html
                setInfo(data.data);
                setOK(true);
            });
    }, []);

    console.log("Navigate set");
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
            departure: data.departure,
            destination: data.destination, 
            method: data.method
        }
        axios
            .post(REMOTE_URL + "api/navigate/", payload, {
                headers: { "Access-Control-Allow-Origin": "*" },
            })
            .then((data) => {
                console.log("return data");
                console.log(data.data);
                // returned as html
                setInfo(data.data["result"]);
                setOK(true);
            });
        // apis.getStudentInfo(data.username);
    };

    return (
        <div>
            <CCard>
                <CCardHeader>
                    <h1>寻路系统</h1>
                </CCardHeader>
                <CCardBody>
                    <CRow>
                        <CCol align="center">
                            <CImage src={SHAHE} width="90%"></CImage>
                        </CCol>
                        <CCol align="center">
                            <CImage src={HAIDIAN} width="75%"></CImage>
                        </CCol>
                    </CRow>
                    <CRow>
                        <CCol>
                            <br />
                            {/* <CImage src={SHAHE} width="90%"></CImage> */}
                            <CCardSubtitle align="center">
                                沙河简化地图
                            </CCardSubtitle>
                        </CCol>
                        <CCol>
                            <br />
                            <CCardSubtitle align="center">
                                海淀简化地图
                            </CCardSubtitle>
                        </CCol>
                    </CRow>
                    <CRow>
                        <CCol xs={6} center>
                            <CForm onSubmit={handleSubmit(onSubmit)}>
                                <p className="text-medium-emphasis"></p>
                                <CInputGroup className="mb-3">
                                    <CInputGroupText>
                                        <font size="3" heavy>
                                            起点
                                        </font>
                                    </CInputGroupText>
                                    <CFormInput
                                        {...register("departure")}
                                        type="text"
                                        placeholder="海淀北一教"
                                    />
                                </CInputGroup>
                                <CInputGroup className="mb-4">
                                    <CInputGroupText>
                                        <font size="3" heavy>
                                            终点
                                        </font>
                                    </CInputGroupText>
                                    <CFormInput
                                        {...register("destination")}
                                        type="text"
                                        placeholder="沙河学生活动中心"
                                    />
                                </CInputGroup>
                                <CInputGroup className="mb-4">
                                    <CInputGroupText>
                                        <font size="3" heavy>
                                            策略
                                        </font>
                                    </CInputGroupText>
                                    <CFormInput
                                        {...register("method")}
                                        type="text"
                                        placeholder="1， 2， 3"
                                    />
                                </CInputGroup>
                                <CRow>
                                    <CCol xs={6}>
                                        <CButton
                                            type="submit"
                                            color="primary"
                                            className="px-4"
                                        >
                                            查询
                                        </CButton>
                                    </CCol>
                                </CRow>
                            </CForm>
                        </CCol>
                        <CCol>
                            {isOK ? (
                                <CCard>
                                    <CCardHeader center>路径</CCardHeader>
                                    <CCardBody>{info}</CCardBody>
                                </CCard>
                            ) : (
                                <div></div>
                            )}
                        </CCol>
                    </CRow>
                </CCardBody>
            </CCard>
        </div>
    );
};

export default Navigate;
