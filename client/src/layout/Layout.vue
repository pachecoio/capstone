<template>
  <div class="layout">
    <Loading v-if="$auth.loading" />
    <Header v-if="$auth.isAuthenticated" />
    <Sidebar v-if="$auth.isAuthenticated" />
    <main :class="['main', ...mainClasses]">
      <slot />
    </main>
  </div>
</template>
<script>
import "./layout.scss";
import Sidebar from "./sidebar";
import Header from "./header";
import Loading from "@/components/loading";
export default {
  components: {
    Sidebar,
    Header,
    Loading,
  },
  computed: {
    mainClasses() {
      if (!this.$auth.isAuthenticated) return ["main--fullscreen"];
      return [];
    },
  },
};
</script>

<style lang="scss" scoped></style>
