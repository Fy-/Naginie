import Vue from "vue";
import VueRouter from "vue-router";
import Home from '../pages/Home'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
];

const router = new VueRouter({
  mode: "history",
  base: '/admin/',
  routes
});

export default router;
