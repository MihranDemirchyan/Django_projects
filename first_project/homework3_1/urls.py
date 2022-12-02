from django.urls import path
from homework3_1 import views

urlpatterns = [
    path('greeting/', views.greeting),
    path('intro/', views.introduction),
    path('time/', views.current_time),
    path('dict/', views.dictionary_keys_squares)
]