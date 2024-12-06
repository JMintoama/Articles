from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect #charger la méthode redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Article

def connexion(request):
    texte="""<h1>Bienvenue sur la page de connexion!</h1>"""
    if request.method == 'POST':
         #vérifier les informations de connexions
         #Rediriger l'utilisateur vers la vue Home si info corrects
         return redirect('Home')
    return HttpResponse(texte)
#    

def Home(request):
       list_articles = Article.objects.all()
       context = {'liste_articles': list_articles}
       return render(request, 'home.html', context)
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

    return render(request, 'search_results.html', {'query': query, 'results': results})