/*
 * @Date: 2022-04-10 19:05:17
 * @LastEditors: Azus
 * @LastEditTime: 2022-06-09 20:57:46
 * @FilePath: /coreui-free-react-admin-template/jest.config.js
 */
/**
 * Copyright (c) 2013-present, creativeLabs Lukasz Holeczek.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// 'use strict'

module.exports = {
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!**/*index.js',
    '!src/serviceWorker.js',
    '!src/polyfill.js',
  ],
}
