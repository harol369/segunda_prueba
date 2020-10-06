from django.urls import path
from .views import index, primera

urlpatterns = [
    path('', index, name='index'),
    path('primera', primera, name='primera')
]
