import axios from 'axios';

export const postUploadImage = async (file: FormData) => {
  return await axios.post('/api/v1/images', file).then((res) => res.data);
};
