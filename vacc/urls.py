from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin


# Admin.py Stuff
admin.site.site_header = f'Vaxxer Admin'
admin.site.site_title = f'Vaxxer Admin'
admin.site.index_title = f'Vaxxer System Administration'
admin.autodiscover()
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
