<template>
    <div class="container">
        <h1 style="margin-bottom:70px"> These are your products </h1>
        <b-table striped hover :items="items" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [
            { name: 'Pizza Margherita', rating: 4.5, reviews: 45},
            { name: 'Pizza Margherita', rating: 4.5, reviews: 45},
            { name: 'Pizza Margherita', rating: 4.5, reviews: 45},
            { name: 'Pizza Margherita', rating: 4.5, reviews: 45}
            ]
        }
    }
}
</script>
