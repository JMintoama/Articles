from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Home'),
    path('', views.connexion, name = 'connexion'), 
    path('inscription/', views.inscription, name = 'inscription'),
    path('déconnexion/', views.deconnexion, name='deconnexion'),
    path('article/', views.article, name='article'),
    path('article/<int:id_article>',detail, name='detail'),
    path('search/', views.search_view, name='search'),
]
