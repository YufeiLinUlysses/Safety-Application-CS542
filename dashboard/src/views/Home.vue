<template>
  <div class="home">
    <b-row>
      <b-col>
        <GM />
      </b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import GM from "@/components/googleMap.vue";
//eslint-disabled
export default {
  name: "Home",
  components: {
    GM,
  },
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("updateLoc", null);
  },
  methods: {},
};
</script>
