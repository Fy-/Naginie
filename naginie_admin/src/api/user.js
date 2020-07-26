import axios from "axios";

const API_URL = "http://0.0.0.0:8888/api";

export function authenticate(userData) {
  return axios.post(`${API_URL}/login/`, userData);
}

export function getUsers(page = 1) {
  return axios.get(`${API_URL}/users/?page=${page}`, {
    headers: { Authorization: `Bearer: ${localStorage.getItem("token")}` }
  });
}

export function searchUser(page = 1, term='') {
  return axios.get(`${API_URL}/users/search/?page=${page}&term=${term}`, {
    headers: { Authorization: `Bearer: ${localStorage.getItem("token")}` }
  });
}

export function profileUser(id) {
  return axios.get(`${API_URL}/users/${id}`, {
    headers: { Authorization: `Bearer: ${localStorage.getItem("token")}` }
  });
}