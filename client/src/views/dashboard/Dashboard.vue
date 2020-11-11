<template>
  <div class="page dashboard">
    <Card class="dashboard__welcome">
      <div class="content">
        <h1 class="content__title">Welcome back, {{ $auth.user.name }}!</h1>
        <p class="content__text">You have {{ tasks }} tasks to finish today.</p>
        <Button class="btn--highlight">
          <span>Check now</span>
        </Button>
      </div>
    </Card>
  </div>
</template>

<script>
import "./dashboard.scss";
import Card from "@/components/card";
import Button from "@/components/button";
export default {
  components: {
    Card,
    Button,
  },
  data() {
    return {
      tasks: 10,
    };
  },
};
</script>

<style></style>
