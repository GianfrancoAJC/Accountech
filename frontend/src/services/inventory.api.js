import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/inventory";

export const initinventory = async () => {
    const { data } = await axios.post(BASE_URL);
  
    return data;
  }

export const updateinventory = async (payload) => {
    const { data } = await axios.patch(BASE_URL, payload);
  
    return data;
  }

export const getinventory = async () => {
    const { data } = await axios.get(BASE_URL);
  
    return data;
  }

export const deleteinventory = async (payload) => {
    const { data } = await axios.post(BASE_URL + "d", payload);
  
    return data;
  }