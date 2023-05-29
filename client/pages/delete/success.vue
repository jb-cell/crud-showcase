<template>
    <v-card>
        <v-card-title>
            <v-icon>mdi-delete</v-icon>
            Delete: Successful!
        </v-card-title>
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
</template>

<script>
    export default {
        
    }
</script>

<style scoped>

</style>