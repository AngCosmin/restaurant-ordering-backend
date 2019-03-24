<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark">
        <b-navbar-brand href="#" class="m-l-3">Tabsquare</b-navbar-brand>

        <b-navbar-toggle target="nav_collapse" />

        <b-collapse is-nav id="nav_collapse">
          <b-navbar-nav>
            <b-nav-item active><router-link v-if="isAuth" :to="{ name: 'home' }">Home</router-link></b-nav-item>
            <b-nav-item><router-link v-if="isAuth" :to="{ name: 'products' }">Products</router-link></b-nav-item>
            <b-nav-item><router-link v-if="isAuth" :to="{ name: 'dashboard' }">Dashboard</router-link></b-nav-item>
            <b-nav-item><router-link v-if="isAuth" :to="{ name: 'tables' }">Tables</router-link></b-nav-item>
          </b-navbar-nav>

          <b-navbar-nav class="ml-auto">
            <b-navbar-nav right>
              <b-nav-item><span v-if="isAuth" @click="onLogout">Logout</span></b-nav-item>
            </b-navbar-nav>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>


    <div>
      <b-nav>

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
}

.nav-item a {
  color: #FFF;
}

.nav-item a:hover {
  text-decoration: none;
  color: #3498db;
}

.navbar {
  background-color: #2c3e50 !important;
  margin-bottom: 25px;
}
</style>
