#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bo Yu'
SITENAME = u'Presentations by Bo Yu'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

PAGE_DIR = 'pages'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

#ARTICLE_DIR = 'articles'
ARTICLE_URL = False
ARTICLE_SAVE_AS = False
AUTHOR_URL = False
AUTHOR_SAVE_AS = False
CATEGORY_URL = False
CATEGORY_SAVE_AS = False
TAG_URL = False
TAG_SAVE_AS = False

DIRECT_TEMPLATES = ('index')
TAGS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
ARCHIVES_SAVE_AS = False
AUTHORS_SAVE_AS = False

TYPOGRIFY = True
THEME = "themes/presentation"

STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'images/favicon.png': {'path': 'favicon.png'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
