<template>
  <div class="column is-half">
    <div class="box">
      <h3 class="is-size-4">{{ faculty.name }}</h3>

      <router-link
        v-bind:to="faculty.get_absolute_url"
        class="button is-info is-light mt-4"
        >View more</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "FacultyBox",
  props: {
    faculty: Object,
  },
};
</script>

<style scoped>
.box {
  border-radius: 10px 10px 0 0;
}
</style>
