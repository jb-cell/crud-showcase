<template>
    <div>
        <v-card-title>
            All Entries
            <v-spacer></v-spacer>
            <v-dialog v-model="addDialog" persistent max-width="290">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn v-bind="attrs" text v-on="on"><v-icon>mdi-plus</v-icon>Add</v-btn>
                </template>
                <v-card>
                    <v-card-title><v-icon>mdi-plus</v-icon>Add</v-card-title>
                        <v-container>
                            <v-form
                                ref="form"
                            >
                                <v-text-field
                                    v-model="name"
                                    color="primary"
                                    :label="`Name`"
                                    variant="underlined"
                                ></v-text-field>

                                <v-text-field
                                    v-model="icon"
                                    color="primary"
                                    :label="`Icon`"
                                    variant="underlined"
                                ></v-text-field>

                                <v-text-field
                                    v-model="description"
                                    color="primary"
                                    :label="`Description`"
                                    variant="underlined"
                                ></v-text-field>

                                <v-textarea
                                    v-model="instructions"
                                    color="primary"
                                    counter
                                    :label="`Instructions`"
                                    maxlength="120"
                                ></v-textarea>
                            </v-form>
                        </v-container>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn text @click="addDialog = false">Cancel</v-btn>
                        <v-btn text @click="addRecipe()">OK</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-card-title>
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
            cardsInfo: [],
            id: null,
            icon: null,
            name: null,
            description: null,
            instructions: null,
            addDialog: false
        }
    },
    methods: {
        async addRecipe () {
            this.id = await this.$axios.get('http://127.0.0.1:8000/get-size')
                .then(res => res.data);
            await this.$axios.post('http://127.0.0.1:8000/add-recipe', {
                id: this.id,
                icon: this.icon,
                name: this.name,
                description: this.description,
                instructions: this.instructions
            })
                .then(res => console.log(res));
            this.addDialog = false;
            this.$nuxt.refresh();
        }
    },
    async fetch () {
        this.cardsInfo = await this.$axios.get('http://127.0.0.1:8000/')
            .then(res => res.data);
    }
}
</script>

<style scoped>

</style>