import React, { useContext, useCallback } from 'react';
import { useHistory } from 'react-router-dom';

import { LOGIN_URL } from 'config/urls';
import { useUserRequired } from 'utils/hooks';
import { UserContext, GithubStars, Layout } from 'components';

import { logout } from './sdk';
import styles from './Home.module.css';

const Home = () => {
  useUserRequired();
  const history = useHistory();
  const { user, setUser } = useContext(UserContext);

  const handleLogout = useCallback(() => {
    logout().then(() => {
      setUser(null);
      history.push(LOGIN_URL);
    });
  }, [setUser, history]);

  if (!user) {
    return null;
  }

  return (
    <Layout className={styles.content}>
      <h2 className={styles.welcome}>Welcome!</h2>
      <h1 className={styles.userEmail}>{user.email}!</h1>
      <button className={styles.logoutBtn} onClick={handleLogout}>
        LOGOUT
      </button>
      <GithubStars className={styles.githubStars} />
    </Layout>
  );
};

export default Home;
