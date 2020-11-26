<template>
  <div>
    <b-nav-item v-b-modal.modal-prevent-closing id="report"
      ><b-icon icon="exclamation-triangle"></b-icon
    ></b-nav-item>
    <b-tooltip target="report" placement="bottom">
      <strong>Report Crime</strong>
    </b-tooltip>
    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Report A Crime"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
      scrollable
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <h4>Crime Info</h4>
        <b-form-group
          :state="nameState"
          label="Criminal"
          label-for="criminal"
          invalid-feedback="Name is required"
        >
          <b-form-input
            id="criminal"
            v-model="criminal"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          :state="nameState"
          label="Victim"
          label-for="victim"
          invalid-feedback="Name is required"
        >
          <b-form-input
            id="criminal"
            v-model="victim"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group label="Relation" label-for="cvr">
          <b-form-select
            id="cvr"
            v-model="relation"
            value-field="value"
            text-field="text"
            :options="relations"
            style="width: 150px"
          >
          </b-form-select>
        </b-form-group>
        <b-form-group label="Type" label-for="ctype">
          <v-selectbox
            v-model="type"
            label="text"
            :options="types"
          ></v-selectbox>
        </b-form-group>
        <h4>Date Time</h4>
        <b-form-group label="Date" label-for="Date">
          <b-form-input id="`date`" type="date" v-model="cdate"></b-form-input>
        </b-form-group>
        <b-form-group label="Time" label-for="time">
          <b-form-input id="`time`" type="time" v-model="ctime"></b-form-input>
        </b-form-group>
        <h4>Location</h4>
        <b-form-group
          :state="nameState"
          label="Latitude"
          label-for="lat"
          invalid-feedback="Longitude is required"
        >
          <b-form-input
            id="lat"
            v-model="latitude"
            :state="nameState"
            required
            type="number"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          :state="nameState"
          label="Longitude"
          label-for="lnt"
          invalid-feedback="Longitude is required"
        >
          <b-form-input
            id="lnt"
            v-model="longitude"
            :state="nameState"
            required
            type="number"
          ></b-form-input>
        </b-form-group>
        <b-form-group label="Police District" label-for="pd">
          <b-form-select
            id="pd"
            v-model="police"
            value-field="value"
            text-field="text"
            :options="policeD"
            style="width: 150px"
          >
          </b-form-select>
        </b-form-group>
      </form>
    </b-modal>
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
  components: {},
  data() {
    return {
      relation: "Not Known",
      police: "Not Known",
      name: "",
      criminal: "",
      cdate: null,
      ctime: null,
      victim: "",
      latitude: 0,
      longitude: 0,
      nameState: null,
      submittedNames: [],
      relations: [
        { text: "Family", value: "Family" },
        { text: "Friend", value: "Friend" },
        { text: "Foreign", value: "Foreign" },
      ],
      types: [
        { text: "Not Known", value: "Not Known" },
        { text: "Burglary", value: "Burglary" },
        { text: "Murder", value: "Murder" },
      ],
      policeD: [
        { text: "Not Known", value: "Not Known" },
        { text: "C12", value: "C12" },
        { text: "C13", value: "C13" },
      ],
      report: {},
    };
  },
  mounted() {
    this.loadDistrict();
    this.loadTypes();
  },
  methods: {
    loadTypes() {
      var vm = this;
      var url = "/ctypes";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [];
          for (var i of temp) {
            var cur = {};
            cur["text"] = i["DESCRIPTION"];
            cur["value"] = i["TYPEID"];
            result.push(cur);
          }
          vm.types = result;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
    loadDistrict() {
      var vm = this;
      var url = "/pds";
      try {
        webcall.get(url).then(async function (response) {
          var temp = await JSON.parse(JSON.stringify(response.data));
          var result = [];
          for (var i of temp) {
            var cur = {};
            cur["text"] = i["POLICE_DISTRICT"];
            cur["value"] = i["POLICE_DISTRICT"];
            result.push(cur);
          }
          vm.policeD = result;
        });
      } catch (err) {
        console.log("error");
        alert(err);
      }
    },
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid;
      return valid;
    },
    resetModal() {
      this.name = "";
      this.nameState = null;
      this.criminal = "";
      this.victim = "";
      this.relation = "Not Known";
      this.latitude = null;
      this.longitude = null;
      this.ctime = null;
      this.cdate = null;
      this.police = "Not Known";
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
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
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      this.report["Criminal"] = this.criminal;
      this.report["Victim"] = this.victim;
      this.report["Relation"] = this.relation;
      this.report["Type"] = this.type["value"];
      this.report["Latitude"] = this.latitude;
      this.report["Longitude"] = this.longitude;
      this.report["Date"] = this.cdate;
      var curTime = Number(this.ctime.split(":")[0]);
      this.report["Time"] = curTime - (curTime % 3);
      this.report["PoliceDistrict"] = this.police;
      console.log(this.report);

      var vm = this;
      try {
        webcall
          .post("/insertCrime", this.report)
          .then(async function (response) {
            if (response.data.success) {
              alert("Your report has been successfully inserted.");
            } else {
              alert("Please contact the database manager.");
            }
            vm.loadData();
          });
      } catch (err) {
        console.log("error");
        alert(err);
      }

      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide("modal-prevent-closing");
      });
    },
  },
};
</script>