<template>
  <div>
    <b-table :items="items" :fields="fields" striped responsive="sm">
      <template #cell(confirmed)="row">
        <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
        <b-form-checkbox v-model="row.item.Confirmed"></b-form-checkbox>
      </template>
    </b-table>
    <div class="text-right">
      <b-button @click="submitChanges">Submit</b-button>
    </div>
  </div>
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
      reloading: true,
      fields: [
        "ID",
        "Lat",
        "Lng",
        "Police_District",
        "Date",
        "Hour",
        "Relation",
        "CriminalID",
        "VictimID",
        "CrimeType",
        "Confirmed",
      ],
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {
    items() {
      return this.$store.state.table;
    },
  },
  methods: {
    loadData() {
      var vm = this;
      try {
        webcall.get("/requestInsert").then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [];
          for (var i of temp) {
            var cur = {};
            cur["ID"] = i["InsertID"];
            cur["Lat"] = i["LAT"];
            cur["Lng"] = i["LON"];
            var curT = new Date(i["TIMESTAMP"] * 1000);
            cur["Date"] =
              curT.getFullYear() + "-" + curT.getMonth() + "-" + curT.getDate();
            cur["Hour"] = i["TIMESLOT"];
            cur["Relation"] = i["Relation"];
            cur["CriminalID"] = i["CriminalID"];
            cur["VictimID"] = i["VictimID"];
            cur["CrimeType"] = i["CrimeType"];
            cur["Police_District"] = i["POLICE_DISTRICT"];
            cur["Confirmed"] = false;
            result.push(cur);
          }
          vm.$store.commit("updateTable", result);
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
    submitChanges() {
      var vm = this;
      var result = [];
      for (var i of this.items) {
        var cur = {};
        if (i["Confirmed"]) {
          cur["ID"] = i["ID"];
          cur["Confirmed"] = i["Confirmed"];
          result.push(cur);
        }
      }
      var final = JSON.stringify(result);
      webcall.post("/crimeConfirm", final).then(async function (response) {
        var temp = await JSON.parse(JSON.stringify(response.data));
        var result = [];
        for (var i of temp) {
          var cur = {};
          cur["ID"] = i["InsertID"];
          cur["Lat"] = i["LAT"];
          cur["Lng"] = i["LON"];
          var curT = new Date(i["TIMESTAMP"] * 1000);
          cur["Date"] =
            curT.getFullYear() + "-" + curT.getMonth() + "-" + curT.getDate();
          cur["Hour"] = i["TIMESLOT"];
          cur["Relation"] = i["Relation"];
          cur["CriminalID"] = i["CriminalID"];
          cur["VictimID"] = i["VictimID"];
          cur["CrimeType"] = i["CrimeType"];
          cur["Police_District"] = i["POLICE_DISTRICT"];
          cur["Confirmed"] = false;
          result.push(cur);
        }
        vm.$store.commit("updateTable", result);
      });
      console.log(result);
    },
  },
};
</script>