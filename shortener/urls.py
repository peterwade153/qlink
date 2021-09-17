from django.urls import path

from shortener import views


urlpatterns = [
    path('shortener/', views.ShortenerView.as_view(), name='url'),
]
