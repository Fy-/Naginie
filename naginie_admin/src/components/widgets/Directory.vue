<template>
  <fragment>
    <tr
      v-if="single.id"
      class=" flex lg:table-row flex-row lg:flex-row flex-wrap lg:flex-no-wrap mb-10 lg:mb-0 "
    >
      <td
        :style="marginIndent"
        class="w-full   border-b border-teal-700 lg:w-auto p-3 text-gray-300    block relative lg:static bg-gray-800"
      >
        <span
          class="lg:hidden absolute top-0 right-0 bg-teal-700 text-gray-200 px-2 py-1 text-xs font-bold uppercase"
          >Name</span
        >{{ indent }} {{ single.title }} (#{{ single.id }})
      </td>
      <td
        class="w-full border-b  border-teal-700 lg:w-auto p-3 text-gray-300    block lg:table-cell relative lg:static bg-gray-800 text-center"
      >
        <span
          class="lg:hidden absolute top-0 right-0 bg-teal-700 text-gray-200 px-2 py-1 text-xs font-bold uppercase"
          >Type</span
        >
        <div v-if="single.id == 1">root</div>
        <div v-else>n/a</div>
      </td>
      <td
        class="w-full border-b border-teal-700 lg:w-auto p-3 text-gray-300    block lg:table-cell relative lg:static bg-gray-800 text-center"
      >
        <span
          class="lg:hidden absolute top-0 right-0 bg-teal-700 text-gray-200 px-2 py-1 text-xs font-bold uppercase "
          >Slug</span
        >{{ single.slug }}
      </td>
      <td
        class="w-full border-b border-teal-700 lg:w-auto p-3 text-gray-300    block lg:table-cell relative lg:static bg-gray-800 text-center"
      >
        <span
          class="lg:hidden absolute top-0 right-0 bg-teal-700 text-gray-200 px-2 py-1 text-xs font-bold uppercase"
          >Actions</span
        >
        <div v-if="single.id != 1">
          <a href="javascript:void(0);" class="text-teal-400">Edit</a>
          -
          <a href="javascript:void(0);" class="text-red-400">Delete</a>
        </div>
        <div v-else>Root Directory</div>
      </td>
    </tr>
    <Directory
      v-for="item in directories"
      :directories="item.children"
      :depth="depth + 1"
      v-bind:key="item.id"
      :single="item"
    ></Directory>
  </fragment>
</template>
<script>
export default {
  name: "Directory",
  props: {
    directories: {
      type: Array,
      default() {
        return [];
      }
    },
    single: {
      type: Object,
      default() {
        return {};
      }
    },
    depth: {
      type: Number,
      default() {
        return 0;
      }
    }
  },
  data() {
    return { showChildren: false };
  },
  computed: {
    indent() {
      //return { 'margin-left': `${this.depth * 50}px !important` };
      let char = "—";
      return `${char.repeat(this.depth)}`;
    },
    marginIndent() {
      return { "margin-left": `${0}px !important` }; // this.depth * 28
    },

    labelClasses() {
      return { "has-children": this.single.children };
    }
  },
  methods: {
    toggleChildren() {
      this.showChildren = !this.showChildren;
    }
  }
};
</script>
<style>
.has-children {
  cursor: pointer;
}
</style>
