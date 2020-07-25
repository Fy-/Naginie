import axios from "axios";

const API_URL = "http://0.0.0.0:8888/api";

export function authenticate(userData) {
	return axios.post(`${API_URL}/login/`, userData);
}

export function test() {
	return axios.get(`${API_URL}/users/`, {
		headers: { Authorization: `Bearer: ${localStorage.getItem("token")}` },
	});
}
