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
              <div class="table-resp clear-both">
                <table class="table-auto border-collapse w-full">
                    <thead>
                        <tr class="text-sm  border font-medium text-gray-700  bg-gray-200  text-left" style="font-size: 0.9674rem">
                            <th class="px-4 py-2 ">ID</th>
                            <th class="px-4 py-2 ">Title</th>
                                                        <th class="px-4 py-2 "> Role</th>

                            <th class="px-4 py-2 ">Description</th>
                        </tr>
                    </thead>
                    <tbody class="text-sm font-normal text-gray-700">
                        <template v-for="crole in roles">
                            <tr v-bind:key="crole.id" class="hover:bg-gray-100 border-b border-gray-200 py-10">
                                <td class="px-4 py-4">
                                    #{{ crole.id }}
                                </td>
                                <td class="px-4 py-4">
                                    {{ crole.title}}
                                </td>
                                 <td class="px-4 py-4">
                                    <strong>{{ crole.role }}</strong>
                                </td>

                                <td class="px-4 py-4">
                                    <small>{{ crole.description}}</small>
                                </td>
                            </tr>
                        </template>
                    </tbody>
                </table></div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from "vuex";
import { getRoles } from "@/api/user";

export default {
    name: "Roles",

    data() {
        return {
            roles: {},
        };
    },
    computed: {
        ...mapState(["user"]),
    },
    created() {
        this.listRoles()
    },
    methods: {

        listRoles() {
            getRoles().then((response) => {
                this.roles = response.data
            });
        }
    },
    mounted() {

    },

};
</script>