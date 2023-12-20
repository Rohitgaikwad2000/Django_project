"""productapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.views import Welcome, Add_product, Update_product, Delete_product, Deleted_product, Restore_product, permanantly_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Welcome, name = "home"),
    path('add-product/',Add_product, name = "add_product"),
    path('update-product/<int:id>/', Update_product, name = "update_product"),
    path('delete-product/<int:id>/', Delete_product, name = "delete_product"),
    path('deleted-product/', Deleted_product, name = "deleted_product"),
    path('restore-product/<int:id>/', Restore_product, name = "restore_product"),
    path('permanantly_delete-product/<int:id>/', permanantly_delete, name = "permanantly_delete_product"),



    path('user/', include('user_app.urls')),    # include all the url forms user_app

]