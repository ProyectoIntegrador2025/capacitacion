import Error404 from '@/views/Error404.vue'
import Recetas from '@/views/Recetas.vue'
import RecetasDetalle from '@/views/RecetasDetalle.vue'
import SobreNosotros from '@/views/SobreNosotros.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', //CON ESTO ES LA RUTA A LA QUE SE ENTRA A LA PAGINA
      component: () => import('@/views/Home.vue'),
      name: 'Home'
    },
    {
      path: '/Sobre-Nosotros',
      component: SobreNosotros,
      name: 'SobreNosotros'
    },
    {
      path: '/Recetas',
      component: Recetas,
      name: 'Recetas'
    },
    {
      path: '/recetas/detalle/:nombre',
      component: RecetasDetalle,
      name: 'RecetasDetalle'
    },
    {
      path: '/:pathMatch(.*)*', //ESTE SIEMPRE VA AL FINAL DE TODAS LAS RUTAS, y es para que si ponen mal una url les muestre un mensaje de que le pifiaron
      component: Error404
    }
  ]
})

export default router
