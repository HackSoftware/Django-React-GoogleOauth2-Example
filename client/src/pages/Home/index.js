import React, { useContext } from 'react';

import { useUserRequired } from 'utils/hooks';
import { UserContext } from 'components';

const Home = () => {
  useUserRequired();

  const { user } = useContext(UserContext);

  if (!user) {
    return null;
  }

  return <h1>Hello, {user.email}!</h1>;
};

export default Home;
