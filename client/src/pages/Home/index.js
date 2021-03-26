import React, { useContext, useCallback } from 'react';
import { useHistory } from 'react-router-dom';

import { LOGIN_URL } from 'config/urls';
import { useUserRequired } from 'utils/hooks';
import { UserContext, GithubStars, Layout } from 'components';

import { logout } from './sdk';

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
    <Layout>
      <h1>Hello, {user.email}!</h1>
      <button onClick={handleLogout}>Logout</button>
      <GithubStars />
    </Layout>
  );
};

export default Home;
