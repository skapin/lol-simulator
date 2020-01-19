<template>
  <div>
    <section id="itemselector" class="hero is-info">
      <div class="hero-body">
        <div class="container">
          <div>
            <item-crafter/>
          </div>
          <h1 class="title">Now, Pick your items: </h1>
          <template v-for="(category, index) in categories">
            <b-message :key="index" :title="category.header" :closable="false" v-if="!['START', 'TOOLS', 'UNCATEGORIZED'].includes(category.header)">
              <template v-for="(subcategory, index) in category.tags">
                <b-message class="is-primary" :key="index" :title="subcategory" :closable="false">
                  <template v-for="(item, index) in items">
                    <span :key="index" v-if="item.categories.includes(subcategory.toLowerCase())">
                      <item-icon :link="item.image_url" :item="item" @on-clicked="itemSelected"/>
                    </span>
                  </template>
                </b-message>
              </template>
            </b-message>
          </template>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import server from '../api/server.vue'
// import ChampionSimpleDisplay from '@/components/ChampionSimpleDisplay.vue'
import ItemIcon from '@/components/ItemIcon.vue'
import ItemCrafter from '@/components/ItemCrafter.vue'
import { mapState } from 'vuex'

export default {
  name: 'ItemSelector',
  data () {
    return {
      items: [],
      categories: [],
      championSelected: this.$store.state.championSelected
    }
  },
  computed: mapState(['itemsSelected']),
  methods: {
    goToNextStep: function () {
      console.log('next')
      this.$emit('to-step', 2)
    },
    itemSelected: function (item) {
      this.$store.commit('addSelectedItem', item)
      if (this.$store.state.itemsSelected.length >= 6) {
        this.setProtectedTimeout(this.goToNextStep, 500)
      }
    },
    getItems: function () {
      server.getItems().then(result => {
        /* eslint-disable-next-line */
        this.categories = result.data.items.tree
        for (let i = 0; i < this.categories.length; i++) {
          this.categories[i].tags = this.categories[i].tags.map(x => { return x.toLowerCase() })
        }
      })
      server.getItemsCdragon().then(result => {
        /* eslint-disable-next-line */
        this.items = result.data.items
        for (let i = 0; i < this.items.length; i++) {
          this.items[i].categories = this.items[i].categories.map(x => { return x.toLowerCase() })
        }
      })
    }
  },
  mounted: function () {
    this.getItems()
  },
  components: {
    ItemIcon, ItemCrafter
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#itemselector {
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
.item-picto {
  width: 50px;
  height: 50px;
}
</style>
