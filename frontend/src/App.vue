<template>
  <div class="wrapper">
    <nav class="navbar is-info">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>KubSU</strong>
          <img src="@/assets/logo.png" alt="KubSU" />
        </router-link>

        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-start">
          <router-link to="/about" class="navbar-item">About</router-link>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons is-centered">
              <template v-if="$store.state.isAuthenticated">
                <router-link
                  to="/profile"
                  class="button is-transparent is-justify-content-flex-start"
                >
                  <span class="icon"><i class="fas fa-user"></i></span>
                  <span>Profile</span>
                  <span></span>
                </router-link>
                <div
                  class="button is-transparent is-justify-content-flex-start"
                  @click="logout"
                >
                  <span class="icon"
                    ><i class="fas fa-right-from-bracket"></i
                  ></span>
                  <span>Logout</span>
                  <span></span>
                </div>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light"
                  >Log in</router-link
                >
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
  <router-view />
  <footer class="footer has-background-white-bis">
    <div class="content has-text-centered">
      <p>2023</p>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },

  beforeCreate() {
    this.$store.commit("initializeStore");
  },

  mounted() {
    document.title = "KubSU";
  },
  methods: {
    logout() {
      this.$store.commit("removeToken");
      this.$store.commit("removeStaff");
      this.$router.push("/");
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
