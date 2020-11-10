<template>
  <div class="layout">
    <Header v-if="$auth.isAuthenticated" />
    <Sidebar v-if="$auth.isAuthenticated" />
    <main class="main">
      <slot />
    </main>
  </div>
</template>
<script>
import "./layout.scss";
import Sidebar from "./sidebar";
import Header from "./header";
export default {
  components: {
    Sidebar,
    Header,
  },
};
</script>

<style lang="scss" scoped></style>
