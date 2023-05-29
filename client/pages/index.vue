<template>
    <hero 
        :card="cardInfo"
    />
</template>

<script>
    export default {
        data () {
            return {
                cardInfo: {
                    icon: "mdi-home",
                    title: "Welcome to MealStation",
                    text: "Get started by navigating to one of the pages!",
                    button: "Start Browsing!",
                    to: "/browse"
                }
            }
        }
    }
</script>

<style scoped>

</style>