<template>
  <v-col id="map" />
</template>
<script>
//Citation: boston geojson data from https://github.com/mjfoster83/d3-workshop
import boston from "@/assets/cityGeo/boston.json";
import * as d3 from "d3";
export default {
  mounted() {
    this.generateMap();
  },
  methods: {
    generateMap() {
      //define the width and height of the graph
      const w = 500;
      const h = 500;

      //construct the graph in the div arc
      const svg = d3
        .select("#map")
        .append("svg")
        .attr("width", w)
        .attr("height", h);

      const albersProjection = d3
        .geoAlbers()
        .scale(190000)
        .rotate([71.057, 0])
        .center([0, 42.313])
        .translate([w/2, h/2]);

      const geoPath = d3.geoPath().projection(albersProjection);

      // Plug the graph into the region
      const g = svg.append("g");

      g.selectAll("path")
        .data(boston.features)
        .enter()
        .append("path")
        .attr("fill", "#ccc")
        .attr("stroke", "#333")
        .attr("d", geoPath);
    },
  },
};
</script>