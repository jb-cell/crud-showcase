<template>
  <v-app dark>
    <v-navigation-drawer
        v-model="drawer"
        fixed
        app
    > 
        <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
        app
    >
      <v-app-bar-nav-icon 
        @click.stop="drawer = !drawer" 
        class="hidden-sm-and-up"
      >
      </v-app-bar-nav-icon>

      <v-toolbar-title>
        <v-icon>{{ titleIcon }}</v-icon> 
        {{ title }}
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items
        class="hidden-xs-only"
      >
        <v-btn 
            v-for="(item, i) in items" 
            :key="i" 
            :to="item.to" 
            router 
            exact
            text
        >
          <v-icon>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: false,
      items: [
        {
          icon: "mdi-home",
          title: "Home",
          to: "/",
        },
        {
          icon: "mdi-book",
          title: "Browse",
          to: "/browse",
        },
        {
          icon: "mdi-plus",
          title: "Add",
          to: "/add",
        },
      ],
      title: "MealStation",
      titleIcon: "mdi-food-off",
    };
  },
};
</script>
