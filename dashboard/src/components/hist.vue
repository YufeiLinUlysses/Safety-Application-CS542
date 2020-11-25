<template>
  <div id="app">
    <b-form-select
      v-model="selected"
      value-field="value"
      text-field="text"
      :options="temp"
      @change="fetchLine($event, selected)"
      style="width: 150px"
    >
      <template #first>
        <b-form-select-option :value="null" disabled
          >-- Please select an option --</b-form-select-option
        >
      </template>
    </b-form-select>
    <br />
    <br />
    <h5 class="text-center">{{ curtitle }}</h5>
    <GChart type="Histogram" :data="chartData" :options="chartOptions" />
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
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [],
      chartOptions: {
        legend: {
          position: "none",
        },
      },
      curtitle: "",
      selected: {
        url: "/humCrime",
        key: "AVGH",
        title: "Humidity - Crime",
      },
      temp: [
        {
          text: "Humidity",
          value: {
            url: "/humCrime",
            key: "AVGH",
            title: "Humidity - Crime",
          },
        },
        {
          text: "Temperature",
          value: {
            url: "/tempCrime",
            key: "AVGT",
            title: "Temperature - Crime",
          },
        },
        {
          text: "Wind Speed",
          value: {
            url: "/wsCrime",
            key: "AVGW",
            title: "Wind Speed - Crime",
          },
        },
        {
          text: "Precipitation",
          value: {
            url: "/preCrime",
            key: "AVGP",
            title: "Precipitation - Crime",
          },
        },
      ],
    };
  },
  methods: {
    fetchLine: function (conn) {
      var vm = this;
      var key = conn.key;
      try {
        webcall.get(conn.url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [["T", key]];
          vm.curtitle = conn.title;
          for (var i of temp) {
            var cur = [];
            cur.push(i["T"]);
            cur.push(parseFloat(i[key]));
            result.push(cur);
          }
          vm.chartData = result;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
  mounted() {
    this.fetchLine(this.selected);
  },
};
</script>