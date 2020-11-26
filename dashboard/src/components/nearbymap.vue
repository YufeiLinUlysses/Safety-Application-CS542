<template>
  <div>
    <gmap-map :center="center" :zoom="15" style="width: 100%; height: 400px">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="center = m.position"
      ></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
import axios from "axios";
var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});
export default {
  data() {
    return {
      lat: 0,
      lng: 0,
      markers: [],
      result: [],
      center: { lat: 0, lng: 0 },
    };
  },
  mounted() {
    this.center.lat = this.$store.state.location.lat;
    this.center.lng = this.$store.state.location.lng;
    this.getLoc();
  },
  methods: {
    getLoc() {
      var vm = this;
      try {
        webcall
          .post("/locAnalysis", this.$store.state.location)
          .then(async function (response) {
            var temp = await JSON.parse(JSON.stringify(response.data));
            if (temp.length == 0) {
              alert(
                "Sorry, We do not have any info on the location you searched"
              );
            }
            var result = [];
            for (var i of temp) {
              result.push({
                position: {
                  lat: parseFloat(i["LAT"]),
                  lng: parseFloat(i["LON"]),
                },
              });
            }
            vm.markers = result;
          });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>