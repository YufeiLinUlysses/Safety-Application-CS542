<template>
  <div id="app">
    <v-app id="inspire">
      <v-toolbar>
        <v-toolbar-side-icon></v-toolbar-side-icon>
        <v-toolbar-title>Title</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn flat>Link One</v-btn>
          <v-btn flat>Link Two</v-btn>
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-btn dark icon v-on="on">
                <v-icon color="primary">notifications</v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-list dense>
                <v-subheader>Notifications</v-subheader>
                <v-divider></v-divider>
                <v-list-tile
                  v-for="notification in notifications"
                  :key="`notification-key-${notification.id}`"
                >
                  <v-list-tile-title>
                    {{ notification.title }}
                  </v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-card>
          </v-menu>
        </v-toolbar-items>
      </v-toolbar>
    </v-app>
  </div>
</template>

<script>
// import MENU from "./menu.vue";
export default {
  // components: {
  //   MENU,
  // },
  data: () => ({
    notifications: [
      { id: 1, title: "Click Me" },
      { id: 2, title: "Click Me" },
      { id: 3, title: "Click Me" },
      { id: 4, title: "Click Me 2" },
    ],
  }),
  methods: {
    goHome: function () {
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style scoped>
.titleLabel {
  text-transform: none !important;
}
</style>

