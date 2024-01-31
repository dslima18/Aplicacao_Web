"""Define padrões de URL para learning_logs"""

from django.urls import include, path, re_path
from . import views
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
]