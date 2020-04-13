from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('categories', views.categories, name='categories'),
]
