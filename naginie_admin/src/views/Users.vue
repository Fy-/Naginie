<template>
  <div id="home">
    <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
      <ol class="list-none p-0 inline-flex">
        <li class="flex items-center text-blue-500">
          <router-link to="/" class="text-gray-700 pr-4">Dashboard</router-link>
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li class="flex items-center">
          <router-link to="/users/" class="text-gray-600 pl-4"
            >Users</router-link
          >
        </li>
      </ol>
    </nav>
    <div class="flex items-center justify-center">
      <div class="container">
        <Paginate :items="users" />
        <table
          class="w-full flex flex-row flex-no-wrap sm:bg-white rounded-lg overflow-hidden sm:shadow-lg my-5"
        >
          <thead class="text-white">
            <template v-for="cuser in users.items">
              <tr
                v-bind:key="cuser.id"
                class="bg-blue-500 flex flex-col flex-no wrap sm:table-row rounded-l-lg sm:rounded-none mb-2 sm:mb-0"
              >
                <th class="p-3 text-left">ID</th>
                <th class="p-3 text-left">Created</th>
                <th class="p-3 text-left">Name</th>
                <th class="p-3 text-left">Email</th>
                <th class="p-3 text-left">Roles</th>
              </tr>
            </template>
          </thead>
          <tbody class="flex-1 sm:flex-none">
            <template v-for="cuser in users.items">
              <tr
                v-bind:key="cuser.id"
                class="flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0"
              >
                <td class="border-grey-light border hover:bg-gray-100 p-3">
                  #{{ cuser.id }}
                </td>
                <td class="border-grey-light border hover:bg-gray-100 p-3">
                  {{ cuser.created | moment("calendar") }}
                </td>
                <td class="border-grey-light border hover:bg-gray-100 p-3">
                  {{ cuser.nicename }}
                </td>
                <td class="border-grey-light border hover:bg-gray-100 p-3">
                  {{ cuser.email }}
                </td>
                <td class="border-grey-light border hover:bg-gray-100 p-3">
                  <template v-for="crole in cuser.roles">
                    <span v-bind:key="crole.id"
                      >{{ crole.title }}(<b>{{ crole.slug }}</b
                      >)</span
                    >
                  </template>
                  <span v-if="cuser.roles.length == 0">n/a</span>
                </td>
              </tr>
            </template>
          </tbody>
        </table>
        <Paginate :items="users" />
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import { getUsers } from "@/api/user";
import Paginate from "@/components/Paginate";
import { EventBus } from "@/helpers/utils";

export default {
  name: "Users",
  components: {
    Paginate,
  },
  data() {
    return {
      users: {},
    };
  },
  computed: {
    ...mapState(["user"]),
  },
  created() {
    this.getUsers(1);
  },
  methods: {
    getUsers(page = 1) {
      getUsers(page).then((response) => {
        this.users = response.data;
      });
    },
  },
  mounted() {
    EventBus.$on("goToPage", (page) => {
      this.getUsers(page);
    });
  },
};
</script>
