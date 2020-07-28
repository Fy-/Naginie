<template>
  <table class="border-collapse w-full">
    <thead>
      <tr>
        <th
          v-for="(title, property) in headers"
          v-bind:key="property"
          class="p-3 font-bold uppercase bg-teal-600 text-gray-200 squared border border-teal-700 hidden lg:table-cell"
        >
          {{ title }}
        </th>
      </tr>
    </thead>
    <tbody>
      <template v-for="item in data">
        <tr
          v-bind:key="item.id"
          class=" lg:hover:bg-gray-700 flex lg:table-row flex-row lg:flex-row flex-wrap lg:flex-no-wrap mb-10 lg:mb-0 bg-gray-800"
        >
          <template v-for="(title, property) in headers">
            <td
              v-bind:key="`${property}_${item.id}`"
              class="w-full border-b border-teal-700 lg:w-auto p-3 text-gray-300  text-center  block lg:table-cell relative lg:static "
            >
              <span
                class="lg:hidden absolute top-0 left-0 bg-teal-700 text-gray-200 px-2 py-1 text-xs font-bold uppercase"
                >{{ title }}</span
              >
              <slot
                :name="`${property}_item`"
                v-bind:data="{ prop: item[property], id: item.id, item: item }"
              >
                {{ item[property] }}
              </slot>
            </td>
          </template>
        </tr>
      </template>
    </tbody>
  </table>
</template>
<script>
//import { EventBus } from "@/helpers/utils";

export default {
  name: "DataTable",
  props: {
    headers: {
      type: Object,
      default() {
        return {};
      }
    },
    data: {
      type: Array,
      default() {
        return [];
      }
    }
  }
};
</script>
