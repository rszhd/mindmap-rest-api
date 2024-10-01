from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MindMapViewSet, NodeViewSet, NoteViewSet, register_user

router = DefaultRouter()
router.register(r'mindmaps', MindMapViewSet, basename='mindmap')
router.register(r'nodes', NodeViewSet, basename='node')
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
]