<template>
  <Card class="task" @click="$emit('click')">
    <div class="task__header">
      <h3 class="task__title">{{ task.title }}</h3>
      <div :class="['task__status', ...statusClasses]">
        <span class="task__status__label">
          {{ task.status }}
        </span>
        <span class="task__status__icon" />
      </div>
    </div>
    <div class="task__body">
      <p class="task__description">
        {{ description }}
      </p>
    </div>
    <div class="task__footer">
      <MessageIcon class="icon" />
      <span>{{ commentsLength }}</span>
    </div>
  </Card>
</template>

<script>
import "./taskcard.scss";
import Card from "@/components/card";
import MessageIcon from "@/assets/icons/message.svg";
import { TASK_STATUSES } from "@/services/TaskService";
export default {
  components: {
    Card,
    MessageIcon,
  },
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  methods: {
    fetchCommentsLength(item) {
      if (!item.comments) return 0;

      const length = item.comments.length;

      for (const c in item.comments) {
        let currentCommentLength = this.fetchCommentsLength(c);
        length += currentCommentLength;
      }
      return length;
    },
  },
  computed: {
    statusClasses() {
      return [`task__status--${this.task.status}`];
    },
    description() {
      return this.task.description.slice(0, 50);
    },
    commentsLength() {
      return this.fetchCommentsLength(this.task);
    },
  },
};
</script>

<style></style>
