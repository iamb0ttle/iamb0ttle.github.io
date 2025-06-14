import attila

THEME = attila.get_path()

AUTHOR = 'Byeonghyeon Na'
SITENAME = 'Byeonghyeon Na Blog'
SITEURL = 'https://iamb0ttle.github.io'
SITESUBTITLE = """Hello 👋 Welcome to Byeonghyeon Na's blog!<br>
I'm a software engineer passionate about <br>
learning and building, sharing my insights and tech explorations here."""

PATH = "content"

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
}

COPYRIGHT_YEAR = 2025

TIMEZONE = 'Asia/Seoul'

DEFAULT_DATE_FORMAT = '%d %b %Y'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None





# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/byeonghyeon-na'),
    ('Github', 'https://github.com/iamb0ttle')
)





HOME_COVER = 'assets/images/home-bg.jpg'






AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'

YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'






MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.tables": {},

        "markdown.extensions.toc": {
            "title": "Table of Contents",
            "marker": "[TOC]",
            "permalink": "false",
        },
    },
    "output_format": "html5",
}



# Plugin
PLUGINS = [
    "pelican.plugins.image_process",
    # "pelican.plugins.minify",
    "pelican.plugins.neighbors",
    "pelican.plugins.related_posts",
    # "pelican.plugins.seo",
    "pelican.plugins.sitemap",
    "pelican.plugins.statistics",
    "pelican.plugins.webassets",
]

DISQUS_SITENAME = 'iamb0ttlegithubio'
GOOGLE_ANALYTICS = 'G-H4PC9Q2STK'

IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 False"]),
            ("2x", ["scale_in 1600 1200 False"]),
            ("4x", ["scale_in 3200 2400 False"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1920px) 2000px, "
            "(min-width: 1400px) 1600px, "
            "(min-width: 1000px) 1200px, "
            "(min-width: 768px) 900px, "
            "100vw"
        ),
        "srcset": [
            ("800w", ["scale_in 800 533 False"]),
            ("1600w", ["scale_in 1600 1067 False"]),
            ("2400w", ["scale_in 2400 1600 False"]),
            ("3200w", ["scale_in 3200 2133 False"]),
        ],
        "default": "1600w",
    },
}

# MINIFY = {
#     "css": True,           
#     "js": False,           
#     "html": True,          
#     "inline_css": True,    
#     "inline_js": True,     
# }

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}




AUTHOR_META = {
  "byeonghyeon na": {
    "name": "Byeonghyeon Na",
    "cover": "assets/images/author-bg.jpg",
    "image": "assets/images/avatar.png",
    "linkedin": "byeonghyeon-na",
    "github": "iamb0ttle",
    "location": "https://dsmhs.djsch.kr/main.do",
    "bio": """My name is Byeonghyeon Na, and I'm pursuing a career as an innovative software engineer. 
    I'm passionate about navigating and contributing to our fast-paced world, 
    with the ultimate goal of making a significant positive impact on society."""
  }
}





TAG_META = {
    # "cupcake": {
    #     "cover": "assets/images/rainbow_cupcake_cover.png",
    #     "description": "Cupcake ipsum dolor sit amet. Topping",
    # },
}





CATEGORY_META = {
    # "examples": {
    #     "cover": "https://images.unsplash.com/photo-1645113720391-279a153b4f53?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2073&q=80",
    #     "description": "Examples ipsum dolor sit amet. Topping"
    # },
}






MENUITEMS = (('Home', '/'),
             ('Tag', '/tag'),
             ('Author', '/author/byeonghyeon-na'),
             ('Category', '/categories'),
             ('Archives','/archive'),)







SHOW_ARTICLE_MODIFIED_TIME = True
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = True
SHOW_CREDITS = True
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = True
SHOW_SITESUBTITLE_IN_HTML_TITLE = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = True




CSS_OVERRIDE = ['assets/css/custom_styles.css']