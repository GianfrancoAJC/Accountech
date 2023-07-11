import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/";

export const showpurchases = async () => {
    const { data } = await axios.get(BASE_URL + "purchase");
  
    return data;
  }

export const showsales = async () => {
    const { data } = await axios.get(BASE_URL + "sale");
  
    return data;
  }

export const showeerr = async () => {
    const { data } = await axios.get(BASE_URL + "eerr");
  
    return data;
  }

export const showmcp = async () => {
    const { data } = await axios.get(BASE_URL + "mcp");
  
    return data;
  }