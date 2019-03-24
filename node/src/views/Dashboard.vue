<template>
    <div>
        <b-container class="bv-example-row">
        <b-row>
            <b-col>
                <div v-if="orders[0]">
                    <b>Table {{ orders[0]['table_id'] }}</b>
                    <br>
                    <div v-for="item in orders[0]['products']" :key="item">{{ item }}</div>
                    <button @click="setStatusComplete(orders[0]['table_id'])">Done</button>
                </div>
            </b-col>
            <b-col>
                <div v-if="orders[2]">
                    <b>Table {{ orders[2]['table_id'] }}</b>
                    <br>
                    <div v-for="item in orders[2]['products']" :key="item">{{ item }}</div>
                    <button @click="setStatusComplete(orders[2]['table_id'])">Done</button>
                </div>
            </b-col>
            <b-col>
                <div v-if="orders[4]">
                    <b>Table {{ orders[4]['table_id'] }}</b>
                    <br>
                    <div v-for="item in orders[4]['products']" :key="item">{{ item }}</div>
                    <button @click="setStatusComplete(orders[4]['table_id'])">Done</button>
                </div>
            </b-col>
        </b-row>
        </b-container>
        <b-container class="bv-example-row">
        <b-row>
            <b-col>
                <div v-if="orders[1]">
                    <b class="title">Table {{ orders[1]['table_id'] }}</b>
                    <br>
                    <div v-for="item in orders[1]['products']" :key="item">{{ item }}</div>
                    <button @click="setStatusComplete(orders[1]['table_id'])">Done</button>
                </div>
            </b-col>
            <b-col>
                <div v-if="orders[3]">
                    <b>Table {{ orders[3]['table_id'] }}</b>
                    <br>
                    <div v-for="item in orders[3]['products']" :key="item">{{ item }}</div>
                    <button @click="setStatusComplete(orders[3]['table_id'])">Done</button>
                </div>
            </b-col>
            <b-col>
                <div v-if="orders[5]">
                    <b>Table {{ orders[5]['table_id'] }}</b>
                    <br>
                    <div v-for="item in orders[5]['products']" :key="item">{{ item }}</div>
                    <button @click="setStatusComplete(orders[5]['table_id'])">Done</button>
                </div>
            </b-col>
        </b-row>
        </b-container>
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
            orders: []
        }
    },
    created() {
        console.log(this.getEmail)
        this.products()
    },
    methods: {
        products() {
            axios.get('/orders', {
                params: {
                    email: this.getEmail,
                }
            }).then(response => {
                console.log(response.data.data)
                this.orders = response.data.data

            }).catch(error => {
                console.error(error);
            })
        },
        setStatusComplete(tableId) {
            axios.post('/restaurant/update_orders_status', {
                table_id: tableId,
                status: 2
            }).then(response => {
                console.log(response.data.data)
                this.products()
            }).catch(error => {
                console.error(error);
            })
        }
    }
}
</script>

<style>
    .title {
        font-size: 2em;
    }
</style