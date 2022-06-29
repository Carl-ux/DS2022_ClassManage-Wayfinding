/*
 * @Date: 2022-04-10 19:05:17
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-12 17:32:51
 * @FilePath: /coreui-free-react-admin-template/src/components/AppContent.js
 */
import React, { Suspense } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import {
    CCard,
    CCardHeader,
    CCardText,
    CContainer,
    CSpinner,
} from "@coreui/react";

// routes config
import routes from "../routes";
import { useDispatch, useSelector } from "react-redux";

const AppContent = () => {
    const unLoggedinContent = () => {
        return (
            <CCard align="center">
                <CCardHeader>需要登陆</CCardHeader>
                <CCardText>
                    需要<a href="/#/login">登陆</a>才能访问功能。
                </CCardText>
            </CCard>
        );
    };

    const dispatch = useDispatch();
    const isLogged = useSelector((state) => state.isLogged);
    const defaultContent = () => {
        return (
            <CContainer lg>
                <Suspense fallback={<CSpinner color="primary" />}>
                    <Routes>
                        {routes.map((route, idx) => {
                            return (
                                route.element && (
                                    <Route
                                        key={idx}
                                        path={route.path}
                                        exact={route.exact}
                                        name={route.name}
                                        element={<route.element />}
                                    />
                                )
                            );
                        })}
                        <Route
                            path="/"
                            element={<Navigate to="dashboard" replace />}
                        />
                    </Routes>
                </Suspense>
            </CContainer>
        );
    };
    return (
      <>
      {isLogged?defaultContent():unLoggedinContent()}
      </>
    )
};

export default React.memo(AppContent);
