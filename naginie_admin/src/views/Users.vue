<template>
  <div id="home">
    <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
      <ol class="list-none p-0 inline-flex">
        <li class="flex items-center text-teal-500">
          <router-link to="/" class="text-gray-700 pr-4">Dashboard</router-link>
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li class="flex items-center">
          <router-link to="/users/" class="text-teal-500 pl-4"
            >Users</router-link
          >
        </li>
      </ol>
    </nav>
    <div class="flex items-center justify-center">
      <div class="container">
        <div class="float-left text-gray-600  my-3">
          <form
          @submit="submitSearch"
          class="flex"
        >
          <input
            type="search"
            name="serch"
            v-model="searchQuery"
            placeholder="Search..."
            class="bg-white h-10 w-full xl:w-64 px-5 rounded-lg border text-sm focus:outline-none"
          />
          <button
            type="submit"
            class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            <font-awesome-icon icon="search"></font-awesome-icon>
          </button></form>
        </div><Paginate :items="users" />
        <table
          class="w-full flex flex-row flex-no-wrap sm:bg-white rounded-lg overflow-hidden sm:shadow-lg my-3"
        >
          <thead class="text-white">
            <template v-for="cuser in users.items">
              <tr
                v-bind:key="cuser.id"
                class="bg-teal-500 flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0"
              >
                <th class="p-3 text-left  ">ID</th>
                <th class="p-3 text-left  ">Created</th>
                <th class="p-3 text-left  ">Name</th>
                <th class="p-3 text-left  ">Email</th>
                <th class="p-3 text-left  ">Roles</th>
              </tr>
            </template>
          </thead>
          <tbody class="flex-1 sm:flex-none">
            <template v-for="cuser in users.items">
              <tr
                v-bind:key="cuser.id"
                class="flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0"
              >
                <td
                  class="border-grey-light text-teal-500 border hover:bg-gray-100 p-3"
                >
                  <router-link :to="`/users/${cuser.id}`"
                    >#{{ cuser.id }}</router-link
                  >
                </td>
                <td class="border-grey-light border hover:bg-gray-100 p-3">
                  {{ cuser.created | moment("calendar") }}
                </td>
                <td
                  class="border-grey-light text-teal-500 border hover:bg-gray-100 p-3"
                >
                  <router-link :to="`/users/${cuser.id}`" v-html="replaceSearch(cuser.nicename)">{{
                    
                  }}</router-link>
                </td>
                <td
                  class="border-grey-light text-teal-500 border hover:bg-gray-100 p-3"
                >
                  <router-link :to="`/users/${cuser.id}`" v-html="replaceSearch(cuser.email)">{{
                  }}</router-link>
                </td>
                <td class="border-grey-light  border hover:bg-gray-100 p-3">
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
import { getUsers, searchUser } from "@/api/user";
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
      searchQuery: '',
      isSearch: false
    };
  },
  computed: {
    ...mapState(["user"]),
  },
  created() {
    this.listUsers()
  },
  methods: {
    submitSearch(evt) {
      evt.preventDefault();
      this.$router.push({ path: '/users/', query: { term: this.searchQuery }})
    },
    searchUser(page = 1) {      
      searchUser(page, this.$route.query.term).then((response) => {
        this.users = response.data;

        this.isSearch = true
      });
    },
    getUsers(page = 1) {
      getUsers(page).then((response) => {
        this.users = response.data;
        this.isSearch = false
      });
    },
    replaceSearch(text) {
      if (!this.isSearch) 
        return text

      if (text == null) 
        return null

      var regEx = new RegExp(this.$route.query.term, "ig");

      return text.replace(regEx, '<span class="bg-teal-400 text-white">'+this.$route.query.term+'</span>')
    },
    listUsers(page=1) {
      if (this.isSearch)
        this.searchUser(page);
      else
        this.getUsers(page);
    }
  },
  mounted() {
    EventBus.$on("goToPage", (page) => {
      this.listUsers(page)
    });
  },
  watch: {
      '$route.query.term': {
          handler(nv, ov) {
            if (ov != nv) {
              this.page = 1
            }
            if (!nv || nv == '') {
              this.isSearch = false
            }
            else {
              this.isSearch = true
            }
            this.listUsers()
          },
          deep: true        
      }
  }
};
</script>
