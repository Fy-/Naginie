<template
  ><div class="flex h-screen bg-gray-300">
    <div class="m-auto">
      <div class="w-full max-w-xs">
        <form
          class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
          @submit="authenticate"
          id="login_form"
        >
          <div class="w-full border-b flex  items-center mb-4">
                    <img
              src="../assets/naginie.png"
              style="width: 70px;"
              class="mr-4"
              @click="dropDownOpen = !dropDownOpen"
            />
            <p class="font-semibold text-3xl text-blue-400 ">
              Naginie
            </p>
          </div>
          <div class="mb-4">
            <label
              class="block text-gray-700 text-sm font-bold mb-2"
              for="email"
            >
              E-Mail
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="email"
              type="email"
              placeholder="Email"
              v-model="email"
              tabindex="0"
              autocomplete="email"
            />
          </div>
          <div class="mb-6">
            <label
              class="block text-gray-700 text-sm font-bold mb-2"
              for="password"
            >
              Password
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="password"
              type="password"
              v-model="password"
              placeholder="Password"
              tabindex="0"
              autocomplete="password"
            />
          </div>
          <div class="mb-6">
            <p class="text-red-500 text-xs italic" v-if="errorMsg">
              {{ errorMsg }}
            </p>
          </div>
          <div class="flex items-center justify-between">
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit"
            >
              Sign In
            </button>
            <!--<a
              class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
              href="#"
            >
              Forgot Password?
            </a>-->
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { EventBus } from "@/helpers/utils";

export default {
  data() {
    return {
      email: "",
      password: "",
      errorMsg: ""
    };
  },
  methods: {
    authenticate(event) {
      event.preventDefault();
      this.$store
        .dispatch("login", { email: this.email, password: this.password })
        .then(() => this.$router.go("/"));
    }
  },
  mounted() {
    EventBus.$on("failedAuthentication", msg => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedAuthentication");
  }
};
</script>
