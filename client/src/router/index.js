import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Dashboard from "@/views/dashboard";
import Search from "@/views/search";
import Projects from "@/views/projects";
import Project from "@/views/project";

import { authGuard, notAuthenticated } from "../auth/authGuard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    beforeEnter: notAuthenticated,
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
    path: "/projects/:id",
    name: "Project/:id",
    component: Project,
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
