<template>
  <div class="columns is-multiline">
    <div class="column is-12">
      <h1 class="title is-1 has-text-centered">Applicants</h1>
    </div>

    <EnrolleeBox
      v-for="applicant in applicants"
      v-bind:key="applicant.id"
      v-bind:applicant="applicant"
    >
    </EnrolleeBox>
  </div>
</template>

<script>
import axios from "axios";
import EnrolleeBox from "@/components/EnrolleeBox.vue";

export default {
  name: "FacultyView",
  components: {
    EnrolleeBox,
  },
  data() {
    return {
      applicants: [],
    };
  },
  mounted() {
    this.getApplicants();
  },
  methods: {
    async getApplicants() {
      const slug = this.$route.params.slug;
      await axios
        .get(`/api/faculties/${slug}/applicants`)
        .then((response) => {
          this.applicants = response.data;
          console.log(this.applicants);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
