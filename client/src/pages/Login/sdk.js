import { post } from 'utils/sdk';

export const userInit = (data) => post('users/init/', data);
