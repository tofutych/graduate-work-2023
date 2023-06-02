<template>
  <div class="home">
    <section class="hero is-small is-info mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">KubSU</p>
        <p class="subtitle">
          Вуз классического университетского образования, в котором гармонично
          сочетаются естественно-научные и гуманитарные направления. Благодаря
          успехам и достижениям в образовании, научно-исследовательской и
          воспитательной деятельности КубГУ по праву считается одним из ведущих
          вузов юга России.
        </p>
      </div>
    </section>

    <template v-if="$store.state.is_staff">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Faculties</h2>
        </div>

        <FacultyBox
          v-for="faculty in faculties"
          v-bind:key="faculty.id"
          v-bind:faculty="faculty"
        ></FacultyBox>
      </div>
    </template>
  </div>
</template>

<script>
import axios from "axios";
import FacultyBox from "@/components/FacultyBox.vue";

export default {
  name: "HomeView",

  data() {
    return {
      faculties: [],
    };
  },
  components: {
    FacultyBox,
  },

  mounted() {
    this.getFaculties();
    document.title = "KubSU";
  },

  methods: {
    getFaculties() {
      axios
        .get("/api/faculties/")
        .then((response) => {
          this.faculties = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
