from django.shortcuts import render
from django.http import HttpResponse
import newspaper
from newspaper import Article
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
	article.parse()
	return render(request, 'post.html',{'article' : article})
