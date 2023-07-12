<template>
    <div class="home">
      <h1>Welcome Client! </h1>
      <p>Make a Purchase in our shop!.</p>
    </div>
    <div>
      <CSale />
    </div>
  </template>
  
  <script>
  import CSale from '@/components/Sale.vue';
  export default {
    name: 'CClient',
    components: {
      CSale,
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
  