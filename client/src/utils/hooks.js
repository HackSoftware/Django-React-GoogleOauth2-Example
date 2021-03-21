import { useContext, useEffect } from 'react';

import { get } from 'utils/sdk';
import { UserContext } from 'components';

const getMe = () => get('users/me');

export const useUserRequired = () => {
  const { user, setUser } = useContext(UserContext);

  useEffect(() => {
    if (!user) {
      getMe().then(resp => setUser(resp.data));
    }
  }, [user, setUser]);
};
