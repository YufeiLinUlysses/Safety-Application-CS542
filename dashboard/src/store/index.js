import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    location: null,
    status: true,
    table: [],
  },
  getters: {
    locToString: (state) => {
      var result = null
      if (state.status) {
        try {
          result = String(state.location.lat) + ", " + String(state.location.lng)
        }
        catch {
          result = null
        }
      }
      return result
    }
  },
  mutations: {
    updateLoc: (state, newLoc) => {
      state.location = newLoc
    },
    updateStatus: (state, newStatus) => {
      state.status = newStatus
    },
    updateTable: (state, newTable) => {
      state.table = newTable
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
