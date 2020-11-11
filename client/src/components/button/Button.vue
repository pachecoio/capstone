<template>
  <button class="btn" @click="$emit('click')">
    <slot />
  </button>
</template>

<script>
import "./button.scss";
export default {};
</script>

<style></style>
