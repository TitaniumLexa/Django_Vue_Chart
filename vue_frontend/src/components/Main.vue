<template>
    <div class="main">
        <h1>{{hello_msg}}</h1>
    </div>
</template>

<script>
    export default {
        name: "Main",
        props: {
            hello_msg: String
        }
    }
</script>

<style scoped>

</style>