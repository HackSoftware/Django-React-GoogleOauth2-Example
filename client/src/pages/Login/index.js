import React, { useCallback, useContext } from 'react';
import { useHistory } from 'react-router-dom';

import { GoogleLogin } from 'react-google-login';
import GoogleButton from 'react-google-button';

import { HOME_URL } from 'config/urls';
import { notifyError, notifySuccess } from 'utils/notifications';
import { UserContext, GithubStars, Layout } from 'components';

import { userInit } from './sdk';
import styles from './Login.module.css';

const Login = () => {
  const history = useHistory();
  const { setUser } = useContext(UserContext);

  const {
    REACT_APP_GOOGLE_CLIENT_ID,
    REACT_APP_BASE_BACKEND_URL
  } = process.env;

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

  const openGoogleLoginPage = () => {
    const googleAuthUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
    const redirectUri = 'api/v1/auth/login/google/';

    const scope = [
      'https://www.googleapis.com/auth/userinfo.email',
      'https://www.googleapis.com/auth/userinfo.profile'
    ].join(' ');

    const params = {
      response_type: 'code',
      client_id: REACT_APP_GOOGLE_CLIENT_ID,
      redirect_uri: `${REACT_APP_BASE_BACKEND_URL}/${redirectUri}`,
      prompt: 'select_account',
      scope
    };

    const urlParams = new URLSearchParams(params).toString();

    window.location = `${googleAuthUrl}?${urlParams}`;
  };

  return (
    <Layout className={styles.content}>
      <h1 className={styles.pageHeader}>Welcome to our Demo App!</h1>

      <h2 className={styles.btnHeader}>Try Backend flow:</h2>
      <GoogleButton
        onClick={openGoogleLoginPage}
        label="Sign in with Google"
        disabled={!REACT_APP_GOOGLE_CLIENT_ID}
      />

      <h2 className={styles.btnHeader}>Try Frontend flow:</h2>
      <GoogleLogin
        render={(renderProps) => <GoogleButton {...renderProps} />}
        clientId={REACT_APP_GOOGLE_CLIENT_ID}
        buttonText="Sign in with Google"
        onSuccess={onGoogleLoginSuccess}
        onFailure={notifyError}
        cookiePolicy={'single_host_origin'}
      />

      <GithubStars className={styles.githubStars} />
    </Layout>
  );
};

export default Login;
