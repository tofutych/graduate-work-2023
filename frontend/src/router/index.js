import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import FacultyView from "../views/FacultyView.vue";
import SignUpView from "../views/SignUpView";
import LogInView from "../views/LogInView";
import ProfileView from "../views/ProfileView";
import AddAchievementView from "../views/AddAchievementView";
import ApplicantView from "../views/ApplicantView";
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/:slug/",
    name: "faculty",
    component: FacultyView,
  },
  {
    path: "/log-in",
    name: "log in",
    component: LogInView,
  },
  {
    path: "/sign-up",
    name: "sign up",
    component: SignUpView,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/applicants/:id/",
    name: "applicant",
    component: ApplicantView,
  },

  {
    path: "/profile/add/achievement",
    name: "add achievement",
    component: AddAchievementView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
