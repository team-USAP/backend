
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .models import Center, Slot
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from booking.models import Appointment

# Center Views


class CenterListView(LoginRequiredMixin, ListView):
    template_name = 'center/center_list.html'
    model = Center
    context_object_name = 'centers'
    ordering = ['-name']


class CenterDetailView(LoginRequiredMixin, DetailView):
    # Also List View for Slots
    template_name = 'center/center_detail.html'
    model = Center
    context_obj_name = 'center'

    def get_context_data(self, **kwargs):
        center = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = center.name
        context['slots'] = Slot.objects.filter(center=center)
        return context

# Slot Views


class SlotUpdateView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Slot
    template_name = 'center/slot_update.html'
    fields = ['capacity']

    def form_valid(self, form):
        form.instance.center = self.request.user.center
        return super().form_valid(form)

    def test_func(self):
        slot = self.get_object()
        return self.request.user == slot.center.user


class SlotCreateView(LoginRequiredMixin, CreateView):
    model = Slot
    template_name = 'center/slot_create.html'
    fields = ['start_time', 'end_time', 'capacity']

    def form_valid(self, form):
        form.instance.center = self.request.user.center
        return super().form_valid(form)


class SlotDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Slot
    success_url = '/centerdashboard/'
    template_name = 'center/confirm_slot_delete.html'
    context_obj_name = 'slot'

    def test_func(self):
        slot = self.get_object()
        return self.request.user == slot.center.user


class SlotDetailView(LoginRequiredMixin, DetailView):
    # Also List View for Slots
    template_name = 'center/slot_detail.html'
    model = Slot
    context_obj_name = 'slot'

    def get_context_data(self, **kwargs):
        slot = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = slot.center.name
        context['app'] = Appointment.objects.filter(slot=slot)
        context['no_app'] = Appointment.objects.filter(slot=slot).count()
        return context


@login_required
def AppUpdate(request, appid):
    center = Center.objects.get(user=request.user)
    template_name = 'center/app_update.html'


class AppointmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Appointment
    template_name = 'center/app_update.html'
    fields = ['status']

    def get_context_data(self, **kwargs):
        app = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Appointment Status'
        context['ap'] = app
        return context

    def test_func(self):
        app = self.get_object()
        return self.request.user == app.slot.center.user

    def get_success_url(self):
        return reverse_lazy('center-dashboard')

# Apointment Lists


@login_required
def CenterDashboard(request):
    center = Center.objects.get(user=request.user)
    slots = Slot.objects.filter(center=center)

    context = {
        'title': 'Center Dashboard ',
        'slots': slots
    }

    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardPending(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardAccepted(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardRejected(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardWaitlisted(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardArrived(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardFailed(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)


@login_required
def CenterDashboardCompleted(request):
    context = {'title': 'Center Dashboard '}
    return render(request, 'center/dashboard.html', context)
