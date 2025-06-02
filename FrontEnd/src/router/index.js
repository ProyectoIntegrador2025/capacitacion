import Error404 from '@/views/Error404.vue'
import FormularioDeContacto from '@/views/FormularioDeContacto.vue'
import LogIn from '@/views/LogIn.vue'
import Recetas from '@/views/Recetas.vue'
import RecetasBuscador from '@/views/RecetasBuscador.vue'
import RecetasDetalle from '@/views/RecetasDetalle.vue'
import Registro from '@/views/Registro.vue'
import Seguridad from '@/views/Registro.vue'
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
      path: '/recetas/detalle/:slug',
      component: RecetasDetalle,
      name: 'RecetasDetalle'
    },
    {
      path: '/recetas/buscador',
      component: RecetasBuscador
    },
    {
      path: '/Contacto',
      component: FormularioDeContacto,
      name: 'FormularioDeContacto'
    },
    {
      path: '/Registro',
      component: Registro,
      name: 'Registro'
    },
    {
      path: '/LogIn',
      component: LogIn,
      name: 'LogIn'
    },
    {
      path: '/:pathMatch(.*)*', //ESTE SIEMPRE VA AL FINAL DE TODAS LAS RUTAS, y es para que si ponen mal una url les muestre un mensaje de que le pifiaron
      component: Error404
    }
  ]
})

export default router
