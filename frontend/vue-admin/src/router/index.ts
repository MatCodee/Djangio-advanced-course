import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import User from "@/views/Users.vue"
import Links from "@/views/Links.vue"
import Products from "@/views/products/Products.vue"
import ProductForm from "@/views/products/ProductForm.vue"
import Orders from "@/views/Orders.vue"
import Profile from "@/views/Profile.vue"
Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: Home,
    children: [
      {path:'',redirect: '/users'},
      {path: '/users', component: User},
      {path: '/users/:id/links', component: Links},
      {path: '/products', component: Products},
      {path: '/products/create',component: ProductForm},
      {path: '/products/:id/edit', component: ProductForm },
      {path: '/Orders',component: Orders},
      {path: '/profile',component: Profile},
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
