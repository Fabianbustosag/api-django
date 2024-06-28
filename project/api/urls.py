from django.urls import path, include

from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views2.view_food import FoodModelView
# from .views2.view_food import algo


router = routers.DefaultRouter()
router.register(r'food',FoodModelView )

urlpatterns = [    
    path('api/', include(router.urls)),
    path('api/', views.hello),
    path('docs/', include_docs_urls),
    # path('docs/', algo()),

]