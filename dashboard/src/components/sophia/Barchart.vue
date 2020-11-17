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
        
      ]
      //setting: {packages:["corechart"]}
    }
  },
  computed: {
    chartOptions () {
      if (!this.chartsLib) return null
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: 'Weather frequency',
          // subtitle: '我才不会那么轻易狗带'
        },
        bars: 'horizontal', // Required for Material Bar Charts.
        hAxis: {
            title: 'here is your x-axis title',
            minxValue: 112, 
            gridlines: { count: 10 },
            format: 'decimal', 
            direction: -1,
            // baselineColor: 'red',
            // textStyle: {color: 'pink'},
            // ticks: [500,1000,1500,2000,] 
            // baselineColor: 'red'
        },
        vAxis: {
            title: 'here is your y-axis title',
            baselineColor: 'red',
            minValue: 112,
            direction: -1 ,
            // ticks: [500,1000,1500,2000,] 
            // gridlines: { count: 10 }
        },
        height: 400,
        bar: {groupWidth: '75%'},
        colors: ['#7570b3'],
        legend: { position: 'none' }
        // backgroundColor: 'red'
        // isStacked: true
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
            cur.push(parseInt(i['value']))
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
    }
  },
  mounted() {
    this.createGraph();
  }
}
</script>
