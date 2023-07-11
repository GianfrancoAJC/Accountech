<template>
  <div>
    <h2>Log In</h2>
    <CForm @form-submit="handleLogInSubmit" />
  </div>
</template>

<script>
import CForm from './Form.vue';
import { getemployee } from '@/services/employee.api';
import { getclient } from '@/services/client.api';

export default {
  name: 'LogIn',
  components: {
    CForm,
  },
  data() {
    return {
      employee_id: '',
      client_id: '',
    };
  },
  methods: {
    async handleLogInSubmit(formData) {
      // Aquí puedes realizar las acciones necesarias para el inicio de sesión
      // utilizando los datos del formulario (formData)
      if (formData.role == 'employee') {
        const { employee_id } = await getemployee(formData);
        console.log('employee: ', employee_id);
      } else {
        const { client_id } = await getclient(formData);
        console.log('client: ', client_id);
      }
      console.log('Log In form submitted:', formData);
      //console.log('Log In form submitted:', formData.name, formData.password, formData.email, formData.role, formData.terms);
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
