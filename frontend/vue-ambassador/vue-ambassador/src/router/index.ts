import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '',
    name: 'Layout',
    component: () => import('@/views/Layout.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: import("@/views/Login.vue")
  },
  {
    path: '/register',
    name: 'register',
    component: import("@/views/Register.vue")
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
