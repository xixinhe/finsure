from django.urls import path, include, re_path
from .views import LenderViewSet, CsvDownloadView, CsvUploadView
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('', LenderViewSet, basename='lender')

urlpatterns = [
    path('upload/', CsvUploadView.as_view()),
    path('csv/', CsvDownloadView.as_view()),
    path('', include(router.urls)),
    
]
