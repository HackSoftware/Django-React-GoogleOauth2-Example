import React from 'react';

import styles from './Layout.module.css';

const Layout = ({ children }) => (
  <div className={styles.pageWrapper}>
    <div className={styles.orangeBar} />
    <div className={styles.content}>{children}</div>
    <div className={styles.orangeBar} />
  </div>
);

export default Layout;
