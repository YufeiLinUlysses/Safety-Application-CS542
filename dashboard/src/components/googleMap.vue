<template>
  <div>
    <gmap-map :center="center" :zoom="12" :style="windStyle" @click="mark">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m"
      ></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
export default {
  name: "GoogleMap",
  data() {
    return {
      // default to Montreal to keep it simple
      // change this to whatever makes sense
      center: { lat: 42.36243, lng: -71.05977 },
      markers: [],
      windWidth: 10,
      windHeight: 10,
      places: [],
      windStyle: "width: 100%;height:400px",
      currentPlace: null,
    };
  },
  mounted() {
    this.$nextTick(function () {
      window.addEventListener("resize", this.winH);
      window.addEventListener("resize", this.winW);

      //Init
      this.winH();
      this.winW();
      this.windStyle = "width: 100%;height:" + String(this.windHeight) + "px";
    });
  },

  methods: {
    winH: function () {
      this.windHeight = document.documentElement.clientHeight;
    },
    winW: function () {
      this.windWidth = document.documentElement.clientWidth;
    },
    // receives a place object via the autocomplete component
    setPlace(place) {
      this.currentPlace = place;
    },
    mark(event) {
      var marker = {
        lat: event.latLng.lat(),
        lng: event.latLng.lng(),
      };
      this.$store.dispatch("updateLoc", marker);
      this.markers = [marker];
      console.log(this.markers);
    },
    addMarker() {
      if (this.currentPlace) {
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng(),
        };
        this.markers.push({ position: marker });
        this.places.push(this.currentPlace);
        this.center = marker;
        this.currentPlace = null;
      }
    },
    geolocate: function () {
      navigator.geolocation.getCurrentPosition((position) => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
      });
    },
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.winW);
    window.removeEventListener("resize", this.winH);
  },
};
</script>

