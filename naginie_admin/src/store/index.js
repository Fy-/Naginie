import Vue from "vue";
import Vuex from "vuex";

import { isValidJwt, getUserFromJwt, EventBus } from "@/helpers/utils";
import { authenticate } from "@/api/user";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    sideBarOpen: false,
    user: getUserFromJwt(localStorage.getItem("token")),
    jwt: localStorage.getItem("token") || false
  },
  getters: {
    sideBarOpen: state => {
      return state.sideBarOpen;
    },
    isAuthenticated(state) {
      if (isValidJwt(state.jwt)) return true;
      localStorage.removeItem("token");
      return false;
    },
    user(state) {
      return state.user;
    }
  },
  mutations: {
    toggleSidebar(state) {
      state.sideBarOpen = !state.sideBarOpen;
    },
    setUserData(state, payload) {
      state.userData = payload.userData;
    },
    setJwtToken(state, payload) {
      localStorage.token = payload.jwt.token;
      state.jwt = payload.jwt.token;
    }
  },
  actions: {
    toggleSidebar(context) {
      context.commit("toggleSidebar");
    },
    login(context, userData) {
      context.commit("setUserData", { userData });
      return authenticate(userData)
        .then(response => {
          context.commit("setJwtToken", { jwt: response.data });
        })
        .catch(error => {
          EventBus.$emit("failedAuthentication", error);
        });
    },
    logout() {
      localStorage.removeItem("token");
    }
  }
});
