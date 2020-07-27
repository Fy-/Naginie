<template>
  <router-link
    v-if="to == current || (current.includes(to) && to != '/')"
    :to="to"
    class="w-full flex items-center text-teal-400 h-10 pl-4  rounded-lg cursor-pointer bg-gray-700 hover:bg-gray-800 text-teal-200"
  >
    <font-awesome-icon :icon="icon"></font-awesome-icon>
    <span class="text-teal-300  pl-4">{{ title }}</span>
  </router-link>

  <router-link
    v-else
    :to="to"
    class="w-full flex items-center text-teal-400  h-10 pl-4 rounded-lg cursor-pointer hover:bg-gray-800 text-teal-200 "
  >
    <font-awesome-icon :icon="icon"></font-awesome-icon>
    <span class="text-gray-400 pl-4">{{ title }}</span>
  </router-link>
</template>
<script>
export default {
  name: "NavLink",
  props: {
    to: {
      type: String,
      default() {
        return "/";
      }
    },
    current: {
      type: String,
      default() {
        return "/";
      }
    },
    title: {
      type: String,
      default() {
        return "Dashboard";
      }
    },
    icon: {
      type: String,
      default() {
        return "icon";
      }
    }
  }
};
</script>
