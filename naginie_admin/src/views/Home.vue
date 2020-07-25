<template>
  <div id="home">
    <!-- breadcrumb -->
    <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
      <ol class="list-none p-0 inline-flex">
        <li class="flex items-center text-blue-500">
          <a href="#" class="text-gray-700 pr-4">Home</a>
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li class="flex items-center">
          <a href="#" class="text-gray-600 pl-4">Dashboard</a>
        </li>
      </ol>
    </nav>

    {{user}}
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Home",
  data() {
    return {};
  },
  computed: {
    ...mapState(["user"]),
  },
};
</script>
