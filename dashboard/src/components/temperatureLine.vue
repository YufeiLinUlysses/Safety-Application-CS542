<template>
  <apexchart
    type="line"
    height="350"
    :options="chartOptions"
    :series="series"
  ></apexchart>
</template>
<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";

var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  components: {
    apexchart: VueApexCharts,
  },
  props: ["url", "cols", "co"],
  data() {
    return {
      series: [],
      chartOptions: {}
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData: function () {
      var vm = this;
      var url = this.url;
      var cols = this.cols;
      var co = this.co;
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var min = [],
            max = [],
            avg = [];
          for (var m of temp) {
            min.push(Number(m[cols[0]]).toFixed(2));
            avg.push(Number(m[cols[1]]).toFixed(2));
            max.push(Number(m[cols[2]]).toFixed(2));
          }
          vm.series = [
            { name: "Max", data: max },
            { name: "Average", data: avg },
            { name: "Min", data: min },
          ];
          vm.chartOptions = co
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>