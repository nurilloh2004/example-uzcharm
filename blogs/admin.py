from django.contrib import admin

from parler import admin as parler_admin
from parler.admin import TranslatableAdmin
from mptt import admin as mptt_admin
from django.utils.translation import gettext_lazy as _

from . import models
from .models import Contact

# Admin decorations
admin.site.site_header = _('Uzcharmsanoat admin panel')
admin.site.site_title = _('Uzcharmsanoat Admin Portal')
admin.site.index_title = _('Welcome to Uzcharmsanoat Portal')


@admin.register(models.Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'publish', 'status',)
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


# @admin.register(models.SiteSetting)
# class SiteSettingAdmin(admin.ModelAdmin):
#     class Media:
#         js = [
#             'https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.js',
#             'https://code.jquery.com/jquery-2.2.4.min.js',
#             'https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v4.5.1/mapbox-gl-geocoder.min.js'
#         ]
#         css = {
#             'all': [
#                 'https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.css',
#             ]
#         }


@admin.register(models.Menu)
class MenuAdmin(parler_admin.TranslatableAdmin, mptt_admin.DraggableMPTTAdmin):
    pass


@admin.register(models.MenuOverlay)
class MenuOverlay(TranslatableAdmin, mptt_admin.DraggableMPTTAdmin):
    pass


@admin.register(models.Banner)
class Banner(TranslatableAdmin):
    pass


@admin.register(models.PressReleasesAdmin)
class PressRealeses(TranslatableAdmin):
    pass


@admin.register(models.PressServiceAdmin)
class PressService(TranslatableAdmin):
    pass


@admin.register(models.PresentationsAdmin)
class Presentations(TranslatableAdmin):
    pass


@admin.register(models.ExportLawAdmin)
class ExportLaw(TranslatableAdmin):
    pass


@admin.register(models.MarketEntryStrategies)
class MarketEntryStrategiesAdmin(TranslatableAdmin):
    pass


@admin.register(models.ExportImplementationAdmin)
class ExportImplementationAdmin(TranslatableAdmin):
    pass


@admin.register(models.InvestmentPotentialAdmin)
class InvestmentPotentialAdmin(TranslatableAdmin):
    pass


@admin.register(models.ExportPotentialAdmin)
class ExportPotentialAdmin(TranslatableAdmin):
    pass


@admin.register(models.EventsAdmin)
class Events(TranslatableAdmin):
    pass


@admin.register(models.PublicationsAdmin)
class Publications(TranslatableAdmin):
    pass


@admin.register(models.HowToJoin)
class HowToJoin(TranslatableAdmin):
    pass


# @admin.register(models.MenuCompanys)
# class MenuCompanys(TranslatableAdmin):
#     pass


@admin.register(models.CompanyTypes)
class CompanyTypes(TranslatableAdmin):
    pass


@admin.register(models.FAQ)
class FAQAdmin(TranslatableAdmin):
    pass


@admin.register(models.BenefitsAdmin)
class BenefitsAdmin(TranslatableAdmin):
    pass


@admin.register(models.StructureAdmin)
class StructureAdmin(TranslatableAdmin):
    pass


@admin.register(models.HistoryAdmin)
class HistoryAdmin(TranslatableAdmin):
    pass


@admin.register(models.ForeighnAdmin)
class ForeighnAdmin(TranslatableAdmin):
    pass


@admin.register(models.SubsidariesAdmin)
class SubsidariesAdmin(TranslatableAdmin):
    pass


@admin.register(models.Subsidaries2Admin)
class Subsidaries2Admin(TranslatableAdmin):
    pass


@admin.register(models.TerritorialAdmin)
class TerritorialAdmin(TranslatableAdmin):
    pass


@admin.register(models.Media)
class MediaAdmin(TranslatableAdmin):
    pass


@admin.register(models.CompanyInfo)
class FAQAdmin(TranslatableAdmin):
    pass


@admin.register(models.UsefulLink)
class UsefulLinkAdmin(TranslatableAdmin):
    pass


@admin.register(models.StaticContent)
class StaticContentAdmin(TranslatableAdmin):
    pass


@admin.register(models.ShortLink)
class ShortLinkAdmin(TranslatableAdmin, mptt_admin.DraggableMPTTAdmin):
    pass


@admin.register(models.Partner)
class PartnerAdmin(TranslatableAdmin):
    pass


@admin.register(models.MoscowAdmin)
class MoscowAdmin(TranslatableAdmin):
    pass


@admin.register(models.InvestorsAdmin)
class InvestorsAdmin(TranslatableAdmin):
    pass


@admin.register(models.ExportersAdmin)
class ExportersAdmin(TranslatableAdmin):
    pass


@admin.register(models.Statistic)
class StatisticAdmin(TranslatableAdmin):
    pass


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(TranslatableAdmin):
    pass


@admin.register(models.VirtualReception)
class VirtualReceptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExpoLink)
class ExpoLinkAdmin(TranslatableAdmin):
    pass


@admin.register(models.Vacancy)
class VacancyAdmin(TranslatableAdmin):
    pass


@admin.register(models.LegalDocument)
class LegalDocumentAdmin(TranslatableAdmin):
    pass


@admin.register(models.Tender)
class TenderAdmin(TranslatableAdmin):
    pass


@admin.register(models.Infographic)
class InfographicAdmin(TranslatableAdmin):
    pass


@admin.register(models.Staff)
class StaffAdmin(TranslatableAdmin):
    pass


@admin.register(models.Exhibition)
class ExhibitionAdmin(TranslatableAdmin):
    pass


@admin.register(models.Legislation)
class LegislationAdmin(TranslatableAdmin):
    pass


@admin.register(models.RegionalAdministration)
class RegionalAdministrationAdmin(TranslatableAdmin):
    pass


@admin.register(models.GalleryImage)
class GalleryImageAdmin(TranslatableAdmin):
    pass


@admin.register(models.GalleryCategory)
class GalleryCategoryAdmin(TranslatableAdmin):
    pass


# @admin.register(models.MenuSettings)
# class MenuSettingsAdmin(parler_admin.TranslatableAdmin):
#     pass


@admin.register(models.Region)
class RegionAdmin(TranslatableAdmin):
    pass


@admin.register(models.ForeignRepresentativeLinks)
class ForeignRepresentativeLinksAdmin(TranslatableAdmin):
    pass


@admin.register(models.ForeignRepresentativeItems)
class ForeignRepresentativeItemsAdmin(TranslatableAdmin):
    pass


admin.site.register(Contact)
admin.site.register(models.Product, TranslatableAdmin)