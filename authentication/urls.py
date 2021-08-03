from django.urls import path

from authentication import views


urlpatterns = [
    path('users/', views.UserView.as_view(), name='users')
]
