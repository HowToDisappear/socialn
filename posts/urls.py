from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts),
    path('<int:pk>', views.post),
    path('<int:pk>/like', views.like),
    path('analytics/likes/', views.likes_daily),
]
urlpatterns = format_suffix_patterns(urlpatterns)