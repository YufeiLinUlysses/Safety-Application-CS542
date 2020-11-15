<template>
  <b-container class="text-center">
    <h1>The Location You Have Entered</h1>
    <br />
    <span>{{ location }}</span>
  </b-container>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {
    location() {
      return this.$store.getters.locToString;
    },
  },
};
</script>