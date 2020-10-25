<template>
  <b-container fluid>
    <MAIN />
    <router-view />
  </b-container>
</template>

<script>
import MAIN from "./components/Templ/main.vue";
export default {
  name: "App",

  components: {
    MAIN,
  },

  data: () => ({
    //
  }),
};
</script>
