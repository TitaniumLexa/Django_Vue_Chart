<template>
    <div id="app">
        <upload-form/>

    </div>
</template>

<script>
    import UploadForm from './components/UploadForm.vue'

    export default {
        name: 'app',
        components: {
            UploadForm
        }
    }


</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        text-align: center;
        color: #2c3e50;
    }
</style>
