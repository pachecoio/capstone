<template>
  <aside class="sidebar">
    <div
      :class="{
        sidebar__wrapper: true,
        'sidebar__wrapper--active': displayActions,
      }"
    >
      <div class="brand sidebar__header">
        <router-link to="/">
          <img
            alt="Vue logo"
            class="brand__image"
            src="../../assets/images/logo.png"
          />
        </router-link>
      </div>
      <div class="sidebar__body">
        <ul class="sidebar__options">
          <li class="sidebar__option option">
            <router-link to="/" class="option__link">
              <DashboardIcon class="icon" />
              <span>Dashboard</span>
            </router-link>
          </li>
        </ul>
      </div>
      <div class="sidebar__footer user-profile" @click="showUserActions()">
        <div class="user-profile__image">
          <img :src="$auth.user.picture" alt="User avatar" />
        </div>
        <span class="user-profile__name">{{ $auth.user.name }}</span>
        <ArrowDownIcon class="icon user-profile__icon" />
      </div>
      <div v-if="displayActions" class="sidebar__actions">
        <div class="option">
          <router-link to="/profile" class="option__link">
            <ProfileIcon class="icon" />
            <span>Profile</span>
          </router-link>
        </div>
        <div class="option">
          <a @click="logout()" class="option__link">
            <LogoutIcon class="icon" />
            <span>Logout</span>
          </a>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
import "./sidebar.scss";
import DashboardIcon from "@/assets/icons/dashboard.svg";
import ArrowDownIcon from "@/assets/icons/down-arrow.svg";
import ProfileIcon from "@/assets/icons/profile.svg";
import LogoutIcon from "@/assets/icons/logout.svg";
export default {
  components: {
    DashboardIcon,
    ArrowDownIcon,
    ProfileIcon,
    LogoutIcon,
  },
  data() {
    return {
      displayActions: false,
    };
  },
  methods: {
    showUserActions() {
      this.displayActions = !this.displayActions;
    },
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin,
      });
    },
  },
};
</script>
