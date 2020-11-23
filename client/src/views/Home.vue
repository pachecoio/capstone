<template>
  <div class="home">
    <button @click="login">Log in</button>
    <button @click="managerLogin">Log in as company</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
  data() {
    return {
      auth: null,
    };
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    managerLogin() {
      this.$auth.loginWithRedirect({
        redirect_uri: "http://localhost:8080?manager=true",
      });
    },
  },
};
</script>
