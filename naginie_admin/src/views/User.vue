<template>
    <div id="home">
        <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
            <ol class="list-none p-0 inline-flex">
                <li class="flex items-center text-teal-500">
                    <router-link to="/" class="text-gray-700 pr-4">Dashboard</router-link>
                    <font-awesome-icon icon="arrow-right"></font-awesome-icon>
                </li>
                <li class="flex items-center text-teal-500">
                    <router-link to="/users/" class="text-gray-600 pl-4 pr-4">Users</router-link>
                    <font-awesome-icon icon="arrow-right"></font-awesome-icon>
                </li>
                <li class="flex items-center">
                    <router-link :to="`/users/${cuser.id}`" class="text-teal-500 pl-4">#{{cuser.id}} - {{cuser.nicename}}</router-link>
                </li>
            </ol>
        </nav>
        <div class="flex items-center justify-center">
            <!-- component -->
            <div class="container mx-auto " v-if="cuser.id">
                <router-link :to="`/users/${cuser.prev_next.prev}`" v-if="cuser.prev_next.prev" class="mb-4  float-left bg-teal-500 hover:bg-teal-700 text-white  py-1 px-2 rounded focus:outline-none focus:shadow-outline ">Prev</router-link>
                <router-link :to="`/users/${cuser.prev_next.next}`" v-if="cuser.prev_next.next" class="mb-4 bg-teal-500 hover:bg-teal-700 text-white  py-1 px-2 rounded focus:outline-none focus:shadow-outline  float-right">Next</router-link>
                <div class="inputs w-full max-w-4xl p-4 mx-auto bg-gray-200 rounded-lg clear-both ">
                    <form @submit="updateUser">
                        <h1 class="font-bold ">#{{cuser.id}} - {{cuser.nicename}} &lt;{{cuser.email}}&gt;</h1><br />
                        <h2 class="text-gray-900">Account informations</h2>
                        <div class="personal w-full border-t border-gray-400 pt-4">
                            <div class="flex items-center justify-between ">
                                <div class='w-full md:w-1/2  mb-6 pr-4  text-sm'>
                                    Account creation
                                </div>
                                <div class='w-full md:w-1/2  mb-6 text-sm text-right'>
                                    {{cuser.created | moment("from", "now") }}
                                </div>
                            </div>
                            <div class="flex items-center justify-between ">
                                <div class='w-full md:w-1/2  mb-6 pr-4  text-sm'>
                                    Account update
                                </div>
                                <div class='w-full md:w-1/2  mb-6  text-sm text-right'>
                                    {{cuser.updated | moment("from", "now") }}
                                </div>
                            </div>
                            <div class="flex items-center justify-between ">
                                <div class='w-full md:w-1/2  mb-6 pr-4  text-sm'>
                                    Last login
                                </div>
                                <div class='w-full md:w-1/2  mb-6  text-sm text-right'>
                                    {{cuser.logged | moment("from", "now") }}
                                </div>
                            </div>
                            <div class="flex items-center justify-between ">
                                <div class='w-full md:w-1/2  mb-6 pr-4  text-sm'>
                                    Role
                                </div>
                                <div class='w-full md:w-1/2  mb-6  text-sm text-right'>
                                    <template v-for="crole in cuser.roles">
                                        <span v-bind:key="crole.id">{{ crole.title }}(<b>{{ crole.slug }}</b>)</span>
                                    </template>
                                </div>
                            </div>
                        </div>
                        <h2 class=" text-gray-900">Account Setting</h2>
                        <div class="personal w-full border-t border-gray-400 pt-4">
                            <div class='flex flex-wrap '>
                                <div class='w-full md:w-full  mb-6'>
                                    <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2' for='grid-text-1'>email address</label>
                                    <input class='appearance-none block w-full bg-white text-gray-700 border border-gray-400 shadow-inner rounded-md py-2 px-3 leading-tight focus:outline-none  focus:border-gray-500' id='grid-text-1' v-model="cuser.email" type='text' placeholder='Enter email' required>
                                </div>
                                <div class='w-full md:w-full  mb-6 '>
                                    <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2'>password</label>
                                    <a href="javascript:void(0)" class="bg-teal-500 hover:bg-teal-700 text-white  py-1 px-2 rounded focus:outline-none focus:shadow-outline " @click="modalPassword=true">Change password</a>
                                </div>
                                <h2 class="text-gray-900">Personal info</h2>
                                <div class="personal w-full border-t border-gray-400 pt-4">
                                    <div class="flex items-center justify-between mt-4">
                                        <div class='w-full md:w-1/2  mb-6 pr-4'>
                                            <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2'>first name</label>
                                            <input class='appearance-none block w-full bg-white text-gray-700 border border-gray-400 shadow-inner rounded-md py-2 px-3 leading-tight focus:outline-none  focus:border-gray-500' type='text' v-model="cuser.firstname">
                                        </div>
                                        <div class='w-full md:w-1/2  mb-6'>
                                            <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2'>last name</label>
                                            <input class='appearance-none block w-full bg-white text-gray-700 border border-gray-400 shadow-inner rounded-md py-2 px-3 leading-tight focus:outline-none  focus:border-gray-500' type='text' v-model="cuser.lastname">
                                        </div>
                                    </div>
                                    <div class='w-full md:w-1/2  mb-6 pr-4'>
                                        <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2'>user name</label>
                                        <input class='appearance-none block w-full bg-white text-gray-700 border border-gray-400 shadow-inner rounded-md py-2 px-3 leading-tight focus:outline-none  focus:border-gray-500' type='text' v-model="cuser.username">
                                    </div>
                                    <div class="flex justify-end">
                                        <button class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">save changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <Modal title="Change Password" id="pwd_change" :show="modalPassword">
            <template v-slot:body>
                <form>
                    <small v-if="passwordErr" class="text-small text-red-600">{{passwordErr}}</small>
                    <div class="flex items-center justify-between mt-4">
                        <div class='w-full md:w-1/2  mb-6 pr-4'>
                            <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2'>Password</label>
                            <input class='appearance-none block w-full bg-white text-gray-700 border border-gray-400 shadow-inner rounded-md py-2 px-3 leading-tight focus:outline-none  focus:border-gray-500' type='password' v-model="password" autocomplete="off" :name="`pwd_${cuser.id}`">
                        </div>
                        <div class='w-full md:w-1/2  mb-6'>
                            <label class='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2'>Repeat password</label>
                            <input class='appearance-none block w-full bg-white text-gray-700 border border-gray-400 shadow-inner rounded-md py-2 px-3 leading-tight focus:outline-none  focus:border-gray-500' type='password' v-model="passwordc" autocomplete="off" :name="`pwdc_${cuser.id}`">
                        </div>
                    </div>
                </form>
            </template>
        </Modal>
    </div>
</template>
<script>
import { mapState } from "vuex";
import { profileUser, passwordUser, dataUser } from '@/api/user';
import { EventBus } from "@/helpers/utils";

export default {
    name: "User",
    data() {
        return {
            'cuser': {},
            'password': '',
            'passwordc': '',
            'passwordErr': '',
            'modalPassword': false
        };
    },
    computed: {
        ...mapState(["user"]),
    },
    created() {
        this.getUser();

    },
    methods: {
        getUser() {
            profileUser(this.$route.params.id).then((response) => {
                if (response.status == 200) {
                    this.cuser = response.data
                }
            })
        },
        updateUser(evt) {
            evt.preventDefault()
            dataUser(this.$route.params.id, {email: this.cuser.email, firstname: this.cuser.firstname, lastname: this.cuser.lastname, username: this.cuser.username}).then((response) => {
                if (response.data.error) {
                    EventBus.$emit('flash-message', {text: response.data.error, type: 'error'});
                } else {
                    this.getUser();
                    EventBus.$emit('flash-message', {text: 'Account saved.', type: 'success'});
                }
            })
        }
    },
    mounted() {
        EventBus.$on('close_pwd_change', () => {
            this.modalPassword = false;
        })
        EventBus.$on('act_pwd_change', () => {
            if (!this.password || this.password == '')
                this.passwordErr = 'Password can\'t be empty.'
            else if (this.password != this.passwordc)
                this.passwordErr = 'Both password fields must be identical.'
            else if (this.password.length > 32 || this.password.length < 4)
                this.passwordErr = 'Your Password must be between 4 and 42 characters.'
            else {
                passwordUser(this.cuser.id, this.password).then((response) => {
                    if (response.data.error)
                        this.passwordErr = response.data.error
                    else if (response.data.message == 'success') {
                        this.modalPassword = false
                        EventBus.$emit('flash-message', {text: `New password saved for ${this.cuser.nicename}`, type: 'success'});
                    }
                });
            }
        })
    },
    watch: {
        '$route.params.id': {
            handler(nv, ov) {
                if (ov != nv) {
                    this.getUser()
                }
            },
            deep: true
        }
    }
};
</script>