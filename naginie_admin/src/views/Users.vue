<template>
  <div id="home">
    <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
      <ol class="list-none p-0 inline-flex">
        <li class="flex items-center text-teal-200">
          <router-link to="/" class="text-gray-500 pr-4">Dashboard</router-link>
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li class="flex items-center">
          <router-link to="/users/" class="text-teal-400 pl-4"
            >Users</router-link
          >
        </li>
      </ol>
    </nav>
    <div class="">
      <div class="container mx-auto">
        <div class="float-left text-gray-300   my-3 display-block">
          <form @submit="submitSearch" class="flex">
            <input
              type="search"
              name="serch"
              v-model="searchQuery"
              placeholder="Search..."
              class="bg-white h-10 w-full xl:w-64 px-5 bg-gray-800 rounded-lg   text-sm focus:outline-none"
            />
            <button
              type="submit"
              class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-3 rounded focus:outline-none focus:shadow-outline"
            >
              <font-awesome-icon icon="search"></font-awesome-icon>
            </button>
          </form>
        </div>
        <Paginate :items="users" />

        <DataTable :data.sync="users.items" :headers="headers">
          <template v-slot:id_item="property">
            <router-link
              class="text-teal-400 hover:text-teal-200"
              :to="`/users/${property.data.id}`"
              >#{{ property.data.prop }}</router-link
            >
          </template>
          <template v-slot:created_item="property">{{
            property.data.prop | moment("from", "now")
          }}</template>
          <template v-slot:logged_item="property">{{
            property.data.prop | moment("from", "now")
          }}</template>
          <template v-slot:nicename_item="property">
            <router-link
              class="text-teal-400 hover:text-teal-200"
              :to="`/users/${property.data.id}`"
              v-html="replaceSearch(property.data.prop)"
            />
          </template>
          <template v-slot:email_item="property">
            <router-link
              class="text-teal-400 hover:text-teal-200"
              :to="`/users/${property.data.id}`"
              v-html="replaceSearch(property.data.prop)"
            />
          </template>
          <template v-slot:status_item="property">
            <span v-if="property.data.prop">{{
              property.data.prop.title
            }}</span>
            <span v-else>n/a</span>
          </template>
        </DataTable>
        <Paginate :items="users" />
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import { getUsers, searchUser } from "@/api/user";
import { EventBus } from "@/helpers/utils";
import DataTable from "@/components/DataTable";
export default {
  name: "Users",
  components: {
    DataTable
  },
  data() {
    return {
      users: {},
      searchQuery: "",
      isSearch: false,
      headers: {
        id: "ID",
        created: "Created",
        logged: "Logged",
        nicename: "Name",
        email: "Email",
        status: "Status"
      }
    };
  },
  computed: {
    ...mapState(["user"])
  },
  created() {
    this.listUsers();
  },
  methods: {
    submitSearch(evt) {
      evt.preventDefault();
      this.$router.push({ path: "/users/", query: { term: this.searchQuery } });
    },
    searchUser(page = 1) {
      searchUser(page, this.$route.query.term).then(response => {
        this.users = response.data;
        this.isSearch = true;
      });
    },
    getUsers(page = 1) {
      getUsers(page).then(response => {
        this.users = response.data;
        this.isSearch = false;
      });
    },
    replaceSearch(text) {
      if (!this.isSearch) return text;
      if (text == null) return null;
      var regEx = new RegExp(this.$route.query.term, "ig");
      return text.replace(
        regEx,
        '<span class="bg-teal-700 text-white">' +
          this.$route.query.term +
          "</span>"
      );
    },
    listUsers(page = 1) {
      if (this.isSearch) this.searchUser(page);
      else this.getUsers(page);
    }
  },
  mounted() {
    EventBus.$on("goToPage", page => {
      this.listUsers(page);
    });
  },
  watch: {
    "$route.query.term": {
      handler(nv, ov) {
        if (ov != nv) {
          this.page = 1;
        }
        if (!nv || nv == "") {
          this.isSearch = false;
        } else {
          this.isSearch = true;
        }
        this.listUsers();
      },
      deep: true
    }
  }
};
</script>
