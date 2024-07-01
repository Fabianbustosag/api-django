from django.urls import path, include
from . import views
from rest_framework import routers
from .views_folder.userData import *
# from .views import CatalogoViewSet

router = routers.DefaultRouter()
# router.register(r'catalogo',views.CatalogoViewSet, 'catalogo') # era el antiguo clase de catalogo

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/',views.hello),
    path('userData/getInfo/<int:user_id>/', get_user_data, name='GetUser'),
    path('userData/postNewUser',post_new_user,name='NewUser'),
    path('userData/update/<int:user_id>/', update_user_data, name='UpdateUser'),
    path('userData/delete/<int:user_id>/', delete_user_data, name='DeleteUser')
]