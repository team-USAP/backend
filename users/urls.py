from django.urls import path
from . import views as user_views


urlpatterns = [
    path('', user_views.index, name='index'),
    path('login/', user_views.LoginView.as_view(), name='login'),
    path('dashboard/', user_views.dashboard, name='dashboard-home'),
    path('register/', user_views.register, name='register'),
    path('terms-of-service/', user_views.TermsofService.as_view(),
         name='terms-of-service'),
    path('privacy-policy/', user_views.PrivacyPolicy.as_view(),
         name='privacy-policy'),
    path('profile/update', user_views.ProfileUpdate,
         name='profile-update'),
    path('profile/', user_views.ProfileDetail,
         name='profile'),
    path('appointments/', user_views.AppointmentList,
         name='appointments'),
    path('createappointmentwithslot/<uuid:slotid>', user_views.CreateAppointment,
         name='create-appointments'),
    path('appointment/<uuid:pk>/delete', user_views.AppointmentDeleteView.as_view(),
         name='delete-appointments'),
]
