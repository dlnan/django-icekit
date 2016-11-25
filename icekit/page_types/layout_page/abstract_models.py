from fluent_pages.integration.fluent_contents import FluentContentsPage

from icekit.models import ICEkitFluentContentsPageMixin
from icekit.mixins import LayoutFieldMixin, HeroMixin, ListableMixin


class AbstractUnpublishableLayoutPage(FluentContentsPage, LayoutFieldMixin):
    class Meta:
        abstract = True


class AbstractLayoutPage(ICEkitFluentContentsPageMixin, LayoutFieldMixin,
                         HeroMixin, ListableMixin):
    class Meta:
        abstract = True

    def get_type(self):
        # we don't normally want pages to say they're a 'page'
        return ""

    def get_parent(self):
        if self.parent:
            return self.parent.get_visible()
        return None