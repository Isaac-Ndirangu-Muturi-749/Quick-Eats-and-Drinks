<template>
	<div class="products">
	  <h2>Our Products</h2>
	  <div class="product-list">
		<ProductCard v-for="product in allProducts" :key="product.name" :product="product" />
	  </div>
	</div>
  </template>

  <script>
  import ProductCard from '../components/ProductCard.vue';
  import { mapGetters } from 'vuex';

  export default {
	components: {
	  ProductCard
	},
	computed: {
	  ...mapGetters(['productsByCategory']),
	  allProducts() {
		// Flatten the product categories into a single array
		return Object.values(this.productsByCategory).flat();
	  }
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
