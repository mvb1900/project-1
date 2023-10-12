import { createRouter, createWebHistory } from 'vue-router'
import ROUTER_APP from './routers'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      ...ROUTER_APP
  ]
})

export default router
