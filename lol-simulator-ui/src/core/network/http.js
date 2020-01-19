import axios from 'axios'

export const http = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  // baseURL: window.localStorage.getItem('backend_url') !== undefined ? window.localStorage.getItem('backend_url') : process.env.API_URL,
  // baseURL: `http://127.0.0.1:9006/`,
  timeout: 3000,
  headers: {
    // Authorization: 'Bearer {token}'
  }
})
