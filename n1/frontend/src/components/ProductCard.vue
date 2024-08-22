<template>
  <div class="product-card">
    <img :src="product.image" alt="product.name" />
    <h3>{{ product.name }}</h3>
    <p>${{ product.price }}</p>
    <button @click="addToCart(product)">Add to Cart</button>
  </div>
</template>

<script>
export default {
  props: ['product'],
  methods: {
    addToCart(product) {
      this.$store.commit('ADD_TO_CART', product);
    }
  }
};
</script>

<style scoped>
.product-card {
  border: 1px solid #ddd;
  padding: 16px;
  text-align: center;
}
</style>
