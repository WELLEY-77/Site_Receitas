from django.urls import path
from. import views

urlpatterns = [
    path('',views.receita , name='receita'),
    path('imagem/', views.imagem, name='imagem')
]