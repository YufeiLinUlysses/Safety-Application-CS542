<template>
  <b-container>
    <b-row>
      <b-col cols="8"><BAR /></b-col>
      <b-col cols="2"><PIE1 /></b-col>
      <b-col cols="2"><PIE2 /></b-col>
    </b-row>
  </b-container>
</template>

<script>
import BAR from "./barchart.vue";
import PIE1 from "./piechart1.vue";
import PIE2 from "./piechart2.vue";

export default {
  components: { BAR, PIE1, PIE2 },
};
</script>