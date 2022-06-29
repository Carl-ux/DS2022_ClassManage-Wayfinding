/*
 * @Date: 2022-06-14 01:31:23
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-14 16:25:44
 * @FilePath: /DS/frontend/src/apis.js
 */

import axios from "axios";
import React, { Component } from "react";

export default class apis {
    static getStudentInfo = (username) => {
        let REMOTE_URL = "http://127.0.0.1:5000/";
        let data = {
            "username": username,
        };
        let res;
        console.log("posting to" + REMOTE_URL + "api/student/" + data);
        axios.post(REMOTE_URL + "api/student/", data, {headers:{"Access-Control-Allow-Origin":"*"}}).then((data) => {
            console.log("return data");
            console.log(data)
            
        });
    };
}
