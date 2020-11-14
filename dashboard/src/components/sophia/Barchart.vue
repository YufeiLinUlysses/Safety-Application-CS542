#author: xli14@WPI.EDU

<template>
  <div id='app'>
  <GChart
    :settings="{packages: ['bar']}"    
    :data="chartData"
    :options="chartOptions"
    :createChart="(el, google) => new google.charts.Bar(el)"
    @ready="onChartReady"
  />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import axios from "axios";

var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  name: 'App',
  components: {
    GChart
  },
  data () {
    return {
      chartsLib: null, 
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        // ['Whether', 'frequency', {role: 'style'}],
        // ['sunny', 1000, 'stroke-color: pink, stroke-width: 100, fill-color:silver'],
        // ['cloudy', 999, 'color:silver'],
        // ['rainy', 876, 'color: blue'],
        // ['snowy', 666, 'color: silver'],
        // ['sandy', 530, 'color: silver'],
        // ['windy', 330, 'color: silver'],
        // ['thunder', 270, 'color: silver'],
        // ['lightening', 93, 'color:silver'],
        // ['hail', 77,'#76A7FA'],
        // ['ratyphooniny', 12,'color:silver'],
        // [result[0]['weather'], result[0]['cnt'],'color:silver'],
      ],
      //setting: {packages:["corechart"]}
    }
  },
  computed: {
    chartOptions () {
      if (!this.chartsLib) return null
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: 'Weather frequency',
          subtitle: 'Here is our subtitle'
        },
        bars: 'horizontal', // Required for Material Bar Charts.
        hAxis: { format: 'decimal' },
        height: 400,
        colors: ['#1b9e77', '#d95f02', '#7570b3'],
        //isStacked: true
      })
    }
  },
  methods: {
    onChartReady (chart, google) {
      this.chartsLib = google
    },
    createGraph() {
      var vm = this;
      var url = "/weathercnt";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [['text', 'value']]
          for(var i of temp){
            var cur = []
            cur.push(i['text'])
            cur.push(i['value'])
            result.push(cur)
          }
          // alert(result)
          // console.log(result)
          vm.chartData = result.slice(0,11)
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
}
</script>
