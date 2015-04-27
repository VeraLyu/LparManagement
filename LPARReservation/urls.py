from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'LPARReservation.views.home', name='home'),
    url(r'^reserve/$', 'LPARReservation.views.reserve', name='reserve'),
    url(r'^cancel/$', 'LPARReservation.views.cancel', name='cancel'),
    url(r'^rsv/$', 'LPARReservation.views.rsv', name='rsv'),
    url(r'^ccl/$', 'LPARReservation.views.ccl', name='ccl'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT }),  
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
