import axios from 'axios';

const BASE_URL = ' http://127.0.0.1:5000/employees';

export const signUp = async (user) => {
    try {
      const { data } = await axios.post(BASE_URL, user);
      console.log('DATA:', data, 'TOKEN:', data.token);
  
      return data;
    } catch (error) {
      console.log('error:', error);
    }
  };
  