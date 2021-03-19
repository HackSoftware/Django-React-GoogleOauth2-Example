import React from 'react';

import { useUserRequired } from 'utils/hooks';

const Home = () => {
  useUserRequired();

  return <h1>Home</h1>;
};

export default Home;
