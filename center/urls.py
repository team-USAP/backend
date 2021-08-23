from django.urls import path
from . import views as center_views


urlpatterns = [
    path('centerdashboard/', center_views.CenterDashboard, name='center-dashboard'),
    path('centerdashboard/pending/',
         center_views.CenterDashboardPending, name='center-pending'),
    path('centerdashboard/accepted/',
         center_views.CenterDashboardAccepted, name='center-accepted'),
    path('centerdashboard/waitlisted',
         center_views.CenterDashboardWaitlisted, name='center-waitlisted'),
    path('centerdashboard/rejected',
         center_views.CenterDashboardRejected, name='center-rejected'),
    path('centerdashboard/arrived',
         center_views.CenterDashboardArrived, name='center-arrived'),
    path('centerdashboard/compeleted',
         center_views.CenterDashboardCompleted, name='center-completed'),
    path('centerdashboard/failed',
         center_views.CenterDashboardFailed, name='center-failed'),
    path('slot/<uuid:pk>/',
         center_views.SlotDetailView.as_view(), name='slot-detail'),
    path('slot/<uuid:pk>/update',
         center_views.SlotUpdateView.as_view(), name='slot-update'),
    path('slot/<uuid:pk>/delete',
         center_views.SlotDeleteView.as_view(), name='slot-delete'),
    path('slot/create/',
         center_views.SlotCreateView.as_view(), name='slot-create'),
    path('center/<uuid:pk>/',
         center_views.CenterDetailView.as_view(), name='center-detail'),
    path('center/list/',
         center_views.CenterListView.as_view(), name='center-list'),
    path('appointment/<uuid:pk>/',
         center_views.AppointmentUpdateView.as_view(), name='app-update'),

]
