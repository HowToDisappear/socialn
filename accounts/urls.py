from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.users),
    path('<int:pk>', views.user),
    path('signup', views.signup),
    path('signin/token/obtain', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns = format_suffix_patterns(urlpatterns)