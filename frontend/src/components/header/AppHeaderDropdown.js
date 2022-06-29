/*
 * @Date: 2022-04-10 19:05:17
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-14 01:25:01
 * @FilePath: /DS/frontend/src/components/header/AppHeaderDropdown.js
 */
import React from 'react'
import {
  CAvatar,
  CBadge,
  CDropdown,
  CDropdownDivider,
  CDropdownHeader,
  CDropdownItem,
  CDropdownMenu,
  CDropdownToggle,
} from '@coreui/react'
import {
  cilBell,
  cilCreditCard,
  cilCommentSquare,
  cilEnvelopeOpen,
  cilFile,
  cilLockLocked,
  cilSettings,
  cilTask,
  cilUser,
} from '@coreui/icons'
import CIcon from '@coreui/icons-react'

import avatar8 from './../../assets/images/avatars/8.jpg'
import { useDispatch, useSelector } from 'react-redux'

const AppHeaderDropdown = () => {
  const dispatch = useDispatch()
  const isLogged = useSelector((state)=> state.isLogged)

  return (
      <>
          {isLogged?loggedDropdown():<a href='/#/login'><font size='2' color='grey'>登陆</font></a>}
      </>
  );

  function loggedDropdown() {
    return <CDropdown variant="nav-item">
      <CDropdownToggle
        placement="bottom-end"
        className="py-0"
        caret={false}
      >
        {/* {isLogged ? (
    <CAvatar src={avatar8} size="md" />
) : (
    <font size="1" color="grey">
        登陆
    </font>
)} */}
        <CAvatar src={avatar8} size="md" />
      </CDropdownToggle>
      <CDropdownMenu className="pt-0" placement="bottom-end">
        <CDropdownHeader className="bg-light fw-semibold py-2">
          个人
        </CDropdownHeader>
        <CDropdownItem href="#">
          <CIcon icon={cilBell} className="me-2" />
          提醒
          <CBadge color="info" className="ms-2">
            114
          </CBadge>
        </CDropdownItem>
        {/* <CDropdownItem href="#">
<CIcon icon={cilEnvelopeOpen} className="me-2" />
Messages
<CBadge color="success" className="ms-2">
42
</CBadge>
</CDropdownItem> */}
        {/* <CDropdownItem href="#">
<CIcon icon={cilTask} className="me-2" />
Tasks
<CBadge color="danger" className="ms-2">
42
</CBadge>
</CDropdownItem> */}
        <CDropdownItem href="#">
          <CIcon icon={cilCommentSquare} className="me-2" />
          评论
          <CBadge color="warning" className="ms-2">
            514
          </CBadge>
        </CDropdownItem>
        <CDropdownHeader className="bg-light fw-semibold py-2">
          设置
        </CDropdownHeader>
        <CDropdownItem href="/#/profile">
          <CIcon icon={cilUser} className="me-2" />
          个人资料
        </CDropdownItem>
        <CDropdownItem href="#">
          <CIcon icon={cilSettings} className="me-2" />
          系统设置
        </CDropdownItem>
        {/* <CDropdownItem href="#">
<CIcon icon={cilCreditCard} className="me-2" />
Payments
<CBadge color="secondary" className="ms-2">
42
</CBadge>
</CDropdownItem> */}
        <CDropdownItem href="#">
          <CIcon icon={cilFile} className="me-2" />
          课程设置
          <CBadge color="primary" className="ms-2">
            42
          </CBadge>
        </CDropdownItem>
        <CDropdownDivider />
        <CDropdownItem href='/#/login/' onClick={()=>{dispatch({type: 'set', isLogged: false})}}>
          <CIcon icon={cilLockLocked} className="me-2" />
          安全退出
        </CDropdownItem>
      </CDropdownMenu>
    </CDropdown>
  }
}

export default AppHeaderDropdown
