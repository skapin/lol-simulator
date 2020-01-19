import Vue from 'vue'
import Vuex from 'vuex'

require('lodash')

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    championSelected: null,
    itemsSelected: []
  },
  mutations: {
    setChampionSelected (state, champion) {
      state.championSelected = champion
    },
    addSelectedItem (state, item) {
      if (state.itemsSelected.length >= 6) {
        return
      }
      state.itemsSelected.push(item)
    },
    removeSelectedItem (state, index) {
      // Vue._.remove(state.itemsSelected, { 'name': item.name })
      state.itemsSelected.splice(index, 1)
    }
  },
  actions: {
  },
  modules: {
  }
})
