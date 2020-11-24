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
          <b-form-select
            id="ctype"
            v-model="type"
            value-field="value"
            text-field="text"
            :options="types"
            style="width: 150px"
          >
          </b-form-select>
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
  data() {
    return {
      relation: "Not Known",
      type: "Not Known",
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
        { text: "Not Known", value: "Not Known" },
        { text: "Friend", value: "Friend" },
        { text: "Lovers", value: "Lovers" },
      ],
      types: [
        { text: "Not Known", value: "Not Known" },
        { text: "Burglary", value: "Burglary" },
        { text: "Murder", value: "Murder" },
      ],
      report: {},
    };
  },
  components: {},
  methods: {
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
      this.type = "Not Known";
      this.name = "";
      this.latitude = null;
      this.longitude = null;
      this.ctime = null;
      this.cdate = null;
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      this.report["Criminal"] = this.criminal;
      this.report["Victim"] = this.victim;
      this.report["Relation"] = this.relation;
      this.report["Type"] = this.type;
      this.report["Latitude"] = this.latitude;
      this.report["Longitude"] = this.longitude;
      this.report["Date"] = this.cdate;
      var curTime = Number(this.ctime.split(":")[0]);
      this.report["Time"] = curTime - (curTime % 3);
      console.log(this.report);

      var vm = this;
      try {
        webcall
          .post("/insertCrime", this.report)
          .then(async function (response) {
            vm.result = response.data;
            console.log(response.data);
            console.log(vm.result);
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