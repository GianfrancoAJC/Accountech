<template>
    <form @submit.prevent.stop="handleSubmit">
      <label>Quantity:</label>
      <input type="quantity" required v-model="formData.quantity">
      <label>Product:</label>
      <select v-model="formData.product_id">
        <option value="1">Cristal</option>
        <option value="2">Pilsen Callao</option>
        <option value="3">Cusquena</option>
        <option value="4">Pilsen Trujillo</option>
        <option value="5">Guarana</option>
        <option value="6">Arequipena</option>
      </select>
      <div class="submit">
        <button>Submit</button>
      </div>
    </form>
    <br>
  </template>
  
  <script>
  export default {
    name: 'BForm',
    components: {
    },
    data() {
      return {
        formData: {
          quantity: '',
          product_id: '',
          type: '',
          id: '',
        },
      };
    },
    methods: {
      handleSubmit() {
        // Emit event with form data
        this.$emit('buy-form-submit', this.formData);
      }
    }
  };
  </script>
  
  <style>
      form{
          max-width: 420px;
          margin: 30px auto;
          background: #ffffff;
          text-align: left;
          padding: 40px;
          border-radius: 10px;
      }
  
      label{
          color: #777;
          display: inline-block;
          margin: 25px 0 15px;
          font-size: 0.6em;
          text-transform: uppercase;
          letter-spacing: 1px;
          font-weight: bold;
      }
  
      input, select{
          display: block;
          padding: 10px 6px;
          width: 100%;
          box-sizing: border-box;
          border: none;
          border-bottom: 1px solid #ddd;
          color: #555
      }
  
      input[type="checkbox"]{
          display: inline-block;
          width: 16px;
          margin: 0 10px 0 0;
          position: relative;
          top: 2px;
      }
  
      .pill{
          display: inline-block;
          margin: 20px 10px 0 0;
          padding: 6px 12px;
          background: #eee;
          border-radius: 20px;
          font-size: 12px;
          letter-spacing: 1px;
          font-weight: bold;
          color: #777;
          cursor: pointer;
      }
  
      button{
          background: #0b6dff;
          border: 0;
          padding: 10px 20px;
          margin-top: 20px;
          color: white;
          border-radius: 20px;
      }
  
      .submit{
          text-align: center;
      }
  
      .error{
          color: #ff0062;
          margin-top: 10px;
          font-size: 0.8em;
          font-weight: bold;
      }
  </style>
  