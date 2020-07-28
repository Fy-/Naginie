<template>
  <div id="home">
    <n-breadcrumb
      :nav="[{ to: '/', name: 'Dashboard' }, { name: 'Directories' }]"
    />

    <div class="text-gray-400">
      <table class="border-collapse w-full">
        <thead>
          <tr>
            <th
              class="p-3 font-bold uppercase bg-teal-600 text-gray-200 squared border border-teal-700 hidden lg:table-cell"
            >
              Name
            </th>
            <th
              class="p-3 font-bold uppercase bg-teal-600 text-gray-200 squared border border-teal-700 hidden lg:table-cell"
            >
              Type
            </th>
            <th
              class="p-3 font-bold uppercase bg-teal-600 text-gray-200 squared border border-teal-700 hidden lg:table-cell"
            >
              Slug
            </th>
            <th
              class="p-3 font-bold uppercase bg-teal-600 text-gray-200 squared border border-teal-700 hidden lg:table-cell"
            >
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          <Directory
            v-bind:key="item.id"
            v-for="item in directories"
            :directories="item.children"
            :depth="0"
            :single="item"
          />
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import Directory from "@/components/widgets/Directory";

import { getDirectories } from "@/api/directories";

export default {
  name: "Directories",
  components: {
    Directory
  },
  data() {
    return {
      directories: []
    };
  },
  computed: {
    ...mapState(["user"])
  },
  created() {
    getDirectories().then(response => {
      this.directories = response.data;
    });
  },
  methods: {},
  mounted() {}
};
</script>
