import React, { useCallback } from 'react';
import { GoogleLogin } from 'react-google-login';

const Login = () => {
  const onGoogleLoginSuccess = useCallback((response) => {
    console.log(response);
  }, []);

  return (
    <div>
      <h1>Login</h1>

      <GoogleLogin
        clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
        buttonText='Login with Google'
        onSuccess={onGoogleLoginSuccess}
        onFailure={console.log}
        cookiePolicy={'single_host_origin'}
      />
    </div>
  );
};

export default Login;
