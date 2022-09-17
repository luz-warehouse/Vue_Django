import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

//配置全局样式
import '@/assets/css/global.css'

//配置elementui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

//使用bootstrap
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import settings from './assets/js/settings'

import moment from 'moment'


Vue.filter('dateFormat', function (dateStr,pattern = "YYYY-MM-DD HH:mm:ss") {
  return moment(dateStr).format(pattern);
})

// console.log(settings)

// 把settings这个对象，放到Vue的原型中
Vue.prototype.$settings = settings

// axios的配置
import axios from 'axios'
Vue.prototype.$http = axios

//cookie的配置
import cookie from 'vue-cookies'
Vue.prototype.$cookies = cookie

// 视频播放相关
// vue-video播放器
// require('video.js/dist/video-js.css');
// require('vue-video-player/src/custom-theme.css');
// import VideoPlayer from 'vue-video-player'
// Vue.use(VideoPlayer);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
