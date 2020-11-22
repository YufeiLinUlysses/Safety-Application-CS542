<template>
  <div>
    <b-table :items="items" :fields="fields" striped responsive="sm">
      <template #cell(confirmed)="row">
        <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
        <b-form-checkbox v-model="row.item.confirmed"></b-form-checkbox>
      </template>
    </b-table>
    <div class="text-right">
      <b-button @click="submitChanges">Submit</b-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fields: ["first_name", "last_name", "age", "confirmed"],
      items: [
        {
          age: 40,
          first_name: "Dickerson",
          last_name: "Macdonald",
          confirmed: false,
        },
        { age: 21, first_name: "Larsen", last_name: "Shaw", confirmed: false },
        {
          age: 89,
          first_name: "Geneva",
          last_name: "Wilson",
          confirmed: false,
        },
        { age: 38, first_name: "Jami", last_name: "Carney", confirmed: false },
      ],
    };
  },
  methods: {
    submitChanges() {
      console.log(this.items);
    },
  },
};
</script>