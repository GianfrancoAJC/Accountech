<template>
  <nav>
    <router-link :to="{ name: 'Signup' }">Signup</router-link> |
    <router-link :to="{ name: 'Login' }">Login</router-link>
  </nav>

  <div class="button-group">
    <button class="redirect-button" @click="redirect">Home</button>
  </div>

  <div class="button-group-right">
    <button class="navigation-button" @click="back">Go Back</button>
    <button class="navigation-button" @click="forward">Go Forward</button>
  </div>

  <router-view/>
  <br>
</template> 

<script>
export default {
  name: 'App',
  methods: {
    redirect() {
      this.$router.push({ name: 'Home' });
    },
    back() {
      this.$router.go(-1);
    },
    forward() {
      this.$router.go(1);
    }
  }
}  
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
}

nav a.router-link-exact-active {
  color: white;
  background: crimson;
}

.button-group {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px;
}

.button-group-right {
  position: absolute;
  top: 0;
  right: 0;
  padding: 10px;
}

.redirect-button,
.navigation-button {
  padding: 10px 16px;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  color: #fff;
  background-color: #2c3e50;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.redirect-button {
  margin-right: 10px;
}

.navigation-button {
  margin-left: 10px;
}

.redirect-button:hover,
.navigation-button:hover {
  background-color: #1a2938;
}

</style>