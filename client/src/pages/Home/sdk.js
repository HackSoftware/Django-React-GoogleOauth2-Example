import { post } from 'utils/sdk';

export const logout = () => post('auth/logout/', {});
