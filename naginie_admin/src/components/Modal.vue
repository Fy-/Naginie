<template>
    <div class="modal   fixed w-full h-full top-0 left-0 flex items-center justify-center" v-bind:class="{ 'opacity-0': !show, 'pointer-events-none': !show }">
        <div class="modal-overlay absolute w-full h-full bg-gray-900 opacity-50"></div>
        <div class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto">
            <div class="modal-close absolute top-0 right-0 cursor-pointer flex flex-col items-center mt-4 mr-4 text-white text-sm z-50">
                <svg class="fill-current text-white" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                    <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                </svg>
                <span class="text-sm">(Esc)</span>
            </div>
            <!-- Add margin if you want to see some of the overlay behind the modal-->
            <div class="modal-content py-4 text-left px-6">
                <!--Title-->
                <slot name="header">
                    <div class="flex justify-between items-center pb-3">
                        <p class="text-2xl font-bold">{{title}}</p>
                        <a href="javascript:void(0)" @click="close" class="modal-close cursor-pointer z-50">
                            <svg class="fill-current text-black" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                                <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                            </svg>
                        </a>
                    </div>
                </slot>
                <slot name="body">
           
                </slot>
                <slot name="footer">
                    <div class="flex justify-end pt-2">
                        <a href="javascript:void(0)" @click="close" class="px-4 bg-transparent p-3 rounded-lg text-teal-500 hover:bg-gray-100 hover:text-teal-400 mr-2">Close</a>
                        <a href="javascript:void(0)" @click="act" class="modal-close px-4 bg-teal-500 p-3 rounded-lg text-white hover:bg-teal-400">Save</a>
                    </div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script>
import { EventBus } from "@/helpers/utils";

export default {
    name: "Modal",
    props: {
        title: {
            type: String,
            default () {
                return "Modal";
            }
        },
        id: {
            type: String,
            default () {
                return "id";
            }
        },
        show: {
            type: Boolean,
            default () {
                return false;
            }
        },
    },
    methods: {
        close() {
          EventBus.$emit(`close_${this.id}`);
        },
        act() {
          EventBus.$emit(`act_${this.id}`);
        },
    }
};
</script>