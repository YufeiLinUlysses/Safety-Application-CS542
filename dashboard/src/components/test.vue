<template>
  <div id="app">
    <GChart
      :settings="settings"
      type="GeoChart"
      :data="chartData"
      :options="chartOptions"
      style="width: 900px; height: 500px"
    />
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
export default {
  name: "App",
  components: {
    GChart,
  },
  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      settings: {
        packages: ["geochart"],
        mapsApiKey: "AIzaSyCESDQdWk4BVXVLLwkKQijvexrPnU6UkAk",
      },
      chartData: [
        ["City", "Population", "Area"],
        ["", 2761477, 1285.31],
        ["Worcester", 1324110, 181.76],
        ["Naples", 959574, 117.27],
        ["Turin", 907563, 130.17],
        ["Palermo", 655875, 158.9],
        ["Genoa", 607906, 243.6],
        ["Bologna", 380181, 140.7],
        ["Florence", 371282, 102.41],
        ["Fiumicino", 67370, 213.44],
        ["Anzio", 52192, 43.43],
        ["Ciampino", 38262, 11],
      ],
      chartOptions: {
        region: 'US-MA',
        displayMode: 'regions',
        resolution: 'metros',
        colorAxis: {colors: ['green', 'blue']}
      },
    };
  },
};
</script>
