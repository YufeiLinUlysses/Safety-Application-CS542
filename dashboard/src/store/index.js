import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    location: null,
  },
  getters: {
    locToString: (state) => {
      var result = null
      try {
        result = String(state.location.lat) + ", " + String(state.location.lng)
      }
      catch {
        result = null
      }
      return result
    }
  },
  mutations: {
    updateLoc: (state, newLoc) => {
      state.location = newLoc
    }
  },
  actions: {
    updateLoc: (context, newLoc) => {
      context.commit("updateLoc", newLoc)
    }
  },
  modules: {
  }
})
