<template>
  <div class="page projects">
    <h1 class="projects__title">Projects</h1>
    <div class="project__list">
      <ProjectCard
        v-for="project in projects"
        :key="project.id"
        :project="project"
        @click="navigateToProject(project.id)"
      />
    </div>
  </div>
</template>

<script>
import ProjectCard from "@/components/project-card";
import { getAxiosInstance } from '@/services';
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
  methods: {
    async loadProjects() {
      const axios = getAxiosInstance(
        this.$auth.token
      );
      const params = {};
      if(this.$auth.user.role === 'manager') {
        params.created_by = this.$auth.user.id;
      } else if (this.$auth.user.role === 'client') {
        params.user_id = this.$auth.user.id;
      }
      const res = await axios.get(`/api/project`, {
        params,
      })
    },
    navigateToProject(id) {
      this.$router.push({
        path: `projects/${id}`,
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import './projects';

</style>></style>
