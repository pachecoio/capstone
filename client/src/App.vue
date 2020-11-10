<template>
  <Layout>
    <router-view />
  </Layout>
</template>

<script>
import "./assets/sass/main.scss";
import Layout from "@/layout";
export default {
  components: {
    Layout,
  },
};
</script>
