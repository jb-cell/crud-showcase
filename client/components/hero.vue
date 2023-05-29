<template>
    <v-card 
        class="mx-auto"
        width="400"
    >
        <v-card-title>
            <v-icon>{{ card.icon }}</v-icon>
            {{ card.title }}
        </v-card-title>

        <v-card-subtitle>
            {{ card.text }}
        </v-card-subtitle>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                :to="card.to"
                router
                text
            >
                {{ card.button }}
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        props: ['card']
    }
</script>

<style scoped>

</style>