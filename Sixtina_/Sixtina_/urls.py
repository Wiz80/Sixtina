"""Sixtina_ URL Configuration

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
from django.urls import path
from django.conf import settings
from Interfaz import views as interviews
from Usuarios import views as userviews
from Clothes import views as ropaviews
from Hombre import views as homviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo-usuario/', userviews.nuevo_usuario, name = "nuevo-usuario"),
    path('login/', userviews.login, name = "login"),
    path('hombre/',interviews.hombre, name = "hombre"),
    path('', interviews.mujer, name = "mujer"),
    path('ropa/', ropaviews.ropa, name = "ropa"),
    path('camisetas-hombre/', homviews.camisetas, name = "camisetas-hombre")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
