<template>
  <div class="page dashboard">
    <section class="section section__welcome">
      <Card v-if="hasPermission" class="dashboard__welcome">
        <div class="content">
          <h1 class="content__title">Welcome back, {{ $auth.user.name }}!</h1>
          <p class="content__text">
            You have <span>{{ tasks }}</span> tasks to finish today.
          </p>
          <Button class="btn--highlight" @click="navigateToTasks">
            <span>Check now</span>
          </Button>
          <img
            class="content__image"
            src="@/assets/images/dashboard_graphic.png"
            alt=""
          />
        </div>
      </Card>
    </section>
    <section class="section section__tasks">
      <h2>Latest tasks</h2>
      <div class="dashboard__tasks">
        <TaskCard
          v-for="task in latestTasks"
          :key="task.id"
          :task="task"
          @click="navigateToTask(task.id)"
        />
      </div>
    </section>
    <section class="section section__activity">
      <h2>Activities</h2>
      <ActivityCard />
    </section>
  </div>
</template>

<script>
import "./dashboard.scss";
import Card from "@/components/card";
import TaskCard from "@/components/task-card";
import ActivityCard from "@/components/activity-card";
import Button from "@/components/button";

import { mapGetters } from "vuex";

export default {
  components: {
    Card,
    Button,
    TaskCard,
    ActivityCard,
  },
  data() {
    return {
      tasks: 10,
      latestTasks: [
        {
          id: 1,
          title: "Task title 1",
          status: "done",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id quam eget ligula tempus semper. Nunc vel viverra tortor. Mauris eget risus ultrices, venenatis odio finibus, malesuada nulla. Vivamus nec leo sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit ante dolor. Vivamus pretium lectus interdum erat vulputate posuere. Donec vel ultrices nisi. Etiam eu urna et lectus pellentesque luctus. Vestibulum laoreet malesuada auctor. Donec suscipit dictum magna, vitae placerat neque molestie nec.",
          comments: [],
        },
        {
          id: 2,
          title: "Task title 2",
          status: "progress",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id quam eget ligula tempus semper. Nunc vel viverra tortor. Mauris eget risus ultrices, venenatis odio finibus, malesuada nulla. Vivamus nec leo sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit ante dolor. Vivamus pretium lectus interdum erat vulputate posuere. Donec vel ultrices nisi. Etiam eu urna et lectus pellentesque luctus. Vestibulum laoreet malesuada auctor. Donec suscipit dictum magna, vitae placerat neque molestie nec.",
          comments: [],
        },
        {
          id: 3,
          title: "Task title 3",
          status: "new",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id quam eget ligula tempus semper. Nunc vel viverra tortor. Mauris eget risus ultrices, venenatis odio finibus, malesuada nulla. Vivamus nec leo sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit ante dolor. Vivamus pretium lectus interdum erat vulputate posuere. Donec vel ultrices nisi. Etiam eu urna et lectus pellentesque luctus. Vestibulum laoreet malesuada auctor. Donec suscipit dictum magna, vitae placerat neque molestie nec.",
          comments: [],
        },
        {
          id: 4,
          title: "Task title 3",
          status: "new",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id quam eget ligula tempus semper. Nunc vel viverra tortor. Mauris eget risus ultrices, venenatis odio finibus, malesuada nulla. Vivamus nec leo sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit ante dolor. Vivamus pretium lectus interdum erat vulputate posuere. Donec vel ultrices nisi. Etiam eu urna et lectus pellentesque luctus. Vestibulum laoreet malesuada auctor. Donec suscipit dictum magna, vitae placerat neque molestie nec.",
          comments: [],
        },
        {
          id: 5,
          title: "Task title 3",
          status: "new",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id quam eget ligula tempus semper. Nunc vel viverra tortor. Mauris eget risus ultrices, venenatis odio finibus, malesuada nulla. Vivamus nec leo sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit ante dolor. Vivamus pretium lectus interdum erat vulputate posuere. Donec vel ultrices nisi. Etiam eu urna et lectus pellentesque luctus. Vestibulum laoreet malesuada auctor. Donec suscipit dictum magna, vitae placerat neque molestie nec.",
          comments: [],
        },
        {
          id: 6,
          title: "Task title 3",
          status: "new",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id quam eget ligula tempus semper. Nunc vel viverra tortor. Mauris eget risus ultrices, venenatis odio finibus, malesuada nulla. Vivamus nec leo sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur blandit ante dolor. Vivamus pretium lectus interdum erat vulputate posuere. Donec vel ultrices nisi. Etiam eu urna et lectus pellentesque luctus. Vestibulum laoreet malesuada auctor. Donec suscipit dictum magna, vitae placerat neque molestie nec.",
          comments: [],
        },
      ],
    };
  },
  methods: {
    navigateToTasks() {
      this.$router.push({
        path: `/tasks`,
      });
    },
    navigateToTask(id) {
      this.$router.push({
        path: `/tasks/${id}`,
      });
    },
  },
  computed: {
    hasPermission() {
      return this.$auth.hasPermissions(["get:users"]);
    },
  },
};
</script>
