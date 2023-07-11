<template>
  <form @submit.prevent.stop="handleSubmit">
    <label>Name:</label>
    <input type="name" required v-model="formData.name">

    <label>Password:</label>
    <input type="password" required v-model="formData.password">
    <div v-if="passwordError" class="error">{{ passwordError }}</div>

    <label>Email:</label>
    <input type="email" required v-model="formData.email">

    <label>Role:</label>
    <select v-model="formData.role">
      <option value="client">Client</option>
      <option value="employee">Employee</option>
    </select>

    <div class="terms">
      <input type="checkbox" v-model="formData.terms" required>
      <label>Accept terms and conditions</label>
    </div>

    <div class="submit">
      <button>Submit</button>
    </div>
  </form>
</template>

<script>
export default {
  name: 'CForm',
  components: {
  },
  data() {
    return {
      formData: {
        name: '',
        password: '',
        email: '',
        role: null,
        terms: false
      },
      passwordError: ''
    };
  },
  methods: {
    handleSubmit() {
      // Validate password
      this.passwordError = this.formData.password.length > 5 ? '' : 'Password must be at least 6 characters long';
      if (!this.passwordError) {
        // Emit event with form data
        this.$emit('form-submit', this.formData);
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
