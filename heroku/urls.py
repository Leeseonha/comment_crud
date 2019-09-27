"""heroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import detail.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:pk>/', detail.views.detail, name='detail'),
    path('new/', detail.views.new, name='new'),
    # path('', detail.views.home, name='home'),
    path('home2/', detail.views.home2, name='home2'),
    path('',detail.views.index, name='index'),
    path('create/', detail.views.create, name='create'),
    path('update/', detail.views.update, name='update'),
    path('detail/<int:pk>/remove/' , detail.views.remove, name='remove'),
    path('detail/<int:pk>/edit/' , detail.views.edit, name='edit'),
    path('newblog/', detail.views.create, name='newblog'),
    path('detail/<int:detail_id>/comment_remove/<int:pk>/' , detail.views.comment_remove, name='comment_remove'),
    path('detail/<int:detail_id>/comment_edit/<int:pk>/' , detail.views.comment_edit, name='comment_edit'),
]
