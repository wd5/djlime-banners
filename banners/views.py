from django.shortcuts import redirect

from models import Banner, Statistics

def banner_manager(request):
    to = request.GET.get('to', None)

    if to is None:
        return redirect('%s/../' %  request.path)

    try:
        clicked_banner = Banner.objects.get(id=to)
    except Banner.DoesNotExist:
        return redirect('%s/../' %  request.path)

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
