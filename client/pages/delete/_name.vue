<template>
    <v-card>
        <v-card-title>
            <v-icon>mdi-delete</v-icon>
            Delete: {{ this.$route.params.name }}
        </v-card-title>

        <v-card-text>
            Are you sure you want to delete this recipe?
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                text
                :to="`/browse`"
            >
                Back
            </v-btn>
            <v-btn
                text
                @click="deleteRecipe()"
                :to="`/delete/success`"
            >
                Delete
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        methods: {
            async deleteRecipe() {
                await this.$axios.delete('http://127.0.0.1:8000/delete-recipie/' + this.$route.params.name)
                    .then(res => console.log(res));
                return true;
            },
        },
    }
</script>

<style scoped>

</style>