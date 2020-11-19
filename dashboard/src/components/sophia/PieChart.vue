// author: LI Xiuhan

<template>
  <div id="app">
    <GChart
      type="PieChart"
      :data="chartData"
      :options="chartOptions"
      style="width: 900px; height: 500px"
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
      var url = "/typecnt";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [['DESCRIPTION', 'ct']]
          for(var i of temp){
            var cur = []
            cur.push(i['DESCRIPTION'])
            cur.push(parseInt(i['ct']))
            result.push(cur)
          }
          // alert(result)
          // console.log(result)
          // vm.chartData = result.slice(0,11)
          vm.chartData = result
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