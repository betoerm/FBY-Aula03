from django.urls import path

# criar a rota para a views.py - importar as views
from .views import people_views

urlpatterns = [    
    path('', people_views.home, name="index"),
    path('listar', people_views.listar, name="listar"),   
    path('detalhar/<int:id_pessoa>/', people_views.detalhar, name="detalhar"),
    path('excluir/<int:id_pessoa>/', people_views.excluir, name="excluir"),
    path('cadastrar', people_views.cadastrar, name="cadastrar")
]


