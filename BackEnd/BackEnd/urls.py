from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')), #Dejar vacio el path es para una pag de inicio o bienvenida por que es que no pusieron nada en particular.
    path('API/V1/', include('Prueba1.urls')),
    path('API/V1/', include('Categorias.urls')),
    path('API/V1/', include('Recetas.urls')),
    path('API/V1/', include('Contacto.urls')),
    path('API/V1/', include('Seguridad.urls')),
    path('API/V1/', include('recetas_helper.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
