<template>
    <div style="margin-left: 25px; margin-right: 25px;">
        <div class="text-center">
            <h3 v-if="getEmail === 'maisondescrepes@gmail.com'">Maison des Crepes</h3>
            <h3 v-else-if="getEmail === 'pizzahut@gmail.com'">Pizza Hut</h3>
        </div>

        <b-card-group deck style="margin-bottom: 25px">
            <b-card v-if="orders[0]" :title="'Table ' + orders[0]['table_identify']">
                <b-card-text v-for="item in orders[0]['products']" :key="item">{{ item }}</b-card-text>
                <div @click="setStatusComplete(orders[0]['table_id'])">
                    <b-button href="#" variant="primary" class="mt-2">Done</b-button>
                </div>
            </b-card>

            <b-card v-if="orders[1]" :title="'Table ' + orders[1]['table_identify']">
                <b-card-text v-for="item in orders[1]['products']" :key="item">{{ item }}</b-card-text>
                <div @click="setStatusComplete(orders[1]['table_id'])">
                    <b-button href="#" variant="primary" class="mt-2">Done</b-button>
                </div>
            </b-card>

            <b-card v-if="orders[2]" :title="'Table ' + orders[2]['table_identify']">
                <b-card-text v-for="item in orders[2]['products']" :key="item">{{ item }}</b-card-text>
                <div @click="setStatusComplete(orders[2]['table_id'])">
                    <b-button href="#" variant="primary" class="mt-2">Done</b-button>
                </div>
            </b-card>
        </b-card-group>

        <b-card-group deck>
            <b-card v-if="orders[3]" :title="'Table ' + orders[3]['table_identify']">
                <b-card-text v-for="item in orders[3]['products']" :key="item">{{ item }}</b-card-text>
                <div @click="setStatusComplete(orders[3]['table_id'])">
                <b-button href="#" variant="primary" class="mt-2">Done</b-button>
                </div>
            </b-card>

            <b-card v-if="orders[4]" :title="'Table ' + orders[4]['table_identify']">
                <b-card-text v-for="item in orders[4]['products']" :key="item">{{ item }}</b-card-text>
                <div @click="setStatusComplete(orders[4]['table_id'])">
                <b-button href="#" variant="primary" class="mt-2">Done</b-button>
                </div>
            </b-card>

            <b-card v-if="orders[5]" :title="'Table ' + orders[5]['table_identify']">
                <b-card-text v-for="item in orders[5]['products']" :key="item">{{ item }}</b-card-text>
                <div @click="setStatusComplete(orders[5]['table_id'])">
                    <b-button variant="primary" class="mt-2">Done</b-button>
                </div>
            </b-card>
        </b-card-group>
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
        this.getOrders()
    },
    mounted: function () {
        this.$nextTick(function () {
            window.setInterval(() => {
                this.getOrders();
            }, 5000);
        })
    },
    methods: {
        getOrders() {
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
                this.getOrders()
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

    .btn-primary {
        background-color: #27ae60;
        border: 1px solid #27ae60;
    }

    .btn-primary:hover {
        background-color: #2ecc71;
        border: 1px solid #2ecc71;
    }

    .card {
        border: 1px solid #27ae60;
    }

    .card-text {
        margin-bottom: 0;
    }
</style>