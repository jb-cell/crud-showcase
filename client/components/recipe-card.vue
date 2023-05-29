<template>
    <v-card>
        <v-card-title>
            <v-icon>{{ card.icon }}</v-icon>
            {{ card.name }}
        </v-card-title>

        <v-card-subtitle>
            {{ card.description }}
        </v-card-subtitle>

        <v-card-text>
            {{ card.instructions }}
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                :to="`/browse/${card.name}`"
                text
            >
                View
            </v-btn>
            <v-btn 
                :to="`/delete/${card.name}`"
                text
            >
                <v-icon>mdi-delete</v-icon>
            </v-btn>
            <v-btn
                :to="`/edit/${card.id}`"
                text
            >
                <v-icon>mdi-pencil</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        props: ['card'],
        data () {
            return {
                card_name: this.card.name
            }
        },
    }
</script>

<style scoped>

</style>