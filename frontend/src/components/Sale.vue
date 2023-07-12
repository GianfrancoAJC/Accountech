<template>
    <div class="home">
      <h1>Here the clients can buy products to the company</h1>
      <BForm @buy-form-submit="handleBuySubmit" />
    </div>
  </template>
  
  <script>
  import BForm from './buyForm.vue';
  import LogIn from './LogIn.vue';
  import { updateinventory } from '@/services/inventory.api';
  export default {
    name: 'CSale',
    components: {
      BForm,
      LogIn,
    },
    data() {
      return {
        client_id: '',
      };
    },
    methods: {
      async handleBuySubmit(formData) {
        formData.type = 'sale';
        formData.id = this.client_id;
        const { data } = await updateinventory(formData);
        console.log('Buy form submitted:', data);
        // Aquí puedes realizar las acciones necesarias para el registro
        // utilizando los datos del formulario (formData)
        console.log('Buy form submitted:', formData);
      },
      async useid(id){
        this.client_id = id;
      },
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
  