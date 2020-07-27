<template>
    <div id="home">
        <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
            <ol class="list-none p-0 inline-flex">
                <li class="flex items-center text-teal-500">
                    <router-link to="/" class="text-gray-700 pr-4">Dashboard</router-link>
                    <font-awesome-icon icon="arrow-right"></font-awesome-icon>
                </li>
                <li class="flex items-center">
                    <router-link to="/users/" class="text-teal-500 pl-4">Users</router-link>
                </li>
            </ol>
        </nav>
        <div class="">
            <div class="container mx-auto">
                <div class="float-left text-gray-600  my-3 display-block">
                    <form @submit="submitSearch" class="flex">
                        <input type="search" name="serch" v-model="searchQuery" placeholder="Search..." class="bg-white h-10 w-full xl:w-64 px-5 rounded-lg border text-sm focus:outline-none" />
                        <button type="submit" class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                            <font-awesome-icon icon="search"></font-awesome-icon>
                        </button></form>
                </div>
                <Paginate :items="users" />
                <div class="table-resp clear-both">
                <table class="table-auto border-collapse w-full ">
                    <thead>
                        <tr class="text-sm  border font-medium text-gray-700  bg-gray-200  text-left" style="font-size: 0.9674rem">
                            <th class="px-4 py-2 ">ID</th>
                            <th class="px-4 py-2 ">Created</th>
                            <th class="px-4 py-2 ">Logged</th>
                            <th class="px-4 py-2 ">Name</th>
                            <th class="px-4 py-2 ">Email</th>
                            <th class="px-4 py-2 ">Roles</th>
                        </tr>
                    </thead>
                    <tbody class="text-sm font-normal text-gray-700">
                        <template v-for="cuser in users.items">
                            <tr v-bind:key="cuser.id" class="hover:bg-gray-100 border-b border-gray-200 py-10">
                                <td class="text-teal-500 px-4 py-2">
                                    <router-link :to="`/users/${cuser.id}`">#{{ cuser.id }}</router-link>
                                </td>
                                <td class="px-4 py-2">
                                    {{ cuser.created| moment("from", "now") }}
                                </td>
                                <td class="px-4 py-2">
                                    {{ cuser.logged| moment("from", "now") }}
                                </td>
                                <td class="px-4 py-2 text-teal-500 ">
                                    <router-link :to="`/users/${cuser.id}`" v-html="replaceSearch(cuser.nicename)">{{
                                        }}</router-link>
                                </td>
                                <td class="bpx-4 py-2 text-teal-500 ">
                                    <router-link :to="`/users/${cuser.id}`" v-html="replaceSearch(cuser.email)">{{
                                        }}</router-link>
                                </td>
                                <td class="border-grey-light text-center   ">
                                    <template v-for="crole in cuser.roles">
                                        <span v-bind:key="crole.id">{{ crole.title }}(<b>{{ crole.slug }}</b>)</span>
                                    </template>
                                    <span v-if="cuser.roles.length == 0">n/a</span>
                                </td>
                            </tr>
                        </template>
                    </tbody>
                </table>
              </div>
                <Paginate :items="users" />
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from "vuex";
import { getUsers, searchUser } from "@/api/user";
import { EventBus } from "@/helpers/utils";

export default {
    name: "Users",

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
            this.$router.push({ path: '/users/', query: { term: this.searchQuery } })
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

            return text.replace(regEx, '<span class="bg-teal-400 text-white">' + this.$route.query.term + '</span>')
        },
        listUsers(page = 1) {
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
                } else {
                    this.isSearch = true
                }
                this.listUsers()
            },
            deep: true
        }
    }
};
</script>