from connexion.models import Article
def run():
    for i in range(13,18):
        article = Article()
        article.title = f"Article {i}" #"....No #%id" % i
        article.desc = f"Description de l'article {i}" #".... No #%id" % i
        article.image = "http://default" #f"article{i}.jpg" 
        article.save()
print("Opération réussie") #f"article{i}.jpg"