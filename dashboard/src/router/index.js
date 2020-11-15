import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import WA from '../views/WeatherAnalysis.vue'
import CA from '../views/CriminalAnalysis.vue'
import LA from '../views/LocationAnalysis.vue'
import TT from '../views/Test_Torres.vue'
import TS from '../views/Test_Sophia.vue'
import TJ from '../views/Test_Jeff.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/weatherAnalysis',
    name: 'WA',
    component: WA
  },
  {
    path: '/crimeAnalysis',
    name: 'CA',
    component: CA
  },
  {
    path: '/locAnalysis',
    name: 'LA',
    component: LA
  },
  {
    path: '/testTorres',
    name: 'tt',
    component: TT
  },
  {
    path: '/testJeff',
    name: 'tj',
    component: TJ
  },
  {
    path: '/testSophia',
    name: 'ts',
    component: TS
  },
]

const router = new VueRouter({
  routes
})

export default router
