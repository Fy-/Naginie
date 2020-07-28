<template>
  <div id="home">
    <n-breadcrumb
      :nav="[{ to: '/', name: 'Dashboard' }, { name: 'Status / Roles' }]"
    />

    <div class="">
      <div class="container mx-auto">
        <a
          class="mb-4  float-left bg-teal-500 hover:bg-teal-700 text-white  py-1 px-2 rounded focus:outline-none focus:shadow-outline "
          href="javascript:void(0)"
          @click="
            resetCurrentStatus();
            modalStatus = true;
          "
          >New Role</a
        >
        <n-table :data.sync="status" :headers="headers">
          <template v-slot:actions_item="property">
            <a
              href="javascript:void(0);"
              @click="edit(property.data.item)"
              class="text-teal-400"
              >Edit</a
            >
            -
            <a
              href="javascript:void(0);"
              class="text-red-400"
              @click="rm(property.data.id, property.data.item.title)"
              >Delete</a
            >
          </template>
        </n-table>
      </div>
    </div>
    <n-modal
      :title="currentStatus.id ? 'Edit User Status' : 'Add User Status'"
      id="status_change"
      :show="modalStatus"
    >
      <template v-slot:body>
        <form>
          <small v-if="statusErr" class="text-small text-red-600">{{
            statusErr
          }}</small>
          <div class="flex items-center justify-between mt-4">
            <div class="w-full md:w-1/2  mb-6 pr-4">
              <label
                class="block uppercase tracking-wide text-gray-500 text-xs font-bold mb-2"
                >Title</label
              >
              <input
                class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                type="text"
                v-model="currentStatus.title"
                autocomplete="off"
              />
            </div>
            <div class="w-full md:w-1/2  mb-6 relative">
              <label
                class="block uppercase tracking-wide text-gray-500 text-xs font-bold mb-2"
                >Role</label
              >
              <select
                class=" block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                type="text"
                v-model="currentStatus.role"
                autocomplete="off"
              >
                <option
                  v-for="role in roles"
                  v-bind:key="role[0]"
                  v-bind:value="role[0]"
                  >{{ role[1] }}
                </option>
              </select>
              <div
                class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
              >
                <svg
                  class="fill-current h-4 w-4"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                  />
                </svg>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-between ">
            <div class="w-full   mb-6">
              <label
                class="block uppercase tracking-wide text-gray-500 text-xs font-bold mb-2"
                >Description</label
              >
              <input
                class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                type="text"
                v-model="currentStatus.description"
                autocomplete="off"
              />
            </div>
          </div>
        </form>
      </template>
    </n-modal>
  </div>
</template>
<script>
import { mapState } from "vuex";
import {
  getRoles,
  getStatus,
  addStatus,
  editStatus,
  delStatus
} from "@/api/user";
import { EventBus } from "@/helpers/utils";

export default {
  name: "Roles",
  components: {},
  data() {
    return {
      status: [],
      roles: {},
      modalStatus: false,
      currentStatus: {
        title: "",
        role: "",
        description: ""
      },
      statusErr: false,
      hoverStatus: 0,
      headers: {
        id: "ID",
        title: "Title",
        role: "Role",
        users: "Users",
        actions: "Actions"
      }
    };
  },
  computed: {
    ...mapState(["user"])
  },
  created() {
    this.listStatus();
    EventBus.$on("close_status_change", () => {
      this.modalStatus = false;
    });
    EventBus.$on("act_status_change", () => {
      if (this.currentStatus.id) {
        editStatus(this.currentStatus.id, this.currentStatus).then(() => {
          this.listStatus();
          this.resetCurrentStatus();
          this.modalStatus = false;
          EventBus.$emit("flash-message", {
            text: `Role saved.`,
            type: "success"
          });
        });
      } else {
        addStatus(this.currentStatus).then(() => {
          this.listStatus();
          this.resetCurrentStatus();
          this.modalStatus = false;
          EventBus.$emit("flash-message", {
            text: `Role added.`,
            type: "success"
          });
        });
      }
    });
    getRoles().then(response => {
      this.roles = response.data;
    });
  },
  methods: {
    showStatus(id) {
      if (id == this.hoverStatus) return true;
      return false;
    },
    rm(id, title = "") {
      this.$confirm(`Do you want to delete: ${title}?`).then(() => {
        delStatus(id).then(() => {
          this.listStatus();
        });
      });
    },
    edit(status) {
      this.currentStatus = status;
      this.modalStatus = true;
    },
    resetCurrentStatus() {
      this.currentStatus = {
        title: "",
        role: "",
        description: ""
      };
    },
    listStatus() {
      getStatus().then(response => {
        this.status = response.data;
      });
    }
  },
  mounted() {}
};
</script>
