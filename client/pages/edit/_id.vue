<template>
    <v-card
    class="mx-auto"
    max-width="344"
    v-if="!$fetchState.pending"
    >
        <v-card-title>
            <v-icon>mdi-pencil</v-icon>
            Edit a Recipe
        </v-card-title>
        <v-container>
            <v-form
                ref="form"
            >
                <v-text-field
                    v-model="name"
                    color="primary"
                    :label="`Name (${recipeInfo.name})`"
                    variant="underlined"
                ></v-text-field>

                <v-text-field
                    v-model="icon"
                    color="primary"
                    :label="`Icon (${recipeInfo.icon})`"
                    variant="underlined"
                ></v-text-field>

                <v-text-field
                    v-model="description"
                    color="primary"
                    :label="`Description (${recipeInfo.description})`"
                    variant="underlined"
                ></v-text-field>

                <v-textarea
                    v-model="instructions"
                    color="primary"
                    counter
                    :label="`Instructions (${recipeInfo.instructions})`"
                    variant="underlined"
                    maxlength="120"
                ></v-textarea>
            </v-form>
        </v-container>

        <v-divider></v-divider>

        <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="success" 
            @click="editRecipe()"
            :to="`/edit/success`"
        >
            Submit
            <v-icon icon="mdi-chevron-right" end></v-icon>
        </v-btn>
        </v-card-actions>
  </v-card>
</template>

<script>
    export default {
        data () {
            return {
                recipeInfo: {},
                id: null,
                name: null,
                icon: null,
                description: null,
                instructions: null
            }
        },
        methods: {
            async editRecipe () {
                await this.$axios.put('http://127.0.0.1:8000/update-recipie/' + this.$route.params.id, {
                    id: this.id,
                    icon: this.icon,
                    name: this.name,
                    description: this.description,
                    instructions: this.instructions
                })
                    .then(res => console.log(res));
                return true;
            }
        },
        async fetch () {
            this.recipeInfo = await this.$axios.get('http://127.0.0.1:8000/get-by-id/' + this.$route.params.id)
                .then(res => res.data);
        }
    }
</script>

<style scoped>

</style>