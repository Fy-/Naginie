<template>
  <div id="home">
    <n-breadcrumb :nav="[{ name: 'Dashboard' }]" />

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
