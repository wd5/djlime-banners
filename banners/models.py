from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djlime.utils import get_file_path
from imagekit.models import ImageSpecField
from imagekit.processors.resize import ResizeToFill

from banners import LOCATION_CHOICES

BANNER_CITY_MODEL =\
getattr(settings, 'BANNER_CITY_MODEL', 'location.City')

BANNER_IMAGES_DIR =\
getattr(settings, 'BANNER_IMAGES_DIR', 'banners/images')

BANNER_THUMBNAIL_SIZE =\
getattr(settings, 'BANNER_THUMBNAIL_SIZE', (60, 60))

BANNER_THUMBNAIL_FORMAT =\
getattr(settings, 'BANNER_THUMBNAIL_FORMAT', 'PNG')

class Banner(models.Model):
    title = models.CharField(_('title'), max_length=255)
    city = models.ForeignKey(BANNER_CITY_MODEL, verbose_name=_('city'),
        blank=True, null=True)
    url = models.URLField('URL')
    location = models.IntegerField(_('location'), default=0,
        choices=LOCATION_CHOICES)
    image = models.ImageField(_('image'), upload_to=get_file_path)
    clicks = models.PositiveIntegerField(_('clicks'), default=0)

    thumbnail = ImageSpecField(
        [ResizeToFill(*BANNER_THUMBNAIL_SIZE)],
        image_field='image',
        format=BANNER_THUMBNAIL_FORMAT,
        options={'quality': 100}
    )

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')

    @property
    def upload_dir(self):
        return BANNER_IMAGES_DIR

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'go?to=%d' % self.id

    def preview(self):
        return '<img src="%s">' % self.thumbnail.url

    preview.short_description = (_('image'))
    preview.allow_tags = True


class Statistics(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_('user'),
        blank=True, null=True)
    banner = models.ForeignKey('Banner', verbose_name=_('banner'),
        on_delete=models.CASCADE)
    ip = models.IPAddressField(_('IP-address'),
        blank=True, null=True)
    created_at = models.DateTimeField(_('date and time'), auto_now_add=True)

    class Meta:
        verbose_name = _('statistics')
        verbose_name_plural = _('statistics')