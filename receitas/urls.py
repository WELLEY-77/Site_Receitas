from django.urls import path
from. import views

urlpatterns = [
    path('',views.receita , name='receita'),
    path('<int:receita_id>', views.imagem, name='imagem'),
]