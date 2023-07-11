<template>
    <div class="home">
      <h1>Here only employees can purchase products for the company</h1>
      <BForm @buy-form-submit="handleBuySubmit" />
    </div>
  </template>
  
  <script>
  import BForm from './buyForm.vue';
  import { updateinventory } from '@/services/inventory.api';
  export default {
    name: 'CPurchase',
    components: {
      BForm
    },
    methods: {
      async handleBuySubmit(formData) {
        formData.type = 'purchase';
        formData.id = 'id';
        const { data } = await updateinventory(formData);
        // Aquí puedes realizar las acciones necesarias para el registro
        // utilizando los datos del formulario (formData)
        console.log('Buy form submitted:', formData);
        //console.log('Buy form submitted:', formData.name, formData.password, formData.email, formData.role, formData.terms);
    }
    },
  };
  </script>
  
  <style>
  .home {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .home h1 {
    font-size: 32px;
    margin-bottom: 20px;
  }
  
  .home p {
    font-size: 16px;
    margin-bottom: 10px;
  }
  
  </style>
  