from django.urls import path, include
# from .views2.view_image import upload_image
# from .views2.view_food import algo

from .views2 import seguimiento_view
from .views2 import view_auth


from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views2.view_food import FoodModelView
from .views2.view_pulication import PublicationModelView
from .views2.view_image import ImageUploadView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'food',FoodModelView)
router.register(r'publication',PublicationModelView)

urlpatterns = [    
    path('login/', view_auth.login),
    path('register/', view_auth.register),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls),
    # path('upload/', upload_image, name='upload_image'),
    path('upload_2/', ImageUploadView.as_view()),
    path('api/weekly_summary/', seguimiento_view.get_weekly_summary, name='weekly_summary'),
    path('api/monthly_summary/', seguimiento_view.get_monthly_summary, name='monthly_summary'),
    path('api/yearly_summary/', seguimiento_view.get_yearly_summary, name='yearly_summary'),
    path('api/weekly_summary_price/', seguimiento_view.get_weekly_summary_price, name='weekly_summary_price'),
    path('api/monthly_summary_price/', seguimiento_view.get_monthly_summary_price, name='monthly_summary_price'),
    path('api/yearly_summary_price/', seguimiento_view.get_yearly_summary_price, name='yearly_summary_price'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)