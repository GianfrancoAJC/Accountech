import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/employee";

export const createemployee = async (payload) => {
    const { data } = await axios.post(BASE_URL + "s", payload);
  
    return data;
  };
  
export const getemployee = async (payload) => {
    const { data } = await axios.post(BASE_URL, payload);
  
    return data;
  };
  