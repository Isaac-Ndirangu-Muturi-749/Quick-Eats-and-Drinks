<template>
  <div class="checkout">
    <h2>Checkout</h2>
    <p>Total: ${{ totalPrice }}</p>
    <button @click="processPayment">Pay Now</button>
  </div>
</template>

<script>
export default {
  computed: {
    totalPrice() {
      return this.$store.getters.totalPrice;
    }
  },
  methods: {
    processPayment() {
      // Logic for processing payment using Stripe or PayPal API
    }
  }
};
</script>

<style scoped>
.checkout {
  text-align: center;
  margin-top: 50px;
}
</style>
