<template>
  <div class="home">
    <!-- <VIS /> -->
    <!-- <MAP /> -->
    <b-row>
      <b-col></b-col>
      <b-col>
        <!-- <BM /> -->
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d188820.8050329451!2d-71.11036833173107!3d42.314264701709575!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e3652d0d3d311b%3A0x787cbf240162e8a0!2z6bq76JCo6K-45aGe5bee5rOi5aOr6aG_!5e0!3m2!1szh-CN!2sus!4v1603893965257!5m2!1sEN!2sus"
          :width="windWidth"
          :height="windHeight"
          frameborder="0"
          style="border: 0"
          allowfullscreen=""
          aria-hidden="false"
          tabindex="0"
        ></iframe>
      </b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
// import BM from "@/components/graphs/map.vue";
//eslint-disabled
export default {
  name: "Home",
  components: {
    // BM,
  },
  data() {
    return {
      windHeight: 0,
      windWidth: 0,
    };
  },
  mounted() {
    this.$nextTick(function () {
      window.addEventListener("resize", this.winH);
      window.addEventListener("resize", this.winW);

      //Init
      this.winH();
      this.winW();
    });
  },

  methods: {
    winH: function () {
      this.windHeight = document.documentElement.clientHeight;
    },
    winW: function () {
      this.windWidth = document.documentElement.clientWidth;
    },
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.winW);
    window.removeEventListener("resize", this.winH);
  },
};
</script>
