import Vue from 'vue'
import App from './App.vue'

// Router
import router from './router'
import VueRouter from 'vue-router'

// Store
import store from './store/index'

Vue.config.productionTip = false

Vue.use(VueRouter)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
