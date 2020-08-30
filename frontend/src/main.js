import Vue from 'vue'
import App from './App'
import router from './router'
import "./style/comment.css";
import axios from 'axios'
import "./../plugins/vant.js";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.prototype.axios=axios;

Vue.config.productionTip = false;

Vue.use(ElementUI);
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});



