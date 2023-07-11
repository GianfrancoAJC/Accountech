<template>
    <div class="home">
      <h1>Tools for employees</h1>
    </div>
  </template>
  
  <script>
  import { initinventory, getinventory, deleteinventory } from '@/services/inventory.api';
  import { showeerr, showmcp, showpurchases, showsales } from '@/services/tools.api';
  export default {
    name: 'CTools',
    components: {},
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
  