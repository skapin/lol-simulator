<template>
  <div>
    <section id="champselector" class="hero is-info">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">First, Pick a Champion: </h1>
          <b-field>
            <b-autocomplete
              rounded
              v-model="name"
              :data="filteredDataArray"
              placeholder="Vayne"
              icon="magnify"
              :disabled="selected"
              @select="championSelectEvent">
              <template slot="empty">No results found</template>
            </b-autocomplete>
          </b-field>
          <div v-if="selected in championsDetailed" >
            <champion-simple-display/>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import server from '../api/server.vue'
import ChampionSimpleDisplay from '@/components/ChampionSimpleDisplay.vue'

export default {
  name: 'ChampionSelector',
  data () {
    return {
      champions: [],
      championsDetailed: {},
      name: '',
      selected: null
    }
  },
  methods: {
    goToNextStep: function () {
      console.log('next')
      this.$emit('to-step', 1)
    },
    championSelectEvent: function (option) {
      this.selected = option
      this.$store.commit('setChampionSelected', this.championsDetailed[this.selected])
      this.setProtectedTimeout(this.goToNextStep, 1000)
    },
    getChampions: function () {
      server.getChampions().then(result => {
        let champs = []
        /* eslint-disable-next-line */
        for (const [key, value] of Object.entries(result.data.champions)) {
          champs.push(key)
        }
        this.champions = champs
        this.championsDetailed = result.data.champions
      })
    }
  },
  computed: {
    filteredDataArray () {
      return this.champions.filter((option) => {
        return option
          .toString()
          .toLowerCase()
          .indexOf(this.name.toLowerCase()) >= 0
      })
    }
  },
  mounted: function () {
    this.getChampions()
  },
  components: {
    ChampionSimpleDisplay
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#champselector {
  padding: 1rem;
  min-height: calc(100vh - 20rem);
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
