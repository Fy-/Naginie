<template>
  <div id="home">
    <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
      <ol class="list-none p-0 inline-flex">
        <li class="flex items-center">
          <router-link to="/" class="text-teal-200 pr-4">Dashboard</router-link>
        </li>
      </ol>
    </nav>

    {{ user }}
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
    ...mapState(["user"])
  }
};
</script>
