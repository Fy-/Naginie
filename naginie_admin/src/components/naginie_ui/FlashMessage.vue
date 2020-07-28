<template>
  <div class="fixed top-0 right-0 m-3  z-50">
    <Transition name="slide-fade">
      <div
        v-if="message.text"
        :class="{
          'bg-red-700 text-red-200': message.type === 'error',
          'bg-green-700 text-green-200': message.type === 'success'
        }"
        class="rounded-lg shadow-md  p-4 pr-30"
        style="min-width: 240px"
      >
        <button
          @click="close"
          class="opacity-75 cursor-pointer absolute top-0 right-0 py-2 px-3 hover:opacity-100"
        >
          ×
        </button>
        <div class="flex items-center">
          {{ message.text }}
        </div>
      </div>
    </Transition>
  </div>
</template>

<script>
import { EventBus } from "@/helpers/utils";

export default {
  data() {
    return {
      message: {
        text: null,
        type: "success"
      }
    };
  },
  methods: {
    close() {
      this.message.text = null;
    }
  },
  mounted() {
    let timer;
    EventBus.$on("flash-message", message => {
      clearTimeout(timer);

      this.message = message;

      timer = setTimeout(() => {
        this.message.text = null;
      }, 2000);
    });
  }
};
</script>

<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.4s;
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateX(400px);
  opacity: 0;
}
</style>
