import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import LineChart from './components/LineChartComponent.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {path: '/:graphID', component: LineChart}
  ]
})

new Vue({
  render: function (h) { return h(App) },
  router
}).$mount('#app')
