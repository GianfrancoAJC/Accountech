<template>
  <div>
    <h2>Sign Up</h2>
    <CForm @form-submit="handleSignUpSubmit" />
  </div>
</template>

<script>
import CForm from './Form.vue';
import { createclient } from '@/services/client.api';
import { createemployee } from '@/services/employee.api';

export default {
  name: 'SignUp',
  components: {
    CForm
  },
  methods: {
    async handleSignUpSubmit(formData) {
      // Aquí puedes realizar las acciones necesarias para el registro
      // utilizando los datos del formulario (formData)
      if (formData.role == 'employee') {
        const { employee_id } = await createemployee(formData);
        console.log('employee: ', employee_id);
      } else {
        const { client_id } = await createclient(formData);
        console.log('client: ', client_id);
      }
      console.log('Sign Up form submitted:', formData);
      //console.log('Sign Up form submitted:', formData.name, formData.password, formData.email, formData.role, formData.terms);
    }
  }
};
</script>

