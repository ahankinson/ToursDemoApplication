from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from goudimel.views.main import BookList, BookDetail
from goudimel.views.main import PieceList, PieceDetail
from goudimel.views.main import PhraseList, PhraseDetail
from goudimel.views.search import SearchView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('goudimel.views.main',

    url(r'^$', 'home'),
    url(r'^browse/$', 'api_root'),
    # these next two are the same view, just one is singular and the other plural
    url(r'^book/$', BookList.as_view(), name="book-list"),
    url(r'^books/$', BookList.as_view(), name="books-list"),
    url(r'^book/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name="book-detail"),

    url(r'^piece/$', PieceList.as_view(), name="piece-list"),
    url(r'^pieces/$', PieceList.as_view(), name="pieces-list"),
    url(r'^piece/(?P<pk>[0-9]+)/$', PieceDetail.as_view(), name="piece-detail"),

    url(r'^phrase/$', PhraseList.as_view(), name="phrase-list"),
    url(r'^phrases/$', PhraseList.as_view(), name="phrases-list"),
    url(r'^phrase/(?P<pk>[0-9]+)/$', PhraseDetail.as_view(), name="phrase-detail"),
    url(r'^search/$', SearchView.as_view(), name="search-view"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
))
