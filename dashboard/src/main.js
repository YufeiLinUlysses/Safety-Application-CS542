import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';
import * as VueGoogleMaps from "vue2-google-maps";
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';


Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyCESDQdWk4BVXVLLwkKQijvexrPnU6UkAk",
    libraries: "places"
  }
});

Vue.component('v-selectbox', vSelect)
Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.use(Chartkick.use(Chart))
Vue.config.productionTip = false
Vue.use(IconsPlugin)
Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
