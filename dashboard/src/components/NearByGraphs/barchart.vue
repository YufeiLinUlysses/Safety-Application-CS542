<!--author: xli14@WPI.EDU-->

<template>
  <div id="app" class="mt-3" v-if="show">
    <h5 class="text-center">Hour Frequency</h5>
    <br />
    <GChart
      :settings="{ packages: ['bar'] }"
      :data="chartData"
      :options="chartOptions"
      :createChart="(el, google) => new google.charts.Bar(el)"
      @ready="onChartReady"
    />
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
import axios from "axios";

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
      show: true,
      chartsLib: null,
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [],
      //setting: {packages:["corechart"]}
    };
  },
  computed: {
    chartOptions() {
      if (!this.chartsLib) return null;
      return this.chartsLib.charts.Bar.convertOptions({
        bars: "horizontal", // Required for Material Bar Charts.
        hAxis: {
          title: "Count",
          minxValue: 112,
          gridlines: { count: 10 },
          format: "decimal",
          direction: -1,
          // baselineColor: 'red',
          // textStyle: {color: 'pink'},
          // ticks: [500,1000,1500,2000,]
          // baselineColor: 'red'
        },
        vAxis: {
          title: "Hour of the Day",
          baselineColor: "red",
          minValue: 112,
          direction: -1,
          // ticks: [500,1000,1500,2000,]
          // gridlines: { count: 10 }
        },
        height: 300,
        bar: { groupWidth: "75%" },
        colors: ["#7570b3"],
        legend: { position: "none" },
        // backgroundColor: 'red'
        // isStacked: true
      });
    },
  },
  methods: {
    onChartReady(chart, google) {
      this.chartsLib = google;
    },
    createGraph() {
      var vm = this;
      var url = "/locTimeCount";
      try {
        webcall
          .post(url, vm.$store.state.location)
          .then(async function (response) {
            var temp = await JSON.parse(JSON.stringify(response.data));
            if (temp.length <= 1 || temp.length == undefined) {
              vm.show = false;
            } else {
              var result = [["TIMESLOT", "NUM"]];
              for (var i of temp) {
                var cur = [];
                cur.push(i["TIMESLOT"]);
                cur.push(parseInt(i["NUM"]));
                result.push(cur);
              }
              vm.chartData = result.slice(0, 11);
            }
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
