<template>
    <router-link v-if="to == current" :to="to" class="w-full flex items-center text-blue-400 h-10 pl-4 bg-gray-300 hover:bg-gray-200 rounded-lg cursor-pointer">
        <font-awesome-icon :icon="icon"></font-awesome-icon>
        <span class="text-gray-700 pl-4">{{title}}</span>
    </router-link>

    <router-link v-else :to="to" class="w-full flex items-center text-blue-400 h-10 pl-4  hover:bg-gray-200 rounded-lg cursor-pointerr">
        <font-awesome-icon :icon="icon"></font-awesome-icon>
        <span class="text-gray-700 pl-4">{{title}}</span>
    </router-link>
</template>
<script>
export default {
    name: "NavLink",
    props: {
        to: {
            type: String,
            default () {
                return "/"
            }
        },
        current: {
            type: String,
            default () {
                return "/"
            }
        },
        title: {
            type: String,
            default () {
                return "Dashboard"
            }
        },
        icon: {
            type: String,
            default () {
                return "icon"
            }
        },
    },
}
</script>