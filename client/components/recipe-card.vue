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
                :to="`/browse/${card.id}`"
                text
            >
                View
            </v-btn>
            <v-dialog v-model="deleteDialog" persistent max-width="290">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn v-bind="attrs" text v-on="on"><v-icon>mdi-delete</v-icon></v-btn>
                </template>
                <v-card>
                    <v-card-title><v-icon>mdi-delete</v-icon>Delete</v-card-title>
                    <v-card-text>Are you sure you want to delete this recipe?</v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn text @click="deleteDialog = false">Cancel</v-btn>
                        <v-btn text @click="deleteRecipe()">OK</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-dialog v-model="editDialog" persistent max-width="290">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn v-bind="attrs" text v-on="on"><v-icon>mdi-pencil</v-icon></v-btn>
                </template>
                <v-card>
                    <v-card-title><v-icon>mdi-pencil</v-icon>Edit</v-card-title>
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
                        <v-btn text @click="editDialog = false">Cancel</v-btn>
                        <v-btn text @click="editRecipe()">OK</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        props: ['card'],
        data () {
            return {
                id: this.card.id,
                icon: this.card.icon,
                name: this.card.name,
                description: this.card.description,
                instructions: this.card.instructions,
                deleteDialog: false,
                editDialog: false
            }
        },
        methods: {
            async deleteRecipe () {
                await this.$axios.delete('http://127.0.0.1:8000/delete-recipe/' + this.card.id)
                    .then(res => console.log(res));
                this.$nuxt.refresh();
            },
            async editRecipe () {
                await this.$axios.put('http://127.0.0.1:8000/update-recipe/' + this.card.id, {
                    id: this.id,
                    icon: this.icon,
                    name: this.name,
                    description: this.description,
                    instructions: this.instructions
                })
                    .then(res => console.log(res));
                this.$nuxt.refresh();
            }
        },
    }
</script>

<style scoped>

</style>