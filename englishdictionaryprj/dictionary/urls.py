from django.urls import path
from .views import home, word

urlpatterns = [
    path('', home, name='home'),
    path('word/', word, name='word'),
]
