<template>
  <gmap-map :center="center" :zoom="12" style="width: 100%; height: 400px">
    <gmap-marker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      @click="center = m.position"
    ></gmap-marker>
  </gmap-map>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      lat: 0,
      lng: 0,
      radius: "5",
      type: "restaurant",
      markers: [ 
        { position: { lat: 42.3061, lng: -71.0827 } },
        { position: { lat: 42.327, lng: -71.1056 } },
        { position: { lat: 42.3315, lng: -71.0709 } },
      ],
      center: { lat: 0, lng: 0 },
    };
  },
  mounted() {
    this.center.lat = this.$store.state.location.lat;
    this.center.lng = this.$store.state.location.lng;
    this.loadData();
  },
  methods: {
    loadData() {
      const URL =
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=restaurants&inputtype=textquery&fields=plus_code,name&locationbias=circle:2000@" +
        String(this.lat) +
        "," +
        String(this.lng) +
        "&key=AIzaSyCESDQdWk4BVXVLLwkKQijvexrPnU6UkAk";
      axios
        .get(URL)
        .then((response) => {
          this.places = response.data.results;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
};
</script>