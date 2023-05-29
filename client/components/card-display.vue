<template>
    <v-card
        class="mx-auto"
        color="grey"
    >
        <v-container fluid>
            <v-row dense>
                <v-col
                    v-for="card in cards"
                    :key="card.id"
                    :cols=6
                >
                    <recipe-card
                        :card="card"
                    />
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    props: ['cards']
}
</script>

<style scoped>

</style>