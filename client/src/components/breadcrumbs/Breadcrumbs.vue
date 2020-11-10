<template>
  <ul class="breadcrumbs">
    <li
      v-for="breadcrumb in breadcrumbs"
      :key="breadcrumb.name"
      class="breadcrumb"
    >
      <span v-if="true" class="breadcrumb breadcrumb--active">
        {{ breadcrumb.name }}
      </span>
      <router-link v-else :to="breadcrumb.url" class="breadcrumb">
        {{ breadcrumb.name }}
      </router-link>
    </li>
  </ul>
</template>

<script>
import "./breadcrumbs.scss";
export default {
  props: {
    breadcrumbs: {
      type: Array,
      required: true,
    },
  },
  created() {
    const items = [];
    const pathname = window.location.pathname;
    for (const path of pathname.split("/")) {
      console.log("url", path);
    }
  },
};
</script>

<style></style>
