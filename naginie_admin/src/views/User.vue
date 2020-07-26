<template>
  <div id="home">
    <nav class="text-sm font-semibold mb-6" aria-label="Breadcrumb">
      <ol class="list-none p-0 inline-flex">
        <li class="flex items-center text-teal-500">
          <router-link to="/" class="text-gray-700 pr-4">Dashboard</router-link>
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li class="flex items-center text-teal-500">
          <router-link to="/users/" class="text-gray-600 pl-4 pr-4"
            >Users</router-link
          >
          <font-awesome-icon icon="arrow-right"></font-awesome-icon>
        </li>
        <li class="flex items-center">
          <router-link :to="`/users/${cuser.id}`" class="text-teal-500 pl-4"
            >#{{cuser.id}} - {{cuser.nicename}}</router-link
          >
        </li>
      </ol>
    </nav>
    <div class="flex items-center justify-center"></div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import  { profileUser} from '@/api/user';

export default {
  name: "User",
  components: {},
  data() {
    return {
      'cuser': {}
    };
  },
  computed: {
    ...mapState(["user"]),
  },
  created() {
    profileUser(this.$route.params.id).then((response) => {
      if (response.status == 200) {
        this.cuser = response.data
      }
    })
  },
  methods: {},
  mounted() {},
};
</script>
