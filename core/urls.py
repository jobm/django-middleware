from django.conf.urls import url
from core.views import IndexPage, TestOne, TestTwo

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name="index"),
    url(r'^test1/$', TestOne.as_view(), name="test_one"),
    url(r'^test2/$', TestTwo.as_view(), name="test_two")
]