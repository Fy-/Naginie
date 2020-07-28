import axios from "axios";

const API_URL = "http://0.0.0.0:8888/api";

export function getDirectories() {
  return axios.get(`${API_URL}/directories/list`, {
    headers: { Authorization: `Bearer: ${localStorage.getItem("token")}` }
  });
}
