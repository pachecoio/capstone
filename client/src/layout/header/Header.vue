<template>
  <header class="header">
    <div class="header__wrapper">
      <Breadcrumbs :breadcrumbs="breadcrumbs" />
      <Input placeholder="Search" v-model="searchTerm" @onPressEnter="search" />
    </div>
  </header>
</template>

<script>
import "./header.scss";
import Breadcrumbs from "./../../components/breadcrumbs";
import Input from "@/components/input";
export default {
  components: {
    Breadcrumbs,
    Input,
  },
  data() {
    return {
      breadcrumbs: [],
      searchTerm: "",
    };
  },
  created() {
    this.breadcrumbs.push({
      name: this.$route.name,
      url: this.$route.path,
    });
  },
  methods: {
    search() {
      if (this.searchTerm)
        this.$router.push({
          path: `/search?term=${this.searchTerm}`,
        });
    },
  },
};
</script>

<style></style>
