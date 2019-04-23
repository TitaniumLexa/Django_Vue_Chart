<template>
    <div class="upload-form">
        <h1>Select an Excel file</h1>
        <form @submit.prevent="handleSubmit" enctype="multipart/form-data" method="post" id="excelfile_form">
            <input type="file" name="file" required="" id="id_file" accept=".xls,.xlsx">
            <input type="submit" value="Upload">
        </form>
        <h2>Last uploaded excel chart</h2>
        <line-chart-component id=0 ref="linechart"/>
    </div>

</template>

<script>
    import axios from 'axios'
    import LineChartComponent from "./LineChartComponent.vue";

    export default {
        name: "UploadForm",
        components: {
            LineChartComponent,
        },
        methods: {
            async handleSubmit(event) {
                event.preventDefault()
                let formData = new FormData(event.target)
                await axios.post('http://localhost:8000/api/upload/0/', formData)
                    .then((response) => (this.updateChart()))

            },
            updateChart: function () {
                this.$refs.linechart.update()
                this.$parent.updateList()              
            }
        }
    }
</script>

<style scoped>
    form{
        margin: 0 0 15px 0;
    }
</style>