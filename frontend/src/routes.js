/*
 * @Date: 2022-04-10 19:05:17
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-15 13:06:09
 * @FilePath: /DS/frontend/src/routes.js
 */
import React from 'react'

const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'))
const Profile = React.lazy(() => import('./views/profile/Profile'))
const Navigate = React.lazy(() => import('./views/navigate/Navigate'))
const Classes = React.lazy(() => import('./views/classes/Classes'))



const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/dashboard', name: 'Dashboard', element: Dashboard },
  { path: '/profile', name: 'Profile', element: Profile },
  { path: '/navigate', name: 'Navigate', element: Navigate },
  { path: '/classes', name: 'Classes', element: Classes },
]

export default routes
