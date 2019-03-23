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
          type="text"
          v-model="form.name"
          required
          placeholder="Enter password" />
      </b-form-group>

      <b-button type="submit" variant="primary">Login</b-button>
    </b-form>
    </div>
</template>

<script>
export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      }
    }
}
</script>
