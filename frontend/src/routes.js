import Vue from "vue";
import VueRouter from "vue-router";
import Savings from "./views/Index";
import Login from "./views/Login";
import Logout from "./views/Logout";
import Register from "./views/Register";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "savings",
      component: Savings,
      meta: {
        requiresLogin: true,
      },
    },
    {
      path: "/login",
      name: "login",
      component: Login,
    },
    {
      path: "/logout",
      name: "logout",
      component: Logout,
    },
    {
      path: "/register",
      name: "register",
      component: Register,
    },
  ],
});
