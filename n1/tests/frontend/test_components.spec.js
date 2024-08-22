import { shallowMount } from '@vue/test-utils';
import ProductList from '@/components/ProductList.vue';

describe('ProductList.vue', () => {
  it('renders product list correctly', () => {
    const products = [
      { id: 1, name: 'Frozen Pizza', price: 10 },
      { id: 2, name: 'Pre-cooked Chicken Breasts', price: 12 }
    ];
    const wrapper = shallowMount(ProductList, {
      propsData: { products }
    });

    expect(wrapper.findAll('.product-item').length).toBe(2);
    expect(wrapper.text()).toContain('Frozen Pizza');
    expect(wrapper.text()).toContain('Pre-cooked Chicken Breasts');
  });
});
