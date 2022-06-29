/*
 * @Date: 2022-06-14 01:26:25
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-15 13:02:51
 * @FilePath: /DS/frontend/src/views/profile/Profile.js
 */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import CIcon from "@coreui/icons-react";

import {
    CCol,
    CCard,
    CCardBody,
    CSpinner,
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
    cilUser,
    cilUserFemale,
} from "@coreui/icons";

const Profile = () => {
    let REMOTE_URL = "http://127.0.0.1:5000/";
    const [info, setInfo] = useState();
    const [isOK, setOK] = useState(false);

    const dispatch = useDispatch();
    const username = useSelector((data) => data.username);
    let data = {
    };

    useEffect(() => {
        axios
            .post(REMOTE_URL + "api/student/", data, {
                headers: { "Access-Control-Allow-Origin": "*" },
            })
            .then((data) => {
                console.log("return data");
                console.log(data.data);
                // returned as html
                setInfo(JSON.parse(data.data));
                console.log(info)
                setOK(true);
            });
    }, []);

    console.log("profile set");
    console.log(info);

    const students = [
        {
            StudentNumber: "2020211554",
            Gender: "M",
            Name: "Carl",
            Event: [202201, 202207, 202251],
        },
        {
            StudentNumber: "2020211555",
            Gender: "M",
            Name: "Azus",
            Event: "",
        },
        {
            StudentNumber: "2020211552",
            Gender: "M",
            Name: "Bai",
            Event: "",
        },
    ];
    // return( <div>username: {info.json}</div>)

    // if (false == isOK) {
    //     return (
    //         <>
    //             <CSpinner color="primary" />
    //         </>
    //     );
    // }

    return (
        <div>
            <CTable align="middle" className="mb-0 border" hover responsive>
                <CTableHead color="light">
                    <CTableRow>
                        <CTableHeaderCell className="text-center">
                            <CIcon icon={cilPeople} />
                        </CTableHeaderCell>
                        <CTableHeaderCell>User</CTableHeaderCell>
                        <CTableHeaderCell className="text-center">
                            StudentNumber
                        </CTableHeaderCell>
                        <CTableHeaderCell className="text-center">
                            Gender
                        </CTableHeaderCell>

                        <CTableHeaderCell>Event List</CTableHeaderCell>
                    </CTableRow>
                </CTableHead>
                <CTableBody>
                    
                    {isOK?
                        info.map((item, index) => (
                        <CTableRow v-for="item in tableItems" key={index}>
                            <CTableDataCell></CTableDataCell>

                            <CTableDataCell>
                                <div>{item.Name}</div>
                            </CTableDataCell>
                            <CTableDataCell className="text-center">
                                <div>{item.StudentNumber}</div>
                            </CTableDataCell>
                            <CTableDataCell>
                                <strong>{item.Gender}</strong>
                            </CTableDataCell>
                            <CTableDataCell>
                                <div className="small text-medium-emphasis">
                                    Event number
                                </div>
                                <strong>{item.Event.toString()} </strong>
                            </CTableDataCell>
                        </CTableRow>
                    ))
                :<CSpinner color="primary" />
                }
                </CTableBody>
            </CTable>
        </div>
    );
};

export default Profile;
