import { getInstance } from "./index";

export const authGuard = async (to, from, next) => {
  const authService = getInstance();

  console.log("current permissions", authService.permissions);

  const fn = () => {
    // If the user is authenticated, continue with the route
    if (authService.isAuthenticated) {
      return next();
    }

    // Otherwise, log in
    authService.loginWithRedirect({ appState: { targetUrl: to.fullPath } });
  };

  // If loading has already finished, check our auth state using `fn()`
  if (!authService.loading) {
    return fn();
  }

  // Watch for the loading property to change before we check isAuthenticated
  authService.$watch("loading", (loading) => {
    if (loading === false) {
      return fn();
    }
  });
};

export const notAuthenticated = async (to, from, next) => {
  const authService = getInstance();

  const fn = () => {
    // If the user is authenticated, show home/login page
    if (!authService.isAuthenticated) {
      return next();
    }

    // Otherwise, redirect to dashboard
    next({ path: "/dashboard" });
  };

  // Watch for the loading property to change before we check isAuthenticated
  authService.$watch("loading", (loading) => {
    if (loading === false) {
      return fn();
    }
  });
};
