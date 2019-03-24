<template>
    <div class="container">
        <img alt="App logo" src="../assets/logo.png">
        <h1 style="margin-bottom:70px"> Add tables in your restaurant </h1>
        <b-form style="margin-bottom:70px" @submit="onSubmit" v-if="show">
        <b-form-group
            id="TableNameGroup"
            label="Table identifier:"
            label-for="TableName">
        <b-form-input
            id="TableName"
            type="text"
            v-model="form.name"
            required
            placeholder="Enter table name" />
        </b-form-group>

        <b-form-group
            id="TextGroup"
            label="Text for QR code:"
            label-for="Text">
        <b-form-input
            id="Text"
            type="text"
            v-model="form.text"
            required
            placeholder="Enter text for qr code" />
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import router from '@/router'

export default {
    computed: {
        ...mapGetters('auth', {
            getEmail: 'getEmail',
        }),
    },
    data() {
      return {
        form: {
          name: '',
          text: '',
        },
        show: true
      }
    },
    methods: {
      onSubmit() {
		axios.post('/restaurant/add_table', {
			email: this.getEmail,
			name: this.form.name,
		}).then(response => {
			this.form.name = ''
            this.form.text = ''
            
		}).catch(error => {
			console.error(error);
		})
      },
	}
}
</script>
