from django.shortcuts import render
from feedparser import parse
import json

from planet_wttd.core.urls import blog_tuple


def home(request):
    g = get_feed_context()
    print(json.dumps(g, indent=4))
    return render(request, 'index.html', g)


def get_feed_context():
    urls = blog_tuple

    context = []
    for url in urls:
        feed = parse(url)

        title = feed['feed']['title']
        link = feed['feed']['link']

        posts = []
        for post in feed['entries'][:5]:

            d = {}

            post_title = post['title']
            post_date = post['updated_parsed']
            post_date = '{}/{}/{}'.format(post_date.tm_mday,
                                          post_date.tm_mon,
                                          post_date.tm_year)

            post_link = post['link']

            d['title'] = post_title
            d['link'] = post_link
            d['date'] = post_date
            posts.append(d)

        context.append(dict(title=title, link=link, posts=posts))

    return {'blogs': context}


