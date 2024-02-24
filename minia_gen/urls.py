from django.urls import path
from .views import hello_world, generer_miniature

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('gen/', generer_miniature, name='generer_miniature'),
]
