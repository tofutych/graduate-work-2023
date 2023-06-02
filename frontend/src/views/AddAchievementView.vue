<template>
  <h1 class="title has-text-centered">Add new achievement</h1>
  <div class="columns">
    <div class="column is-4 is-offset-4">
      <br />
      <form @submit.prevent="submitForm">
        <div class="field">
          <label>Title</label>
          <div class="control">
            <input type="text" class="input" v-model="title" />
          </div>
        </div>

        <div class="field">
          <label>Description</label>
          <div class="control">
            <input type="text" class="input" v-model="description" />
          </div>
        </div>

        <div class="field">
          <label>Date</label>
          <div class="control">
            <input type="text" class="input" v-model="date" />
          </div>
        </div>

        <div class="field">
          <label>Url</label>
          <div class="control">
            <input type="text" class="input" v-model="url" />
          </div>
        </div>

        <div class="file">
          <label class="file-label">
            <input class="file-input" type="file" name="image" />
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label"> Choose a file… </span>
            </span>
          </label>
        </div>

        <div class="field">
          <div class="control has-text-centered">
            <button class="button is-info">Submit</button>
          </div>
        </div>
        <hr />
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "AddAchievementView",
  data() {
    return {
      title: "",
      description: "",
      date: "",
      url: "",
      image: "",
    };
  },
  methods: {
    async submitForm() {
      const formData = {
        enrollee: this.$store.state.id,
        title: this.title,
        description: this.description,
        date: this.date,
        url: this.url,
      };

      await axios
        .post(
          `/api/faculties/${this.$store.state.faculty}/applicants/${this.$store.state.id}/achievements/`,
          formData
        )
        .then((response) => {
          toast({
            message: "Данные были успешно добавлены!",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        })
        .catch((error) => {
          toast({
            message: "Error!",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });
    },
  },
};
</script>
