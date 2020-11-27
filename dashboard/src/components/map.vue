<template>
  <div>
    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 400px; width: 100%"
      zoomDisable="false"
      minZoom="11"
      maxZoom="11"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-geo-json
        v-if="show"
        :geojson="geojson"
        :options="options"
        :options-style="styleFunction"
      />
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";
import bostonGeo from "../assets/cityGeo/boston.json";

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
  },
  data() {
    return {
      loading: false,
      show: true,
      enableTooltip: true,
      zoom: 11,
      center: [42.32243, -71.07977],
      geojson: null,
      fillColor: null,
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    };
  },
  computed: {
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
    },
    styleFunction() {
      // important! need touch fillColor in computed for re-calculate when change fillColor
      return (feature) => {
        var fillColor = this.getColor(feature.properties.density);
        return {
          weight: 2,
          color: "#ECEFF1",
          opacity: 1,
          fillColor: fillColor,
          fillOpacity: 1,
        };
      };
    },
    onEachFeatureFunction() {
      if (!this.enableTooltip) {
        return () => {};
      }
      return (feature, layer) => {
        layer.bindTooltip(
          "<div>Number of Crimes:" +
            feature.properties.density +
            "</div><div>Region: " +
            feature.properties.Name +
            "</div>",
          { permanent: false, sticky: true }
        );
        this.fillColor = this.getColor(feature.properties.density);
      };
    },
  },
  async created() {
    this.loading = true;
    const data = bostonGeo;
    this.geojson = data;
    this.loading = false;
  },
  methods: {
    getColor: function (d) {
      return d > 38010
        ? "#800026"
        : d > 29266
        ? "#BD0026"
        : d > 20522
        ? "#E31A1C"
        : d > 12829
        ? "#FC4E2A"
        : d > 5137
        ? "#FD8D3C"
        : "#FFEDA0";
    },
  },
};
</script>
