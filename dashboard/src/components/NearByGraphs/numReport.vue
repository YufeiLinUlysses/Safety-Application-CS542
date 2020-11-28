<template>
  <b-col class="text-center">
    <b-row
      ><div>
        Crime Count
        <p>{{ cnt }}</p>
      </div></b-row
    ><b-row></b-row>
    <div>
      Safety Index
      <p>{{ sI }}</p>
    </div>
  </b-col>
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
    return { sI: 0, cnt: 0 };
  },
  mounted() {
    this.createGraph();
    this.loadSafe();
  },
  methods: {
    createGraph() {
      var vm = this;
      var url = "/locCrimeCount";
      try {
        webcall
          .post(url, vm.$store.state.location)
          .then(async function (response) {
            var temp = await JSON.parse(JSON.stringify(response.data));
            console.log(temp);
            var result = temp[0].NUM;
            vm.cnt = result;
          });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
    loadSafe() {
      var vm = this;
      var url = "/safetyindex";
      var postData = {};
      var today = new Date();
      postData["lat"] = vm.$store.state.location.lat;
      postData["lng"] = vm.$store.state.location.lng;
      postData["month"] = today.getMonth();
      postData["day"] = today.getDay() == 7 ? 7 : today.getDay();
      postData["hour"] = today.getHours();
      try {
        webcall.post(url, postData).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          console.log(temp);
          var result = temp.SI;
          vm.sI = result;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>