<template>
  <div class="input__wrapper">
    <label v-if="label" for="" class="input__label">{{ label }}</label>
    <div class="input__field">
      <input
        type="text"
        :placeholder="placeholder"
        :value="initialValue"
        @input="onChange"
        @keyup.enter="onPressEnter"
        @keyup="keyup"
      />
    </div>
  </div>
</template>

<script>
import "./input.scss";
export default {
  props: {
    label: {
      type: String,
    },
    placeholder: {
      type: String,
    },
    initialValue: {
      type: String,
    },
  },
  methods: {
    onChange(e) {
      this.$emit("input", e.target.value);
    },
    onPressEnter(e) {
      this.$emit("onPressEnter", e);
    },
    keyup(e) {
      this.$emit("keyup", e);
    },
  },
};
</script>

<style></style>
