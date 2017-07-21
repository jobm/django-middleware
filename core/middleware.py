from django.http import HttpResponse

from pawame.settings import CACHE_URLS
from django.core.cache import cache


class CacheUrlsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        # print(dir(request))
        request_url = request.path.strip('/')
        for to_cache_url in CACHE_URLS:
            if request_url in to_cache_url[0]:
                if cache.get(request_url):
                    # use the response body
                    return HttpResponse(cache.get(request_url))
                else:
                    # cache here
                    body = response
                    url = request_url
                    time_to_cache = to_cache_url[1]
                    cache.set(url, body, time_to_cache)
        return response
