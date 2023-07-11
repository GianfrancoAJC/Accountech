<template>
  <div>
    <h2>Sign Up</h2>
    <Form @form-submit="handleSignUpSubmit" />
  </div>
</template>

<script>
import Form from './Form.vue';
import { signUp } from './users.api';

export default {
  name: 'SignUp',
  components: {
    Form
  },
  methods: {
    async handleSignUpSubmit(formData) {
      try {
        const { success, errors = [], token = null } = await signUp(formData);
        if (success) {
          // Acciones a realizar cuando el registro es exitoso
          console.log('Sign Up successful');
          console.log('Token:', token);
          // Redireccionar a otra página
          this.$router.push({ name: 'Purchase' });
        } else {
          // Acciones a realizar cuando hay errores de registro
          console.log('Sign Up errors:', errors);
          // Actualizar el estado de errores en el formulario
          // this.$refs.form.setErrorMessages(errors);
        }
      } catch (error) {
        // Acciones a realizar cuando hay un error en la solicitud
        console.log('Error:', error);
      }
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
