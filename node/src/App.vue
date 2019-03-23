<template>
  <div id="app">
    <router-link v-if="isAuth" :to="{ name: 'home' }">Home</router-link>
    <router-link :to="{ name: 'login' }">Login</router-link>
    <router-link :to="{ name: 'products' }">Products</router-link>
    <router-link :to="{ name: 'dashboard' }">Dashboard</router-link>

    <router-view/>

    <b-button type="submit" @click.prevent="onLogout" variant="primary">Logout</b-button>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'app',
  computed: {
            ...mapGetters('auth', {
                isAuth: 'isAuthenticated',
            }),
        },

  methods: {
      onLogout(evt) {
				this.$store.dispatch('auth/logout').then(() => {
					this.$router.replace('/login');
				});

      }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
