import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cart: [],
    products: [
      {
        category: 'Ready-Made Meals',
        items: [
          { name: 'Frozen Pizza', price: 10, image: require('@/assets/frozen_pizza.jpg') },
          { name: 'Pre-Cooked Chicken Breasts', price: 12, image: require('@/assets/pre_cooked_chicken_breasts.jpg') },
          { name: 'Instant Noodles', price: 5, image: require('@/assets/instant_noodles.jpg') }
        ]
      },
      {
        category: 'Snacks',
        items: [
          { name: 'Potato Chips', price: 3, image: require('@/assets/potato_chips.jpg') },
          { name: 'Granola Bars', price: 4, image: require('@/assets/granola_bars.jpg') },
          { name: 'Mixed Nuts', price: 6, image: require('@/assets/mixed_nuts.jpg') }
        ]
      },
      {
        category: 'Beverages',
        items: [
          { name: 'Cola', price: 2, image: require('@/assets/cola.jpg') },
          { name: 'Orange Juice', price: 4, image: require('@/assets/orange_juice.jpg') },
          { name: 'Energy Drinks', price: 3, image: require('@/assets/energy_drinks.jpg') }
        ]
      },
      {
        category: 'Desserts',
        items: [
          { name: 'Ice Cream', price: 5, image: require('@/assets/ice_cream.jpg') },
          { name: 'Cookies', price: 4, image: require('@/assets/cookies.jpg') },
          { name: 'Brownies', price: 6, image: require('@/assets/brownies.jpg') }
        ]
      },
      {
        category: 'Pantry Staples',
        items: [
          { name: 'Canned Beans', price: 2, image: require('@/assets/canned_beans.jpg') },
          { name: 'Pasta', price: 3, image: require('@/assets/pasta.jpg') },
          { name: 'Cooking Oil', price: 5, image: require('@/assets/cooking_oil.jpg') }
        ]
      },
      {
        category: 'Frozen Foods',
        items: [
          { name: 'Frozen Vegetables', price: 4, image: require('@/assets/frozen_vegetables.jpg') },
          { name: 'Frozen Fish', price: 8, image: require('@/assets/frozen_fish.jpg') },
          { name: 'Frozen Burgers', price: 7, image: require('@/assets/frozen_burgers.jpg') }
        ]
      }
    ]
  },
  mutations: {
    ADD_TO_CART(state, product) {
      state.cart.push(product);
    }
  },
  getters: {
    cartItems: (state) => state.cart,
    totalPrice: (state) => state.cart.reduce((acc, product) => acc + product.price, 0),
    productsByCategory: (state) => {
      return state.products.reduce((acc, category) => {
        acc[category.category] = category.items;
        return acc;
      }, {});
    }
  }
});
