<template>
  <div class="leading-normal tracking-normal" id="main-body">
    <div class="flex flex-wrap">
      <div
        class="w-1/2 md:w-1/3 lg:w-64 fixed md:top-0 md:left-0 h-screen lg:block bg-gray-100 border-r z-30"
        :class="sideBarOpen ? '' : 'hidden'"
        id="main-nav"
      >
        <div class="w-full h-20 border-b flex px-4 items-center mb-8">
          <img
            src="../assets/naginie.png"
            class=""
            style="width: 64px;"
            @click="dropDownOpen = !dropDownOpen"
          />
          <p class="font-semibold text-3xl text-teal-400 pl-4">
            Naginie
          </p>
        </div>

        <div class="mb-4 px-4">
          <p class="pl-4 text-sm font-semibold mb-1">MAIN</p>
          <NavLink
            to="/"
            icon="tachometer-alt"
            title="Dashboard"
            :current="this.$route.path"
          />
          <NavLink
            to="/directories/"
            icon="sitemap"
            title="Directories"
            :current="this.$route.path"
          />
          <NavLink
            to="/files/"
            icon="file-code"
            title="Files"
            :current="this.$route.path"
          />
        </div>

        <div class="mb-4 px-4">
          <p class="pl-4 text-sm font-semibold mb-1">USERS</p>
          <NavLink
            to="/users/"
            icon="users"
            title="Users"
            :current="this.$route.path"
          />
          <NavLink
            to="/roles/"
            icon="user-tag"
            title="Roles"
            :current="this.$route.path"
          />
        </div>

        <div class="mb-4 px-4">
          <p class="pl-4 text-sm font-semibold mb-1">MISC</p>
          <NavLink
            to="/settings/"
            icon="cogs"
            title="Settings"
            :current="this.$route.path"
          />
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
                  class="hover:text-teal-500 hover:border-white focus:outline-none navbar-burger"
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


            </div>

            <div class="flex items-center relative">
              <p class="mr-4" @click="dropDownOpen = !dropDownOpen">
                Ho, hi {{ user.nicename }}!
              </p>
            </div>
          </div>

          <div
            class="absolute bg-gray-100 border border-t-0 shadow-xl text-gray-700 rounded-b-lg w-48 bottom-10 right-0 mr-6"
            :class="dropDownOpen ? '' : 'hidden'"
          >
            <a href="#" class="block px-4 py-2 hover:bg-gray-200">Account</a>
            <a
              @click="logout"
              href="javascript:void(0);"
              class="block px-4 py-2 hover:bg-gray-200"
              >Logout</a
            >
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
                    <flash-message />

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import NavLink from "@/components/NavLink";

export default {
  name: "Dashboard",
  components: {
    NavLink
  },
  computed: {
    ...mapState(["sideBarOpen", "user"])
  },
  data() {
    return {
      dropDownOpen: false
    };
  },
  methods: {
    toggleSidebar() {
      this.$store.dispatch("toggleSidebar");
    },
    logout() {
      this.$store.dispatch("logout").then(() => this.$router.go("/"));
    }
  }
};
</script>
