version = (0, 9, 7)
__version__ = '.'.join(map(str, version))

from django.utils.translation import ugettext_lazy as _

LOCATION_HEADER = 0
LOCATION_CONTENT = 1
LOCATION_SIDEBAR = 2

LOCATION_CHOICES = (
    (LOCATION_HEADER, _('header')),
    (LOCATION_CONTENT, _('main column')),
    (LOCATION_SIDEBAR, _('side bar')),
)
