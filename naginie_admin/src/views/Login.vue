<template
  ><div class="flex h-screen bg-gray-900">
    <div class="m-auto">
      <div class="w-full max-w-xs">
        <form
          class="bg-gray-800 shadow-md rounded px-8 pt-6 pb-8 mb-4"
          @submit="authenticate"
          id="login_form"
        >
          <div class="w-full  flex  items-center mb-4">
            <img
              src="../assets/naginie.png"
              style="width: 70px;"
              class=" mr-8 "
              @click="dropDownOpen = !dropDownOpen"
            />
            <div class="font-semibold  text-3xl text-teal-200 ">
              Naginie
            </div>
          </div>
          <div class="mb-4 clear-both">
            <label
              class="block uppercase tracking-wide text-gray-500 text-xs font-bold mb-2"
              for="email"
            >
              E-Mail
            </label>
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-800 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
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
              class="block uppercase tracking-wide text-gray-500 text-xs font-bold mb-2"
              for="password"
            >
              Password
            </label>
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-800 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
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
              class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit"
            >
              Sign In
            </button>
            <!--<a
              class="inline-block align-baseline font-bold text-sm text-teal-500 hover:text-teal-800"
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
