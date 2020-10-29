import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import WA from '../views/WeatherAnalysis.vue'
import CA from '../views/CriminalAnalysis.vue'

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
]

const router = new VueRouter({
  routes
})

export default router
