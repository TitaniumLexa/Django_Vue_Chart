<template>
    <div class="graph-list" v-if="itemlist">
        <h2>You can select graph from list to show</h2>
        <table align="center">
            <tr v-for="item in itemlist" :key="item.id">
                <td> 
                    <router-link :to="'/' + item.id + '/'" v-on:click.native="changeGraph">{{item.file}}</router-link> 
                </td>
                <td>
                    uploaded: {{item.upload_date}}s    
                </td>
            </tr>            
        </table>
        <router-view :id=this.graphId ref="graph"></router-view>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "GraphList",
        data: function(){
        return {           
            itemlist: null,
            loaded: false
        }},
        created: function()
        {
            this.updateList()
        },
        computed: {
            graphId () {
                if (this.$route.params.graphID != null)
                    return this.$route.params.graphID
                else
                    return 0
            }
        },
        methods: 
        {
            changeGraph: function()
            {
                this.updateList()
                this.$refs.graph.update()
            },
            updateList: function()
            {
                axios.get('http://127.0.0.1:8000/api/graph/')
                .then((response) => {
                    this.itemlist = response.data
                    this.loaded = true
                    console.log("Created")
                });  
            }
        }
    }
</script>

<style scoped>
tr
{
    font-weight: bold;
}
td
{
    text-align: left;
}
</style>