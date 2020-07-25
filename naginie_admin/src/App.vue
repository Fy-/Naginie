<template>
  <div id="app">
    <Dashboard v-if="isAuthenticated" />
    <Login v-else />
  </div>
</template>

<script>
import Dashboard from "./views/Dashboard";
import Login from "./views/Login";
export default {
  name: "app",
  components: {
    Dashboard,
    Login
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  }
};
</script>
