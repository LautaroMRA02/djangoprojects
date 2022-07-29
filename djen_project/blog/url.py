from django.urls import path
from .views import BlogPost

urlpatterns = [
    path('', BlogPost.as_view(), name='create'),
]   