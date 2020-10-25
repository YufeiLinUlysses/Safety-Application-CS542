<template>
  <div>
    <WC />
    <TLG :cols = "colsT" :url = "urlT"/>
    <TLG :cols = "colsH" :url = "urlH"/>

  </div>
</template>

<script>
// @ is an alias to /src
import WC from "@/components/weatherWordCloud.vue";
import TLG from "@/components/temperatureLine.vue";
export default {
  name: "wa",
  components: {
    WC,
    TLG,
  },
  data(){
    return{
      urlT:"/temperature",
      colsT:["minT","avgT","maxT"],
      urlH:"/humidity",
      colsH:["minH","avgH","maxH"],
    }
  }
};
</script>
