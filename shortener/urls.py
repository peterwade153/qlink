from django.urls import path

from shortener import views


urlpatterns = [
    path('shortener/', views.ShortenerView.as_view(), name='shortener'),
    path('<str:short_url>', views.RedirectView.as_view(), name='redirect_url'),
]
