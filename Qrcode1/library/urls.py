"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 

from rest_framework import routers
from qrcode import viewsets

from django.conf.urls.static import static
from django.conf import settings
# as viewssets

#route = routers.DefaultRouter() 
#route.register(r'caso',viewssets.CasoViewSet,basename="caso" )


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include(route.urls))
    path('caso/', viewsets.CasoManutencaoViewSet.as_view()),
    path('caso/delete/<int:pk>/', viewsets.user_detail),
    path('historico/', viewsets.HistoricoViewSet.as_view()),
    path('historico/delete/<int:pk>/', viewsets.user_detail),
    path('historico/get/<int:pk>/', viewsets.user_details),
    path('avarias/', viewsets.AvariasViewSet.as_view()),
    path('avarias/delete/<int:pk>/', viewsets.user_detail),
    path('informacao/', viewsets.InformacaoViewSet.as_view()),
    path('informacao/delete/<int:pk>/', viewsets.user_detail),
    path('fotos/', viewsets.FotosViewSet.as_view()),
    path('fotos/delete/<int:pk>/', viewsets.user_detail2),
    path('fotos/get/<int:pk>/', viewsets.user_details2),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


