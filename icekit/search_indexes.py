from django.conf import settings
from django.utils import translation
from fluent_pages.models import Page
from haystack import indexes
from fluent_pages.models.db import UrlNode
from icekit.utils.search import AbstractLayoutIndex


class PageIndex(AbstractLayoutIndex, indexes.Indexable):
    """Index all Fluent Pages"""

    def get_model(self):
        return Page

    def index_queryset(self, using=None):
        translation.activate(settings.LANGUAGE_CODE)
        return self.get_model().objects.filter(status=UrlNode.PUBLISHED).select_related()
