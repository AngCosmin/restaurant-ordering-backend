<template>
    <div class="container">
        <h1 style="margin-bottom:70px"> Add products to your menu </h1>
        <b-form @submit="onSubmit" v-if="show">
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
        optional
        placeholder="Enter picture url" />
        </b-form-group>

        <b-form-group id="exampleInputGroup3" label="Category:" label-for="exampleInput3">
        <b-form-select id="exampleInput3" :options="categories" required v-model="form.categories" />
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>
</template>

<script>
export default {
    data() {
      return {
        form: {
          name: '',
          ingredients: '',
          price: 0,
          url: '',
        },
        categories: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
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
