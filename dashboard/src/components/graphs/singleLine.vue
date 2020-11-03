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
  props: ["url", "co", "name"],
  data() {
    return {
      series: [],
      chartOptions: {},
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData: function () {
      var vm = this;
      var url = this.url;
      var co = this.co;
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var data = []
          for(var m of temp){
              data[m["humidity"]] = m["count"]
          }
          console.log(data)
          vm.series = [{
              name:vm.name,
              data:data
          }];
          vm.chartOptions = co;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>