from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.contrib.auth import views as auth_views

# Admin.py Stuff
admin.site.site_header = f'Vaxxer Admin'
admin.site.site_title = f'Vaxxer Admin'
admin.site.index_title = f'Vaxxer System Administration'
admin.autodiscover()
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('', include('users.urls')),
    path('', include('center.urls')),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='unlogged/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='unlogged/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confrim/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='unlogged/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='unlogged/password_reset_complete.html'),
         name='password_reset_complete'),


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
