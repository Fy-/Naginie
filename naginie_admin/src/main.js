import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";

import "./assets/css/index.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faTachometerAlt,
  faCogs,
  faSitemap,
  faFileCode,
  faArrowRight,
  faUsers,
  faUserTag,
  faSearch
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import VueSimpleAlert from "vue-simple-alert";

Vue.config.productionTip = false;
Vue.component("font-awesome-icon", FontAwesomeIcon);
library.add(
  faTachometerAlt,
  faCogs,
  faSitemap,
  faFileCode,
  faArrowRight,
  faUsers,
  faUserTag,
  faSearch
);
Vue.use(require("vue-moment"));
Vue.component("FlashMessage", require("./components/FlashMessage.vue").default);
Vue.component("Modal", require("./components/Modal.vue").default);
Vue.component("Paginate", require("./components/Paginate.vue").default);
Vue.use(VueSimpleAlert);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
