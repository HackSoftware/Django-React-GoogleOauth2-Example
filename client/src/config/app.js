import React, { useState } from 'react';

import { UserContext } from 'components';
import Routes from 'config/routes';

function App() {
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <Routes />
    </UserContext.Provider>
  );
}

export default App;
