<template>
  <div class="home">
    <!-- <VIS /> -->
    <!-- <MAP /> -->
    <b-row>
      <b-col></b-col>
      <b-col><BM /></b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import BM from "@/components/graphs/map.vue";
export default {
  name: "Home",
  components: {
    BM,
  },
};
</script>
