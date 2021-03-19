import { useContext, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

import { LOGIN_URL } from 'config/urls';
import { notifyError } from 'utils/notifications';
import { UserContext } from 'components';

export const useUserRequired = () => {
  const history = useHistory();
  const { user } = useContext(UserContext);

  useEffect(() => {
    if (!user) {
      notifyError('You have to login first.');
      history.push(LOGIN_URL);
    }
  }, [user, history]);
};
