from django.shortcuts import render
from feedparser import parse
import json

from planet_wttd.core.urls import blog_tuple


def home(request):
    return render(request, 'index.html', {'blogs': get_feed_context()})


def get_feed_context():
    urls = blog_tuple

    context = []
    for url in urls:
        feed = parse(url)

        if feed['status'] != 200:
            continue
        title = feed['feed']['title']
        link = feed['feed']['link']

        posts = []
        for post in feed['entries'][:5]:
            d = {'title': post['title'], 'link': post['link']}

            post_date = post['updated_parsed']
            d['date'] = '{}/{}/{}'.format(post_date.tm_mday,
                                          post_date.tm_mon,
                                          post_date.tm_year)

            posts.append(d)

        context.append(dict(title=title, link=link, posts=posts))

    return context


