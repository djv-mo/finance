import Vue from "vue";
import Vuex from "vuex";
import { getAPI } from "./axios-api";

Vue.use(Vuex);
export default new Vuex.Store({
  state: {
    accessToken: localStorage.getItem("accessToken") || null,
    refreshToken: localStorage.getItem("refreshToken") || null,
    APIData: "",
    username: localStorage.getItem("username"),
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
      localStorage.setItem("accessToken", access);
      localStorage.setItem("refreshToken", refresh);
    },
    destroyToken(state) {
      state.accessToken = null;
      state.refreshToken = null;
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
    },
    setUsername(state, username) {
      localStorage.setItem("username", username);
    },
  },
  getters: {
    loggedIn(state) {
      return state.accessToken !== null;
    },
  },
  actions: {
    userLogout(context) {
      if (context.getters.loggedIn) {
        context.commit("destroyToken");
      }
    },
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        getAPI
          .post("auth/jwt/create/", {
            username: usercredentials.username,
            password: usercredentials.password,
          })
          .then((response) => {
            context.commit("updateStorage", {
              access: response.data.access,
              refresh: response.data.refresh,
            });
            resolve();
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
    userRegister(context, usercredentials) {
      return new Promise((resolve, reject) => {
        getAPI
          .post("auth/users/", {
            username: usercredentials.username,
            email: usercredentials.email,
            password: usercredentials.password,
          })
          .then((response) => {
            resolve("Registration successful");
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
  },
});
