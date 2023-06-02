<template>
  <div class="columns is-multiline">
    <div class="column">
      <br />
      <div class="card">
        <div class="card-content">
          <div class="media">
            <div class="media-left">
              <figure>
                <i class="fa-sharp fa-solid fa-graduation-cap"></i>
              </figure>
            </div>
            <div class="media-content">
              <p class="title is-2">{{ user.surname }}</p>
              <p class="title is-2">{{ user.name }}</p>
              <p class="title is-2">{{ user.patronymic }}</p>
              <p class="fa fa-calendar">&nbsp; {{ user.date_of_birth }}</p>
              <p class="title is-4">{{ faculty_name }} {{ url }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="column">
      <br />
      <div class="card">
        <div class="card-content">
          <div class="media">
            <p class="title is-4">certificate: &nbsp;</p>
            <figure class="image is-64x64">
              <img v-bind:src="certificate" alt="Image" />
            </figure>
          </div>
          <div class="media">
            <p class="title is-4">special_rights: &nbsp;</p>
            <figure class="image is-64x64">
              <img v-bind:src="special_rights" alt="Image" />
            </figure>
          </div>
          <div class="media">
            <p class="title is-4">disability: &nbsp;</p>
            <figure class="image is-64x64">
              <img v-bind:src="disability" alt="Image" />
            </figure>
          </div>
        </div>
      </div>
    </div>
  </div>
  <h1 class="title">Achievements</h1>

  <AchievementBox
    v-for="achievement in achievements"
    v-bind:key="achievement.id"
    v-bind:achievement="achievement"
  ></AchievementBox>

  <div class="box">
    <article class="media-content">
      <div class="content">
        <figure>
          <router-link to="/profile/add/achievement"><button class="button is-info is-centered"><i class="fa-solid fa-plus has-text-"></i></button></router-link>
        </figure>
        </div>
    </article>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import AchievementBox from "@/components/AchievementBox.vue";

export default {
  name: "ProfileView",
  data() {
    return {
      user: {},
      certificate: "",
      special_rights: "",
      disability: "",
      achievements: [],
      path: "",
      faculty_name: "",
      achievements_url: "",
    };
  },
  components: {
    AchievementBox,
  },

  mounted() {
    this.token = this.$store.state.token;
    this.getUserSummary();
  },
  methods: {
    async getUserSummary() {
      await axios
        .post(`/api/applicants/`, { token: this.token })
        .then((response) => {
          this.user = response.data;
          document.title = "Profile";
          this.certificate = this.user.get_images[0];
          this.special_rights = this.user.get_images[1];
          this.disability = this.user.get_images[2];
          this.achievements = this.user.achievements;
          this.achievements_url = `/api/${this.user.get_absolute_url}achievements/`
          localStorage.removeItem("id")
          localStorage.removeItem("faculty")
          this.$store.commit('setId', this.user.id)
          this.$store.commit('setFaculty', this.user.faculty)
          this.$store.commit('setStaff', this.user.is_staff)
          
          const splitted = this.user.get_absolute_url.split("/");
          this.path = `/api/faculties/${splitted[1]}/`;
          axios.get(this.path).then((response) => {
            this.faculty_name = response.data.name;
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
img {
  border-radius: 10px;
}
</style>
