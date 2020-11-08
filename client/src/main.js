import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import { Auth0Plugin } from './auth';

const domain = process.env.VUE_APP_DOMAIN;
const clientId = process.env.VUE_APP_CLIENT_ID;

// Install the authentication plugin here
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
