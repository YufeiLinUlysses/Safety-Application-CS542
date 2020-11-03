<template>
  <div>
    <b-row>
      <b-col>
        <b-form-select
          v-model="selected"
          value-field="value"
          text-field="text"
          :options="temp"
          @change="fetchLine($event, selected)"
          style="width: 150px"
        >
          <template #first>
            <b-form-select-option :value="null" disabled
              >-- Please select an option --</b-form-select-option
            >
          </template>
        </b-form-select>
        <br />
        <br />

        <line-chart :data="result"></line-chart>
      </b-col>
      <b-col align-self="center">
        <WC />
      </b-col>
      <b-col> </b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import WC from "@/components/wCrimeWordCloud.vue";
import axios from "axios";

var webcall = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 20000,
  withCredentials: false,
  headers: { "Content-Type": "application/json" },
});

export default {
  name: "ca",
  components: {
    WC,
  },
  data() {
    return {
      result: {},
      selected: {
        url: "/humCrime",
        key: "humidity",
      },
      temp: [
        {
          text: "Humidity",
          value: {
            url: "/humCrime",
            key: "humidity",
          },
        },
        {
          text: "Temperature",
          value: {
            url: "/tempCrime",
            key: "temp",
          },
        },
        {
          text: "Wind Speed",
          value: {
            url: "/wsCrime",
            key: "ws",
          },
        },
        {
          text: "Precipitation",
          value: {
            url: "/preCrime",
            type: "pre",
          },
        },
      ],
      analysis: {
        humidity: {
          name: "Humidity",
          url: "/humCrime",
        },
      },
    };
  },
  mounted() {
    this.fetchLine(this.selected);
  },
  methods: {
    fetchLine: function (conn) {
      var vm = this;
      var key = conn.key;
      try {
        webcall.get(conn.url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          alert(response.data);
          var data = {};
          for (var m of temp) {
            data[m[key]] = parseInt(m["count"]);
          }
          vm.result = data;
          console.log(vm.result);
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
  },
};
</script>
