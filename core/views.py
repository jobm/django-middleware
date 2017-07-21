# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.cache import cache


class IndexPage(TemplateView):

    def get(self, request, *args, **kwargs):
        print(cache.get('test1'))
        return HttpResponse("<h4>THis is a very responsive page, but not cached</h1>")


class TestOne(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h4>This is Caching Though</h4>")


class TestTwo(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h4>Not Cached</h1>")