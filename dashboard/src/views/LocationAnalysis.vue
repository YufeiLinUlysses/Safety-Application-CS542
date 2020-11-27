<template>
  <b-container class="text-center">
    <h1 class="mb-3">The Location You Have Entered</h1>
    <span
      ><h5>Latitude:{{ lat }}, Longitude: {{ lng }}</h5></span
    >
    <br />
    <nearBy />
    <dash />
  </b-container>
</template>

<script>
import nearBy from "@/components/nearbymap.vue";
import dash from "@/components/NearByGraphs/dash.vue";
export default {
  components: {
    nearBy,
    dash,
  },
  data() {
    return { lat: 0, lng: 0 };
  },
  mounted() {
    this.lat = this.$store.state.location.lat;
    this.lng = this.$store.state.location.lng;
  },
};
</script>