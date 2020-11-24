<template>
  <div>result:{{ result }}</div>
</template>

<script>
import axios from "axios";
var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});
export default {
  data() {
    return {
      result: [],
    };
  },
  mounted() {
    this.getLoc();
  },
  methods: {
    getLoc() {
      var vm = this;
      try {
        webcall
          .post("/locAnalysis", {
            latitude: 42.3315,
            longitude: -71.0709,
          })
          .then(async function (response) {
            vm.result = response.data;
            console.log(vm.result)
          });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>