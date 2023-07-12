<template>
    <div class="home">
      <h1>Welcome Employee! </h1>
      <p>Welcome to our website! We offer a wide range of products and services to meet your needs. Whether you're looking for stylish clothing, high-quality electronics, or reliable home appliances, we've got you covered.</p>
    </div>
    <div>
      <CPurchase />
    </div>
    <div>
      <Tools />
    </div>
  </template>
  
  <script>
  import CPurchase from '@/components/Purchase.vue';
  import Tools from '@/components/Tools.vue';
  export default {
    name: 'CClient',
    components: {
      CPurchase,
      Tools,
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
  