<template>
  <div id="app">
    <div class="leading-normal tracking-normal" id="main-body">
      <div class="flex flex-wrap">
        <div
          class="w-1/2 md:w-1/3 lg:w-64 fixed md:top-0 md:left-0 h-screen lg:block bg-gray-100 border-r z-30"
          :class="sideBarOpen ? '' : 'hidden'"
          id="main-nav"
        >
          <div class="w-full h-20 border-b flex px-4 items-center mb-8">
            <p class="font-semibold text-3xl text-blue-400 pl-4">
              Naginie
            </p>
          </div>

          <div class="mb-4 px-4">
            <p class="pl-4 text-sm font-semibold mb-1">MAIN</p>
            <div
              class="w-full flex items-center text-blue-400 h-10 pl-4 bg-gray-200 hover:bg-gray-200 rounded-lg cursor-pointer"
            >
              <font-awesome-icon icon="user-secret"></font-awesome-icon>

              <span class="text-gray-700 pl-4">Dashboard</span>
            </div>
          </div>

          <div class="mb-4 px-4">
            <p class="pl-4 text-sm font-semibold mb-1">MISC</p>

            <div
              class="w-full flex items-center text-blue-400 h-10 pl-4 hover:bg-gray-200 rounded-lg cursor-pointer"
            >
              <font-awesome-icon icon="user-secret"></font-awesome-icon>
              <span class="text-gray-700 pl-4">Settings</span>
            </div>
          </div>
        </div>

        <div
          class="w-full bg-gray-100 pl-0 lg:pl-64 min-h-screen"
          :class="sideBarOpen ? 'overlay' : ''"
          id="main-content"
        >
          <div class="sticky top-0 z-40">
            <div
              class="w-full h-20 px-6 bg-gray-100 border-b flex items-center justify-between"
            >
              <div class="flex">
                <div class="inline-block lg:hidden flex items-center mr-4">
                  <button
                    class="hover:text-blue-500 hover:border-white focus:outline-none navbar-burger"
                    @click="toggleSidebar()"
                  >
                    <svg
                      class="h-5 w-5"
                      viewBox="0 0 20 20"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <title>Menu</title>
                      <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
                    </svg>
                  </button>
                </div>

                <div class="relative text-gray-600">
                  <input
                    type="search"
                    name="serch"
                    placeholder="Search products..."
                    class="bg-white h-10 w-full xl:w-64 px-5 rounded-lg border text-sm focus:outline-none"
                  />
                  <button
                    type="submit"
                    class="absolute right-0 top-0 mt-3 mr-4"
                  ></button>
                </div>
              </div>

              <div class="flex items-center relative">
                <img
                  src="https://a7sas.net/wp-content/uploads/2019/07/4060.jpeg"
                  class="w-12 h-12 rounded-full shadow-lg"
                  @click="dropDownOpen = !dropDownOpen"
                />
              </div>
            </div>

            <div
              class="absolute bg-gray-100 border border-t-0 shadow-xl text-gray-700 rounded-b-lg w-48 bottom-10 right-0 mr-6"
              :class="dropDownOpen ? '' : 'hidden'"
            >
              <a href="#" class="block px-4 py-2 hover:bg-gray-200">Account</a>
              <a href="#" class="block px-4 py-2 hover:bg-gray-200">Logout</a>
            </div>
          </div>

          <div class="p-6 bg-gray-100 mb-20">
            <router-view />
          </div>

          <div
            class="w-full border-t-2 px-8 py-6 lg:flex justify-between items-center"
          >
            <p class="mb-2 lg:mb-0">
              Powered by Naginie, made with ❤
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "app",

  computed: {
    ...mapState(["sideBarOpen"])
  },
  data() {
    return {
      dropDownOpen: false
    };
  },
  methods: {
    toggleSidebar() {
      this.$store.dispatch("toggleSidebar");
    }
  }
};
</script>
