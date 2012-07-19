from django.db.models import Q
from django.conf import settings
from django.template import Library

from banners.models import Banner
from banners import LOCATION_HEADER, LOCATION_CONTENT, LOCATION_SIDEBAR

register = Library()

CITY_CONTEXT_KEY = getattr(settings, 'CITY_CONTEXT_KEY', 'city')

BANNER_HEADER_TEMPLATE = \
getattr(settings, 'BANNER_HEADER_TEMPLATE', 'banners/includes/single_banner.html')

BANNER_CONTENT_TEMPLATE = \
getattr(settings, 'BANNER_CONTENT_TEMPLATE', 'banners/includes/single_banner.html')

BANNER_SIDEBAR_TEMPLATE = \
getattr(settings, 'BANNER_SIDEBAR_TEMPLATE', 'banners/includes/banners_block.html')

BANNER_COUNT_PER_SIDEBAR = getattr(settings, 'BANNER_COUNT_PER_SIDEBAR', False)


@register.inclusion_tag(BANNER_HEADER_TEMPLATE, takes_context=True)
def include_header_banner(context):
    city = context.get(CITY_CONTEXT_KEY, None)

    try:
        banner = Banner.objects.filter(Q(city__exact=city) | Q(city__exact=None),
            location=LOCATION_HEADER
        ).order_by('?')[0]
    except IndexError:
        banner = None

    return {'banner': banner}

@register.inclusion_tag(BANNER_HEADER_TEMPLATE, takes_context=True)
def include_content_banner(context):
    city = context.get(CITY_CONTEXT_KEY, None)

    try:
        banner = Banner.objects.filter(Q(city__exact=city) | Q(city__exact=None),
            location=LOCATION_CONTENT
        ).order_by('?')[0]
    except IndexError:
        banner = None

    return {'banner': banner}

@register.inclusion_tag(BANNER_SIDEBAR_TEMPLATE, takes_context=True)
def include_sidebar_banners(context):
    city = context.get(CITY_CONTEXT_KEY, None)

    banners = Banner.objects.filter(Q(city__exact=city) | Q(city__exact=None),
        location=LOCATION_SIDEBAR
    )

    if BANNER_COUNT_PER_SIDEBAR:
        banners = banners[:int(BANNER_COUNT_PER_SIDEBAR)]

    return {'banners': banners}
