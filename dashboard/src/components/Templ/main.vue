<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#" @click="home('Home')">
        Safety Application
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item disabled>For People in Boston</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item @click="goto('About')">About</b-nav-item>
          <!-- If want to replace with more fancy writing 
            <template #button-content>
              <em>User</em>
            </template> -->
          <b-nav-item-dropdown text="Analysis" right>
            <b-dropdown-item @click="goto('WA')"
              >Weather Analysis</b-dropdown-item
            >
            <b-dropdown-item @click="goto('CA')"
              >Crime Analysis</b-dropdown-item
            >
          </b-nav-item-dropdown>
          <CR />
          <ADMIN />
          <v-spacer />
          <b-nav-form>
            <b-form-input
              size="sm"
              class="mr-sm-2"
              placeholder="Search"
              :value="getValue"
            ></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" @click="search('LA')"
              >Search</b-button
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import CR from "./crimeReport.vue";
import ADMIN from "./admin.vue";
export default {
  data() {
    return {
      location: null,
      searchLoc: null,
    };
  },
  components: {
    CR,
    ADMIN,
  },
  methods: {
    goto: function (page) {
      this.$router.push({ name: page });
    },
    search: function (page) {
      if (this.$store.getters.locToString === null) {
        alert("Please Select A Location");
      } else {
        this.$store.commit("updateStatus", false);
        this.$router.push({ name: page });
      }
    },
    home: function (page) {
      this.$store.dispatch("updateLoc", null);
      this.$store.commit("updateStatus", true);
      this.$router.push({ name: page });
    },
  },
  computed: {
    getValue() {
      return this.$store.getters.locToString;
    },
  },
};
</script>

<style scoped>
.navbar.navbar-dark.bg-dark {
  background-color: #557cbb !important;
}
</style>