import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Products from '../views/Products.vue';
import Checkout from '../views/Checkout.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/products', name: 'Products', component: Products },
  { path: '/checkout', name: 'Checkout', component: Checkout },
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router;
