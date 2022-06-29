import React from 'react'
import CIcon from '@coreui/icons-react'
import {
  cilBell,
  cilCalculator,
  cilChartPie,
  cilCursor,
  cilDrop,
  cilNotes,
  cilPencil,
  cilPuzzle,
  cilSpeedometer,
  cilStar,
} from '@coreui/icons'
import { CNavGroup, CNavItem, CNavTitle } from '@coreui/react'

const _nav = [
    {
        component: CNavItem,
        name: "总览",
        to: "/dashboard",
        icon: <CIcon icon={cilSpeedometer} customClassName="nav-icon" />,

    },
    {
        component: CNavTitle,
        name: "课程",
    },
    {
        component: CNavItem,
        name: "课表",
        to: "/dashboard",
        icon: <CIcon icon={cilPencil} customClassName="nav-icon" />,
    },
    {
        component: CNavItem,
        name: "寻路",
        to: "/navigate",
        icon: <CIcon icon={cilCursor} customClassName="nav-icon" />,
        badge: {
            color: "info",
            text: "NEW",
        },
    },
    {
        component: CNavTitle,
        name: "设置",
    },
    {
        component: CNavItem,
        name: "学生信息",
        to: "/profile",
        icon: <CIcon icon={cilPuzzle} customClassName="nav-icon" />,
    },
    // {
    //     component: CNavGroup,
    //     name: "学生信息",
    //     to: "/profile",
    //     icon: <CIcon icon={cilPuzzle} customClassName="nav-icon" />,
    //     items: [
    //         {
    //             component: CNavItem,
    //             name: "Accordion",
    //             to: "/base/accordion",
    //         },
    //         {
    //             component: CNavItem,
    //             name: "Progress",
    //             to: "/base/progress",
    //         },
    //     ],
    // },
    {
        component: CNavItem,
        name: "课程信息",
        to: "/classes",
        icon: <CIcon icon={cilChartPie} customClassName="nav-icon" />,
    },
    {
        component: CNavItem,
        name: "提醒事项",
        to: "/alarm",
        icon: <CIcon icon={cilBell} customClassName="nav-icon" />,
    },
    {
        component: CNavItem,
        name: "成绩",
        to: "/#",
        icon: <CIcon icon={cilCalculator} customClassName="nav-icon" />,
        badge: {
            color: "info",
            text: "COMING SOON",
        },
    },
    {
        component: CNavTitle,
        name: "附页",
    },
    {
        component: CNavGroup,
        name: "页面展示",
        icon: <CIcon icon={cilStar} customClassName="nav-icon" />,
        items: [
            {
                component: CNavItem,
                name: "登陆",
                to: "/login",
            },
            {
                component: CNavItem,
                name: "注册",
                to: "/register",
            },
            {
                component: CNavItem,
                name: "Error 404",
                to: "/404",
            },
            {
                component: CNavItem,
                name: "Error 500",
                to: "/500",
            },
        ],
    },
];

export default _nav
