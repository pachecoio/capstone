<template>
  <div class="card" @click="$emit('click')">
    <slot />
  </div>
</template>

<script>
import "./card.scss";
export default {};
</script>
