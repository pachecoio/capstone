<template>
  <header class="header">
    <div class="header__wrapper">
      <Breadcrumbs :breadcrumbs="breadcrumbs" />
    </div>
  </header>
</template>

<script>
import "./header.scss";
import Breadcrumbs from "./../../components/breadcrumbs";
export default {
  components: {
    Breadcrumbs,
  },
  data() {
    return {
      breadcrumbs: [],
    };
  },
  created() {
    console.log("current route", this.$route);
    this.breadcrumbs.push({
      name: this.$route.name,
      url: this.$route.path,
    });
  },
};
</script>

<style></style>
