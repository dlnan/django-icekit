from fluent_pages.integration.fluent_contents.admin import FluentContentsPageAdmin

from icekit.admin_mixins import FluentLayoutsMixin, HeroMixinAdmin, \
    ListableMixinAdmin
from icekit.publishing.admin import PublishingAdmin


class UnpublishableLayoutPageAdmin(FluentLayoutsMixin, FluentContentsPageAdmin):
    raw_id_fields = ('parent',)


class LayoutPageAdmin(
    FluentLayoutsMixin,
    FluentContentsPageAdmin,
    PublishingAdmin,
    HeroMixinAdmin,
    ListableMixinAdmin,
):

    raw_id_fields = HeroMixinAdmin.raw_id_fields + ('parent',)

    base_fieldsets = FluentContentsPageAdmin.base_fieldsets[0:1] + \
                     HeroMixinAdmin.FIELDSETS + \
                     ListableMixinAdmin.FIELDSETS + \
                     FluentContentsPageAdmin.base_fieldsets[1:]