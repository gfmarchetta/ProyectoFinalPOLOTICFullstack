from django import urls
from django.urls import path
from django.urls.conf import include
from  . import views
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade', views.acercade, name='acercade'),
    path('categorias', views.categorias, name='categorias'),
    #path('contacto', views.contacto, name='contacto'),
    #Spath('nuevo_producto', views.nuevo_producto, name='nuevo_producto'),
    path('resultados', views.resultados, name='resultados'),
    path('<int:producto_id>', views.producto, name='producto'),
    path('resultados/', views.buscar, name='buscar'),
     path('carro/', views.carro, name='carro'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
