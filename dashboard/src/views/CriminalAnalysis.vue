<template>
  <div>
    <b-row>
      <b-col> </b-col>
      <b-col cols="8" align-self="center">
        <MAP />
      </b-col>
      <b-col> </b-col>
    </b-row>
    <b-row>
      <b-col align-self="center"><Hist /></b-col>
      <b-col align-self="center">
        <BarChart />
      </b-col>
      <b-col align-self="center"><PieChart /></b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import MAP from "@/components/map.vue";
import BarChart from "@/components/Barchart.vue";
import PieChart from "@/components/PieChart.vue";
import Hist from "@/components/hist.vue";

export default {
  name: "ca",
  components: {
    BarChart,
    MAP,
    PieChart,
    Hist,
  },
  data() {
    return {
      result: {},
      analysis: {
        humidity: {
          name: "Humidity",
          url: "/humCrime",
        },
      },
    };
  },
};
</script>
