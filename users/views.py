from .forms import ProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm
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
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from booking.models import Appointment
from center.models import Slot


def index(request):
    return render(request, 'index.html', {'title': 'Homepage'})


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['form'] = UserLoginForm
        return context


@login_required
def dashboard(request):
    context = {
        'title': 'Homepage',
        'vacc_500': 45,
        'vacc_1000': 147,
        'vacc_5000': 793,
    }
    return render(request, 'dashboard.html', context)


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_obj = form.save()

            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password1)
            login(request, user)
            Profile.objects.create(user=user_obj)
            # return redirect('profile-update')
            return redirect('profile-update')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard-home')

        form = UserRegisterForm()
    return render(request, 'users/register.html', {'title': 'Register', 'form': form})


class PrivacyPolicy(TemplateView):
    template_name = 'unlogged/privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Privacy Policy'
        return context


class TermsofService(TemplateView):
    template_name = 'unlogged/terms-of-service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Terms of Service'
        return context


# class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Profile
#     template_name = 'dashboard/profile_update.html'
#     fields = ['gender', 'phone_no', 'dob', 'address', 'city' 'bloodType',
#               'allergy', 'alzheimer', 'asthama', 'diabetes', 'stroke']

#     def test_func(self):
#         profile = self.get_object()
#         return self.request.user == profile.user

#     def get_success_url(self):
#         return reverse_lazy('dashboard-home')

#     def get_context_data(self, **kwargs):

#         work = self.get_object()
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Profile Update'

#         # context['form'] = ProfileForm(
#         #     initial={
#         #         'employer': work.employer,
#         #         'role': work.role,
#         #         'start': work.start,
#         #         'end': work.end,
#         #         'currently_working': work.currently_working,
#         #         'description': work.description
#         #     }
#         # )

#         return context


@login_required
def ProfileUpdate(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.gender = form.cleaned_data.get('gender')
            profile.phone_no = form.cleaned_data.get('phone_no')
            profile.dob = form.cleaned_data.get('dob')
            profile.address = form.cleaned_data.get('address')
            profile.city = form.cleaned_data.get('city')
            profile.allergy = form.cleaned_data.get('allergy')
            profile.allergy = form.cleaned_data.get('allergy')
            profile.alzheimer = form.cleaned_data.get('alzheimer')
            profile.asthma = form.cleaned_data.get('asthma')
            profile.diabetes = form.cleaned_data.get('diabetes')
            profile.stroke = form.cleaned_data.get('stroke')
            profile.aadhar_card = form.cleaned_data.get('aadhar_card')

            profile.save()
            return redirect('dashboard-home')

    context = {
        'title': 'Profile ',
        'form': ProfileForm(initial={
            'gender': profile.gender,
            'phone_no': profile.phone_no,
            'dob': profile.dob,
            'address': profile.address,
            'city': profile.city,
            'bloodType': profile.bloodType,
            'allergy': profile.allergy,
            'alzheimer': profile.alzheimer,
            'asthma': profile.asthma,
            'diabetes': profile.diabetes,
            'stroke': profile.stroke,
            'aadhar_card': profile.aadhar_card
        }),

    }
    return render(request, 'users/profile_update.html', context)


def ProfileDetail(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'users/profile_detail.html', context)


class AppointmentListView(LoginRequiredMixin, ListView):
    template_name = 'users/appointment_list.html'
    model = Appointment
    context_obj_name = 'appoints'
    ordering = ['-created_date']
    paginate_by = 3


@login_required
def CreateAppointment(request, slotid):

    queryset = Slot.objects.all()
    slot_obj = get_object_or_404(queryset, pk=slotid)
    profile = Profile.objects.get(user=request.user)
    a = Appointment.objects.create(slot=slot_obj, profile=profile)
    a.save()
    slot_obj.capacity = slot_obj.capacity - 1
    slot_obj.save()
    return redirect('appointments')


@login_required
def AppointmentList(request):
    profile = Profile.objects.get(user=request.user)
    template_name = 'users/appointment_list.html'
    app = None
    no_app = False

    app = Appointment.objects.filter(profile=profile)
    no_app = Appointment.objects.filter(profile=profile).count()

    context = {
        'title': 'Appointments',
        'app': app,
        'no_app': no_app
    }

    return render(request, template_name, context)


class AppointmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Appointment
    success_url = '/appointments/'
    context_object_name = 'ap'

    def test_func(self):
        app = self.get_object()
        return self.request.user == app.profile.user
