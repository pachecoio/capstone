<template>
  <Card class="dashboard__activity">
    <div class="activity" v-for="activity in activities" :key="activity.id">
      <span class="activity__date">
        {{ formatDate(activity.created_at) }}
      </span>
      <div
        class="activity__avatar"
        :style="{
          'background-image': `url(&quot;${activity.user.picture}&quot;)`,
        }"
      />
      <span class="activity__content">
        {{ buildActivityContent(activity) }}
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
          project_name: "Project 1",
          user: {
            id: 1,
            name: "Thiago Pacheco",
            picture: "https://www.placecage.com/200/300",
          },
        },
        {
          id: 2,
          content: "{user_name} moved {task_name} from Progress to Done",
          created_at: new Date(),
          task_name: "Task 1",
          user: {
            id: 2,
            name: "Thiago Pacheco",
            picture: "https://www.placecage.com/200/300",
          },
        },
        {
          id: 3,
          content: "{user_name} moved {task_name} from New to Progress",
          created_at: new Date(),
          task_name: "Task 2",
          user: {
            id: 3,
            name: "Thiago Pacheco",
            picture: "https://www.placecage.com/200/300",
          },
        },
      ],
    };
  },
  methods: {
    formatDate(date) {
      return getShortDateTime(date);
    },
    buildActivityContent(activity) {
      return activity.content
        .replace("{user_name}", activity.user.name)
        .replace("{task_name}", activity.task_name)
        .replace("{project_name}", activity.project_name);
    },
  },
};
</script>

<style></style>
