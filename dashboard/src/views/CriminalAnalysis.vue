<template>
  <div>
    <b-row>
      <b-col cols="6" md="4" align-self="center">
        <Hist />
      </b-col>
      <b-col cols="6" md="4" align-self="center">
        <MAP />
        <BarChart />
      </b-col>
      <b-col cols="6" md="4" align-self="center"> <PieChart /></b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
// import WC from "@/components/wCrimeWordCloud.vue";
import MAP from "@/components/map.vue";
import BarChart from "@/components/Barchart.vue";
import PieChart from "@/components/PieChart.vue";
import Hist from "@/components/hist.vue";
// import axios from "axios";

// var webcall = axios.create({
//   baseURL: "http://127.0.0.1:5000/",
//   timeout: 20000,
//   withCredentials: false,
//   headers: { "Content-Type": "application/json" },
// });

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
