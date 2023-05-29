<template>
    <v-card
    class="mx-auto"
    max-width="344"
    >
        <v-card-title>
            <v-icon>mdi-plus</v-icon>
            Add a Recipe
        </v-card-title>
        <v-container>
            <v-form
                ref="form"
            >
                <v-text-field
                    v-model="name"
                    color="primary"
                    label="Name"
                    variant="underlined"
                ></v-text-field>

                <v-text-field
                    v-model="icon"
                    color="primary"
                    label="Icon"
                    variant="underlined"
                ></v-text-field>

                <v-text-field
                    v-model="description"
                    color="primary"
                    label="Description"
                    variant="underlined"
                ></v-text-field>

                <v-textarea
                    v-model="instructions"
                    color="primary"
                    counter
                    label="Instructions"
                    variant="underlined"
                    maxlength="120"
                ></v-textarea>
            </v-form>
        </v-container>

        <v-divider></v-divider>

        <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="success" 
            @click="addRecipe()"
            :to="`/add/success`"
        >
            Submit
            <v-icon icon="mdi-chevron-right" end></v-icon>
        </v-btn>
        </v-card-actions>
  </v-card>
</template>

<script>
    export default {
        data() {
            return {
                id: null,
                name: null,
                icon: null,
                description: null,
                instructions: null
            }
        },
        methods: {
            async addRecipe () {
                this.id = await this.$axios.get('http://127.0.0.1:8000/get-size')
                    .then(res => res.data);
                await this.$axios.post('http://127.0.0.1:8000/add-recipie', {
                    id: this.id,
                    icon: this.icon,
                    name: this.name,
                    description: this.description,
                    instructions: this.instructions
                })
                    .then(res => console.log(res));
            }
        },
    }
</script>

<style scoped>

</style>