<template>
    <div id="app">
        <upload-form/>
        <graph-list />        
    </div>
</template>

<script>
    import UploadForm from './components/UploadForm.vue'
    import GraphList from './components/Graph_list.vue'

    export default {
        name: 'app',
        components: {
            UploadForm,
            GraphList
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
