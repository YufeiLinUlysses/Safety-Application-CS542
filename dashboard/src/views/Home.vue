<template>
  <div class="home">
    <vis/>
    <MAP/>
  </div>
</template>

<script>
// @ is an alias to /src
import vis from '@/components/d3vis.vue'
import MAP from '@/components/d3map.vue'

export default {
  name: 'Home',
  components: {
    vis,
    MAP
  }
}
</script>
