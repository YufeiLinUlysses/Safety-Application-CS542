<template>
  <div>
    <v-col id="arc" />
    <p>{{ gdp }}</p>
  </div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";

var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  name: "vis",
  data() {
    return {
      gdp: [],
    };
  },
  mounted() {
    this.createGraph();
  },
  methods: {
    generateArc(gdp) {
      //define the width and height of the graph
      const w = 500;
      const h = 500;
      var gdp1 = gdp;
      //construct the graph in the div arc
      const svg = d3
        .select("#arc")
        .append("svg")
        .attr("width", w)
        .attr("height", h);

      // Sort data
      const sortedGDP = gdp1.sort((a, b) => (a.value > b.value ? 1 : -1));

      //Set Color
      const color = d3.scaleOrdinal(d3.schemeDark2);

      //Get max gdp
      const max_gdp = d3.max(sortedGDP, (o) => o.value);

      //Define necessary components for graph
      const angleScale = d3
        .scaleLinear()
        .domain([0, max_gdp])
        .range([0, 1.5 * Math.PI]); //Define whether it is going to be a full circle

      const arc = d3
        .arc()
        .innerRadius((d, i) => (i + 1) * 25)
        .outerRadius((d, i) => (i + 2) * 25)
        .startAngle(angleScale(0))
        .endAngle((d) => angleScale(d.value));

      // Plug the graph into the region
      const g = svg.append("g");

      g.selectAll("path")
        .data(sortedGDP)
        .enter()
        .append("path")
        .attr("d", arc)
        .attr("fill", (d, i) => color(i))
        .attr("stroke", "#FFF")
        .attr("stroke-width", "1px")
        .on("mouseenter", function () {
          d3.select(this).transition().duration(200).attr("opacity", 0.5);
        }) // define interaction function
        .on("mouseout", function () {
          d3.select(this).transition().duration(200).attr("opacity", 1);
        }); //define interaction function

      g.selectAll("text")
        .data(gdp1)
        .enter()
        .append("text")
        .text((d) => `${d.country} -  ${d.value} Trillion`)
        .attr("x", -150)
        .attr("dy", -8)
        .attr("y", (d, i) => -(i + 1) * 25);

      g.attr("transform", "translate(200,300)");
    },
    createGraph() {
      var vm = this;
      var url = "/gdp";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          vm.gdp = await temp;
          vm.generateArc(vm.gdp);
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>



