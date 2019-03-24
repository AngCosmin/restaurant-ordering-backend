<template>
    <div class="container">
        <img alt="App logo" src="../assets/logo.png">
        <h1 style="margin-bottom:70px"> Add products to your menu </h1>
        <b-form style="margin-bottom:70px" @submit="onSubmit" v-if="show">
        <b-form-group
            id="FoodInputGroup"
            label="Food name:"
            label-for="exampleInput1">
        <b-form-input
            id="FoodInput"
            type="text"
            v-model="form.food"
            required
            placeholder="Enter food name" />
        </b-form-group>

        <b-form-group id="exampleInputGroup2" label="Ingredients:" label-for="exampleInput2">
        <b-form-input
        id="exampleInput2"
        type="text"
        v-model="form.name"
        required
        placeholder="Enter ingredients" />
        </b-form-group>

        <b-form-group id="priceGroup" label="Price:" label-for="priceInput">
        <b-form-input
        id="priceInput"
        type="number"
        v-model="form.price"
        required
        placeholder="Enter price" />
        </b-form-group>

        <b-form-group id="pictureInputGroup" label="Picture:" label-for="pictureInput">
        <b-form-input
        id="pictureInput"
        type="url"
        v-model="form.url"
        required
        placeholder="Enter picture url" />
        </b-form-group>

        <b-form-group id="exampleInputGroup3" label="Category:" label-for="exampleInput3">
        <b-form-select id="exampleInput3" :options="categories" required v-model="form.category" />
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
          ingredients: '',
          price: 0,
		  url: '',
		  category: '',
        },
        categories: [],
        show: true
      }
    },
    created() {
      this.getCategories()
    },
    methods: {
      onSubmit() {
		axios.post('/add_product', {
			email: this.getEmail,
			name: this.form.name,
			ingredients: this.form.ingredients,
			price: this.form.price,
			url: this.form.url,
			category: this.form.category
		}).then(response => {
			this.form.name = ''
			this.form.ingredients = ''
			this.form.price = 0
			this.form.url = ''
			this.form.category = ''
		}).catch(error => {
			console.error(error);
		})
      },
      getCategories() {
            axios.get('/categories', {
            }).then(response => {
                console.log(response.data.data)
                this.categories = response.data.data

            }).catch(error => {
                console.error(error);
            })
		}
	}
}
</script>
