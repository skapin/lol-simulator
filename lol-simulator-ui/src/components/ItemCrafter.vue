<template>
  <div v-if="championSelected" id="champ-crafter-container">
    <div id="crafter-item-list">
      <img id="item-crafter" src="../assets/item_selector.png" alt="itemselector">
      <img id="champ-crafter-icon" :src="championSelected.image_url" alt="champion_url"/>
      <img v-for="(item, index) in itemsSelected"
          :key="index"
          @click="unselectItem(item, index)"
          class="item-selected"
          :id="'item-n-'+index"
          :src="item.image_url"
      >
    </div>
  </div>
</template>

<script>

import { mapState } from 'vuex'

export default {

  name: 'ItemCrafter',
  props: [],
  data () {
    return {
    }
  },
  methods: {
    unselectItem: function (item, index) {
      this.$store.commit('removeSelectedItem', index)
      this.$forceUpdate()
    }
  },
  computed: mapState(['championSelected', 'itemsSelected']),
  mounted: function () {
  },
  components: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#champ-crafter-container {
  position: relative;
  height: 20vh;
  margin-bottom: 2vh;
}

#champ-crafter-container #item-crafter{
  position: absolute;
  z-index: 1;
  height: 20vh;
}
#champ-crafter-container #champ-crafter-icon{
  position: absolute;
  z-index: 11;
  height: 9vh;
  border-radius: 50%;
}
#crafter-item-list img {
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
#crafter-item-list {
  z-index: 22;
}
.item-selected {
  position: absolute;
  z-index: 33;
  border-radius: 50%;
  height: 50px;
}
#item-n-0 {
  top: -160px !important;
  left: -105px !important;
}
#item-n-1 {
  top: -157px !important;
  left: 113px !important;
}
#item-n-2 {
  top: -5px !important;
  left: 195px !important;
}
#item-n-3 {
  top: 180px !important;
  left: 90px !important;
}
#item-n-4 {
  top: 180px !important;
  left: -90px !important;
}
#item-n-5 {
  top: -5px !important;
  left: -197px !important;
}
.item-selected:hover {
  /*border: 11px solid black;*/
  /*height: 72px;*/
  outline: none;
  border-color: #9ecaed;
  box-shadow: 0 0 10px #9ecaed;
  box-shadow:
  inset 0 0 50px #fff,      /* inner white */
  inset 20px 0 80px #f0f,   /* inner left magenta short */
  inset -20px 0 80px #0ff,  /* inner right cyan short */
  inset 20px 0 300px #f0f,  /* inner left magenta broad */
  inset -20px 0 300px #0ff, /* inner right cyan broad */
  0 0 50px #fff,            /* outer white */
  -10px 0 80px #f0f,        /* outer left magenta */
  10px 0 80px #0ff;         /* outer right cyan */
}
</style>
