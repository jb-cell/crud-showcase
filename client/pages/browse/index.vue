<template>
    <div>
        <div v-if="!$fetchState.pending">
            <card-display
                :cards="cardsInfo.results"
            />
        </div>
        <div v-else>
            Loading...
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            cardsInfo: []
        }
    },
    async fetch () {
        this.cardsInfo = await this.$axios.get('http://127.0.0.1:8000/',{ headers: {"Access-Control-Allow-Origin": "*"} })
            .then(res => res.data);
    }
}
</script>

<style scoped>

</style>