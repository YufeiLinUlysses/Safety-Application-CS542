<template>
  <div id="cloud">
    <h3 class="text-center">Top 10 Weather with Most Crimes in Boston</h3>
    <cloud :words="weathers" :nameK="temp[0]" :valueK="temp[1]"/>
  </div>
</template>

<script>
import Cloud from "@/components/graphs/cloud.vue";
import axios from "axios";

var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  name: "app",
  components: {
    Cloud,
  },
  data() {
    return {
      weathers: [],
      temp:["weather","value"],
      fontSizeMapper: (word) => Math.log2(word.value) * 5,
    };
  },
  mounted() {
    this.createGraph();
  },
  methods: {
    createGraph() {
      var vm = this;
      var url = "/weatherCrime";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          vm.weathers = temp;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>