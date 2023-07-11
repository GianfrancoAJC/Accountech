import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../components/SignUp.vue'
import LogIn from '../components/LogIn.vue'
import Purchase from '../views/Purchase.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignUp,
  },
  {
    path: '/login',
    name: 'Login',
    component: LogIn,
  },
  {
    path: '/purchase',
    name: 'Purchase',
    component: Purchase,
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
