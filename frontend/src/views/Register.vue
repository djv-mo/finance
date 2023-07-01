<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Register</h1>

          <p v-if="registrationError">Registration failed. Please try again.</p>
          <p v-if="registrationSuccess">Registration successful!</p>

          <form v-on:submit.prevent="register">
            <div class="form-group">
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="form-control"
                placeholder="Username"
              />
            </div>
            <div class="form-group">
              <input
                type="email"
                name="email"
                id="email"
                v-model="email"
                class="form-control"
                placeholder="Email"
              />
            </div>
            <div class="form-group">
              <input
                type="password"
                name="password"
                id="pass"
                v-model="password"
                class="form-control"
                placeholder="Password"
              />
            </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block">
              Register
            </button>
          </form>

          <router-link
            :to="{ name: 'login' }"
            class="btn btn-lg btn-secondary btn-block"
          >
            Back to Login
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "register",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      registrationError: false,
      registrationSuccess: false,
    };
  },
  methods: {
    register() {
      this.$store
        .dispatch("userRegister", {
          username: this.username,
          email: this.email,
          password: this.password,
        })
        .then((message) => {
          this.registrationSuccess = true;
          this.registrationError = false;
        })
        .catch((err) => {
          console.log(err);
          this.registrationSuccess = false;
          this.registrationError = true;
        });
    },
  },
};
</script>

<style>
body {
  background-color: #f4f4f4;
}
.login {
  background-color: #fff;
  margin-top: 10%;
}
input {
  padding: 25px 10px;
}
</style>
