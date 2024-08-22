<template>
  <div class="products">
    <h2>Our Products</h2>
    <div class="product-list">
      <ProductCard v-for="product in products" :key="product.id" :product="product" />
    </div>
  </div>
</template>

<script>
import ProductCard from '../components/ProductCard.vue';

export default {
  components: {
    ProductCard
  },
  data() {
    return {
      products: [
        { id: 1, name: 'Frozen Pizza', price: 10, image: '/src/assets/frozen-pizza.jpg' },
        { id: 2, name: 'Pre-cooked Chicken Breasts', price: 12, image: '/src/assets/chicken-breasts.jpg' },
        // Add more products here
      ]
    };
  }
};
</script>

<style scoped>
.products {
  margin: 20px;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
}
</style>
