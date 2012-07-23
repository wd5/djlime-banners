from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

from models import Banner, Statistics

def banner_manager(request):
    to = request.GET.get('to', None)

    if to is None:
        raise Http404

    clicked_banner = get_object_or_404(Banner, id=to)

    statistics = Statistics(
        banner = clicked_banner,
        ip = request.META['REMOTE_ADDR'],
    )

    if request.user.is_authenticated():
        statistics.user = request.user

    statistics.save()

    clicked_banner.clicks = Statistics.objects.filter(banner=clicked_banner).count()
    clicked_banner.save()

    return redirect(clicked_banner.url)