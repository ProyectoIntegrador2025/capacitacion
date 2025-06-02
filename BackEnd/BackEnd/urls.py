from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#SWAGGER
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Curso Python Django",
        default_version='v1',
        description="API para capacitación",
        terms_of_service="http://127.0.0.1:8000/Documentacion/",
        contact=openapi.Contact(email="camachopanizza@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('Home.urls')), #Dejar vacio el path es para una pag de inicio o bienvenida por que es que no pusieron nada en particular.
    
    path('API/V1/', include('Prueba1.urls')),
    
    path('API/V1/', include('Categorias.urls')),

    path('API/V1/', include('Recetas.urls')),

    path('API/V1/', include('Contacto.urls')),

    path('API/V1/', include('Seguridad.urls')),

    path('API/V1/', include('recetas_helper.urls')),

    #RUTAS SWAGGER ESTO SIEMPRE ES ASI SE COPIA Y SE PEGA
    path('Documentacion<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), #ESTO ES PARA EL JSON LA URL
    path('Documentacion/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-json-ui'), #ESTA ES LA URL GENERAL DE LA DOCUMENTACION
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc') #ESTA ES UNA DOCUMENTACION ADICIONAL UTIL
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
