import Vue from "vue";
import App from "./App.vue";
//import "./registerServiceWorker";
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
  faSearch,
  faBars,
  faPlusSquare,
  faMinusSquare
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import VueSimpleAlert from "vue-simple-alert"; //to remove

import Fragment from "vue-fragment";
Vue.use(Fragment.Plugin);

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
  faSearch,
  faBars,
  faPlusSquare,
  faMinusSquare
);
Vue.use(require("vue-moment"));

Vue.component(
  "n-flash",
  require("./components/naginie_ui/FlashMessage.vue").default
);
Vue.component("n-modal", require("./components/naginie_ui/Modal.vue").default);
Vue.component(
  "n-paginate",
  require("./components/naginie_ui/Paginate.vue").default
);
Vue.component(
  "n-table",
  require("./components/naginie_ui/DataTable.vue").default
);
Vue.component(
  "n-breadcrumb",
  require("./components/naginie_ui/Breadcrumb.vue").default
);

Vue.use(VueSimpleAlert);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
