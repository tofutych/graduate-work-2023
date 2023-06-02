<template>
  <div class="column is-3">
    <div class="box">
      <h3 class="is-size-4">
        {{ applicant.surname }} {{ applicant.name }} {{ applicant.patronymic }}
      </h3>
      <p class="is-size-6 has-text-grey">{{ applicant.date_of_birth }}</p>
      <router-link v-bind:to="this.url" class="button is-info is-light mt-4"
        >View details</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "EnrolleeBox",
  props: {
    applicant: Object,
  },
  data() {
    return {
      url: this.applicant.get_absolute_url.slice(-14),
    };
  },
};
</script>

<style scoped>
.box {
  border-radius: 10px 10px 0 0;
}
</style>
