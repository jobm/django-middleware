# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from core.middleware import CacheUrlsMiddleware
from django.core.cache import cache


class CacheUrlsMiddlewareTests(TestCase):

    def test_call_middleware_without_to_cache_url(self):
        url = '/test2/'
        response = self.client.get(url)
        CacheUrlsMiddleware(response)
        self.assertEquals(cache.get(url.strip('/')), None)

    def test_call_middleware_with_to_cache_url(self):
        url = '/test1/'
        response = self.client.get(url)
        CacheUrlsMiddleware(response)
        self.assertEquals(cache.get(url.strip('/')).status_code, 200)

