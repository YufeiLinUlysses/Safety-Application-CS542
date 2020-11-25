<template>
  <div id="app">
    <h5 class="text-center">Percentage of Each Crime Type</h5>
    <GChart
      type="PieChart"
      :data="chartData"
      :options="chartOptions"
      style="width: 100%; height: 100%"
    />
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
import axios from "axios";
// import { delete } from 'vue/types/umd';

var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  name: "App",
  components: {
    GChart,
  },

  data() {
    return {
      chartsLib: null,
      chartData: [],
      chartOptions: {
        chartArea: { width: "100%", height: "90%" },
        legend: {
          position: "top",
        },
      },
    };
  },
  methods: {
    onChartReady(chart, google) {
      this.chartsLib = google;
    },
    createGraph() {
      var vm = this;
      var url = "/typecnt";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [["DESCRIPTION", "ct"]];
          temp[5]["DESCRIPTION"] = "OTHER";
          for (var i = 6; i < temp.length; i++) {
            temp[5]["ct"] = parseInt(temp[i]["ct"]) + parseInt(temp[5]["ct"]);
            temp.splice(i, 1);
            i--;
          }
          for (var j of temp) {
            var cur = [];
            cur.push(j["DESCRIPTION"]);
            cur.push(parseInt(j["ct"]));
            result.push(cur);
          }
          // alert(result)
          // console.log(result)
          // vm.chartData = result.slice(0,11)
          vm.chartData = result;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
  mounted() {
    this.createGraph();
  },
};
</script>