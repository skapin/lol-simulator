<template>
  <div class="home">
    <section>
      <b-steps v-model="activeStep"
                type="is-success"
                size="is-large"
                :has-navigation="navigation">
          <template v-for="(step, index) in steps">
              <b-step-item
                  :key="index"
                  :label="step.label">
                  <div v-if="step.id===0">
                    <ChampionSelector @to-step="step => activeStep = step"/>
                  </div>
                  <div v-if="step.id===1">
                    <ItemSelector @to-step="step => activeStep = step"/>
                  </div>
                  <div v-if="step.id===2">
                    <Analyze @to-step="step => activeStep = step"/>
                  </div>
              </b-step-item>
          </template>
      </b-steps>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import ChampionSelector from '@/components/ChampionSelector.vue'
import ItemSelector from '@/components/ItemSelector.vue'
import Analyze from '@/components/Analyze.vue'

export default {
  name: 'home',
  data () {
    return {
      activeStep: 0,
      navigation: false
    }
  },
  computed: {
    baseSteps () {
      return [
        {
          id: 0,
          label: 'Champion',
          component: '->>'
        },
        {
          id: 1,
          label: 'Items',
          content: 'Lorem ipsum dolor sit amet.'
        },
        {
          id: 2,
          label: 'Results',
          content: 'Lorem ipsum dolor sit amet.'
        }
      ]
    },
    steps () {
      const steps = [...this.baseSteps]
      if (this.showBooks) {
        steps.splice(steps.length - 1, 0, this.bookStep)
      }
      return steps
    },
    bookStep () {
      return {
        label: 'Books',
        content: 'Lorem ipsum dolor sit amet.',
        displayed: true
      }
    }
  },
  components: {
    ChampionSelector, ItemSelector, Analyze
  }
}
</script>
<style>
.steps {
  /*margin-bottom: 10vh;*/
  height: 10rem;
}
.step-content {
  padding: 0 !important;
}

</style>
