<template>
  <div id="app">
    <div>
      <b-nav>
        <b-nav-item active><router-link v-if="isAuth" :to="{ name: 'home' }">Home</router-link></b-nav-item>
        <b-nav-item><router-link v-if="isAuth" :to="{ name: 'products' }">Products</router-link></b-nav-item>
        <b-nav-item><router-link v-if="isAuth" :to="{ name: 'dashboard' }">Dashboard</router-link></b-nav-item>
        <b-nav-item><router-link v-if="isAuth" :to="{ name: 'tables' }">Tables</router-link></b-nav-item>
        <b-nav-item><b-button v-if="isAuth" type="submit" @click.prevent="onLogout" variant="outline-primary">Logout</b-button></b-nav-item>
        <!-- <b-nav-item><router-link v-if="!isAuth" :to="{ name: 'login' }">Login</router-link></b-nav-item> -->
      </b-nav>
    </div>

    <!-- <router-link v-if="isAuth" :to="{ name: 'home' }">Home</router-link>
    <router-link v-if="!isAuth" :to="{ name: 'login' }">Login</router-link>
    <router-link v-if="isAuth" :to="{ name: 'products' }">Products</router-link>
    <router-link v-if="isAuth" :to="{ name: 'dashboard' }">Dashboard</router-link> -->

    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "app",
  computed: {
    ...mapGetters("auth", {
      isAuth: "isAuthenticated"
    })
  },
  created() {
    this.$store.dispatch('auth/autoLogin')
  },
  methods: {
    onLogout(evt) {
      this.$store.dispatch("auth/logout").then(() => {
        this.$router.replace("/login");
      });
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}
</style>
