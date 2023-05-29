<template>
    <div>
        <v-card v-if="!$fetchState.pending">
            <v-card-title>
                <v-icon>{{ recipeInfo.icon }}</v-icon>
                {{ recipeInfo.name }}
            </v-card-title>

            <v-card-subtitle>
                {{ recipeInfo.description }}
            </v-card-subtitle>

            <v-card-text>
                {{ recipeInfo.instructions }}
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    text
                    :to="`/browse`"
                >
                    Back
                </v-btn>
            </v-card-actions>
        </v-card>
        <div v-else>
            Loading...
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                recipeInfo: {}
            }
        },
        async fetch () {
            this.recipeInfo = await this.$axios.get('http://127.0.0.1:8000/get-by-name/' + this.$route.params.name)
                .then(res => res.data);
        }
    }
</script>

<style scoped>

</style>