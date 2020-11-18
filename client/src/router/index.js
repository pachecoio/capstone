import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Dashboard from "@/views/dashboard";
import Search from "@/views/search";
import Projects from "@/views/projects";

import { authGuard } from "../auth/authGuard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    beforeEnter: authGuard,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    beforeEnter: authGuard,
  },
  {
    path: "/projects",
    name: "Projects",
    component: Projects,
    beforeEnter: authGuard,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
    beforeEnter: authGuard,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
