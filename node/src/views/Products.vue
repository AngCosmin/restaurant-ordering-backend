<template>
    <div class="container">
        <img alt="App logo" src="../assets/logo.png">
        <b-table style="margin-bottom:100px" striped hover :items="items" />
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
    computed: {
        ...mapGetters('auth', {
            getEmail: 'getEmail',
        }),
    },
    data() {
        return {
            items: []
        }
    },
    created() {
        console.log(this.getEmail)
        this.products()
    },
    methods: {
        products() {
            axios.get('/restaurant/products', {
                params: {
                    email: this.getEmail,
                }
            }).then(response => {
                console.log(response.data.data)
                this.items = response.data.data
            }).catch(error => {
                console.error(error);
            })
        }
    }
    
}
</script>
