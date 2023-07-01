<template>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
      <div class="container mw-0 px-3">
        <a class="navbar-brand" href="#">Finance</a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item" v-if="accessToken != null">
              <span class="nav-link">Hi, {{ username }}</span>
            </li>
            <li class="nav-item" v-if="accessToken != null">
              <router-link :to="{ name: 'logout' }" class="nav-link"
                >Logout</router-link
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Navbar",
  computed: mapState(["accessToken", "username"]),
};
</script>

<style scoped>
a {
  color: #000;
}
</style>