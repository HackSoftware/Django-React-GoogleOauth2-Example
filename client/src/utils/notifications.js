import { toast } from 'react-toastify';

export const notifyError = (error, options) => {
  toast.error(error.toString(), options);
};

export const notifySuccess = (msg, options) => {
  toast.success(msg, options);
};
