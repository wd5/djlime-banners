from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Banner, Statistics

_('Banners')

class BannerAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'city', 'location', 'clicks')
    list_display_links = ('preview', 'title')
    list_editable = ('city', 'location')
    readonly_fields = ('clicks',)
    list_filter = ('city',)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('banner', 'user', 'ip', 'created_at')
    readonly_fields = ('banner', 'user', 'ip', 'created_at')
    list_filter = ('banner',)

admin.site.register(Banner, BannerAdmin)
admin.site.register(Statistics, StatisticsAdmin)