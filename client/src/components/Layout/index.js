import React from 'react';
import classnames from 'classnames';

import hackSoftLogo from './assets/hacksoft-logo.svg';

import styles from './Layout.module.css';

const Layout = ({ children, className }) => (
  <div className={styles.pageWrapper}>
    <div className={styles.border}>
      <div className={classnames(styles.content, className)}>{children}</div>
    </div>

    <a
      className={styles.logo}
      href="https://www.hacksoft.io/"
      target="_blank"
      rel="noreferrer noopener">
      powered by <img src={hackSoftLogo} alt="HackSoft Logo" />
    </a>
  </div>
);

export default Layout;
