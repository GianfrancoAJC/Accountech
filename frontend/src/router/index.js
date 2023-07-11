import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../components/SignUp.vue'
import LogIn from '../components/LogIn.vue'
import Purchase from '../components/Purchase.vue'
import Sale from '../components/Sale.vue'
import Tools from '../components/Purchase.vue'
import buyForm from '../components/buyForm.vue'
import client from '../views/client.vue'
import employee from '../views/employee.vue'

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
  },
  {
    path: '/sale',
    name: 'Sale',
    component: Sale,
  },
  {
    path: '/tools',
    name: 'Tools',
    component: Tools,
  },
  {
    path: '/buyForm',
    name: 'buyForm',
    component: buyForm,
  },
  {
    path: '/client',
    name: 'Client',
    component: client,
  },
  {
    path: '/employee',
    name: 'Employee',
    component: employee,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
