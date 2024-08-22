import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cart: []
  },
  mutations: {
    ADD_TO_CART(state, product) {
      state.cart.push(product);
    }
  },
  getters: {
    cartItems: (state) => state.cart,
    totalPrice: (state) => state.cart.reduce((acc, product) => acc + product.price, 0)
  }
});
