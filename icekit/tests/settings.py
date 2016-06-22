"""
Test settings for ``icekit`` app.
"""
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SITE_ID = 1

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = (
    'bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_nose',
    'django_wysiwyg',
    'forms_builder.forms',
    'fluent_contents',
    'fluent_contents.plugins.oembeditem',
    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',
    'haystack',
    'icekit',
    'icekit.page_types.layout_page',
    'icekit.page_types.search_page',
    'icekit.plugins.child_pages',
    'icekit.plugins.faq',
    'icekit.plugins.file',
    'icekit.plugins.horizontal_rule',
    'icekit.plugins.image',
    'icekit.plugins.instagram_embed',
    'icekit.plugins.map',
    'icekit.plugins.map_with_text',
    'icekit.plugins.oembed_with_caption',
    'icekit.plugins.page_anchor',
    'icekit.plugins.page_anchor_list',
    'icekit.plugins.quote',
    'icekit.plugins.reusable_quote',
    'icekit.plugins.reusable_form',
    'icekit.plugins.slideshow',
    'icekit.plugins.twitter_embed',
    'icekit.response_pages',
    'icekit.tests',

    # Required for oembed
    'micawber',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'icekit.tests.urls'
SECRET_KEY = 'secret-key'
STATIC_URL = '/static/'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
FLUENT_PAGES_TEMPLATE_DIR = os.path.join(
    BASE_DIR, 'icekit', 'templates',
)

BRIGHTCOVE_PLAYER = {}
BRIGHTCOVE_TOKEN = ''

RESPONSE_PAGE_PLUGINS = ['ImagePlugin', ]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

THUMBNAIL_BASEDIR = 'thumbs'

NOSE_ARGS = [
    '--logging-clear-handlers',  # Clear all other logging handlers
    '--nocapture',  # Don't capture stdout
    '--nologcapture',  # Disable logging capture plugin
    # '--processes=-1',  # Automatically set to the number of cores
    '--with-progressive',  # See: https://pypi.python.org/pypi/nose-progressive
]

# TRAVIS ######################################################################

if 'TRAVIS' in os.environ:
    NOSE_ARGS.remove('--with-progressive')
