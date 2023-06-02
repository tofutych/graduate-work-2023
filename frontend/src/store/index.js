import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
    id: null,
    faculty: null,
    is_staff: false,
  },
  getters: {},

  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },

    setId(state, id) {
      state.id = id;
    },

    setFaculty(state, faculty) {
      state.faculty = faculty;
    },

    setStaff(state, is_staff) {
      state.is_staff = is_staff;
    },

    removeStaff(state) {
      state.is_staff = false;
    },

    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },

    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
