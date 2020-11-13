<template>
  <div class="layout">
    <Loading v-if="$auth.loading" />
    <Header />
    <Sidebar />
    <main class="main">
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
};
</script>

<style lang="scss" scoped></style>
