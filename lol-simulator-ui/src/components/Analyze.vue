<template>
  <div>
    <section id="analyze" class="hero is-info">
      <div class="hero-body">
      </div>
    </section>
  </div>
</template>

<script>

// import server from '../api/server.vue'
import { mapState } from 'vuex'

export default {
  name: 'Analyze',
  data () {
    return {
    }
  },
  computed: mapState(['itemsSelected', 'championSelected']),
  methods: {
    goToNextStep: function () {
      console.log('next')
      this.$emit('to-step', 2)
    }
  },
  mounted: function () {
  },
  components: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#analyze {
  padding: 1rem;
  min-height: calc(100vh - 20rem);
}
</style>
