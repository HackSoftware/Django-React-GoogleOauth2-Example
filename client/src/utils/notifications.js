import { toast } from 'react-toastify';

export const notifyError = (error, options) => {
  toast.error(error, options);
};
