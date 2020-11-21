<template>
  <Card class="project" @click="$emit('click')">
    <div class="project__header">
      <h3 class="project__title">{{ project.title }}</h3>
      <div :class="['project__status', ...statusClasses]">
        <span class="project__status__label">
          {{ project.status }}
        </span>
        <span class="project__status__icon" />
      </div>
    </div>
    <div class="project__body">
      <p class="project__description">
        {{ description }}
      </p>
    </div>
    <div class="project__footer">
      <ClipboardIcon class="icon" />
      <span>{{ tasksLength }}</span>
    </div>
  </Card>
</template>

<script>
import Card from "@/components/card";
import ClipboardIcon from "@/assets/icons/clipboard.svg";
import { PROJECT_STATUSES } from "@/services/ProjectService";
export default {
  components: {
    Card,
    ClipboardIcon,
  },
  props: {
    project: {
      type: Object,
      required: true,
    },
  },
  methods: {},
  computed: {
    statusClasses() {
      return [`project__status--${this.project.status}`];
    },
    description() {
      return this.project.description.slice(0, 50);
    },
    tasksLength() {
      return this.project.tasks.length;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "./projectcard";
</style>
