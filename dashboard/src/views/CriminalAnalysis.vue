<template>
  <div>
    <b-row>
      <b-col>
        <!-- <TLG :cols="colsT" :url="urlT" :co="chartsOptionT" /> -->
        <LG :url="urlH" :co="chartsOptionH" :name="nameH" />
      </b-col>
      <b-col align-self="center">
        <WC />
      </b-col>
      <b-col>
        <!-- <TLG :cols="colsW" :url="urlW" :co="chartsOptionW" /> -->
        <!-- <TLG :cols="colsP" :url="urlP" :co="chartsOptionP" /> -->
      </b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import WC from "@/components/wCrimeWordCloud.vue";
import LG from "@/components/graphs/singleLine.vue";
export default {
  name: "ca",
  components: {
    WC,
    LG,
  },
  data() {
    return {
      nameH: "Humidity",
      urlH: "/humCrime",
      chartOptionsh: {
        chart: {
          height: 350,
          type: "line",
          zoom: {
            enabled: false,
          },
          animations: {
            enabled: false,
          },
        },
        stroke: {
          width: [5, 5, 4],
          curve: "straight",
        },
        labels: [5,10,15,20,25,30,35,40,55,60,65,70,75,80,85,90,95,100],
        title: {
          text: "Humidity-Crime Rate",
        },
        xaxis: {},
      },
    };
  },
};
</script>
