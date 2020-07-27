import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Users from "../views/Users.vue";
import User from "../views/User.vue";
import Roles from "../views/Roles.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/users/",
    name: "Users",
    component: Users,
  },
  {
    path: "/users/:id",
    name: "User",
    component: User,
  },
  {
    path: "/roles/",
    name: "Roles",
    component: Roles,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
