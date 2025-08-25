from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Vérifier si l’utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            return render(request, 'inscription.html', {'error': "Nom d'utilisateur déjà pris"})

        # Créer un nouvel utilisateur
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Connecter automatiquement l’utilisateur après inscription
        login(request, user)
        return redirect('Home')

    return render(request, 'inscription.html')


def connexion(request):
    texte="""<h1>Bienvenue sur la page de connexion!</h1>"""
    if request.method == 'POST':
         #vérifier les informations de connexions
         #Rediriger l'utilisateur vers la vue Home si info corrects
         return redirect('Home')
    return HttpResponse(texte)
#  

from django.contrib.auth.decorators import login_required
@login_required
def Home(request):
       list_articles = Article.objects.all()
       context = {'liste_articles': list_articles}
       return render(request, 'home.html', context, {'user': request.user})
def detail(request,id_article):
     article=Article.objects.get(id=id_article)
     category=article.category
     articles_en_relation=Article.objects.filter(category=category)[:5]
     return render(request, 'detail.html', {'article': article, 'aer':articles_en_relation})

def search_view(request):
    query = request.GET.get('q')  # Récupérer la valeur de recherche
    results = []  # Liste pour stocker les résultats

    if query:
        results = Article.objects.filter(title__icontains=query)  # Recherche dans le champ "title"

    return render(request, 'search.html', {'query': query, 'results': results})
