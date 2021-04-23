import { post } from 'utils/sdk';

export const validateTokenAndObtainSession = ({ data, idToken }) => {
  const headers = {
    Authorization: idToken,
    'Content-Type': 'application/json'
  };

  return post('users/init/', data, { headers });
};
