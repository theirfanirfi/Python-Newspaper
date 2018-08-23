from django.shortcuts import render
from django.http import HttpResponse
import newspaper
from NewspaperApp.models import ArticleModel
from newspaper import Article
import datetime
import json
# Create your views here.
def index(request):
	return render(request, 'index.html')

def article(request, value):
	return HttpResponse("your value is "+value)

def detail(request):
	query = request.GET.get("u")
	article = Article(url=query)
	article.download()
	if article.download_state == 1:
	    return HttpResponse("Article can not be downloaded. Possible Reason: Invalid URL.")
	elif article.download_state == 0:
	    return HttpResponse("Article can not be downloaded. Possible Reason: Invalid URL.")
	else:
		isExist = ArticleModel.objects.filter(article_url=query)
		if len(isExist) == 0:
			article.parse()
			obj = ArticleModel(
				publish_date = article.publish_date,
				visit_date = datetime.datetime.now(),
				article_url = article.url
				)

			obj.save()
		else:
			article.parse()

		return render(request, 'post.html', {'article' : article})
