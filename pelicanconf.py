#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'bonohu'
SITENAME = u'bonohu blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (('Dr.Bono\'s website', 'http://dbcls.jp/%7Ebono/'),
         ('GitHub', 'https://github.com/bonohu'),
         ('ORCID', 'http://orcid.org/0000-0003-4413-0651'),
         ('PubMed', 'https://www.ncbi.nlm.nih.gov/pubmed?cmd=search&term=Bono%20H[au]%20AND%201995%3A2100[dp]%20NOT%20jpn[la]'),
         ('ResearchMap', 'https://researchmap.jp/bonohu/?lang=english'),)

# Social
SOCIAL = (('Twitter', 'https://twitter.com/drbonohu'),
	 ('GoogleScholar', 'https://scholar.google.co.jp/citations?user=e6OaeXQAAAAJ&hl=en'),
         ('Figshare', 'https://figshare.com/authors/Hidemasa_Bono/476712'),
         ('ImpactStory', 'https://profiles.impactstory.org/u/0000-0003-4413-0651'),
         ('ResearchGate', 'https://www.researchgate.net/profile/Hidemasa_Bono'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/bono/Documents/etc/pelican-themes/foundation-default-colours"
GOOGLE_ANALYTICS = 'UA-113297-11'  # Tracking ID
