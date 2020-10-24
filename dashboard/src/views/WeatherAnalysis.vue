<template>
  <div class="home">
    <!-- <VIS /> -->
    <!-- <MAP /> -->
    <WC />
  </div>
</template>

<script>
// @ is an alias to /src
// import VIS from "@/components/d3vis.vue";
// import MAP from "@/components/d3map.vue";
import WC from "@/components/weatherWordCloud.vue"
export default {
  name: "Home",
  components: {
    // VIS,
    // MAP,
    WC,
  },
};
</script>
