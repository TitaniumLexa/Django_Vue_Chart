<template>
    <div class="container">
        <line-chart v-if="loaded" :chart-data="data" :options="chartOptions"/>
    </div>
</template>

<script>
    import LineChart from './LineChart.js'
    import axios from 'axios'

    export default {
        name: "LineChartComponent",
        components: {
            LineChart
        },
        props:
        {
            id: 0
        },
        data: function () {
            return {
                loaded: false,
                data: [],
                chartOptions: {
                    responsive: true,
                    maintainAspectRatio: true,
                    scales: {
                        xAxes: [{
                            type: 'linear',
                            display: true,
                            scaleLabel: {
                                display: false,
                                labelString: 'x'
                            }
                        }],
                        yAxes: [{
                            type: 'linear',
                            display: true,
                            scaleLabel: {
                                display: false,
                                labelString: 'y'
                            }
                        }]
                    }
                }
            }
        },
        mounted() {
            this.loaded = false
            this.update()
        },
        methods: {
            update: async function () {
                console.log("updating" + this.id)
                await axios.get('http://127.0.0.1:8000/api/upload/' + this.id + '/').then((response) => {
                    if (response.status == 204)
                        this.loaded = false
                    else {
                        this.data = {
                            datasets: [
                                {
                                    label: 'data',
                                    backgroundColor: '#f87979',
                                    data: response.data.points
                                }
                            ]
                        }
                        this.loaded = true
                    }
                });
            },
            graphId () {
                if (this.$route.params.graphID != null)
                    return this.$route.params.graphID
                else
                    return 0
            }
        }
    }
</script>

<style scoped>
    .container {
        width: 40%;
        margin:0 auto;
    }
</style>