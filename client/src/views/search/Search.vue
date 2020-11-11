<template>
  <div class="page search">
    <h1>Results for "{{ searchTerm }}"</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchTerm: "",
    };
  },
  methods: {
    setTerm() {
      if (this.$route.query && this.$route.query.term)
        this.searchTerm = this.$route.query.term;
    },
  },
  watch: {
    $route: {
      immediate: true,
      handler: "setTerm",
    },
  },
};
</script>

<style></style>
