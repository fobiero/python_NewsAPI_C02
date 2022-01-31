# from distutils.log import debug
from urllib.parse import urljoin
from wsgiref.util import request_uri
from flask import Flask,render_template,request
from newsapi import NewsApiClient

app=Flask(__name__, template_folder='app/templates', static_folder='app/static')


@app.route("/")
def home():
    news_api = NewsApiClient(api_key = '4c332f55740d4613ba5b782849fad70e')
    top_headlines = news_api.get_top_headlines(sources="bbc-news,the-verge")

    articles = top_headlines['articles']

    news = []
    # description = []
    img = []
    posted_at = []

    for i in range(len(articles)):
        all_news = articles[i]

        news.append(all_news['title'])
        # description.append(all_news['descripton'])
        img.append(all_news['urlToImage'])
        posted_at.append(all_news['publishedAt'])
    
    news_data = zip(news, img, posted_at)
    return render_template('home.html', news_data = news_data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')



if __name__=="__main__":
    app.run(debug=True)
