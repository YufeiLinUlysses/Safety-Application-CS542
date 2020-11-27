<template>
  <div>
    <b-nav-item v-b-modal="'adminPage'" id="login"
      ><b-icon icon="person-circle"></b-icon
    ></b-nav-item>
    <b-tooltip target="login" placement="bottom">
      <strong>Admin</strong>
    </b-tooltip>
    <b-modal
      id="adminPage"
      title="Log In as Administrator"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
      scrollable
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <h4>User Name</h4>
        <b-form-group
          :state="nameState"
          label="Username"
          label-for="usr"
          invalid-feedback="Name is required"
        >
          <b-form-input
            id="usr"
            v-model="usr"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          :state="nameState"
          label="Password"
          label-for="pwd"
          invalid-feedback="Password is required"
        >
          <b-form-input
            id="pwd"
            type="password"
            v-model="pwd"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      usr: null,
      pwd: null,
    };
  },
  mounted() {},
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid;
      return valid;
    },
    resetModal() {
      this.usr = null;
      this.pwd = null;
      this.nameState = null;
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
      if (this.usr == "Admin" && this.pwd == "Admin") {
        this.$router.push({ name: "ADM" });
      } else {
        alert("Wrong Username or Password");
      }

      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide("adminPage");
      });
    },
  },
};
</script>