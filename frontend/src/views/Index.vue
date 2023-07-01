<template>
  <div class="savings-posts">
    <NavBar></NavBar>

    <div class="container">
      <h1>Savings</h1>
      <form v-on:submit.prevent="createSavingGoal" class="form">
        <div class="form-group">
          <div class="form-field">
            <label for="amount">Amount:</label>
            <input
              type="number"
              name="amount"
              id="amount"
              v-model="amount"
              class="form-control"
              required
            />
          </div>
          <div class="form-field">
            <label for="date">Date:</label>
            <input
              type="date"
              name="date"
              id="date"
              v-model="date"
              class="form-control"
              required
            />
          </div>
        </div>
        <div class="button-container">
          <button type="submit" class="btn btn-primary">
            Create Saving Goal
          </button>
        </div>
      </form>
      <table class="table">
        <thead>
          <tr>
            <th>Amount</th>
            <th>Date to reach goal</th>
            <th>Monthly Deposit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="goal in APIData" :key="goal.id">
            <td>{{ goal.amount }}</td>
            <td>{{ goal.date }}</td>
            <td>{{ goal.monthly_deposit }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { getAPI } from "../axios-api";
import NavBar from "../components/Navbar";

export default {
  name: "Savings",
  components: {
    NavBar,
  },
  computed: mapState(["APIData"]),
  data() {
    return {
      amount: null,
      date: null,
    };
  },
  created() {
    getAPI
      .get("api/v1/saving-goals/", {
        headers: { Authorization: `JWT ${this.$store.state.accessToken}` },
      })
      .then((response) => {
        this.$store.state.APIData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    createSavingGoal() {
      const data = {
        amount: this.amount,
        date: this.date,
      };

      getAPI
        .post("api/v1/saving-goals/", data, {
          headers: { Authorization: `JWT ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData.unshift(response.data);

          // Reset form fields
          this.amount = null;
          this.date = null;
        })
        .catch((error) => {
          // Handle error
          console.log("Error creating saving goal:", error);
        });
    },
  },
};
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.form-field {
  margin-right: 10px;
}

.button-container {
  display: flex;
  justify-content: center;
}
</style>
