<template>
  <section>
    <div v-if="champion" class="hero-body">
      <div class="container">
        <h1 class="title">
          {{ champion['name'] }}
        </h1>
        <h2 class="subtitle">
          {{ champion['title'] }}
        </h2>
        <div id="summoner-picture">
          <img id="border" src="../assets/champ-border.png" alt="border" height="200">
          <img id="champion-picto" :src="champion['image_url']" :alt="champion['name']">
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ChampionSimpleDisplay',
  props: [],
  data () {
    return {
      champion: this.$store.state.championSelected
    }
  },
  methods: {
    getChampions: function () {

    }
  },
  mounted: function () {
  }
}
</script>

<style scoped>
#summoner-picture {
  margin-top: 10vh;
  position: relative;
}
#summoner-picture #champion-picto{
  position: absolute;
  z-index: 1;
  border-radius: 50%;
}
#summoner-picture #border{
  position: absolute;
  z-index: 11;
  height: 200px;
}
#summoner-picture img {
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
</style>
