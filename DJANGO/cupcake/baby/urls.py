from django.urls import path
from baby import views

urlpatterns = [
    path('', views.index, name='baby'),
]

