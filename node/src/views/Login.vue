<template>
    <div class="container">
        <h1 style="margin-bottom:70px"> Sign in to your account </h1>
        <b-form @submit="onSubmit" v-if="show">
      <b-form-group
        id="exampleInputGroup1"
        label="Email address:"
        label-for="exampleInput1"
      >
        <b-form-input
          id="exampleInput1"
          type="email"
          v-model="form.email"
          required
          placeholder="Enter email" />
      </b-form-group>

      <b-form-group id="exampleInputGroup2" label="Your password:" label-for="exampleInput2">
        <b-form-input
          id="exampleInput2"
          type="password"
          v-model="form.password"
          required
          placeholder="Enter password" />
      </b-form-group>

      <b-button type="submit" @click.prevent="onSubmit" variant="primary">Login</b-button>
    </b-form>
    </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
    data() {
      return {
        form: {
          email: '',
          password: '',
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        let formData = {
					email: this.form.email,
					password: this.form.password,
				}

				this.$store.dispatch('auth/login', formData).then(() => {
					this.$router.replace('/dashboard');
				});

      }
    }
}
</script>
