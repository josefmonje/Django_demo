from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from .views import ProfileListView, ProfileSlugDetailView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProfileListView.as_view(), name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', include('main.urls', namespace='main')),
    url(r'^(?P<slug>\w+)/$', ProfileSlugDetailView.as_view(), name='slugdetail'),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
