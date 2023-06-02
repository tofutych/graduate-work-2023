<template>
  <div class="box">
    <article class="media">
      <div class="media-left">
        <figure class="image is-128x128">
          <a v-bind:href="achievement.get_image"
            ><img v-bind:src="achievement.get_image" alt="Image"
          /></a>
        </figure>
      </div>
      <div class="media-content">
        <div class="content">
          <p>
            <strong>{{ achievement.title }}</strong>
            <br />
            <small>{{ achievement.date }}</small>
            <br />
            {{ achievement.description }}
          </p>
        </div>
        <nav class="level is-mobile">
          <div class="level-left">
            <a class="level-item" aria-label="reply">
              <span class="icon is-small">
                <a
                  v-bind:href="achievement.url"
                  class="fas fa-link"
                  aria-hidden="true"
                ></a>
              </span>
            </a>
            <div
              class="button is-danger is-light is-justify-content-flex-start"
              @click="deleteAchievement()"
            >
              <span class="icon"><i class="fas fa-trash"></i></span>
              <span>Delete</span>
              <span></span>
            </div>
          </div>
        </nav>
      </div>
    </article>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AchievementBox",
  props: {
    achievement: Object,
  },
  methods: {
    async deleteAchievement() {
      const id = this.achievement.id;
      await axios
        .delete(`/api/achievements/${id}/`)
        .then((response) => {
          this.$router.go("/profile");
          toast({
            message: "Достижение удалено!!",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        })
        .catch((error) => {
          console.log(JSON.stringify(error));
        });
    },
  },
};
</script>

<style scoped></style>
