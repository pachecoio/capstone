<template>
  <div class="layout">
    
    <Sidebar v-if="$auth.isAuthenticated" />
    <main class="main">
      <slot />
    </main>
  </div>
</template>
<script>
import "./layout.scss";
import Sidebar from "./sidebar";
export default {
  components: {
    Sidebar,
  },
};
</script>

<style lang="scss" scoped></style>
