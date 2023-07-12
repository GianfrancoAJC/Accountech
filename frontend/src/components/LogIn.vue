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
        const { data } = await getemployee(formData);
        console.log('employee: ', data);
        
      } else {
        const { data } = await getclient(formData);
        console.log('client: ', data);
      }
      console.log('Log In form submitted:', formData);
      //console.log('Log In form submitted:', formData.name, formData.password, formData.email, formData.role, formData.terms);
    }
  }
};
</script>

