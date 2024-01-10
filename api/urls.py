from rest_framework import routers
from django.urls import path, include

from api.views import LoginApiView, DrawingModelViewSet, ShapeModelViewSet, AnnotationModelViewSet

router = routers.SimpleRouter()
router.register(r'drawing', DrawingModelViewSet)
router.register(r'shape', ShapeModelViewSet)
router.register(r'annotation', AnnotationModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginApiView.as_view(), name='login-api'),
]