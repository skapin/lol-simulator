import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/axios'
import './plugins/fontawesome'
import './plugins/bootstrap-vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import Buefy from 'buefy'

import 'buefy/dist/buefy.css'
// import _ from 'lodash'
import VueLodash from 'vue-lodash'

require('lodash')

Vue.use(Buefy)
Vue.use(VueLodash)

Vue.config.productionTip = false

// Object.defineProperty(Vue.prototype, '$_', { value: _ })

Vue.mixin({
  data () {
    return {
    }
  },
  methods: {
    goTo: function (path) {
      this.$router.push(path)
    },
    // dont call callback if context is destroyed
    setProtectedTimeout (callback, timeoutInSec) {
      if (this._isDestroyed) {
      } else {
        setTimeout(callback, timeoutInSec)
      }
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
