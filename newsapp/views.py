from django.shortcuts import render, HttpResponse
from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsapi = NewsApiClient("6343b56ea7024331950d3a47c05767c5")
    top = newsapi.get_top_headlines(sources="the-times-of-india,google-news-in")
    articles = top['articles']
    news = []
    dec = []
    img = []
    original = []
    author = []
    date = []
    time = []
    for i in range(len(articles)):
        curr = articles[i]
        news.append(curr['title'])
        dec.append(curr['description'])
        img.append(curr['urlToImage'])
        original.append(curr['url'])
        author.append(curr['author'])
        date.append(curr['publishedAt'][:10])
        time.append(curr['publishedAt'][11:16])
    context = zip(news,dec, img, original, author, date, time)

    return render(request, 'index.html', context={"mylist": context})
