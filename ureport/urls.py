# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views import static
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog

admin.autodiscover()


urlpatterns = [
    url(r"^v2/", include("ureport.public.urls")),
    url(r"^v2/manage/", include("ureport.admins.urls")),
    url(r"^v2/manage/", include("dash.orgs.urls")),
    url(r"^v2/manage/", include("dash.dashblocks.urls")),
    url(r"^v2/manage/", include("dash.stories.urls")),
    url(r"^v2/manage/", include("ureport.polls.urls")),
    url(r"^v2/manage/", include("dash.categories.urls")),
    url(r"^v2/manage/", include("ureport.news.urls")),
    url(r"^v2/manage/", include("ureport.jobs.urls")),
    url(r"^v2/manage/", include("ureport.bots.urls")),
    url(r"^v2/manage/", include("ureport.landingpages.urls")),
    url(r"^v2/manage/", include("ureport.countries.urls")),
    url(r"^v2/manage/", include("ureport.assets.urls")),
    url(r"^v2/users/", include("dash.users.urls")),
    url(r"^v2/manage/", include("smartmin.csv_imports.urls")),
    url(r"^v1/", include("ureport.public.urls")),
    url(r"^v1/manage/", include("ureport.admins.urls")),
    url(r"^v1/manage/", include("dash.orgs.urls")),
    url(r"^v1/manage/", include("dash.dashblocks.urls")),
    url(r"^v1/manage/", include("dash.stories.urls")),
    url(r"^v1/manage/", include("ureport.polls.urls")),
    url(r"^v1/manage/", include("dash.categories.urls")),
    url(r"^v1/manage/", include("ureport.news.urls")),
    url(r"^v1/manage/", include("ureport.jobs.urls")),
    url(r"^v1/manage/", include("ureport.bots.urls")),
    url(r"^v1/manage/", include("ureport.landingpages.urls")),
    url(r"^v1/manage/", include("ureport.countries.urls")),
    url(r"^v1/manage/", include("ureport.assets.urls")),
    url(r"^v1/users/", include("dash.users.urls")),
    url(r"^v1/manage/", include("smartmin.csv_imports.urls")),
    url(r"^", include("ureport.public.urls")),
    url(r"^manage/", include("ureport.admins.urls")),
    url(r"^manage/", include("dash.orgs.urls")),
    url(r"^manage/", include("dash.dashblocks.urls")),
    url(r"^manage/", include("dash.stories.urls")),
    url(r"^manage/", include("ureport.polls.urls")),
    url(r"^manage/", include("dash.categories.urls")),
    url(r"^manage/", include("dash.tags.urls")),
    url(r"^manage/", include("ureport.news.urls")),
    url(r"^manage/", include("ureport.jobs.urls")),
    url(r"^manage/", include("ureport.bots.urls")),
    url(r"^manage/", include("ureport.landingpages.urls")),
    url(r"^manage/", include("ureport.countries.urls")),
    url(r"^manage/", include("ureport.assets.urls")),
    url(r"^users/", include("dash.users.urls")),
    url(r"^manage/", include("smartmin.csv_imports.urls")),
    url(r"^api/$", RedirectView.as_view(pattern_name="api.v1.docs", permanent=False), name="api"),
    url(r"^api/v1/", include("ureport.api.urls")),
    url(r"^jsi18n/$", JavaScriptCatalog.as_view(), name="javascript-catalog"),
]

if settings.DEBUG:

    try:
        import debug_toolbar

        urlpatterns.append(url(r"^__debug__/", include(debug_toolbar.urls)))
    except ImportError:
        pass

    urlpatterns = [
        url(r"^media/(?P<path>.*)$", static.serve, {"document_root": settings.MEDIA_ROOT, "show_indexes": True}),
        url(r"", include("django.contrib.staticfiles.urls")),
    ] + urlpatterns
