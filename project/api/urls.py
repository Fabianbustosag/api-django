from django.urls import path, include
# from .views2.view_image import upload_image
# from .views2.view_food import algo

from . import views

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views2.view_food import FoodModelView
from .views2.view_pulication import PublicationModelView
from .views2.view_image import ImageUploadView
from django.conf import settings
from django.conf.urls.static import static

from .views2.view_image import test_eval, test_eval2

router = routers.DefaultRouter()
router.register(r'food',FoodModelView)
router.register(r'publication',PublicationModelView)

urlpatterns = [    
    path('api/', include(router.urls)),
    path('hello/', views.hello),
    path('docs/', include_docs_urls),
    # path('upload/', upload_image, name='upload_image'),
    path('upload_2/', ImageUploadView.as_view()),
    # path('test/', test_eval),
    path('test/', test_eval2),


    path('create/',views.create_model),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)