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
        const { data, success } = await createemployee(formData);
        console.log('employee: ', data);
        if(success){
          this.employee_id = data;
          this.$router.push({ name: 'Employee', params: { id: this.employee_id } });
        } else {
          alert('Wrong credentials');
        }

      } else {
        const { data, success } = await createclient(formData);
        console.log('client: ', data);
        console.log('success: ', success);
        if(success){
          this.client_id = data;
          this.$router.push({ name: 'Client', params: { id: this.client_id } });
        } else {
          alert('Wrong credentials');
        }
      }
      console.log('Sign Up form submitted:', formData);
      //console.log('Sign Up form submitted:', formData.name, formData.password, formData.email, formData.role, formData.terms);
    }
  }
};
</script>

