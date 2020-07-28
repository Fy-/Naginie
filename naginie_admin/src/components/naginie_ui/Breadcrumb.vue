<template>
  <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
    <ol class="list-none p-0 inline-flex">
      <template v-for="item in nav">
        <li
          v-if="item.to"
          class="flex items-center text-teal-200 pr-2"
          v-bind:key="item.to"
        >
          <router-link :to="item.to" class="text-gray-500 pr-2">{{
            item.name
          }}</router-link>
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li v-else class="flex items-center" v-bind:key="item.to">
          <span class="text-teal-200">{{ item.name }}</span>
        </li>
      </template>
    </ol>
  </nav>
</template>
<script>
export default {
  name: "Breadcrumb",
  props: {
    nav: {
      type: Array,
      default() {
        return [];
      }
    }
  }
};
</script>
