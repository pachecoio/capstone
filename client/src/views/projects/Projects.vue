<template>
  <div class="page projects">
    <h1>Projects</h1>
    <div class="project__list">
      <ProjectCard
        v-for="project in projects"
        :key="project.id"
        :project="project"
      />
    </div>
  </div>
</template>

<script>
import "./projects.scss";
import ProjectCard from "@/components/project-card";
export default {
  components: {
    ProjectCard,
  },
  data() {
    return {
      projects: [
        {
          id: 1,
          title: "Project 1",
          description:
            "Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. ",
          status: "new",
          tasks: [],
        },
        {
          id: 2,
          title: "Project 1",
          description:
            "Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. ",
          status: "progress",
          tasks: [],
        },
      ],
    };
  },
};
</script>

<style></style>
