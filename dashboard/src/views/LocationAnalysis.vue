<template>
  <b-container class="text-center">
    <h1>The Location You Have Entered</h1>
    <br />
    <span>{{ location }}</span>
    <br />
    <nearBy />
  </b-container>
</template>

<script>
import nearBy from "@/components/nearbymap.vue"
export default {
  components:{
    nearBy
  },
  data() {
    return {};
  },
  computed: {
    location() {
      return this.$store.state.location;
    },
  },
};
</script>