import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import axios from 'axios'

// Router
import router from './router'
import VueRouter from 'vue-router'

// Store
import store from './store/index'

import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:5000';

Vue.use(BootstrapVue)
Vue.use(Vuex)
Vue.use(VueRouter)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
