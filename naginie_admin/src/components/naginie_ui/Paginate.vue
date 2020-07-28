<template>
  <ul class="flex list-reset  w-auto float-right my-3" v-if="items.pages">
    <li v-if="items.has_prev">
      <a
        class="block hover:text-white hover:bg-teal-500 border-r border-teal-700  text-gray-300 px-3 py-2"
        href="javascript:void(0);"
        @click="prev()"
        >Previous</a
      >
    </li>
    <template v-for="i in items.pages">
      <li v-bind:key="i">
        <a
          v-if="i != items.page"
          class="block hover:text-white hover:bg-teal-500  text-gray-300 border-teal-700 border-r  px-3 py-2"
          href="javascript:void(0);"
          @click="page(i)"
          >{{ i }}</a
        >
        <a
          v-else
          class="block font-bold border-teal-700  hover:text-white text-gray-300 bg-teal-700 border-r  px-3 py-2"
          href="javascript:void(0);"
          >{{ i }}</a
        >
      </li>
    </template>
    <li v-if="items.has_next">
      <a
        class="block hover:text-white text-gray-300 hover:bg-teal-500 px-3 py-2"
        href="javascript:void(0);"
        @click="next()"
        >Next</a
      >
    </li>
  </ul>
</template>
<script>
import { EventBus } from "@/helpers/utils";
export default {
  name: "Paginate",
  props: {
    items: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  methods: {
    next() {
      EventBus.$emit("goToPage", this.items.page + 1);
    },
    prev() {
      EventBus.$emit("goToPage", this.items.page - 1);
    },
    page(page) {
      EventBus.$emit("goToPage", page);
    }
  }
};
</script>
