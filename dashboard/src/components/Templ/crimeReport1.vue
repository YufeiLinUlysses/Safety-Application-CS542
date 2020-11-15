<template>
  <div>
    <div>
      <b-nav-item id="report" v-b-modal.modal-scrollable @click="show = true"
        ><b-icon icon="exclamation-triangle"></b-icon
      ></b-nav-item>
      <b-tooltip target="report" placement="bottom">
        <strong>Report Crime</strong>
      </b-tooltip>
      <b-modal
        v-model="show"
        id="modal-scrollable"
        scrollable
        title="Report A Crime"
      >
        <p class="my-4" v-for="i in 20" :key="i">
          Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
          dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
          consectetur ac, vestibulum at eros.
        </p>

        <template #modal-footer>
          <div>
            <!-- <p class="float-left">Modal Footer Content</p> -->
            <b-button
              variant="primary"
              size="sm"
              class="float-right"
              @click="reportCrime"
            >
              Submit
            </b-button>
            <b-button
              variant="outline-primary"
              size="sm"
              class="float-right mr-2"
              @click="show = false"
              >Close</b-button
            >
          </div>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
    };
  },
  methods: {
    reportCrime() {
      alert("Hi");
      this.show = false;
    },
  },
};
</script>