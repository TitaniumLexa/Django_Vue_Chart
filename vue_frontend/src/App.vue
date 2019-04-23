<template>
    <div id="app">
        <upload-form/>
        <graph-list ref="chartlist"/>        
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
        },
        methods: {
            updateList: function()
            {
                this.$refs.chartlist.changeGraph()
            }
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
