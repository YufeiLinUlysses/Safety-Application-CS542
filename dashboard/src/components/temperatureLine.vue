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
  props:["url","cols"],
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          height: 350,
          type: "line",
          dropShadow: {
            enabled: true,
            color: "#000",
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2,
          },
          toolbar: {
            show: false,
          },
        },
        colors: ["#77B6EA", "#545454","#D3D3D3"],
        dataLabels: {
          enabled: true,
        },
        stroke: {
          curve: "smooth",
        },
        title: {
          text: "Summary of Temperature",
          align: "center",
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5,
          },
        },
        markers: {
          size: 1,
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ],
          title: {
            text: "Month",
          },
        },
        yaxis: {
          title: {
            text: "Temperature(°C)",
          },
        },
        legend: {
          position: "top",
          horizontalAlign: "right",
          floating: true,
          offsetY: -25,
          offsetX: -5,
        },
      },
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData: function () {
      var vm = this;
      var url =this.url;
      var cols = this.cols;
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
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>