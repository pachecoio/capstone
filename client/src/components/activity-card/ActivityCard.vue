<template>
  <Card class="dashboard__activity">
    <div class="activity" v-for="activity in activities" :key="activity.id">
      <span class="activity__date">
        {{ formatDate(activity.created_at) }}
      </span>
    </div>
  </Card>
</template>

<script>
import "./activity_card.scss";
import Card from "@/components/card";
import { getShortDateTime } from "@/helpers/utils";

export default {
  components: {
    Card,
  },
  data() {
    return {
      activities: [
        {
          id: 1,
          content: "{user_name} joined {project_name}",
          created_at: new Date(),
          type: "project_join",
          user: {
            name: "Thiago Pacheco",
          },
        },
        {
          id: 2,
          content: "{user_name} moved {task_name} from Progress to Done",
          created_at: new Date(),
          type: "task_done",
          user: {
            name: "Thiago Pacheco",
          },
        },
        {
          id: 3,
          content: "{user_name} moved {task_name} from New to Progress",
          created_at: new Date(),
          type: "task_progress",
          user: {
            name: "Thiago Pacheco",
          },
        },
      ],
    };
  },
  methods: {
    formatDate(date) {
      return getShortDateTime(date);
    },
  },
};
</script>

<style></style>
