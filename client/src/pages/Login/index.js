import React, { useCallback, useContext } from 'react';
import { GoogleLogin } from 'react-google-login';
import { useHistory } from 'react-router-dom';

import { HOME_URL } from 'config/urls';
import { notifyError, notifySuccess } from 'utils/notifications';
import { UserContext, GithubStars } from 'components';

import { userInit } from './sdk';

const Login = () => {
  const history = useHistory();
  const { setUser } = useContext(UserContext);

  const handleUserInit = useCallback(
    resp => {
      if (resp.status === 201) {
        notifySuccess(
          'We successfully created your account in our database. You can now login to the app.'
        );
      } else {
        setUser(resp.data);
        history.push(HOME_URL);
      }
    },
    [history, setUser]
  );

  const onGoogleLoginSuccess = useCallback(
    response => {
      const profileData = {
        email: response.profileObj.email,
        first_name: response.profileObj.givenName,
        last_name: response.profileObj.familyName
      };

      userInit(profileData)
        .then(handleUserInit)
        .catch(notifyError);
    },
    [handleUserInit]
  );

  return (
    <div>
      <h1>Login</h1>

      <GoogleLogin
        clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
        buttonText="Login with Google"
        onSuccess={onGoogleLoginSuccess}
        onFailure={console.log}
        cookiePolicy={'single_host_origin'}
      />

      <GithubStars />
    </div>
  );
};

export default Login;
