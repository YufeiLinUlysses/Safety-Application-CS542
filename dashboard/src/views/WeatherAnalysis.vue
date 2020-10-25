<template>
  <div>
    <b-row>
      <b-col>
        <TLG :cols="colsT" :url="urlT" :co="chartsOptionT" />
        <TLG :cols="colsH" :url="urlH" :co="chartsOptionH" />
      </b-col>
      <b-col align-self="center">
        <WC />
      </b-col>
      <b-col>
        <TLG :cols="colsW" :url="urlW" :co="chartsOptionW" />
        <TLG :cols="colsP" :url="urlP" :co="chartsOptionP" />
      </b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import WC from "@/components/weatherWordCloud.vue";
import TLG from "@/components/temperatureLine.vue";
export default {
  name: "wa",
  components: {
    WC,
    TLG,
  },
  data() {
    return {
      urlW: "/windspeed",
      colsW: ["minW", "avgW", "maxW"],
      chartsOptionW: {
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
        colors: ["#77B6EA", "#545454", "#D3D3D3"],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
        },
        title: {
          text: "Summary of Wind Speed",
          align: "center",
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"],
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
            text: "Wind Speed (km/h)",
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
      urlP: "/precipitation",
      colsP: ["minP", "avgP", "maxP"],
      chartsOptionP: {
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
        colors: ["#77B6EA", "#545454", "#D3D3D3"],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
        },
        title: {
          text: "Summary of Precipitation",
          align: "center",
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"],
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
            text: "Precipitation (mm)",
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
      urlT: "/temperature",
      colsT: ["minT", "avgT", "maxT"],
      chartsOptionT: {
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
        colors: ["#77B6EA", "#545454", "#D3D3D3"],
        dataLabels: {
          enabled: false,
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
            colors: ["#f3f3f3", "transparent"],
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
      yaxisT: "Hi",
      urlH: "/humidity",
      colsH: ["minH", "avgH", "maxH"],
      chartsOptionH: {
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
        colors: ["#77B6EA", "#545454", "#D3D3D3"],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
        },
        title: {
          text: "Summary of Humidity",
          align: "center",
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"],
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
            text: "Humidity(%)",
          },
          max: 100,
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
};
</script>
