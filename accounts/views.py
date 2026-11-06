from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserUpdateForm



class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account created successfully! You can now log in."



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserUpdateForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self, queryset=None):
        return self.request.user
