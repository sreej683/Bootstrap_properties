"""
URL configuration for project10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('alerts/',alerts,name='alerts'),
    path('badge/',badge,name='badge'),
    path('breadcrumb/',breadcrumb,name='breadcrumb'),
    path('buttons/',buttons, name='buttons'),
    path('buttongroup/',buttongroup,name='buttongroup'),
    path('card/',card,name='card.html'),
    path('carousel/',carousel,name='carousel.html'),
    path('collapse/',collapse,name='collapse.html'),
    path('dropdown/',dropdown,name='dropdown.html'),
    path('forms/',forms,name='forms.html'),
    path('inputgroup/',inputgroup,name='inputgroup.html'),
    path('jumpbortron/',jumpbortron,name='jumpbortron.html'),
    path('list/',list,name='list.html'),
    path('mediaobject/',mediaobject,name='mediaobject.html'),
    path('modal/',modal,name='modal.html'),
    path('navs/',navs,name='navs.html'),
    path('navbar/',navbar,name='navbar'),
    path('pagination/',pagination,name='pagination'),
    path('popovers/',popovers,name='popovers.html'),
    path('progress/',progress,name='progress.html'),
    path('scrollspy/',scrollspy,name='scrollspy.html'),
    path('spinners/',spinners,name='spinners.html'),
    path('toasts/',toasts,name='toasts.html'),
    path('tooltips/',tooltips,name='tooltips.html'),
]
